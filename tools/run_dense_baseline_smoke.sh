#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}"

CUDA_DEVICES="${CUDA_VISIBLE_DEVICES:-0,1}"
NPROC="${NPROC_PER_NODE:-2}"
WORKERS="${WORKERS:-4}"
EPOCHS="${SMOKE_EPOCHS:-1}"
BASE_PORT="${BASE_PORT:-18910}"

RUNS=(
  "second cfgs/dense_models/second.yaml 8"
  "pointpillar cfgs/dense_models/pointpillar.yaml 8"
  "pv_rcnn cfgs/dense_models/pv_rcnn.yaml 4"
  "PartA2 cfgs/dense_models/PartA2.yaml 4"
)

run_one() {
  local name="$1"
  local cfg_file="$2"
  local batch_size="$3"
  local port="$4"
  local extra_tag="dense_${name}_smoke_2gpu"

  echo "============================================================"
  echo "Smoke test: ${name}"
  echo "Config: ${cfg_file}"
  echo "Epochs: ${EPOCHS}"
  echo "Batch size: ${batch_size} total, $((batch_size / NPROC)) per GPU"
  echo "CUDA_VISIBLE_DEVICES=${CUDA_DEVICES}"
  echo "Port: ${port}"
  echo "Extra tag: ${extra_tag}"
  echo "============================================================"

  CUDA_VISIBLE_DEVICES="${CUDA_DEVICES}" python -m torch.distributed.launch \
    --nproc_per_node="${NPROC}" \
    --master_port="${port}" \
    train.py \
    --launcher pytorch \
    --cfg_file "${cfg_file}" \
    --batch_size "${batch_size}" \
    --epochs "${EPOCHS}" \
    --workers "${WORKERS}" \
    --ckpt_save_interval 1 \
    --max_ckpt_save_num 1 \
    --extra_tag "${extra_tag}"
}

idx=0
for run in "${RUNS[@]}"; do
  read -r name cfg_file batch_size <<< "${run}"
  run_one "${name}" "${cfg_file}" "${batch_size}" "$((BASE_PORT + idx))"
  idx=$((idx + 1))
done

