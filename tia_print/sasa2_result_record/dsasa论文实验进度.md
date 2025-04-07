# Main Results

## Results on KITTI Dataset.
[x] car 
[ ] ped
    整体低 
    重新训练,降低2个点
    直接使用sasa的结果,降低0.5个点
    []调整一下radius\maxmin等参数再测试
    [x]调整一下数据扩增的rotation等参数训练
    使用tanet的参数比原始参数还低2个点
    [x]训练pointrcnn的ped
    baseline [3d   AP:69.4389, 60.1026, 52.9259]
    baseline+sasa [3d   AP:60.1516, 52.4282, 45.7060]

[ ] cyc
sasa:[3d   AP:89.2252, 69.9372, 65.2625] 
dsasa重新训练:[3d   AP:89.9093, 69.5442, 64.9459] easy的有0.7提升,其余降低0.4
dsasa不训练:[3d   AP:89.0262, 69.5176, 65.1980]
降低0.2个点
    []调整一下radius\maxmin等参数再测试
    [x]训练pointrcnn的cyc
    baseline: [3d   AP:91.7778, 75.5811, 71.0154]
    baseline+sasa:[3d   AP:93.1348, 74.6689, 70.1785]


## Results on nuScenes Dataset.
[ ] all classes
cuda显存不够
尝试多显卡,目前会卡住
## Results on CADC Dataset.
[ ] all classes
已下载

## Results on DENSE Dataset.
[ ] all classes
- [x] 加入snow噪声点的代码运行/qt可视化 ok
- [x] 数据集读取ok (dense_dataset.py中有很多需要修改的路径bug)
- [ ] 但训练模型不行:lidar_snow_sim所用pcdet的版本(1.0) 和sasa2(0.3)不一样, 无法直接运行

## Inference Speed.
[ ] kitti

# Ablation Study 

## Effects of Semantics-guided Point Sampling.
[ ] kitti car 3dssd baseline, 调节使用fps\ffps\sfps\sdfps
[ ] 找 Visualization results
[x] 统计 point recall (名字应该叫box recall) 保留的正样本点,所属的物体的数目(同Appendix)
the proportion of GT boxes that have at least one internal sample point comparing to the total number of GT boxes
[x] 统计 召回的point的数目(同Appendix)
[ ] 保留的同一物体的正样本点的分散程度 (需要写代码)
## Effects of density-based Point Segmentation Layer.
同上
## Effects of Semantics Balance Factor.
[ ] 调节sdfps的weight decay (不用训练)

# Compatibility Study

## Results on KITTI Dataset.
[x] 3dssd+sa+dsa > 3dssd+sa
[x] pointrcnn+sa+dsa > pointrcnn+sa

## Quantitative Analysis.
[x] Proposal recall rate under different numbers of
RoIs with and without SASA on PointRCNN.

## Qualitative Analysis.
[]

CUDA_VISIBLE_DEVICES=1 python demo.py --cfg_file cfgs/kitti_models/ped/3dssd.yaml --data_path ../data/kitti/testing/velodyne/ --ckpt ../output/kitti_models/car/3dssd/default/ckpt/checkpoint_epoch_71.pth

# Appendix: A Further Analysis of Point Sampling (此项合并到ablation study)

## A.1 Analysis of Sampling Performance
[x] 
无需训练直接测试
前景点的召回率不如sasa
注:不如sasa不代表不好
## A.2 Analysis of the Level 2 SA Layer
[x] 
无需训练直接测试
前景点的召回率不如sasa
注:不如sasa不代表不好
