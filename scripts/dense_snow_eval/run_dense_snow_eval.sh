#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="${ROOT_DIR:-/home/ubuntu/codes/2025codes/SASA2}"
LOG_DIR="${LOG_DIR:-$ROOT_DIR/dense_snow_test_logs}"
CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"
PYTHON="${PYTHON:-python}"

export CUDA_VISIBLE_DEVICES

cd "$ROOT_DIR"
mkdir -p "$LOG_DIR"

COMMON_SET=(
  DATA_CONFIG.DATA_SPLIT.test test_snow
  DATA_CONFIG.INFO_PATH.test dense_infos_test_snow.pkl
)

find_first_existing() {
  local item
  for item in "$@"; do
    if [[ -e "$item" ]]; then
      printf '%s\n' "$item"
      return 0
    fi
  done
  return 1
}

find_by_glob() {
  local pattern="$1"
  local found
  found="$(find "$ROOT_DIR" -path "$pattern" -print -quit 2>/dev/null || true)"
  if [[ -n "$found" ]]; then
    printf '%s\n' "$found"
    return 0
  fi
  return 1
}

run_eval() {
  local name="$1"
  local cfg="$2"
  local ckpt="$3"
  local epoch="$4"
  local batch_size="${5:-1}"
  local workers="${6:-4}"

  local safe_name="${name// /_}"
  safe_name="${safe_name//+/plus}"
  safe_name="${safe_name//\//_}"
  local console_log="$LOG_DIR/${safe_name}_test_snow_console.log"
  local status_file="$LOG_DIR/${safe_name}.status"

  if [[ ! -f "$cfg" ]]; then
    echo "SKIP $name: missing cfg $cfg" | tee "$status_file"
    return 0
  fi
  if [[ ! -f "$ckpt" ]]; then
    echo "SKIP $name: missing ckpt $ckpt" | tee "$status_file"
    return 0
  fi

  echo "RUN $name" | tee "$status_file"
  echo "  cfg:  $cfg" | tee -a "$status_file"
  echo "  ckpt: $ckpt" | tee -a "$status_file"
  echo "  log:  $console_log" | tee -a "$status_file"

  "$PYTHON" tools/test.py \
    --cfg_file "$cfg" \
    --batch_size "$batch_size" \
    --workers "$workers" \
    --extra_tag dense_snow_test \
    --ckpt "$ckpt" \
    --eval_tag "${safe_name}_test_snow" \
    --save_to_file \
    --set "${COMMON_SET[@]}" 2>&1 | tee "$console_log"

  echo "DONE $name" | tee -a "$status_file"
}

SASA_CKPT_74="$ROOT_DIR/output/dense_models/3dssd_sasa/dense_sasa_2gpu_bs16/ckpt/checkpoint_epoch_74.pth"
SASA_CKPT_80="$ROOT_DIR/output/dense_models/3dssd_sasa/dense_sasa_2gpu_bs16/ckpt/checkpoint_epoch_80.pth"

run_eval "DSASA fixed_r025_ns12 e74" \
  "tools/cfgs/dense_models/3dssd_dsasa_fixed_r025_ns12.yaml" \
  "$SASA_CKPT_74" 74

run_eval "DSASA r025 gated e74" \
  "tools/cfgs/dense_models/3dssd_dsasa_gated_alpha02_tau03.yaml" \
  "$SASA_CKPT_74" 74

run_eval "SASA baseline e80" \
  "tools/cfgs/dense_models/3dssd_sasa.yaml" \
  "$SASA_CKPT_80" 80

run_eval "3DSSD baseline e80" \
  "tools/cfgs/dense_models/3dssd.yaml" \
  "$ROOT_DIR/output/dense_models/3dssd/dense_3dssd_2gpu_bs16/ckpt/checkpoint_epoch_80.pth" 80

run_eval "PV-RCNN baseline e76" \
  "tools/cfgs/dense_models/pv_rcnn.yaml" \
  "$ROOT_DIR/output/dense_models/pv_rcnn/dense_pv_rcnn_2gpu_bs12/ckpt/checkpoint_epoch_76.pth" 76

run_eval "PV-RCNN baseline e80" \
  "tools/cfgs/dense_models/pv_rcnn.yaml" \
  "$ROOT_DIR/output/dense_models/pv_rcnn/dense_pv_rcnn_2gpu_bs12/ckpt/checkpoint_epoch_80.pth" 80

run_eval "SECOND baseline e80" \
  "tools/cfgs/dense_models/second.yaml" \
  "$ROOT_DIR/output/dense_models/second/dense_second_2gpu_bs24/ckpt/checkpoint_epoch_80.pth" 80 1 4

run_eval "PointPillars baseline e80" \
  "tools/cfgs/dense_models/pointpillar.yaml" \
  "$ROOT_DIR/output/dense_models/pointpillar/dense_pointpillar_2gpu_bs32/ckpt/checkpoint_epoch_80.pth" 80 1 4

VOXELNEXT_CFG="$(find_first_existing \
  tools/cfgs/dense_models/voxelnext.yaml \
  tools/cfgs/dense_models/voxelnext_2d.yaml \
  tools/cfgs/dense_models/voxelnext_dense.yaml \
  || find_by_glob '*/cfgs/dense_models/*voxelnext*.yaml' \
  || true)"
VOXELNEXT_CKPT="$(find_first_existing \
  "$ROOT_DIR/output/dense_models/voxelnext/default/ckpt/checkpoint_epoch_80.pth" \
  "$ROOT_DIR/output/dense_models/voxelnext/dense_voxelnext/ckpt/checkpoint_epoch_80.pth" \
  "$ROOT_DIR/output/dense_models/voxelnext/dense_voxelnext_2gpu/ckpt/checkpoint_epoch_80.pth" \
  || find_by_glob '*/output/dense_models/*voxelnext*/**/checkpoint_epoch_80.pth' \
  || true)"
run_eval "VoxelNeXt e80" "$VOXELNEXT_CFG" "$VOXELNEXT_CKPT" 80 1 4

HEDNET_CFG="$(find_first_existing \
  tools/cfgs/dense_models/hednet.yaml \
  tools/cfgs/dense_models/hednet_dense.yaml \
  || find_by_glob '*/cfgs/dense_models/*hednet*.yaml' \
  || true)"
HEDNET_CKPT="$(find_first_existing \
  "$ROOT_DIR/output/dense_models/hednet/default/ckpt/checkpoint_epoch_80.pth" \
  "$ROOT_DIR/output/dense_models/hednet/dense_hednet/ckpt/checkpoint_epoch_80.pth" \
  "$ROOT_DIR/output/dense_models/hednet/dense_hednet_2gpu/ckpt/checkpoint_epoch_80.pth" \
  || find_by_glob '*/output/dense_models/*hednet*/**/checkpoint_epoch_80.pth' \
  || true)"
run_eval "HEDNet e80" "$HEDNET_CFG" "$HEDNET_CKPT" 80 1 4

"$PYTHON" scripts/dense_snow_eval/parse_dense_snow_logs.py "$LOG_DIR" \
  --output "$LOG_DIR/dense_snow_selected_results_with_van.md"

echo "All available runs finished. Summary: $LOG_DIR/dense_snow_selected_results_with_van.md"
