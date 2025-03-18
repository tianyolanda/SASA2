# Main Results

## Results on KITTI Dataset.
[x] car 
[ ] ped 
    重新训练,降低2个点
    直接使用sasa的结果,降低0.5个点
    []调整一下radius\maxmin等参数再测试
[ ] cyc
sasa:[3d   AP:89.2252, 69.9372, 65.2625] 
dsasa重新训练:[3d   AP:89.9093, 69.5442, 64.9459] easy的有0.7提升,其余降低0.4
dsasa不训练:[3d   AP:89.0262, 69.5176, 65.1980]
降低0.2个点
    []调整一下radius\maxmin等参数再测试

## Results on nuScenes Dataset.
[ ] all classes
cuda显存不够
尝试多显卡,目前会卡住
## Results on CADC Dataset.
[ ] all classes
下载地址无
让孙文蔚去找

## Results on DENSE Dataset.
[ ] all classes
数据集下载太慢
需要u盘拷贝
已拷完

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
