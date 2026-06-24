#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}"

CUDA_DEVICES="${CUDA_VISIBLE_DEVICES:-0,1}"
NPROC="${NPROC_PER_NODE:-2}"
WORKERS="${WORKERS:-4}"
EPOCHS="${EPOCHS:-80}"
BASE_PORT="${BASE_PORT:-18920}"

RUNS=(
  "second cfgs/dense_models/second.yaml 8 dense_second_2gpu_bs8"
  "pointpillar cfgs/dense_models/pointpillar.yaml 8 dense_pointpillar_2gpu_bs8"
  "pv_rcnn cfgs/dense_models/pv_rcnn.yaml 4 dense_pv_rcnn_2gpu_bs4"
  "PartA2 cfgs/dense_models/PartA2.yaml 4 dense_PartA2_2gpu_bs4"
)

run_one() {
  local name="$1"
  local cfg_file="$2"
  local batch_size="$3"
  local extra_tag="$4"
  local port="$5"

  echo "============================================================"
  echo "Training: ${name}"
  echo "Config: ${cfg_file}"
  echo "Epochs: ${EPOCHS}"
  echo "Batch size: ${batch_size} total, $((batch_size / NPROC)) per GPU"
  echo "CUDA_VISIBLE_DEVICES=${CUDA_DEVICES}"
  echo "Port: ${port}"
  echo "Extra tag: ${extra_tag}"
  echo "Started at: $(date)"
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
    --max_ckpt_save_num 10 \
    --extra_tag "${extra_tag}"

  echo "Finished ${name} at: $(date)"
}

idx=0
for run in "${RUNS[@]}"; do
  read -r name cfg_file batch_size extra_tag <<< "${run}"
  run_one "${name}" "${cfg_file}" "${batch_size}" "${extra_tag}" "$((BASE_PORT + idx))"
  idx=$((idx + 1))
done

