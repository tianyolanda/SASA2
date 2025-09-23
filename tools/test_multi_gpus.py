# test_multi_gpus_fixed.py
import os
import torch
import torch.distributed as dist
import time


def test_distributed():
    print("Starting distributed test...")

    # 初始化分布式
    dist.init_process_group(backend='nccl', init_method='env://')

    world_size = dist.get_world_size()
    rank = dist.get_rank()
    local_rank = int(os.environ.get('LOCAL_RANK', 0))

    # 设置当前GPU
    torch.cuda.set_device(local_rank)

    print(f"Rank {rank}/{world_size} (local_rank={local_rank}) initialized successfully")

    # 确保所有进程都完成初始化
    dist.barrier()

    try:
        # 创建CUDA张量（在当前GPU上）
        tensor = torch.tensor([1.0 * (rank + 1)]).cuda()
        print(f"Rank {rank}: Tensor created: {tensor}")

        # 等待所有进程完成张量创建
        dist.barrier()

        # 执行all_reduce
        print(f"Rank {rank}: Starting all_reduce...")
        dist.all_reduce(tensor)
        print(f"Rank {rank}: All reduce completed. Result: {tensor}")

    except Exception as e:
        print(f"Rank {rank}: Error occurred: {e}")

    finally:
        # 清理
        dist.destroy_process_group()
        print(f"Rank {rank}: Test completed")


if __name__ == "__main__":
    test_distributed()