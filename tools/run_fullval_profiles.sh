#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

COMMON_ARGS=(
  --batch_size 1
  --workers 4
  --warmup_iters 20
  --profile_iters 6019
  --flops_iters 1
)

echo "[$(date '+%F %T')] Starting 3DSSD on GPU 0..."
CUDA_VISIBLE_DEVICES=0 nohup python profile_model.py \
  --cfg_file cfgs/nuscenes_models/3dssd.yaml \
  --ckpt ../output/nuscenes_models/3dssd/default/ckpt/checkpoint_epoch_20.pth \
  --extra_tag profile_3dssd_epoch20_skip_density_fullval \
  --skip_density \
  "${COMMON_ARGS[@]}" \
  > profile_3dssd_fullval.log 2>&1 &
PID_3DSSD=$!

echo "[$(date '+%F %T')] Starting 3DSSD + SASA on GPU 1..."
CUDA_VISIBLE_DEVICES=1 nohup python profile_model.py \
  --cfg_file cfgs/nuscenes_models/3dssd_sasa.yaml \
  --ckpt ../output/nuscenes_models/3dssd_sasa/default/ckpt/checkpoint_epoch_20.pth \
  --extra_tag profile_sasa_epoch20_skip_density_fullval \
  --skip_density \
  "${COMMON_ARGS[@]}" \
  > profile_sasa_fullval.log 2>&1 &
PID_SASA=$!

echo "[$(date '+%F %T')] Starting 3DSSD + DSASA on GPU 2..."
CUDA_VISIBLE_DEVICES=2 nohup python profile_model.py \
  --cfg_file cfgs/nuscenes_models/3dssd_dsasa_fixed_r018_ns10.yaml \
  --ckpt ../output/nuscenes_models/3dssd_sasa/default/ckpt/checkpoint_epoch_19.pth \
  --extra_tag profile_dsasa_r018_ns10_sasa_epoch19_fullval \
  "${COMMON_ARGS[@]}" \
  > profile_dsasa_fullval.log 2>&1 &
PID_DSASA=$!

echo "[$(date '+%F %T')] Started jobs:"
echo "  3DSSD PID=${PID_3DSSD}, log=profile_3dssd_fullval.log"
echo "  SASA  PID=${PID_SASA}, log=profile_sasa_fullval.log"
echo "  DSASA PID=${PID_DSASA}, log=profile_dsasa_fullval.log"
echo "[$(date '+%F %T')] Jobs are running in background. Use tail -f profile_*_fullval.log to monitor."
