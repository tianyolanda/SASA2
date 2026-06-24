#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}"

CKPT="${CKPT:-/home/ubuntu/codes/2025codes/SASA2/output/dense_models/3dssd_sasa/dense_sasa_2gpu_bs16/ckpt/checkpoint_epoch_74.pth}"
EXTRA_TAG="${EXTRA_TAG:-dense_sasa_2gpu_bs16}"
CUDA_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"
BATCH_SIZE="${BATCH_SIZE:-1}"
WORKERS="${WORKERS:-4}"

CFG_FILES=(
  "cfgs/dense_models/3dssd_dsasa_fixed_r015_ns8.yaml"
  "cfgs/dense_models/3dssd_dsasa_fixed_r020_norm.yaml"
  "cfgs/dense_models/3dssd_dsasa_fixed_r025_ns12.yaml"
  "cfgs/dense_models/3dssd_dsasa_gated_alpha02_tau03.yaml"
  "cfgs/dense_models/3dssd_dsasa_range_balanced.yaml"
)

if [[ ! -f "${CKPT}" ]]; then
  echo "Checkpoint not found: ${CKPT}" >&2
  exit 1
fi

for cfg_file in "${CFG_FILES[@]}"; do
  cfg_name="$(basename "${cfg_file}" .yaml)"
  eval_tag="${EVAL_TAG_PREFIX:-dsasa_sweep}_${cfg_name}_e$(basename "${CKPT}" .pth | sed 's/checkpoint_epoch_//')"

  echo "============================================================"
  echo "Config: ${cfg_file}"
  echo "Checkpoint: ${CKPT}"
  echo "Eval tag: ${eval_tag}"
  echo "CUDA_VISIBLE_DEVICES=${CUDA_DEVICES}"
  echo "============================================================"

  CUDA_VISIBLE_DEVICES="${CUDA_DEVICES}" python test.py \
    --cfg_file "${cfg_file}" \
    --batch_size "${BATCH_SIZE}" \
    --workers "${WORKERS}" \
    --ckpt "${CKPT}" \
    --extra_tag "${EXTRA_TAG}" \
    --eval_tag "${eval_tag}"
done

