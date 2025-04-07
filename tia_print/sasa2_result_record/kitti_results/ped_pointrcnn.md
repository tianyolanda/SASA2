# pointrcnn
         CUDA_VISIBLE_DEVICES=1 python train.py --cfg_file cfgs/kitti_models/ped/pointrcnn.yaml 

epoch_74 

2025-03-27 01:56:43,096   INFO  Generate label finished(sec_per_example: 0.1078 second).
2025-03-27 01:56:43,096   INFO  recall_roi_0.3: 0.819298
2025-03-27 01:56:43,096   INFO  recall_rcnn_0.3: 0.821491
2025-03-27 01:56:43,096   INFO  recall_roi_0.5: 0.729825
2025-03-27 01:56:43,096   INFO  recall_rcnn_0.5: 0.739912
2025-03-27 01:56:43,096   INFO  recall_roi_0.7: 0.298246
2025-03-27 01:56:43,096   INFO  recall_rcnn_0.7: 0.366667
2025-03-27 01:56:43,099   INFO  Average predicted number of objects(3769 samples): 3.598
2025-03-27 01:56:53,497   INFO  Pedestrian AP@0.50, 0.50, 0.50:
bbox AP:73.2288, 66.1624, 61.1247
bev  AP:72.2713, 63.4105, 56.6662
3d   AP:69.6468, 60.8283, 53.5663
aos  AP:71.68, 64.22, 58.88
Pedestrian AP_R40@0.50, 0.50, 0.50:
bbox AP:74.8006, 67.2055, 60.7964
bev  AP:72.7024, 63.6436, 56.5229
[3d   AP:69.4389, 60.1026, 52.9259]
aos  AP:73.12, 65.03, 58.39
Pedestrian AP@0.50, 0.25, 0.25:
bbox AP:73.2288, 66.1624, 61.1247
bev  AP:81.7824, 74.7855, 68.3943
3d   AP:81.7550, 74.6733, 68.0328
aos  AP:71.68, 64.22, 58.88
Pedestrian AP_R40@0.50, 0.25, 0.25:
bbox AP:74.8006, 67.2055, 60.7964
bev  AP:82.6078, 75.7322, 68.5059
3d   AP:82.5862, 75.4836, 68.2690
aos  AP:73.12, 65.03, 58.39

# pointrcnn_sasa
         CUDA_VISIBLE_DEVICES=1 python train.py --cfg_file cfgs/kitti_models/ped/pointrcnn_sasa.yaml 

epoch_71

2025-03-29 02:52:36,467   INFO  *************** Performance of EPOCH 71 *****************
2025-03-29 02:52:36,467   INFO  Generate label finished(sec_per_example: 0.1083 second).
2025-03-29 02:52:36,467   INFO  recall_roi_0.3: 0.704825
2025-03-29 02:52:36,467   INFO  recall_rcnn_0.3: 0.708772
2025-03-29 02:52:36,467   INFO  recall_roi_0.5: 0.592544
2025-03-29 02:52:36,467   INFO  recall_rcnn_0.5: 0.619298
2025-03-29 02:52:36,467   INFO  recall_roi_0.7: 0.225000
2025-03-29 02:52:36,467   INFO  recall_rcnn_0.7: 0.327632
2025-03-29 02:52:36,470   INFO  Average predicted number of objects(3769 samples): 1.858

2025-03-29 02:53:05,186   INFO  Pedestrian AP@0.50, 0.50, 0.50:
bbox AP:64.7277, 59.3889, 55.3390
bev  AP:63.2176, 55.5284, 50.1502
3d   AP:60.6779, 53.7227, 46.5935
aos  AP:63.62, 57.78, 53.62
Pedestrian AP_R40@0.50, 0.50, 0.50:
bbox AP:64.8330, 59.1872, 54.0793
bev  AP:62.9953, 55.4846, 48.9043
[3d   AP:60.1516, 52.4282, 45.7060]
aos  AP:63.57, 57.45, 52.19
Pedestrian AP@0.50, 0.25, 0.25:
bbox AP:64.7277, 59.3889, 55.3390
bev  AP:71.5718, 66.4445, 61.8269
3d   AP:71.5271, 66.3150, 61.3622
aos  AP:63.62, 57.78, 53.62
Pedestrian AP_R40@0.50, 0.25, 0.25:
bbox AP:64.8330, 59.1872, 54.0793
bev  AP:73.2762, 67.5004, 61.8781
3d   AP:73.2271, 67.3250, 61.6091
aos  AP:63.57, 57.45, 52.19

