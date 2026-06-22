import argparse
import csv
import sys
from pathlib import Path

import numpy as np
import torch
from tqdm import tqdm


FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pcdet.config import cfg, cfg_from_yaml_file
from pcdet.datasets import build_dataloader
from pcdet.ops.pointnet2.pointnet2_batch.pointnet2_utils import ball_query
from pcdet.utils import common_utils


def parse_pair(text):
    sep = ':' if ':' in text else ','
    if sep not in text:
        raise argparse.ArgumentTypeError('Use RADIUS:NSAMPLE, e.g. 0.2:10')
    radius, nsample = text.split(sep, 1)
    return float(radius), int(nsample)


def parse_args():
    parser = argparse.ArgumentParser(description='Full split DSASA density statistics.')
    parser.add_argument('--cfg_file', type=str, default='cfgs/nuscenes_models/3dssd_dsasa.yaml')
    parser.add_argument(
        '--pairs',
        type=parse_pair,
        nargs='+',
        default=[(0.1, 5), (0.15, 8), (0.18, 10), (0.2, 10), (0.22, 12), (0.25, 12), (0.3, 15)],
        help='candidate radius:max_nsample list'
    )
    parser.add_argument('--batch_size', type=int, default=1)
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--split', choices=['train', 'val'], default='train')
    parser.add_argument('--with_train_aug', action='store_true', default=False)
    parser.add_argument('--output', type=str, default='../output/density_stats_nusc_all.csv')
    return parser.parse_args()


class StreamingStats:
    def __init__(self, max_nsample):
        self.max_nsample = max_nsample
        self.hist = np.zeros(max_nsample + 1, dtype=np.int64)
        self.total = 0
        self.sum = 0.0
        self.sum_sq = 0.0
        self.min = None
        self.max = None

    def update(self, values):
        values = np.clip(values.astype(np.int64, copy=False), 0, self.max_nsample)
        self.hist += np.bincount(values, minlength=self.max_nsample + 1)[:self.max_nsample + 1]
        self.total += int(values.size)
        self.sum += float(values.sum())
        self.sum_sq += float((values.astype(np.float64) ** 2).sum())
        if values.size:
            cur_min, cur_max = int(values.min()), int(values.max())
            self.min = cur_min if self.min is None else min(self.min, cur_min)
            self.max = cur_max if self.max is None else max(self.max, cur_max)

    def percentile(self, q):
        if self.total == 0:
            return float('nan')
        target = self.total * q / 100.0
        return int(np.searchsorted(np.cumsum(self.hist), target, side='left'))

    def to_row(self, radius, nsample, bucket):
        mean = self.sum / max(self.total, 1)
        var = self.sum_sq / max(self.total, 1) - mean ** 2
        return {
            'bucket': bucket,
            'radius': radius,
            'max_nsample': nsample,
            'num_points': self.total,
            'mean': mean,
            'std': max(var, 0.0) ** 0.5,
            'min': self.min,
            'p50': self.percentile(50),
            'p75': self.percentile(75),
            'p90': self.percentile(90),
            'p95': self.percentile(95),
            'p99': self.percentile(99),
            'max': self.max,
            'saturation_ratio': self.hist[self.max_nsample] / max(self.total, 1),
            'one_or_less_ratio': self.hist[:2].sum() / max(self.total, 1),
        }


def score_candidate(rows_for_pair):
    by_bucket = {r['bucket']: r for r in rows_for_pair}
    mid = by_bucket.get('20-40m')
    far = by_bucket.get('40-60m')
    near = by_bucket.get('0-20m')
    if mid is None or far is None or near is None:
        return -1e9, 'missing bucket'

    score = 0.0
    notes = []

    score -= max(near['saturation_ratio'] - 0.60, 0) * 4
    score -= max(mid['saturation_ratio'] - 0.15, 0) * 6
    score -= max(far['saturation_ratio'] - 0.05, 0) * 8
    score -= max(mid['one_or_less_ratio'] - 0.20, 0) * 3
    score -= max(far['one_or_less_ratio'] - 0.35, 0) * 2

    if mid['p95'] >= mid['max_nsample']:
        notes.append('mid p95 hits cap')
    if near['saturation_ratio'] > 0.70:
        notes.append('near heavily saturated')
    if far['one_or_less_ratio'] > 0.40:
        notes.append('far too sparse')
    if not notes:
        notes.append('balanced')
    return score, '; '.join(notes)


def print_row(row):
    print(
        f"{row['bucket']:>8s} r={row['radius']:<4g} ns={row['max_nsample']:<3d} "
        f"N={row['num_points']:<10d} mean={row['mean']:.3f} "
        f"p50={row['p50']:<2} p90={row['p90']:<2} p95={row['p95']:<2} p99={row['p99']:<2} "
        f"sat={row['saturation_ratio']:.3%} <=1={row['one_or_less_ratio']:.3%}"
    )


def main():
    args = parse_args()
    cfg_from_yaml_file(args.cfg_file, cfg)

    if args.split == 'train' and not args.with_train_aug:
        cfg.DATA_CONFIG.DATA_SPLIT['test'] = cfg.DATA_CONFIG.DATA_SPLIT['train']
        cfg.DATA_CONFIG.INFO_PATH['test'] = cfg.DATA_CONFIG.INFO_PATH['train']

    logger = common_utils.create_logger()
    dataset, dataloader, _ = build_dataloader(
        dataset_cfg=cfg.DATA_CONFIG,
        class_names=cfg.CLASS_NAMES,
        batch_size=args.batch_size,
        dist=False,
        workers=args.workers,
        logger=logger,
        training=args.with_train_aug,
    )

    if not torch.cuda.is_available():
        raise RuntimeError('CUDA is required by the ball_query op.')

    buckets = [(0, 20, '0-20m'), (20, 40, '20-40m'), (40, 60, '40-60m'), (60, 1e9, '60m+')]
    stats = {}
    for radius, nsample in args.pairs:
        stats[(radius, nsample, 'all')] = StreamingStats(nsample)
        for _, _, name in buckets:
            stats[(radius, nsample, name)] = StreamingStats(nsample)

    frames = 0
    for batch in tqdm(dataloader, total=len(dataloader), desc='density-all'):
        points = batch['points']
        batch_ids = points[:, 0].astype(np.int64)
        for b in range(batch['batch_size']):
            cur_points = points[batch_ids == b]
            if cur_points.shape[0] == 0:
                continue
            xyz_np = cur_points[:, 1:4].astype(np.float32, copy=False)
            dist = np.linalg.norm(xyz_np[:, :2], axis=1)
            xyz = torch.from_numpy(xyz_np).cuda(non_blocking=True).view(1, -1, 3).contiguous()

            for radius, nsample in args.pairs:
                idx_cnt, _ = ball_query(radius, nsample, xyz, xyz)
                counts = idx_cnt.view(-1).detach().cpu().numpy()
                stats[(radius, nsample, 'all')].update(counts)
                for lo, hi, name in buckets:
                    mask = (dist >= lo) & (dist < hi)
                    if mask.any():
                        stats[(radius, nsample, name)].update(counts[mask])
            frames += 1

    rows = []
    print('\nFull density count distribution')
    print(f'cfg={args.cfg_file}, split={args.split}, with_train_aug={args.with_train_aug}, frames={frames}')
    for radius, nsample in args.pairs:
        pair_rows = []
        for bucket in ['all', '0-20m', '20-40m', '40-60m', '60m+']:
            row = stats[(radius, nsample, bucket)].to_row(radius, nsample, bucket)
            rows.append(row)
            pair_rows.append(row)
            print_row(row)
        score, note = score_candidate(pair_rows)
        print(f"  candidate_score={score:.3f} note={note}\n")

    best = {}
    for radius, nsample in args.pairs:
        pair_rows = [r for r in rows if r['radius'] == radius and r['max_nsample'] == nsample]
        score, note = score_candidate(pair_rows)
        best[(radius, nsample)] = (score, note)
    print('Recommended order:')
    for (radius, nsample), (score, note) in sorted(best.items(), key=lambda item: item[1][0], reverse=True):
        print(f'  r={radius:g}, max_nsample={nsample}: score={score:.3f}, {note}')

    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        with open(output, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
        print(f'Saved csv to {output}')


if __name__ == '__main__':
    main()
