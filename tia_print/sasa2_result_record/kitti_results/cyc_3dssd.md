# 3dssd
==epoch 79==
 INFO  Cyclist AP@0.50, 0.50, 0.50:
bbox AP:86.5355, 71.7027, 69.9779
bev  AP:84.9679, 67.7836, 63.5694
3d   AP:82.9133, 63.3856, 60.7885
aos  AP:86.47, 70.81, 68.98
Cyclist AP_R40@0.50, 0.50, 0.50:
bbox AP:90.1694, 73.0016, 69.8916
bev  AP:88.4209, 67.5169, 63.5569
[3d   AP:85.0599, 63.8522, 60.2338]
aos  AP:90.08, 71.97, 68.90
Cyclist AP@0.50, 0.25, 0.25:
bbox AP:86.5355, 71.7027, 69.9779
bev  AP:86.2091, 70.6430, 68.3808
3d   AP:86.2091, 70.6044, 68.2018
aos  AP:86.47, 70.81, 68.98
Cyclist AP_R40@0.50, 0.25, 0.25:
bbox AP:90.1694, 73.0016, 69.8916
bev  AP:89.6985, 71.6024, 68.8121
3d   AP:89.6974, 71.5253, 68.7328
aos  AP:90.08, 71.97, 68.90

# 3dssd_sasa
 CUDA_VISIBLE_DEVICES=0 python test.py --cfg_file cfgs/kitti_models/3dssd_sasa.yaml --ckpt  ../output/kitti_models/cyc/3dssd_sasa/default/ckpt/checkpoint_epoch_80.pth
==epoch 80 ==
2025-03-14 02:29:00,311   INFO  *************** EPOCH 80 EVALUATION *****************
2025-03-14 02:32:42,360   INFO  *************** Performance of EPOCH 80 *****************
2025-03-14 02:32:42,361   INFO  Generate label finished(sec_per_example: 0.0589 second).
2025-03-14 02:32:42,361   INFO  recall_roi_0.3: 0.000000
2025-03-14 02:32:42,361   INFO  recall_rcnn_0.3: 0.811870
2025-03-14 02:32:42,361   INFO  recall_roi_0.5: 0.000000
2025-03-14 02:32:42,361   INFO  recall_rcnn_0.5: 0.709966
2025-03-14 02:32:42,361   INFO  recall_roi_0.7: 0.000000
2025-03-14 02:32:42,361   INFO  recall_rcnn_0.7: 0.342665
2025-03-14 02:32:42,361   INFO  positive_point_L0S0: 5.573627
2025-03-14 02:32:42,361   INFO  recall_point_L0S0: 0.982083
2025-03-14 02:32:42,361   INFO  	- Cyclist: 0.982083
2025-03-14 02:32:42,361   INFO  positive_point_L1S0: 4.400371
2025-03-14 02:32:42,361   INFO  recall_point_L1S0: 0.980963
2025-03-14 02:32:42,361   INFO  	- Cyclist: 0.980963
2025-03-14 02:32:42,361   INFO  positive_point_L1S1: 0.409658
2025-03-14 02:32:42,361   INFO  recall_point_L1S1: 0.941769
2025-03-14 02:32:42,361   INFO  	- Cyclist: 0.941769
2025-03-14 02:32:42,361   INFO  positive_point_L2S0: 4.390024
2025-03-14 02:32:42,361   INFO  recall_point_L2S0: 0.979843
2025-03-14 02:32:42,361   INFO  	- Cyclist: 0.979843
2025-03-14 02:32:42,361   INFO  positive_point_L2S1: 0.193685
2025-03-14 02:32:42,361   INFO  recall_point_L2S1: 0.724524
2025-03-14 02:32:42,361   INFO  	- Cyclist: 0.724524
2025-03-14 02:32:42,361   INFO  positive_point_candidate: 4.390024
2025-03-14 02:32:42,361   INFO  recall_point_candidate: 0.979843
2025-03-14 02:32:42,361   INFO  	- Cyclist: 0.979843
2025-03-14 02:32:42,361   INFO  positive_point_vote: 5.297161
2025-03-14 02:32:42,361   INFO  recall_point_vote: 0.966405
2025-03-14 02:32:42,361   INFO  	- Cyclist: 0.966405
2025-03-14 02:32:42,362   INFO  positive_point_candidate: 4.390024
2025-03-14 02:32:42,362   INFO  recall_point_candidate: 0.979843
2025-03-14 02:32:42,362   INFO  	- Cyclist: 0.979843
2025-03-14 02:32:42,362   INFO  positive_point_vote: 5.297161
2025-03-14 02:32:42,362   INFO  recall_point_vote: 0.966405
2025-03-14 02:32:42,362   INFO  	- Cyclist: 0.966405
2025-03-14 02:32:42,364   INFO  Average predicted number of objects(3769 samples): 0.774
Cyclist AP@0.50, 0.50, 0.50:
bbox AP:88.4286, 78.3461, 76.0875
bev  AP:87.9809, 72.6733, 68.8697
3d   AP:85.9062, 69.4060, 64.4574
aos  AP:88.34, 77.38, 75.04
Cyclist AP_R40@0.50, 0.50, 0.50:
bbox AP:92.2186, 79.6552, 76.6392
bev  AP:91.6676, 73.9374, 69.4433
[3d   AP:89.2252, 69.9372, 65.2625] 
aos  AP:92.11, 78.58, 75.53
Cyclist AP@0.50, 0.25, 0.25:
bbox AP:88.4286, 78.3461, 76.0875
bev  AP:88.0957, 77.2920, 74.1510
3d   AP:88.0957, 77.2920, 74.1510
aos  AP:88.34, 77.38, 75.04
Cyclist AP_R40@0.50, 0.25, 0.25:
bbox AP:92.2186, 79.6552, 76.6392
bev  AP:91.8633, 78.7515, 74.8827
3d   AP:91.8633, 78.7515, 74.8827
aos  AP:92.11, 78.58, 75.53

## again
2025-03-17 12:21:01,363   INFO  *************** Performance of EPOCH 80 *****************
2025-03-17 12:21:01,363   INFO  Generate label finished(sec_per_example: 0.0583 second).
2025-03-17 12:21:01,363   INFO  recall_roi_0.3: 0.000000
2025-03-17 12:21:01,363   INFO  recall_rcnn_0.3: 0.809630
2025-03-17 12:21:01,363   INFO  recall_roi_0.5: 0.000000
2025-03-17 12:21:01,363   INFO  recall_rcnn_0.5: 0.696529
2025-03-17 12:21:01,363   INFO  recall_roi_0.7: 0.000000
2025-03-17 12:21:01,363   INFO  recall_rcnn_0.7: 0.338186
2025-03-17 12:21:01,363   INFO  positive_point_L0S0: 5.577341
2025-03-17 12:21:01,364   INFO  recall_point_L0S0: 0.982083
2025-03-17 12:21:01,364   INFO  	- Cyclist: 0.982083
2025-03-17 12:21:01,364   INFO  positive_point_L1S0: 4.384452
2025-03-17 12:21:01,364   INFO  recall_point_L1S0: 0.980963
2025-03-17 12:21:01,364   INFO  	- Cyclist: 0.980963
2025-03-17 12:21:01,364   INFO  positive_point_L1S1: 0.407270
2025-03-17 12:21:01,364   INFO  recall_point_L1S1: 0.930571
2025-03-17 12:21:01,364   INFO  	- Cyclist: 0.930571
2025-03-17 12:21:01,364   INFO  positive_point_L2S0: 4.372247
2025-03-17 12:21:01,364   INFO  recall_point_L2S0: 0.977604
2025-03-17 12:21:01,364   INFO  	- Cyclist: 0.977604
2025-03-17 12:21:01,364   INFO  positive_point_L2S1: 0.192889
2025-03-17 12:21:01,364   INFO  recall_point_L2S1: 0.721165
2025-03-17 12:21:01,365   INFO  	- Cyclist: 0.721165
2025-03-17 12:21:01,365   INFO  positive_point_candidate: 4.372247
2025-03-17 12:21:01,365   INFO  recall_point_candidate: 0.977604
2025-03-17 12:21:01,365   INFO  	- Cyclist: 0.977604
2025-03-17 12:21:01,365   INFO  positive_point_vote: 5.286283
2025-03-17 12:21:01,365   INFO  recall_point_vote: 0.967525
2025-03-17 12:21:01,365   INFO  	- Cyclist: 0.967525
2025-03-17 12:21:01,365   INFO  positive_point_candidate: 4.372247
2025-03-17 12:21:01,365   INFO  recall_point_candidate: 0.977604
2025-03-17 12:21:01,365   INFO  	- Cyclist: 0.977604
2025-03-17 12:21:01,365   INFO  positive_point_vote: 5.286283
2025-03-17 12:21:01,365   INFO  recall_point_vote: 0.967525
2025-03-17 12:21:01,366   INFO  	- Cyclist: 0.967525
2025-03-17 12:21:01,369   INFO  Average predicted number of objects(3769 samples): 0.771
2025-03-17 12:21:19,283   INFO  Cyclist AP@0.50, 0.50, 0.50:
bbox AP:88.2730, 77.9320, 76.2372
bev  AP:86.8573, 70.3930, 67.6966
3d   AP:85.2950, 67.2041, 63.3260
aos  AP:88.15, 77.45, 75.73
Cyclist AP_R40@0.50, 0.50, 0.50:
bbox AP:92.7026, 79.4797, 76.6585
bev  AP:90.9342, 70.8995, 67.5828
[3d   AP:88.9089, 67.6154, 64.1170] **this one**
aos  AP:92.55, 78.94, 76.13
Cyclist AP@0.50, 0.25, 0.25:
bbox AP:88.2730, 77.9320, 76.2372
bev  AP:91.1451, 76.2074, 73.7804
3d   AP:91.1402, 76.1812, 73.7718
aos  AP:88.15, 77.45, 75.73
Cyclist AP_R40@0.50, 0.25, 0.25:
bbox AP:92.7026, 79.4797, 76.6585
bev  AP:93.0529, 77.9992, 74.4095
3d   AP:93.0500, 77.4472, 74.4014
aos  AP:92.55, 78.94, 76.13


# 3dssd_dsasa
    # density_factor = (1 + density ** weight)/2
    
 CUDA_VISIBLE_DEVICES=0 python test.py --cfg_file cfgs/kitti_models/3dssd_dsasa_cyc.yaml --ckpt  ../output/kitti_models/cyc/3dssd_dsasa_0.5/default/ckpt/checkpoint_epoch_80.pth
 
  CUDA_VISIBLE_DEVICES=0 python test.py --cfg_file cfgs/kitti_models/cyc/3dssd_dsasa.yaml --ckpt  ../output/kitti_models/cyc/3dssd_dsasa_0.5/default/ckpt/checkpoint_epoch_80.pth


    
==epoch 80==
INFO  Cyclist AP@0.50, 0.50, 0.50:
bbox AP:92.4711, 78.5431, 74.9186
bev  AP:90.9357, 73.9561, 68.6706
3d   AP:86.1002, 68.6710, 64.7428
aos  AP:92.30, 77.86, 74.32
Cyclist AP_R40@0.50, 0.50, 0.50:
bbox AP:94.2490, 79.7408, 76.5998
bev  AP:92.6933, 74.3362, 69.7537
[3d   AP:89.9093, 69.5442, 64.9459]
aos  AP:94.08, 79.04, 75.88
Cyclist AP@0.50, 0.25, 0.25:
bbox AP:92.4711, 78.5431, 74.9186
bev  AP:91.1069, 76.4255, 72.4898
3d   AP:91.1015, 76.4205, 72.4842
aos  AP:92.30, 77.86, 74.32
Cyclist AP_R40@0.50, 0.25, 0.25:
bbox AP:94.2490, 79.7408, 76.5998
bev  AP:93.5234, 77.7952, 73.9834
3d   AP:93.5219, 77.7722, 73.9420
aos  AP:94.08, 79.04, 75.88

## again
 INFO  Cyclist AP@0.50, 0.50, 0.50:
bbox AP:88.9057, 79.0540, 75.0291
bev  AP:87.2199, 72.0816, 66.7251
3d   AP:85.8075, 68.2772, 64.3954
aos  AP:88.71, 78.31, 74.30
Cyclist AP_R40@0.50, 0.50, 0.50:
bbox AP:93.9307, 80.8357, 76.9885
bev  AP:91.4846, 72.5803, 67.9882
[3d   AP:88.2077, 68.9389, 64.3450]
aos  AP:93.68, 80.00, 76.14
Cyclist AP@0.50, 0.25, 0.25:
bbox AP:88.9057, 79.0540, 75.0291
bev  AP:93.2591, 77.1584, 74.3903
3d   AP:87.7766, 77.0655, 74.3324
aos  AP:88.71, 78.31, 74.30
Cyclist AP_R40@0.50, 0.25, 0.25:
bbox AP:93.9307, 80.8357, 76.9885
bev  AP:94.3276, 78.4539, 74.8368
3d   AP:92.6374, 78.3152, 74.7532
aos  AP:93.68, 80.00, 76.14

## again
INFO  Cyclist AP@0.50, 0.50, 0.50:
bbox AP:89.1364, 79.0172, 76.8883
bev  AP:87.3113, 72.4816, 68.7912
3d   AP:85.2296, 68.6278, 65.0390
aos  AP:88.95, 78.17, 76.04
Cyclist AP_R40@0.50, 0.50, 0.50:
bbox AP:93.4805, 80.3903, 77.4460
bev  AP:91.0801, 72.7290, 68.9170
[3d   AP:87.2602, 69.8519, 65.6838]
aos  AP:93.28, 79.52, 76.53
Cyclist AP@0.50, 0.25, 0.25:
bbox AP:89.1364, 79.0172, 76.8883
bev  AP:87.6396, 76.5558, 74.0878
3d   AP:87.6396, 76.4191, 73.9472
aos  AP:88.95, 78.17, 76.04
Cyclist AP_R40@0.50, 0.25, 0.25:
bbox AP:93.4805, 80.3903, 77.4460
bev  AP:91.6500, 77.5199, 74.3946
3d   AP:91.6383, 77.4284, 74.2121
aos  AP:93.28, 79.52, 76.53

## again
INFO  Cyclist AP@0.50, 0.50, 0.50:
bbox AP:93.6535, 78.5331, 74.2239
bev  AP:87.3063, 71.4851, 67.6852
3d   AP:85.7442, 68.0710, 64.4945
aos  AP:93.40, 77.68, 73.46
Cyclist AP_R40@0.50, 0.50, 0.50:
bbox AP:95.1210, 80.0397, 76.4300
bev  AP:91.3875, 71.8504, 67.9745
[3d   AP:89.4379, 68.6203, 64.9387]
aos  AP:94.88, 79.13, 75.53
Cyclist AP@0.50, 0.25, 0.25:
bbox AP:93.6535, 78.5331, 74.2239
bev  AP:92.3039, 75.7448, 71.4610
3d   AP:92.3039, 75.7439, 71.4610
aos  AP:93.40, 77.68, 73.46
Cyclist AP_R40@0.50, 0.25, 0.25:
bbox AP:95.1210, 80.0397, 76.4300
bev  AP:93.6541, 77.1005, 73.3088
3d   AP:93.6541, 77.0993, 73.3079
aos  AP:94.88, 79.13, 75.53


## again
INFO  Cyclist AP@0.50, 0.50, 0.50:
bbox AP:88.5778, 78.2979, 74.2913
bev  AP:86.7866, 72.2029, 68.2424
3d   AP:86.1900, 68.6083, 64.8384
aos  AP:88.26, 77.44, 73.44
Cyclist AP_R40@0.50, 0.50, 0.50:
bbox AP:93.2568, 79.4623, 76.4307
bev  AP:91.0233, 72.9422, 68.3172
[3d   AP:88.8091, 69.5390, 65.5218] **this one**
aos  AP:92.92, 78.53, 75.46
Cyclist AP@0.50, 0.25, 0.25:
bbox AP:88.5778, 78.2979, 74.2913
bev  AP:87.3191, 75.7709, 71.9123
3d   AP:87.3191, 75.7709, 71.9123
aos  AP:88.26, 77.44, 73.44
Cyclist AP_R40@0.50, 0.25, 0.25:
bbox AP:93.2568, 79.4623, 76.4307
bev  AP:91.7567, 77.2374, 73.5261
3d   AP:91.7567, 77.2374, 73.5261
aos  AP:92.92, 78.53, 75.46

## again (使用3dssd_sasa的模型,3dssd_dsasa的cfg)
 CUDA_VISIBLE_DEVICES=0 python test.py --cfg_file cfgs/kitti_models/3dssd_dsasa_cyc.yaml --ckpt  ../output/kitti_models/cyc/3dssd_sasa/default/ckpt/checkpoint_epoch_80.pth
 
2025-03-17 11:47:09,786   INFO  Cyclist AP@0.50, 0.50, 0.50:
bbox AP:88.4227, 77.5629, 73.4575
bev  AP:87.8451, 72.1889, 68.5952
3d   AP:86.3645, 69.0607, 64.3989
aos  AP:88.31, 77.04, 72.93
Cyclist AP_R40@0.50, 0.50, 0.50:
bbox AP:92.0034, 78.2514, 75.1325
bev  AP:91.1729, 73.0341, 68.6284
[3d   AP:89.0262, 69.5176, 65.1980] 
aos  AP:91.88, 77.68, 74.54
Cyclist AP@0.50, 0.25, 0.25:
bbox AP:88.4227, 77.5629, 73.4575
bev  AP:88.0868, 76.9396, 74.2539
3d   AP:88.0868, 76.9311, 74.2502
aos  AP:88.31, 77.04, 72.93
Cyclist AP_R40@0.50, 0.25, 0.25:
bbox AP:92.0034, 78.2514, 75.1325
bev  AP:91.7306, 77.8428, 74.5562
3d   AP:91.7300, 77.7964, 74.5098
aos  AP:91.88, 77.68, 74.54

第二次
2025-03-17 12:11:04,011   INFO  Cyclist AP@0.50, 0.50, 0.50:
bbox AP:88.0198, 77.1683, 73.5075
bev  AP:87.0806, 70.5488, 67.2303
3d   AP:85.9558, 67.8310, 64.1954
aos  AP:87.94, 76.47, 72.79
Cyclist AP_R40@0.50, 0.50, 0.50:
bbox AP:92.0478, 78.9325, 75.4232
bev  AP:90.9669, 71.0170, 67.1551
3d   AP:89.9620, 68.8811, 64.5109
aos  AP:91.94, 78.12, 74.61
Cyclist AP@0.50, 0.25, 0.25:
bbox AP:88.0198, 77.1683, 73.5075
bev  AP:87.4457, 75.8778, 73.5843
3d   AP:87.4457, 75.8763, 73.5836
aos  AP:87.94, 76.47, 72.79
Cyclist AP_R40@0.50, 0.25, 0.25:
bbox AP:92.0478, 78.9325, 75.4232
bev  AP:91.6688, 77.2428, 74.0799
3d   AP:91.6688, 77.2422, 74.0793
aos  AP:91.94, 78.12, 74.61


# 3dssd_dsasa
    # density_factor =  density ** weight
==epoch 80==
INFO  Cyclist AP@0.50, 0.50, 0.50:
bbox AP:87.9224, 77.4350, 73.2534
bev  AP:85.8186, 68.5378, 64.4353
3d   AP:84.9308, 67.3301, 62.4710
aos  AP:87.81, 76.79, 72.61
Cyclist AP_R40@0.50, 0.50, 0.50:
bbox AP:92.6957, 78.5843, 75.1197
bev  AP:88.6183, 69.4757, 64.9087
[3d   AP:87.6895, 67.4017, 62.6294]
aos  AP:92.56, 77.91, 74.40
Cyclist AP@0.50, 0.25, 0.25:
bbox AP:87.9224, 77.4350, 73.2534
bev  AP:86.6914, 75.5796, 72.3046
3d   AP:86.6914, 75.2811, 70.3961
aos  AP:87.81, 76.79, 72.61
Cyclist AP_R40@0.50, 0.25, 0.25:
bbox AP:92.6957, 78.5843, 75.1197
bev  AP:91.2410, 76.8551, 72.5347
3d   AP:91.2382, 76.1171, 71.7253
aos  AP:92.56, 77.91, 74.40


