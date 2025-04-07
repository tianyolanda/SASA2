# 3dssd
CUDA_VISIBLE_DEVICES=1 python test.py --cfg_file cfgs/kitti_models/car/3dssd.yaml --ckpt ../output/kitti_models/car/3dssd/default/ckpt/checkpoint_epoch_80.pth

==epoch 80==

INFO  Car AP@0.70, 0.70, 0.70:
bbox AP:96.6303, 89.8601, 89.2231
bev  AP:90.1650, 88.3721, 87.2458
3d   AP:88.8634, 78.9477, 78.0350
aos  AP:96.59, 89.79, 89.10
Car AP_R40@0.70, 0.70, 0.70:
bbox AP:98.2676, 95.0057, 92.5373
bev  AP:95.1056, 91.2226, 88.7855
[3d   AP:91.4175, 82.7117, 80.0564]
aos  AP:98.24, 94.91, 92.39
Car AP@0.70, 0.50, 0.50:
bbox AP:96.6303, 89.8601, 89.2231
bev  AP:96.7127, 89.9460, 89.4696
3d   AP:96.6540, 89.9232, 89.4066
aos  AP:96.59, 89.79, 89.10
Car AP_R40@0.70, 0.50, 0.50:
bbox AP:98.2676, 95.0057, 92.5373
bev  AP:98.3097, 95.2831, 94.8271
3d   AP:98.2736, 95.2167, 94.6870
aos  AP:98.24, 94.91, 92.39

# sasa
CUDA_VISIBLE_DEVICES=1 python test.py --cfg_file cfgs/kitti_models/car/3dssd_sasa.yaml --ckpt ../output/kitti_models/car/3dssd_sasa/default/ckpt/checkpoint_epoch_80.pth

epoch 80

INFO  Car AP@0.70, 0.70, 0.70:
bbox AP:96.8118, 90.1745, 89.6547
bev  AP:90.2334, 88.5069, 87.3765
3d   AP:89.1396, 84.3921, 78.6972
aos  AP:96.77, 90.09, 89.53
Car AP_R40@0.70, 0.70, 0.70:
bbox AP:98.5238, 95.3692, 92.9543
bev  AP:95.0813, 91.1508, 88.9602
[3d   AP:91.8367, 84.7708, 82.4250]
aos  AP:98.50, 95.26, 92.80
Car AP@0.70, 0.50, 0.50:
bbox AP:96.8118, 90.1745, 89.6547
bev  AP:96.8710, 90.1926, 89.7419
3d   AP:96.8122, 90.1801, 89.7068
aos  AP:96.77, 90.09, 89.53
Car AP_R40@0.70, 0.50, 0.50:
bbox AP:98.5238, 95.3692, 92.9543
bev  AP:98.5262, 95.5716, 95.1292
3d   AP:98.5015, 95.5298, 95.0258
aos  AP:98.50, 95.26, 92.80


# dsasa
## density_factor = (1 + density ** weight)/2
CUDA_VISIBLE_DEVICES=0 python test.py --cfg_file cfgs/kitti_models/car/3dssd_dsasa.yaml --ckpt ../output/kitti_models/car/3dssd_dsasa_0.5/default/ckpt/checkpoint_epoch_79.pth

epoch 79

INFO  Car AP@0.70, 0.70, 0.70:
bbox AP:97.0815, 90.1522, 89.6292
bev  AP:90.3288, 88.6558, 87.4646
3d   AP:89.4129, 84.7273, 78.7853
aos  AP:97.05, 90.11, 89.53
Car AP_R40@0.70, 0.70, 0.70:
bbox AP:98.5677, 95.4402, 92.9627
bev  AP:95.2575, 91.4689, 89.0832
[3d   AP:92.3083, 85.1426, 82.6005]
aos  AP:98.55, 95.37, 92.84
Car AP@0.70, 0.50, 0.50:
bbox AP:97.0815, 90.1522, 89.6292
bev  AP:97.1684, 90.1723, 89.7108
3d   AP:97.0960, 90.1502, 89.6684
aos  AP:97.05, 90.11, 89.53
Car AP_R40@0.70, 0.50, 0.50:
bbox AP:98.5677, 95.4402, 92.9627
bev  AP:98.6887, 95.6235, 95.1262
3d   AP:98.6316, 95.5558, 94.9909
aos  AP:98.55, 95.37, 92.84

## density_factor =  density ** weight
epoch 80

INFO  Car AP@0.70, 0.70, 0.70:
bbox AP:96.8118, 90.1745, 89.6547
bev  AP:90.2334, 88.5069, 87.3765
3d   AP:89.1396, 84.3921, 78.6972
aos  AP:96.77, 90.09, 89.53
Car AP_R40@0.70, 0.70, 0.70:
bbox AP:98.5238, 95.3692, 92.9543
bev  AP:95.0813, 91.1508, 88.9602
3d   AP:91.8367, 84.7708, 82.4250
aos  AP:98.50, 95.26, 92.80
Car AP@0.70, 0.50, 0.50:
bbox AP:96.8118, 90.1745, 89.6547
bev  AP:96.8710, 90.1926, 89.7419
3d   AP:96.8122, 90.1801, 89.7068
aos  AP:96.77, 90.09, 89.53
Car AP_R40@0.70, 0.50, 0.50:
bbox AP:98.5238, 95.3692, 92.9543
bev  AP:98.5262, 95.5716, 95.1292
3d   AP:98.5015, 95.5298, 95.0258
aos  AP:98.50, 95.26, 92.80

CUDA_VISIBLE_DEVICES=1 python train.py --cfg_file cfgs/kitti_models/3dssd_dsasa.yaml --epochs 90 --pretrained_model ../output/kitti_models/3dssd_dsasa/default/ckpt/checkpoint_epoch_80.pth
