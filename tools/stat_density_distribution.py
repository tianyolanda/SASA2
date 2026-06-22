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
    if ':' in text:
        radius, nsample = text.split(':', 1)
    elif ',' in text:
        radius, nsample = text.split(',', 1)
    else:
        raise argparse.ArgumentTypeError('Use RADIUS:NSAMPLE, for example 0.3:15')
    return float(radius), int(nsample)


def parse_args():
    parser = argparse.ArgumentParser(
        description='Statistic ball-query density count distribution for DSASA.'
    )
    parser.add_argument(
        '--cfg_file',
        type=str,
        default='cfgs/nuscenes_models/3dssd_dsasa.yaml',
        help='config path relative to tools/, same style as train.py/test.py'
    )
    parser.add_argument(
        '--pairs',
        type=parse_pair,
        nargs='+',
        default=[(0.2, 10), (0.3, 15), (0.5, 20)],
        help='radius:max_nsample list, e.g. --pairs 0.2:10 0.3:15 0.5:20'
    )
    parser.add_argument('--num_samples', type=int, default=300, help='number of frames to scan')
    parser.add_argument('--batch_size', type=int, default=1, help='keep 1 if GPU memory is tight')
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument(
        '--split',
        choices=['train', 'val'],
        default='train',
        help='train uses train infos without data augmentation; val uses cfg test split'
    )
    parser.add_argument(
        '--with_train_aug',
        action='store_true',
        default=False,
        help='use training=True, including gt sampling and random augmentation'
    )
    parser.add_argument(
        '--output',
        type=str,
        default=None,
        help='optional csv output path'
    )
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
        values = values.astype(np.int64, copy=False)
        values = np.clip(values, 0, self.max_nsample)
        hist = np.bincount(values, minlength=self.max_nsample + 1)
        self.hist += hist[:self.max_nsample + 1]
        self.total += int(values.size)
        self.sum += float(values.sum())
        self.sum_sq += float((values.astype(np.float64) ** 2).sum())
        cur_min = int(values.min()) if values.size else None
        cur_max = int(values.max()) if values.size else None
        self.min = cur_min if self.min is None else min(self.min, cur_min)
        self.max = cur_max if self.max is None else max(self.max, cur_max)

    def percentile(self, q):
        if self.total == 0:
            return float('nan')
        target = self.total * q / 100.0
        cumulative = np.cumsum(self.hist)
        return int(np.searchsorted(cumulative, target, side='left'))

    def row(self, radius, nsample, name='all'):
        mean = self.sum / max(self.total, 1)
        var = self.sum_sq / max(self.total, 1) - mean ** 2
        std = max(var, 0.0) ** 0.5
        sat = self.hist[self.max_nsample] / max(self.total, 1)
        return {
            'name': name,
            'radius': radius,
            'max_nsample': nsample,
            'num_points': self.total,
            'mean': mean,
            'std': std,
            'min': self.min,
            'p50': self.percentile(50),
            'p75': self.percentile(75),
            'p90': self.percentile(90),
            'p95': self.percentile(95),
            'p99': self.percentile(99),
            'max': self.max,
            'saturation_ratio': sat,
            'one_or_less_ratio': self.hist[:2].sum() / max(self.total, 1),
        }


def format_row(row):
    return (
        f"{row['name']:>8s}  r={row['radius']:<4g} ns={row['max_nsample']:<3d} "
        f"N={row['num_points']:<9d} mean={row['mean']:.3f} std={row['std']:.3f} "
        f"p50={row['p50']:<2} p75={row['p75']:<2} p90={row['p90']:<2} "
        f"p95={row['p95']:<2} p99={row['p99']:<2} max={row['max']:<2} "
        f"sat={row['saturation_ratio']:.3%} <=1={row['one_or_less_ratio']:.3%}"
    )


def main():
    args = parse_args()
    cfg_from_yaml_file(args.cfg_file, cfg)

    if args.split == 'train' and not args.with_train_aug:
        cfg.DATA_CONFIG.DATA_SPLIT['test'] = cfg.DATA_CONFIG.DATA_SPLIT['train']
        cfg.DATA_CONFIG.INFO_PATH['test'] = cfg.DATA_CONFIG.INFO_PATH['train']

    logger = common_utils.create_logger()
    training = args.with_train_aug
    dataset, dataloader, _ = build_dataloader(
        dataset_cfg=cfg.DATA_CONFIG,
        class_names=cfg.CLASS_NAMES,
        batch_size=args.batch_size,
        dist=False,
        workers=args.workers,
        logger=logger,
        training=training,
    )

    if not torch.cuda.is_available():
        raise RuntimeError('ball_query CUDA op requires a CUDA GPU.')

    bins = [(0, 20), (20, 40), (40, 60), (60, 1e9)]
    stats = {}
    for radius, nsample in args.pairs:
        stats[(radius, nsample, 'all')] = StreamingStats(nsample)
        for lo, hi in bins:
            stats[(radius, nsample, f'{lo:g}-{hi:g}m')] = StreamingStats(nsample)

    seen = 0
    for batch in tqdm(dataloader, total=min(len(dataloader), args.num_samples), desc='density'):
        points = batch['points']
        batch_ids = points[:, 0].astype(np.int64)
        for b in range(batch['batch_size']):
            cur_points = points[batch_ids == b]
            if cur_points.shape[0] == 0:
                continue

            xyz_np = cur_points[:, 1:4].astype(np.float32, copy=False)
            dist_np = np.linalg.norm(xyz_np[:, :2], axis=1)
            xyz = torch.from_numpy(xyz_np).cuda(non_blocking=True).view(1, -1, 3).contiguous()

            for radius, nsample in args.pairs:
                idx_cnt, _ = ball_query(radius, nsample, xyz, xyz)
                counts = idx_cnt.view(-1).detach().cpu().numpy()
                stats[(radius, nsample, 'all')].update(counts)
                for lo, hi in bins:
                    mask = (dist_np >= lo) & (dist_np < hi)
                    if mask.any():
                        stats[(radius, nsample, f'{lo:g}-{hi:g}m')].update(counts[mask])

            seen += 1
            if seen >= args.num_samples:
                break
        if seen >= args.num_samples:
            break

    rows = []
    print('\nDensity count distribution')
    print(f'cfg={args.cfg_file}, split={args.split}, with_train_aug={args.with_train_aug}, frames={seen}')
    for radius, nsample in args.pairs:
        for name in ['all', '0-20m', '20-40m', '40-60m', '60-1e+09m']:
            row = stats[(radius, nsample, name)].row(radius, nsample, name=name)
            rows.append(row)
            print(format_row(row))
        print('')

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
