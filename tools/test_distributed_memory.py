# test_distributed_memory.py
import os
import torch
import torch.distributed as dist
import torch.nn as nn


def test_memory():
    local_rank = int(os.environ.get('LOCAL_RANK', 0))
    torch.cuda.set_device(local_rank)

    dist.init_process_group(backend='nccl', init_method='env://')

    # 创建一个小的模型测试
    model = nn.Sequential(
        nn.Linear(1000, 500),
        nn.ReLU(),
        nn.Linear(500, 10)
    ).cuda()

    if dist.get_world_size() > 1:
        model = nn.parallel.DistributedDataParallel(model)

    # 小的输入数据
    x = torch.randn(32, 1000).cuda()
    output = model(x)

    print(f"Rank {dist.get_rank()}: Memory test passed!")
    dist.destroy_process_group()


if __name__ == '__main__':
    test_memory()