import argparse
import csv
import datetime
import json
import sys
import time
from pathlib import Path

import numpy as np
import torch


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from pcdet.config import cfg, cfg_from_list, cfg_from_yaml_file, log_config_to_file
from pcdet.datasets import build_dataloader
from pcdet.models import build_network, load_data_to_gpu
from pcdet.utils import common_utils


def parse_config():
    parser = argparse.ArgumentParser(description='Profile OpenPCDet model efficiency')
    parser.add_argument('--cfg_file', type=str, required=True, help='model config file')
    parser.add_argument('--ckpt', type=str, required=True, help='checkpoint file')
    parser.add_argument('--batch_size', type=int, default=1, help='batch size for profiling')
    parser.add_argument('--workers', type=int, default=4, help='number of dataloader workers')
    parser.add_argument('--warmup_iters', type=int, default=20, help='warmup iterations before timing')
    parser.add_argument('--profile_iters', type=int, default=100, help='iterations used for latency/memory')
    parser.add_argument('--flops_iters', type=int, default=1, help='iterations used for torch.profiler FLOPs estimate')
    parser.add_argument('--extra_tag', type=str, default='profile', help='output subdirectory tag')
    parser.add_argument('--output_dir', type=str, default=None, help='custom output directory')
    parser.add_argument('--skip_density', action='store_true',
                        help='replace model.get_density with a zero tensor for latency ablation')
    parser.add_argument('--set', dest='set_cfgs', default=None, nargs=argparse.REMAINDER,
                        help='set extra config keys if needed')
    args = parser.parse_args()

    cfg_from_yaml_file(args.cfg_file, cfg)
    cfg.TAG = Path(args.cfg_file).stem
    cfg.EXP_GROUP_PATH = '/'.join(args.cfg_file.split('/')[1:-1])

    np.random.seed(1024)
    torch.manual_seed(1024)

    if args.set_cfgs is not None:
        cfg_from_list(args.set_cfgs, cfg)

    return args, cfg


def count_parameters(model):
    total = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    return total, trainable


def bytes_to_mb(num_bytes):
    return float(num_bytes) / (1024.0 ** 2)


def get_next_batch(dataloader, iterator):
    try:
        batch_dict = next(iterator)
    except StopIteration:
        iterator = iter(dataloader)
        batch_dict = next(iterator)
    return batch_dict, iterator


def forward_once(model, batch_dict):
    load_data_to_gpu(batch_dict)
    with torch.no_grad():
        model(batch_dict)


def patch_density_with_zeros(model, logger):
    if not hasattr(model, 'get_density'):
        logger.warning('skip_density is set, but the model has no get_density method.')
        return

    def zero_density(batch_dict):
        points = batch_dict['points']
        if points.dim() == 2 and points.shape[1] >= 1:
            batch_size = int(points[:, 0].max().item()) + 1
        else:
            batch_size = int(batch_dict.get('batch_size', 1))
        num_points = points.shape[0] // max(1, batch_size)
        return points.new_zeros((batch_size, num_points))

    model.get_density = zero_density
    logger.info('Patched model.get_density: returning zeros for density latency ablation.')


def measure_latency_and_memory(model, dataloader, warmup_iters, profile_iters, logger):
    iterator = iter(dataloader)
    model.eval()

    logger.info('Warmup iterations: %d' % warmup_iters)
    for _ in range(warmup_iters):
        batch_dict, iterator = get_next_batch(dataloader, iterator)
        forward_once(model, batch_dict)

    torch.cuda.synchronize()
    torch.cuda.reset_peak_memory_stats()
    start_event = torch.cuda.Event(enable_timing=True)
    end_event = torch.cuda.Event(enable_timing=True)

    iter_latencies = []
    wall_start = time.perf_counter()
    num_examples = 0

    logger.info('Latency/profile iterations: %d' % profile_iters)
    for _ in range(profile_iters):
        batch_dict, iterator = get_next_batch(dataloader, iterator)
        batch_size = int(batch_dict.get('batch_size', 1))

        start_event.record()
        forward_once(model, batch_dict)
        end_event.record()
        torch.cuda.synchronize()

        elapsed_ms = start_event.elapsed_time(end_event)
        iter_latencies.append(elapsed_ms)
        num_examples += batch_size

    wall_total = time.perf_counter() - wall_start
    iter_latencies = np.array(iter_latencies, dtype=np.float64)

    peak_allocated_mb = bytes_to_mb(torch.cuda.max_memory_allocated())
    peak_reserved_mb = bytes_to_mb(torch.cuda.max_memory_reserved())
    current_allocated_mb = bytes_to_mb(torch.cuda.memory_allocated())

    latency_per_batch_ms = float(iter_latencies.mean())
    avg_batch_size = float(num_examples) / max(1, profile_iters)
    latency_per_frame_ms = latency_per_batch_ms / max(1.0, avg_batch_size)
    throughput_fps = float(num_examples / max(wall_total, 1e-6))

    return {
        'latency_ms_per_batch_mean': latency_per_batch_ms,
        'latency_ms_per_batch_std': float(iter_latencies.std()),
        'latency_ms_per_frame_mean': latency_per_frame_ms,
        'throughput_fps': throughput_fps,
        'profile_iters': int(profile_iters),
        'profiled_examples': int(num_examples),
        'avg_batch_size': avg_batch_size,
        'peak_memory_allocated_mb': peak_allocated_mb,
        'peak_memory_reserved_mb': peak_reserved_mb,
        'current_memory_allocated_mb': current_allocated_mb,
    }


def estimate_flops_with_torch_profiler(model, dataloader, flops_iters, logger):
    if flops_iters <= 0:
        return None, 'Skipped because --flops_iters <= 0.'

    try:
        activities = [torch.profiler.ProfilerActivity.CPU, torch.profiler.ProfilerActivity.CUDA]
        iterator = iter(dataloader)

        with torch.profiler.profile(
            activities=activities,
            record_shapes=True,
            profile_memory=True,
            with_flops=True
        ) as prof:
            total_examples = 0
            for _ in range(flops_iters):
                batch_dict, iterator = get_next_batch(dataloader, iterator)
                total_examples += int(batch_dict.get('batch_size', 1))
                forward_once(model, batch_dict)
                prof.step()

        total_flops = 0
        for event in prof.key_averages():
            total_flops += getattr(event, 'flops', 0) or 0

        if total_flops <= 0:
            return {
                'flops_total': None,
                'flops_per_frame': None,
                'flops_g_per_frame': None,
                'flops_iters': int(flops_iters),
                'flops_profiled_examples': int(total_examples),
            }, 'torch.profiler did not report FLOPs for this model/custom CUDA ops.'

        flops_per_frame = float(total_flops) / max(1, total_examples)
        return {
            'flops_total': float(total_flops),
            'flops_per_frame': flops_per_frame,
            'flops_g_per_frame': flops_per_frame / 1e9,
            'flops_iters': int(flops_iters),
            'flops_profiled_examples': int(total_examples),
        }, None
    except Exception as err:
        logger.warning('FLOPs profiling failed: %s' % str(err))
        return None, str(err)


def write_outputs(result, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / 'profile_metrics.json'
    csv_path = output_dir / 'profile_metrics.csv'
    md_path = output_dir / 'profile_metrics.md'

    with open(json_path, 'w') as f:
        json.dump(result, f, indent=2, sort_keys=True)

    flat_keys = [
        'cfg_file', 'ckpt', 'batch_size', 'params_total_m', 'params_trainable_m',
        'flops_g_per_frame', 'peak_memory_allocated_mb', 'peak_memory_reserved_mb',
        'latency_ms_per_frame_mean', 'latency_ms_per_batch_mean', 'throughput_fps'
    ]
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=flat_keys)
        writer.writeheader()
        writer.writerow({key: result.get(key, '') for key in flat_keys})

    flops_text = 'N/A' if result.get('flops_g_per_frame') is None else '%.3f' % result['flops_g_per_frame']
    md_lines = [
        '| Config | Params (M) | FLOPs (G/frame) | Peak mem alloc. (MB) | Peak mem reserved (MB) | Latency (ms/frame) | FPS |',
        '|---|---:|---:|---:|---:|---:|---:|',
        '| %s | %.3f | %s | %.1f | %.1f | %.2f | %.2f |' % (
            Path(result['cfg_file']).stem,
            result['params_total_m'],
            flops_text,
            result['peak_memory_allocated_mb'],
            result['peak_memory_reserved_mb'],
            result['latency_ms_per_frame_mean'],
            result['throughput_fps'],
        )
    ]
    if result.get('flops_note'):
        md_lines += ['', 'FLOPs note: %s' % result['flops_note']]
    md_path.write_text('\n'.join(md_lines) + '\n')

    return json_path, csv_path, md_path


def main():
    args, cfg = parse_config()
    assert torch.cuda.is_available(), 'CUDA is required for latency and memory profiling.'

    if args.output_dir is None:
        output_dir = cfg.ROOT_DIR / 'output' / cfg.EXP_GROUP_PATH / cfg.TAG / args.extra_tag
    else:
        output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    log_file = output_dir / ('log_profile_%s.txt' % datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))
    logger = common_utils.create_logger(log_file, rank=0)
    logger.info('**********************Start profiling**********************')
    logger.info('CUDA_VISIBLE_DEVICES=%s' % torch.cuda.get_device_name(torch.cuda.current_device()))
    for key, val in vars(args).items():
        logger.info('{:16} {}'.format(key, val))
    log_config_to_file(cfg, logger=logger)

    test_set, test_loader, _ = build_dataloader(
        dataset_cfg=cfg.DATA_CONFIG,
        class_names=cfg.CLASS_NAMES,
        batch_size=args.batch_size,
        dist=False,
        workers=args.workers,
        logger=logger,
        training=False
    )

    model = build_network(model_cfg=cfg.MODEL, num_class=len(cfg.CLASS_NAMES), dataset=test_set)
    model.load_params_from_file(filename=args.ckpt, logger=logger, to_cpu=False)
    model.cuda()
    model.eval()
    if args.skip_density:
        patch_density_with_zeros(model, logger)

    params_total, params_trainable = count_parameters(model)
    latency_mem = measure_latency_and_memory(
        model, test_loader, args.warmup_iters, args.profile_iters, logger
    )
    flops_result, flops_note = estimate_flops_with_torch_profiler(
        model, test_loader, args.flops_iters, logger
    )

    result = {
        'cfg_file': args.cfg_file,
        'ckpt': args.ckpt,
        'batch_size': args.batch_size,
        'skip_density': bool(args.skip_density),
        'device_name': torch.cuda.get_device_name(torch.cuda.current_device()),
        'params_total': int(params_total),
        'params_trainable': int(params_trainable),
        'params_total_m': float(params_total) / 1e6,
        'params_trainable_m': float(params_trainable) / 1e6,
    }
    result.update(latency_mem)
    if flops_result is not None:
        result.update(flops_result)
    else:
        result.update({
            'flops_total': None,
            'flops_per_frame': None,
            'flops_g_per_frame': None,
            'flops_iters': int(args.flops_iters),
        })
    if flops_note:
        result['flops_note'] = flops_note

    json_path, csv_path, md_path = write_outputs(result, output_dir)

    logger.info('Params total: %.3f M' % result['params_total_m'])
    logger.info('Params trainable: %.3f M' % result['params_trainable_m'])
    logger.info('FLOPs: %s G/frame' % (
        'N/A' if result['flops_g_per_frame'] is None else '%.3f' % result['flops_g_per_frame']
    ))
    logger.info('Peak memory allocated: %.1f MB' % result['peak_memory_allocated_mb'])
    logger.info('Peak memory reserved: %.1f MB' % result['peak_memory_reserved_mb'])
    logger.info('Latency: %.2f ms/frame' % result['latency_ms_per_frame_mean'])
    logger.info('Throughput: %.2f FPS' % result['throughput_fps'])
    logger.info('Saved JSON to %s' % json_path)
    logger.info('Saved CSV to %s' % csv_path)
    logger.info('Saved Markdown to %s' % md_path)
    logger.info('**********************Profiling done**********************')


if __name__ == '__main__':
    main()
