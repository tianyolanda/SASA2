# pyyaml版本 
(sasa2) ubuntu@ubuntu-tt:~/codes/2025codes/SASA2/tools$ pip install pyyaml==5.3 Collecting pyyaml==5.3
  Using cached PyYAML-5.3-cp37-cp37m-linux_x86_64.whl
Installing collected packages: pyyaml
  Attempting uninstall: pyyaml
    Found existing installation: PyYAML 5.4.1
    Uninstalling PyYAML-5.4.1:
      Successfully uninstalled PyYAML-5.4.1
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
open3d 0.13.0 requires pyyaml>=5.4.1, but you have pyyaml 5.3 which is incompatible.
Successfully installed pyyaml-5.3


# nuscene 训练
CUDA_VISIBLE_DEVICES=1 python train.py --cfg_file cfgs/nuscenes_models/3dssd.yaml
会报错RuntimeError: CUDA out of memory. 

## 尝试多gpu训练
export OMP_NUM_THREADS=2 
bash scripts/dist_train2.sh 2 --cfg_file cfgs/nuscenes_models/3dssd.yaml
会卡住

# 准备数据集nuscene
python -m pcdet.datasets.nuscenes.nuscenes_dataset --func create_nuscenes_infos   --cfg_file tools/cfgs/dataset_configs/nuscenes_dataset.yaml --version v1.0-mini

## 结果
======
total scene num: 10
exist scene num: 10
v1.0-mini: train scene(8), val scene(2)
create_info: 100%|████████████████████████████████████████████████| 404/404 [00:07<00:00, 53.91it/s]
train sample: 323, val sample: 81
2025-03-10 11:52:27,892   INFO  Loading NuScenes dataset
2025-03-10 11:52:27,917   INFO  Total samples for NuScenes dataset: 323
100%|█████████████████████████████████████████████████████████████| 323/323 [00:41<00:00,  7.82it/s]
Database pedestrian: 3068
Database car: 4082
Database traffic_cone: 773
Database bicycle: 147
Database barrier: 1851
Database truck: 451
Database bus: 337
Database construction_vehicle: 174
Database ignore: 95
Database motorcycle: 179
Database trailer: 59


#　conda环境
sasa2
export PYTHONPATH='/home/ubuntu/codes/2025codes/SASA2'

# 训练
export OMP_NUM_THREADS=2 
bash scripts/dist_train2.sh 2 --cfg_file cfgs/kitti_models/3dssd.yaml


CUDA_VISIBLE_DEVICES=1 python -m torch.distributed.run train.py --cfg_file cfgs/kitti_models/3dssd.yaml


CUDA_VISIBLE_DEVICES=0,1 python train.py --cfg_file cfgs/kitti_models/3dssd.yaml

CUDA_VISIBLE_DEVICES=0,1 python -m torch.distributed.launch --nproc_per_node=2 train.py --cfg_file cfgs/kitti_models/3dssd.yaml

sh scripts/dist_train.sh 2 --cfg_file cfgs/kitti_models/3dssd.yaml


# 单卡
python train.py --cfg_file cfgs/kitti_models/3dssd.yaml

python train.py --cfg_file cfgs/kitti_models/3dssd_sasa.yaml

CUDA_VISIBLE_DEVICES=1 python train.py --cfg_file cfgs/kitti_models/pointrcnn_dsasa.yaml

# 计算网络每层尺寸(没跑明白)
pip install torchsummary

# 训练报错(20250224)
OSError: libcuhash.so: cannot open shared object file: No such file or directory
## 解决
1. 查看libcuhash.so是否存在
ubuntu@ubuntu-tt:~$ find / -name "libcuhash.so" 2>/dev/null
/home/ubuntu/anaconda3/envs/sasa2/lib/python3.7/site-packages/spconv/libcuhash.so
/home/ubuntu/.local/share/Trash/files/lib.6.linux-x86_64-cpython-37/spconv/libcuhash.so
/home/ubuntu/.local/share/Trash/files/SASA/spconv/build/lib.linux-x86_64-cpython-37/spconv/libcuhash.so
/home/ubuntu/codes/2025codes/SASA1/spconv/build/lib.linux-x86_64-cpython-37/spconv/libcuhash.so
/home/ubuntu/codes/2025codes/SASA2/spconv/build/lib.linux-x86_64-cpython-37/spconv/libcuhash.so
/home/ubuntu/codes/2025codes/backup/SASA(修改代码至能训练)/spconv/build/lib.linux-x86_64-cpython-37/spconv/libcuhash.so
/home/ubuntu/codes/2025codes/backup/SASA(20250224)/spconv/build/lib.linux-x86_64-cpython-37/spconv/libcuhash.so

2. 复制到LD_LIBRARY_PATH=/opt/cuda/lib64路径下
ubuntu@ubuntu-tt:/usr/local/cuda/lib64$ ln -s /home/ubuntu/anaconda3/envs/sasa2/lib/python3.7/site-packages/spconv/libcuhash.so .
ln: failed to create symbolic link './libcuhash.so': Permission denied
ubuntu@ubuntu-tt:/usr/local/cuda/lib64$ sudo ln -s /home/ubuntu/anaconda3/envs/sasa2/lib/python3.7/site-packages/spconv/libcuhash.so .

3. 出现错误的原因
不清楚

# 训练报错
## 解决

/home/ubuntu/codes/2025codes/SASA/pcdet/ops/pointnet2/pointnet2_batch/pointnet2_modules.py
将 =* 改为:

            new_features = new_features * idx_cnt_mask
            
##　分析原因
“In-place运算是一种直接改变给定线性函数、向量、矩阵(张量)内容而不复制的运算。"

出现了inplace操作,不产生新对象,在不改变存储地址的前提下直接修改值(原地赋值),会导致覆盖了计算梯度所需的值.

典型的inplace操作包括:+=, *=, 给切片赋值a[:,1:,:,:]=func1(a[:,1:,:,:]),torch.relu(inplace=True) torch.sigmoid(inplace=True)

```
在autograd支持in-place操作是一件困难的事情，我们在大多数情况下不鼓励使用它们。Autograd的主动缓冲区释放和重用使其非常高效，在很少情况下，in-place操作实际上会显著降低内存使用量。除非你正在承受巨大的内存压力，否则你可能永远都不需要使用它们。

限制in-place作业的适用性的主要原因有两个：

1、in-place操作可能会覆盖计算梯度所需的值。

2、每个in-place操作实际上都需要实现重写计算图。Out-of-place版本只是简单地分配新对象并保持对旧图的引用，而in-place操作则要求将所有输入的创建者更改为表示该操作的函数。
```

因此,叶子节点不要使用inpalce.

参考:
https://discuss.pytorch.org/t/runtimeerror-one-of-the-variables-needed-for-gradient-computation-has-been-modified-by-an-inplace-operation-torch-cuda-floattensor-1-1-256-256-which-is-output-0-of-relubackward0-is-at-version-1-expected-version-0-instead/143490/7

https://github.com/open-mmlab/mmocr/pull/884

https://blog.csdn.net/weixin_46917495/article/details/127616022

https://zhuanlan.zhihu.com/p/588994442

## 报错内容
RuntimeError: one of the variables needed for gradient computation has been modified by an inplace operation: [torch.cuda.FloatTensor [4, 1024, 256, 64]], which is output 0 of ReluBackward0, is at version 1; expected version 0 instead. Hint: the backtrace further above shows the operation that failed to compute its gradient. The variable in question was changed in there or anywhere later. Good luck!


RuntimeError: one of the variables needed for gradient computation has been modified by an inplace operation: [torch.cuda.FloatTensor [4, 1024, 256, 64]], which is output 0 of ReluBackward0, is at version 1; expected version 0 instead. Hint: enable anomaly detection to find the operation that failed to compute its gradient, with torch.autograd.set_detect_anomaly(True).


# 训练

python train.py --cfg_file cfgs/kitti_models/3dssd_sasa.yaml

# 数据集准备 成功
gt_database sample: 7481/7481
Database Pedestrian: 4487
Database Car: 28742
Database Cyclist: 1627
Database Van: 2914
Database Truck: 1094
Database Tram: 511
Database Misc: 973
Database Person_sitting: 222
---------------Data preparation Done---------------


# 准备数据集报错2
缺少一些img
kitti数据集的train和test所有7412张数据需要全部放在train文件夹下

# 准备数据集报错
TypeError: load() missing 1 required positional argument: 'Loader'
解决:
pip install pyyaml==5.3 

# 编译spconv报错:cudnn缺少
-- Caffe2: CUDA detected: 10.2
-- Caffe2: CUDA nvcc is: /usr/local/cuda/bin/nvcc
-- Caffe2: CUDA toolkit directory: /usr/local/cuda
-- Caffe2: Header version is: 10.2
-- Could NOT find CUDNN (missing: CUDNN_LIBRARY_PATH CUDNN_INCLUDE_PATH) 
CMake Warning at /home/ubuntu/anaconda3/envs/sasa2/lib/python3.7/site-packages/torch/share/cmake/Caffe2/public/cuda.cmake:111 (message):
  Caffe2: Cannot find cuDNN library.  Turning the option off
Call Stack (most recent call first):
  /home/ubuntu/anaconda3/envs/sasa2/lib/python3.7/site-packages/torch/share/cmake/Caffe2/Caffe2Config.cmake:88 (include)
  /home/ubuntu/anaconda3/envs/sasa2/lib/python3.7/site-packages/torch/share/cmake/Torch/TorchConfig.cmake:68 (find_package)
  CMakeLists.txt:23 (find_package)

  Your installed Caffe2 version uses cuDNN but I cannot find the cuDNN
  libraries.  Please set the proper cuDNN prefixes and / or install cuDNN.

## 解决:安装cudnn
1. 官网下载cudnn 7.6.5
三个deb
2. 安装
sudo dpkg -i libcudnn7_7.6.5.32-1+cuda10.2_amd64.deb 
sudo dpkg -i libcudnn7-dev_7.6.5.32-1+cuda10.2_amd64.deb 
sudo dpkg -i libcudnn7-doc_7.6.5.32-1+cuda10.2_amd64.deb 
3. 安装成功
即使安装成功也无法使用查看版本的方式判断:
cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
会报错
但是spconv编译通过了~

# 关于科学上网
使用clash的时候,需要打开系统设置的proxy,就可以上google了
但是terminal中如果使用了proxy,会导致下载不下来pytorch(下面的pytorch安装命令的网址一直在retry)
所以需要在终端将proxy删掉

export http_proxy=''
export https_proxy=''
export socks_proxy=''
export all_proxy=''

# 编译spconv报错:cuda版本太低
-- Caffe2: CUDA detected: 10.0
-- Caffe2: CUDA nvcc is: /usr/local/cuda-10.0/bin/nvcc
-- Caffe2: CUDA toolkit directory: /usr/local/cuda-10.0
CMake Error at /home/ubuntu/anaconda3/envs/sasa/lib/python3.7/site-packages/torch/share/cmake/Caffe2/public/cuda.cmake:42 (message):
  PyTorch requires CUDA 10.2 or above.

##　解决:修改setup.py，指定编译的cuda版本        
cmake_args = [# '-G "Visual Studio 15 2017 Win64"',
                      '-DCMAKE_PREFIX_PATH={}'.format(LIBTORCH_ROOT),
                      '-DPYBIND11_PYTHON_VERSION={}'.format(PYTHON_VERSION),
                      '-DSPCONV_BuildTests=OFF',
                      '-DPYTORCH_VERSION={}'.format(PYTORCH_VERSION_NUMBER),
            '-DCMAKE_CUDA_COMPILER=/usr/local/cuda-10.2/bin/nvcc'
        ] #  -arch=sm_61


# 安装torch 
pip install torch==1.10.0+cu102 torchvision==0.11.0+cu102 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html

