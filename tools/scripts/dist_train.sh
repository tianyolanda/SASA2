#!/usr/bin/env bash

set -x
NGPUS=$2
PY_ARGS=${@:3}

python -m torch.distributed.launch --nproc_per_node=${NGPUS} train.py --launcher pytorch ${PY_ARGS}

