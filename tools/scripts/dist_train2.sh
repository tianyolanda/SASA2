#!/usr/bin/env bash

set -x
NGPUS=$2
PY_ARGS=${@:3}

torchrun --nproc_per_node=${NGPUS} train_multigpus.py --launcher pytorch ${PY_ARGS}
