# pointrcnn
    CUDA_VISIBLE_DEVICES=0 python train.py --cfg_file cfgs/kitti_models/cyc/pointrcnn.yaml 

2025-03-27 01:10:17,228   INFO  recall_roi_0.3: 0.924972
2025-03-27 01:10:17,228   INFO  recall_rcnn_0.3: 0.923852
2025-03-27 01:10:17,228   INFO  recall_roi_0.5: 0.856663
2025-03-27 01:10:17,228   INFO  recall_rcnn_0.5: 0.862262
2025-03-27 01:10:17,228   INFO  recall_roi_0.7: 0.471445
2025-03-27 01:10:17,228   INFO  recall_rcnn_0.7: 0.507279
2025-03-27 01:10:17,231   INFO  Average predicted number of objects(3769 samples): 0.620

2025-03-27 01:10:33,808   INFO  Cyclist AP@0.50, 0.50, 0.50:
bbox AP:93.0712, 82.2671, 79.5997
bev  AP:91.2233, 77.1384, 72.0829
3d   AP:87.6709, 73.6225, 70.5343
aos  AP:92.85, 81.29, 78.68
Cyclist AP_R40@0.50, 0.50, 0.50:
bbox AP:96.5251, 84.7035, 80.2088
bev  AP:94.2660, 77.9066, 73.3163
[3d   AP:91.7778, 75.5811, 71.0154]
aos  AP:96.31, 83.65, 79.21
Cyclist AP@0.50, 0.25, 0.25:
bbox AP:93.0712, 82.2671, 79.5997
bev  AP:91.8944, 79.5816, 76.8876
3d   AP:91.8944, 79.5816, 76.8876
aos  AP:92.85, 81.29, 78.68
Cyclist AP_R40@0.50, 0.25, 0.25:
bbox AP:96.5251, 84.7035, 80.2088
bev  AP:95.2582, 81.7987, 77.2793
3d   AP:95.2582, 81.7987, 77.2793
aos  AP:96.31, 83.65, 79.21

# pointrcnn_sasa
        CUDA_VISIBLE_DEVICES=0 python train.py --cfg_file cfgs/kitti_models/cyc/pointrcnn_sasa.yaml 

2025-03-29 02:15:13,007   INFO  *************** Performance of EPOCH 71 *****************
2025-03-29 02:15:13,007   INFO  Generate label finished(sec_per_example: 0.1020 second).
2025-03-29 02:15:13,007   INFO  recall_roi_0.3: 0.938410
2025-03-29 02:15:13,008   INFO  recall_rcnn_0.3: 0.938410
2025-03-29 02:15:13,008   INFO  recall_roi_0.5: 0.888018
2025-03-29 02:15:13,008   INFO  recall_rcnn_0.5: 0.890258
2025-03-29 02:15:13,008   INFO  recall_roi_0.7: 0.518477
2025-03-29 02:15:13,008   INFO  recall_rcnn_0.7: 0.499440
2025-03-29 02:15:13,010   INFO  Average predicted number of objects(3769 samples): 1.027

2025-03-29 02:15:30,837   INFO  Cyclist AP@0.50, 0.50, 0.50:
bbox AP:91.2424, 81.0971, 77.3025
bev  AP:87.9522, 76.1515, 70.8502
3d   AP:87.7718, 73.9052, 69.1390
aos  AP:91.15, 80.50, 76.68
Cyclist AP_R40@0.50, 0.50, 0.50:
bbox AP:96.0080, 82.6230, 79.1253
bev  AP:93.4666, 76.9851, 72.4033
[3d   AP:93.1348, 74.6689, 70.1785]
aos  AP:95.90, 81.96, 78.44
Cyclist AP@0.50, 0.25, 0.25:
bbox AP:91.2424, 81.0971, 77.3025
bev  AP:95.8932, 78.5979, 74.5540
3d   AP:95.8932, 78.5979, 74.5540
aos  AP:91.15, 80.50, 76.68
Cyclist AP_R40@0.50, 0.25, 0.25:
bbox AP:96.0080, 82.6230, 79.1253
bev  AP:96.2992, 80.2590, 75.9401
3d   AP:96.2992, 80.2590, 75.9401
aos  AP:95.90, 81.96, 78.44