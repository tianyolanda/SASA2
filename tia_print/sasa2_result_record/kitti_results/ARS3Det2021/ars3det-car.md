 ubuntu@ubuntu-tt:~/disk2/models/1TALite/models3.0$ gedit ./car/52m_fhd_rpn128/vehicle/model_paper_use/cb_rbrc.p_sv_combine_dc.IALL.Last_scse.ca_rw1/log_dir_2/log.txt


Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:75.08, 66.84, 62.87
bev  AP:82.89, 74.45, 71.34
3d   AP:22.28, 23.23, 23.01
aos  AP:3.83, 5.49, 6.89
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:75.08, 66.84, 62.87
bev  AP:87.30, 84.56, 81.90
3d   AP:86.81, 83.06, 76.64
aos  AP:3.83, 5.49, 6.89
Car bbox_mAP(sigma(all_difficulties)/3):@68.26
Car bev_mAP(sigma(all_difficulties)/3):@76.22
Car 3d_mAP(sigma(all_difficulties)/3):@22.84
Car aos_mAP(sigma(all_difficulties)/3):@5.40
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:22.35, 19.78, 15.97
bev  AP:14.62, 15.47, 14.01
3d   AP:1.38, 2.46, 1.64
aos  AP:12.06, 3.43, 2.52
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:22.35, 19.78, 15.97
bev  AP:25.20, 23.45, 20.14
3d   AP:24.79, 22.79, 18.58
aos  AP:12.06, 3.43, 2.52
Van bbox_mAP(sigma(all_difficulties)/3):@19.36
Van bev_mAP(sigma(all_difficulties)/3):@14.70
Van 3d_mAP(sigma(all_difficulties)/3):@1.83
Van aos_mAP(sigma(all_difficulties)/3):@6.00
bbox_mAP(sigma(allclass_mod)/num_cls):43.30988553093614
bev_mAP(sigma(allclass_mod)/num_cls):44.961534447004404
3d_mAP(sigma(allclass_mod)/num_cls):12.848531443671225
aos_mAP(sigma(allclass_mod)/num_cls):4.461041223333391

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:50.70, 48.10, 46.08
bev  AP:56.65, 53.68, 51.47
3d   AP:32.56, 30.94, 29.13
aos  AP:2.53, 4.11, 5.22
Van coco AP@0.50:0.05:0.95:
bbox AP:13.88, 13.51, 11.28
bev  AP:11.82, 11.37, 9.90
3d   AP:6.61, 6.30, 5.26
aos  AP:6.69, 2.37, 1.78

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:33.60, 34.35, 34.97
bev  AP:84.94, 75.52, 71.51
3d   AP:1.50, 2.29, 2.57
aos  AP:1.19, 1.92, 2.99
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:33.60, 34.35, 34.97
bev  AP:88.98, 85.57, 82.32
3d   AP:85.66, 79.89, 74.39
aos  AP:1.19, 1.92, 2.99
Car bbox_mAP(sigma(all_difficulties)/3):@34.31
Car bev_mAP(sigma(all_difficulties)/3):@77.32
Car 3d_mAP(sigma(all_difficulties)/3):@2.12
Car aos_mAP(sigma(all_difficulties)/3):@2.03
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:16.48, 14.61, 12.95
bev  AP:17.33, 14.06, 10.76
3d   AP:0.84, 1.31, 0.95
aos  AP:0.01, 0.35, 0.33
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:16.48, 14.61, 12.95
bev  AP:32.86, 26.57, 22.17
3d   AP:25.18, 23.21, 18.45
aos  AP:0.01, 0.35, 0.33
Van bbox_mAP(sigma(all_difficulties)/3):@14.68
Van bev_mAP(sigma(all_difficulties)/3):@14.05
Van 3d_mAP(sigma(all_difficulties)/3):@1.04
Van aos_mAP(sigma(all_difficulties)/3):@0.23
bbox_mAP(sigma(allclass_mod)/num_cls):24.479113737114282
bev_mAP(sigma(allclass_mod)/num_cls):44.78705525939168
3d_mAP(sigma(allclass_mod)/num_cls):1.7991334068934997
aos_mAP(sigma(allclass_mod)/num_cls):1.1308203875735963

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:37.09, 35.05, 34.00
bev  AP:58.10, 54.18, 50.72
3d   AP:20.22, 19.87, 18.79
aos  AP:1.63, 2.35, 3.42
Van coco AP@0.50:0.05:0.95:
bbox AP:14.03, 12.61, 10.34
bev  AP:14.79, 12.32, 10.15
3d   AP:6.20, 5.66, 4.26
aos  AP:0.01, 0.25, 0.37

eval.kitti.official.Car.bbox@0.70=[33.6, 34.35, 34.97], eval.kitti.official.Car.bev@0.70=[84.94, 75.52, 71.51], eval.kitti.official.Car.3d@0.70=[1.499, 2.285, 2.573], eval.kitti.official.Car.aos=[1.185, 1.915, 2.993], eval.kitti.official.Car.bev@0.50=[88.98, 85.57, 82.32], eval.kitti.official.Car.3d@0.50=[85.66, 79.89, 74.39], eval.kitti.official.Car.bbox_mAP@0.70=34.31, eval.kitti.official.Car.bev_mAP@0.70=77.32, eval.kitti.official.Car.3d_mAP@0.70=2.119, eval.kitti.official.Car.aos_mAP=2.031, eval.kitti.official.Van.bbox@0.70=[16.48, 14.61, 12.95], eval.kitti.official.Van.bev@0.70=[17.33, 14.06, 10.76], eval.kitti.official.Van.3d@0.70=[0.8447, 1.313, 0.9518], eval.kitti.official.Van.aos=[0.005986, 0.3462, 0.3329], eval.kitti.official.Van.bev@0.50=[32.86, 26.57, 22.17], eval.kitti.official.Van.3d@0.50=[25.18, 23.21, 18.45], eval.kitti.official.Van.bbox_mAP@0.70=14.68, eval.kitti.official.Van.bev_mAP@0.70=14.05, eval.kitti.official.Van.3d_mAP@0.70=1.036, eval.kitti.official.Van.aos_mAP=0.2284, eval.kitti.official.mAP_mod.bbox=24.48, eval.kitti.official.mAP_mod.bev=44.79, eval.kitti.official.mAP_mod.3d=1.799, eval.kitti.official.mAP_mod.aos=1.131, eval.kitti.coco.Car.bbox=[37.09, 35.05, 34.0], eval.kitti.coco.Car.bev=[58.1, 54.18, 50.72], eval.kitti.coco.Car.3d=[20.22, 19.87, 18.79], eval.kitti.coco.Car.aos=[1.631, 2.348, 3.421], eval.kitti.coco.Van.bbox=[14.03, 12.61, 10.34], eval.kitti.coco.Van.bev=[14.79, 12.32, 10.15], eval.kitti.coco.Van.3d=[6.195, 5.662, 4.263], eval.kitti.coco.Van.aos=[0.008573, 0.252, 0.3674]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:87.93, 78.71, 77.83
bev  AP:84.65, 76.24, 74.56
3d   AP:66.27, 57.91, 53.19
aos  AP:2.84, 3.70, 5.46
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:87.93, 78.71, 77.83
bev  AP:89.02, 86.22, 85.81
3d   AP:88.90, 85.28, 79.43
aos  AP:2.84, 3.70, 5.46
Car bbox_mAP(sigma(all_difficulties)/3):@81.49
Car bev_mAP(sigma(all_difficulties)/3):@78.48
Car 3d_mAP(sigma(all_difficulties)/3):@59.12
Car aos_mAP(sigma(all_difficulties)/3):@4.00
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:43.91, 33.93, 30.05
bev  AP:42.41, 32.56, 29.11
3d   AP:19.41, 14.96, 13.41
aos  AP:6.13, 3.08, 2.65
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:43.91, 33.93, 30.05
bev  AP:45.91, 38.73, 34.89
3d   AP:45.82, 36.40, 34.31
aos  AP:6.13, 3.08, 2.65
Van bbox_mAP(sigma(all_difficulties)/3):@35.97
Van bev_mAP(sigma(all_difficulties)/3):@34.69
Van 3d_mAP(sigma(all_difficulties)/3):@15.93
Van aos_mAP(sigma(all_difficulties)/3):@3.95
bbox_mAP(sigma(allclass_mod)/num_cls):56.32056527077182
bev_mAP(sigma(allclass_mod)/num_cls):54.40432656579473
3d_mAP(sigma(allclass_mod)/num_cls):36.43709452194032
aos_mAP(sigma(allclass_mod)/num_cls):3.38725671310663

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:63.70, 60.02, 57.92
bev  AP:58.53, 55.30, 53.90
3d   AP:46.67, 43.27, 40.46
aos  AP:1.97, 2.84, 4.07
Van coco AP@0.50:0.05:0.95:
bbox AP:28.83, 23.53, 20.97
bev  AP:26.55, 21.85, 19.68
3d   AP:19.67, 15.68, 14.03
aos  AP:4.07, 2.12, 1.89

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:88.22, 78.73, 77.75
bev  AP:86.72, 77.54, 76.24
3d   AP:71.06, 62.17, 55.93
aos  AP:2.18, 3.58, 5.21
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:88.22, 78.73, 77.75
bev  AP:89.26, 86.02, 85.84
3d   AP:89.15, 85.42, 79.46
aos  AP:2.18, 3.58, 5.21
Car bbox_mAP(sigma(all_difficulties)/3):@81.57
Car bev_mAP(sigma(all_difficulties)/3):@80.17
Car 3d_mAP(sigma(all_difficulties)/3):@63.05
Car aos_mAP(sigma(all_difficulties)/3):@3.66
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:30.62, 27.77, 26.94
bev  AP:37.58, 30.51, 28.33
3d   AP:9.16, 7.81, 7.83
aos  AP:1.45, 9.95, 10.86
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:30.62, 27.77, 26.94
bev  AP:43.07, 36.28, 34.50
3d   AP:42.35, 35.21, 32.99
aos  AP:1.45, 9.95, 10.86
Van bbox_mAP(sigma(all_difficulties)/3):@28.44
Van bev_mAP(sigma(all_difficulties)/3):@32.14
Van 3d_mAP(sigma(all_difficulties)/3):@8.27
Van aos_mAP(sigma(all_difficulties)/3):@7.42
bbox_mAP(sigma(allclass_mod)/num_cls):53.24907463257202
bev_mAP(sigma(allclass_mod)/num_cls):54.02517433325127
3d_mAP(sigma(allclass_mod)/num_cls):34.98851656079317
aos_mAP(sigma(allclass_mod)/num_cls):6.762677423918817

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:63.47, 58.87, 56.92
bev  AP:62.26, 56.88, 55.14
3d   AP:48.68, 44.16, 41.08
aos  AP:1.55, 2.74, 3.92
Van coco AP@0.50:0.05:0.95:
bbox AP:24.29, 20.47, 19.57
bev  AP:23.44, 20.14, 19.06
3d   AP:15.23, 13.05, 12.28
aos  AP:0.98, 6.07, 6.75

eval.kitti.official.Car.bbox@0.70=[88.22, 78.73, 77.75], eval.kitti.official.Car.bev@0.70=[86.72, 77.54, 76.24], eval.kitti.official.Car.3d@0.70=[71.06, 62.17, 55.93], eval.kitti.official.Car.aos=[2.184, 3.578, 5.21], eval.kitti.official.Car.bev@0.50=[89.26, 86.02, 85.84], eval.kitti.official.Car.3d@0.50=[89.15, 85.42, 79.46], eval.kitti.official.Car.bbox_mAP@0.70=81.57, eval.kitti.official.Car.bev_mAP@0.70=80.17, eval.kitti.official.Car.3d_mAP@0.70=63.05, eval.kitti.official.Car.aos_mAP=3.657, eval.kitti.official.Van.bbox@0.70=[30.62, 27.77, 26.94], eval.kitti.official.Van.bev@0.70=[37.58, 30.51, 28.33], eval.kitti.official.Van.3d@0.70=[9.158, 7.806, 7.833], eval.kitti.official.Van.aos=[1.45, 9.947, 10.86], eval.kitti.official.Van.bev@0.50=[43.07, 36.28, 34.5], eval.kitti.official.Van.3d@0.50=[42.35, 35.21, 32.99], eval.kitti.official.Van.bbox_mAP@0.70=28.44, eval.kitti.official.Van.bev_mAP@0.70=32.14, eval.kitti.official.Van.3d_mAP@0.70=8.266, eval.kitti.official.Van.aos_mAP=7.419, eval.kitti.official.mAP_mod.bbox=53.25, eval.kitti.official.mAP_mod.bev=54.03, eval.kitti.official.mAP_mod.3d=34.99, eval.kitti.official.mAP_mod.aos=6.763, eval.kitti.coco.Car.bbox=[63.47, 58.87, 56.92], eval.kitti.coco.Car.bev=[62.26, 56.88, 55.14], eval.kitti.coco.Car.3d=[48.68, 44.16, 41.08], eval.kitti.coco.Car.aos=[1.546, 2.737, 3.917], eval.kitti.coco.Van.bbox=[24.29, 20.47, 19.57], eval.kitti.coco.Van.bev=[23.44, 20.14, 19.06], eval.kitti.coco.Van.3d=[15.23, 13.05, 12.28], eval.kitti.coco.Van.aos=[0.9792, 6.071, 6.749]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:89.91, 85.68, 79.06
bev  AP:87.75, 77.89, 76.47
3d   AP:73.12, 62.33, 56.37
aos  AP:1.22, 2.82, 3.93
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:89.91, 85.68, 79.06
bev  AP:90.36, 88.41, 87.00
3d   AP:90.24, 88.02, 86.68
aos  AP:1.22, 2.82, 3.93
Car bbox_mAP(sigma(all_difficulties)/3):@84.89
Car bev_mAP(sigma(all_difficulties)/3):@80.70
Car 3d_mAP(sigma(all_difficulties)/3):@63.94
Car aos_mAP(sigma(all_difficulties)/3):@2.66
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:30.51, 28.75, 28.62
bev  AP:25.32, 26.80, 25.39
3d   AP:12.75, 11.81, 12.18
aos  AP:0.71, 0.39, 1.76
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:30.51, 28.75, 28.62
bev  AP:33.02, 33.36, 32.85
3d   AP:32.89, 32.95, 32.08
aos  AP:0.71, 0.39, 1.76
Van bbox_mAP(sigma(all_difficulties)/3):@29.29
Van bev_mAP(sigma(all_difficulties)/3):@25.84
Van 3d_mAP(sigma(all_difficulties)/3):@12.24
Van aos_mAP(sigma(all_difficulties)/3):@0.95
bbox_mAP(sigma(allclass_mod)/num_cls):57.217481089004735
bev_mAP(sigma(allclass_mod)/num_cls):52.34424783213139
3d_mAP(sigma(allclass_mod)/num_cls):37.06843167141166
aos_mAP(sigma(allclass_mod)/num_cls):1.6022650911143974

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:65.77, 61.81, 59.22
bev  AP:62.21, 58.05, 55.14
3d   AP:49.05, 44.70, 42.06
aos  AP:0.85, 2.04, 3.03
Van coco AP@0.50:0.05:0.95:
bbox AP:20.17, 20.17, 19.73
bev  AP:19.17, 19.24, 18.87
3d   AP:13.29, 13.17, 12.71
aos  AP:0.43, 0.31, 1.09

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:87.72, 78.26, 77.44
bev  AP:60.37, 58.47, 59.29
3d   AP:11.98, 17.11, 18.78
aos  AP:1.87, 2.89, 4.27
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:87.72, 78.26, 77.44
bev  AP:90.40, 88.57, 86.79
3d   AP:89.87, 87.60, 79.73
aos  AP:1.87, 2.89, 4.27
Car bbox_mAP(sigma(all_difficulties)/3):@81.14
Car bev_mAP(sigma(all_difficulties)/3):@59.38
Car 3d_mAP(sigma(all_difficulties)/3):@15.96
Car aos_mAP(sigma(all_difficulties)/3):@3.01
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:26.50, 27.26, 25.58
bev  AP:27.14, 28.12, 27.77
3d   AP:12.37, 12.06, 11.86
aos  AP:0.50, 0.46, 1.10
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:26.50, 27.26, 25.58
bev  AP:30.49, 31.78, 31.71
3d   AP:30.22, 31.14, 30.99
aos  AP:0.50, 0.46, 1.10
Van bbox_mAP(sigma(all_difficulties)/3):@26.45
Van bev_mAP(sigma(all_difficulties)/3):@27.67
Van 3d_mAP(sigma(all_difficulties)/3):@12.10
Van aos_mAP(sigma(all_difficulties)/3):@0.69
bbox_mAP(sigma(allclass_mod)/num_cls):52.76096764395771
bev_mAP(sigma(allclass_mod)/num_cls):43.29454531545138
3d_mAP(sigma(allclass_mod)/num_cls):14.585088356528573
aos_mAP(sigma(allclass_mod)/num_cls):1.6705189188402412

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:55.46, 53.51, 52.38
bev  AP:44.92, 44.43, 43.43
3d   AP:30.62, 30.79, 29.74
aos  AP:1.23, 2.18, 3.16
Van coco AP@0.50:0.05:0.95:
bbox AP:17.83, 19.19, 18.77
bev  AP:17.92, 18.76, 18.46
3d   AP:12.41, 12.61, 12.34
aos  AP:0.36, 0.34, 0.77

eval.kitti.official.Car.bbox@0.70=[87.72, 78.26, 77.44], eval.kitti.official.Car.bev@0.70=[60.37, 58.47, 59.29], eval.kitti.official.Car.3d@0.70=[11.98, 17.11, 18.78], eval.kitti.official.Car.aos=[1.869, 2.886, 4.265], eval.kitti.official.Car.bev@0.50=[90.4, 88.57, 86.79], eval.kitti.official.Car.3d@0.50=[89.87, 87.6, 79.73], eval.kitti.official.Car.bbox_mAP@0.70=81.14, eval.kitti.official.Car.bev_mAP@0.70=59.38, eval.kitti.official.Car.3d_mAP@0.70=15.96, eval.kitti.official.Car.aos_mAP=3.007, eval.kitti.official.Van.bbox@0.70=[26.5, 27.26, 25.58], eval.kitti.official.Van.bev@0.70=[27.14, 28.12, 27.77], eval.kitti.official.Van.3d@0.70=[12.37, 12.06, 11.86], eval.kitti.official.Van.aos=[0.5027, 0.4554, 1.097], eval.kitti.official.Van.bev@0.50=[30.49, 31.78, 31.71], eval.kitti.official.Van.3d@0.50=[30.22, 31.14, 30.99], eval.kitti.official.Van.bbox_mAP@0.70=26.45, eval.kitti.official.Van.bev_mAP@0.70=27.67, eval.kitti.official.Van.3d_mAP@0.70=12.1, eval.kitti.official.Van.aos_mAP=0.6851, eval.kitti.official.mAP_mod.bbox=52.76, eval.kitti.official.mAP_mod.bev=43.29, eval.kitti.official.mAP_mod.3d=14.59, eval.kitti.official.mAP_mod.aos=1.671, eval.kitti.coco.Car.bbox=[55.46, 53.51, 52.38], eval.kitti.coco.Car.bev=[44.92, 44.43, 43.43], eval.kitti.coco.Car.3d=[30.62, 30.79, 29.74], eval.kitti.coco.Car.aos=[1.234, 2.181, 3.156], eval.kitti.coco.Van.bbox=[17.83, 19.19, 18.77], eval.kitti.coco.Van.bev=[17.92, 18.76, 18.46], eval.kitti.coco.Van.3d=[12.41, 12.61, 12.34], eval.kitti.coco.Van.aos=[0.3605, 0.3401, 0.7661]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.07, 84.77, 79.05
bev  AP:87.37, 78.47, 77.13
3d   AP:68.68, 58.47, 54.24
aos  AP:1.09, 2.59, 3.36
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.07, 84.77, 79.05
bev  AP:90.50, 88.98, 87.56
3d   AP:90.46, 88.47, 86.19
aos  AP:1.09, 2.59, 3.36
Car bbox_mAP(sigma(all_difficulties)/3):@84.63
Car bev_mAP(sigma(all_difficulties)/3):@80.99
Car 3d_mAP(sigma(all_difficulties)/3):@60.46
Car aos_mAP(sigma(all_difficulties)/3):@2.35
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:25.53, 24.42, 20.80
bev  AP:22.76, 22.54, 20.59
3d   AP:12.64, 11.25, 9.61
aos  AP:0.48, 0.88, 0.76
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:25.53, 24.42, 20.80
bev  AP:32.21, 30.62, 26.97
3d   AP:32.13, 30.24, 26.41
aos  AP:0.48, 0.88, 0.76
Van bbox_mAP(sigma(all_difficulties)/3):@23.58
Van bev_mAP(sigma(all_difficulties)/3):@21.96
Van 3d_mAP(sigma(all_difficulties)/3):@11.17
Van aos_mAP(sigma(all_difficulties)/3):@0.71
bbox_mAP(sigma(allclass_mod)/num_cls):54.597453831592354
bev_mAP(sigma(allclass_mod)/num_cls):50.5062962942035
3d_mAP(sigma(allclass_mod)/num_cls):34.859528524833465
aos_mAP(sigma(allclass_mod)/num_cls):1.736123171396887

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:65.64, 61.12, 59.06
bev  AP:60.79, 57.53, 55.39
3d   AP:47.28, 43.15, 41.24
aos  AP:0.93, 1.89, 2.68
Van coco AP@0.50:0.05:0.95:
bbox AP:19.10, 18.60, 16.03
bev  AP:17.51, 16.60, 14.69
3d   AP:11.84, 11.23, 9.60
aos  AP:0.31, 0.59, 0.61

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:89.60, 79.33, 78.49
bev  AP:88.55, 79.16, 78.13
3d   AP:70.17, 59.08, 54.93
aos  AP:1.61, 2.82, 3.87
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:89.60, 79.33, 78.49
bev  AP:90.52, 88.85, 87.79
3d   AP:90.50, 88.51, 86.19
aos  AP:1.61, 2.82, 3.87
Car bbox_mAP(sigma(all_difficulties)/3):@82.47
Car bev_mAP(sigma(all_difficulties)/3):@81.94
Car 3d_mAP(sigma(all_difficulties)/3):@61.39
Car aos_mAP(sigma(all_difficulties)/3):@2.77
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:30.47, 24.90, 19.75
bev  AP:14.64, 14.17, 12.93
3d   AP:4.60, 5.05, 4.34
aos  AP:0.93, 1.47, 1.11
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:30.47, 24.90, 19.75
bev  AP:35.32, 32.10, 27.32
3d   AP:35.12, 31.52, 26.26
aos  AP:0.93, 1.47, 1.11
Van bbox_mAP(sigma(all_difficulties)/3):@25.04
Van bev_mAP(sigma(all_difficulties)/3):@13.91
Van 3d_mAP(sigma(all_difficulties)/3):@4.66
Van aos_mAP(sigma(all_difficulties)/3):@1.17
bbox_mAP(sigma(allclass_mod)/num_cls):52.11711267692434
bev_mAP(sigma(allclass_mod)/num_cls):46.66374401214722
3d_mAP(sigma(allclass_mod)/num_cls):32.06351768886958
aos_mAP(sigma(allclass_mod)/num_cls):2.1450742892603105

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:62.19, 57.66, 56.41
bev  AP:63.70, 59.28, 57.44
3d   AP:47.63, 43.40, 41.72
aos  AP:1.17, 2.21, 3.03
Van coco AP@0.50:0.05:0.95:
bbox AP:20.89, 19.05, 15.75
bev  AP:15.76, 14.35, 12.27
3d   AP:11.06, 9.83, 8.07
aos  AP:0.63, 0.98, 0.79

eval.kitti.official.Car.bbox@0.70=[89.6, 79.33, 78.49], eval.kitti.official.Car.bev@0.70=[88.55, 79.16, 78.13], eval.kitti.official.Car.3d@0.70=[70.17, 59.08, 54.93], eval.kitti.official.Car.aos=[1.608, 2.82, 3.869], eval.kitti.official.Car.bev@0.50=[90.52, 88.85, 87.79], eval.kitti.official.Car.3d@0.50=[90.5, 88.51, 86.19], eval.kitti.official.Car.bbox_mAP@0.70=82.47, eval.kitti.official.Car.bev_mAP@0.70=81.94, eval.kitti.official.Car.3d_mAP@0.70=61.39, eval.kitti.official.Car.aos_mAP=2.766, eval.kitti.official.Van.bbox@0.70=[30.47, 24.9, 19.75], eval.kitti.official.Van.bev@0.70=[14.64, 14.17, 12.93], eval.kitti.official.Van.3d@0.70=[4.599, 5.046, 4.338], eval.kitti.official.Van.aos=[0.9277, 1.47, 1.114], eval.kitti.official.Van.bev@0.50=[35.32, 32.1, 27.32], eval.kitti.official.Van.3d@0.50=[35.12, 31.52, 26.26], eval.kitti.official.Van.bbox_mAP@0.70=25.04, eval.kitti.official.Van.bev_mAP@0.70=13.91, eval.kitti.official.Van.3d_mAP@0.70=4.661, eval.kitti.official.Van.aos_mAP=1.17, eval.kitti.official.mAP_mod.bbox=52.12, eval.kitti.official.mAP_mod.bev=46.66, eval.kitti.official.mAP_mod.3d=32.06, eval.kitti.official.mAP_mod.aos=2.145, eval.kitti.coco.Car.bbox=[62.19, 57.66, 56.41], eval.kitti.coco.Car.bev=[63.7, 59.28, 57.44], eval.kitti.coco.Car.3d=[47.63, 43.4, 41.72], eval.kitti.coco.Car.aos=[1.172, 2.213, 3.031], eval.kitti.coco.Van.bbox=[20.89, 19.05, 15.75], eval.kitti.coco.Van.bev=[15.76, 14.35, 12.27], eval.kitti.coco.Van.3d=[11.06, 9.83, 8.066], eval.kitti.coco.Van.aos=[0.6277, 0.9796, 0.7857]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:89.21, 85.29, 79.20
bev  AP:87.84, 78.50, 77.55
3d   AP:71.15, 62.45, 56.13
aos  AP:0.83, 2.28, 3.29
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:89.21, 85.29, 79.20
bev  AP:90.19, 88.75, 87.29
3d   AP:90.11, 88.38, 86.64
aos  AP:0.83, 2.28, 3.29
Car bbox_mAP(sigma(all_difficulties)/3):@84.57
Car bev_mAP(sigma(all_difficulties)/3):@81.29
Car 3d_mAP(sigma(all_difficulties)/3):@63.24
Car aos_mAP(sigma(all_difficulties)/3):@2.13
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:45.40, 34.94, 30.08
bev  AP:41.79, 31.97, 28.04
3d   AP:22.04, 20.24, 17.45
aos  AP:1.34, 0.57, 1.19
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:45.40, 34.94, 30.08
bev  AP:53.65, 40.50, 36.68
3d   AP:53.26, 39.76, 35.51
aos  AP:1.34, 0.57, 1.19
Van bbox_mAP(sigma(all_difficulties)/3):@36.80
Van bev_mAP(sigma(all_difficulties)/3):@33.93
Van 3d_mAP(sigma(all_difficulties)/3):@19.91
Van aos_mAP(sigma(all_difficulties)/3):@1.03
bbox_mAP(sigma(allclass_mod)/num_cls):60.114768529081196
bev_mAP(sigma(allclass_mod)/num_cls):55.23238052441808
3d_mAP(sigma(allclass_mod)/num_cls):41.343582615059226
aos_mAP(sigma(allclass_mod)/num_cls):1.4219417428795165

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:64.06, 61.06, 59.18
bev  AP:63.83, 59.40, 56.99
3d   AP:49.71, 46.17, 43.69
aos  AP:0.63, 1.70, 2.61
Van coco AP@0.50:0.05:0.95:
bbox AP:32.94, 26.84, 23.78
bev  AP:30.30, 24.18, 21.68
3d   AP:22.40, 17.79, 15.58
aos  AP:1.03, 0.44, 1.04

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:88.52, 84.95, 78.90
bev  AP:88.37, 79.10, 78.21
3d   AP:67.17, 60.83, 54.84
aos  AP:0.80, 2.08, 3.23
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:88.52, 84.95, 78.90
bev  AP:90.30, 88.90, 87.66
3d   AP:90.17, 88.48, 86.88
aos  AP:0.80, 2.08, 3.23
Car bbox_mAP(sigma(all_difficulties)/3):@84.12
Car bev_mAP(sigma(all_difficulties)/3):@81.89
Car 3d_mAP(sigma(all_difficulties)/3):@60.95
Car aos_mAP(sigma(all_difficulties)/3):@2.04
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:52.68, 37.72, 31.95
bev  AP:36.63, 26.05, 24.48
3d   AP:9.30, 7.65, 7.50
aos  AP:2.16, 0.86, 1.25
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:52.68, 37.72, 31.95
bev  AP:60.04, 42.61, 37.72
3d   AP:59.05, 41.52, 36.23
aos  AP:2.16, 0.86, 1.25
Van bbox_mAP(sigma(all_difficulties)/3):@40.79
Van bev_mAP(sigma(all_difficulties)/3):@29.06
Van 3d_mAP(sigma(all_difficulties)/3):@8.15
Van aos_mAP(sigma(all_difficulties)/3):@1.42
bbox_mAP(sigma(allclass_mod)/num_cls):61.335860827600456
bev_mAP(sigma(allclass_mod)/num_cls):52.57826601934974
3d_mAP(sigma(allclass_mod)/num_cls):34.24105129255101
aos_mAP(sigma(allclass_mod)/num_cls):1.4699781337411517

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:60.77, 59.00, 57.28
bev  AP:65.47, 61.18, 58.07
3d   AP:47.57, 45.25, 43.50
aos  AP:0.55, 1.56, 2.53
Van coco AP@0.50:0.05:0.95:
bbox AP:35.35, 25.95, 22.65
bev  AP:28.17, 20.62, 18.77
3d   AP:19.92, 14.37, 12.89
aos  AP:1.54, 0.60, 0.89

eval.kitti.official.Car.bbox@0.70=[88.52, 84.95, 78.9], eval.kitti.official.Car.bev@0.70=[88.37, 79.1, 78.21], eval.kitti.official.Car.3d@0.70=[67.17, 60.83, 54.84], eval.kitti.official.Car.aos=[0.7967, 2.078, 3.231], eval.kitti.official.Car.bev@0.50=[90.3, 88.9, 87.66], eval.kitti.official.Car.3d@0.50=[90.17, 88.48, 86.88], eval.kitti.official.Car.bbox_mAP@0.70=84.12, eval.kitti.official.Car.bev_mAP@0.70=81.89, eval.kitti.official.Car.3d_mAP@0.70=60.95, eval.kitti.official.Car.aos_mAP=2.035, eval.kitti.official.Van.bbox@0.70=[52.68, 37.72, 31.95], eval.kitti.official.Van.bev@0.70=[36.63, 26.05, 24.48], eval.kitti.official.Van.3d@0.70=[9.296, 7.647, 7.503], eval.kitti.official.Van.aos=[2.163, 0.8618, 1.249], eval.kitti.official.Van.bev@0.50=[60.04, 42.61, 37.72], eval.kitti.official.Van.3d@0.50=[59.05, 41.52, 36.23], eval.kitti.official.Van.bbox_mAP@0.70=40.79, eval.kitti.official.Van.bev_mAP@0.70=29.06, eval.kitti.official.Van.3d_mAP@0.70=8.149, eval.kitti.official.Van.aos_mAP=1.425, eval.kitti.official.mAP_mod.bbox=61.34, eval.kitti.official.mAP_mod.bev=52.58, eval.kitti.official.mAP_mod.3d=34.24, eval.kitti.official.mAP_mod.aos=1.47, eval.kitti.coco.Car.bbox=[60.77, 59.0, 57.28], eval.kitti.coco.Car.bev=[65.47, 61.18, 58.07], eval.kitti.coco.Car.3d=[47.57, 45.25, 43.5], eval.kitti.coco.Car.aos=[0.5508, 1.56, 2.53], eval.kitti.coco.Van.bbox=[35.35, 25.95, 22.65], eval.kitti.coco.Van.bev=[28.17, 20.62, 18.77], eval.kitti.coco.Van.3d=[19.92, 14.37, 12.89], eval.kitti.coco.Van.aos=[1.542, 0.5965, 0.8915]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:89.81, 86.33, 79.53
bev  AP:88.51, 78.88, 77.98
3d   AP:81.02, 65.72, 63.33
aos  AP:0.79, 1.64, 2.79
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:89.81, 86.33, 79.53
bev  AP:90.33, 88.96, 87.83
3d   AP:90.31, 88.61, 87.57
aos  AP:0.79, 1.64, 2.79
Car bbox_mAP(sigma(all_difficulties)/3):@85.23
Car bev_mAP(sigma(all_difficulties)/3):@81.79
Car 3d_mAP(sigma(all_difficulties)/3):@70.03
Car aos_mAP(sigma(all_difficulties)/3):@1.74
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:56.82, 39.70, 33.70
bev  AP:55.87, 40.39, 32.96
3d   AP:36.74, 24.48, 20.36
aos  AP:0.65, 0.73, 1.09
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:56.82, 39.70, 33.70
bev  AP:59.90, 45.00, 39.14
3d   AP:59.34, 43.77, 38.01
aos  AP:0.65, 0.73, 1.09
Van bbox_mAP(sigma(all_difficulties)/3):@43.40
Van bev_mAP(sigma(all_difficulties)/3):@43.07
Van 3d_mAP(sigma(all_difficulties)/3):@27.19
Van aos_mAP(sigma(all_difficulties)/3):@0.82
bbox_mAP(sigma(allclass_mod)/num_cls):63.01590495739949
bev_mAP(sigma(allclass_mod)/num_cls):59.63486617116174
3d_mAP(sigma(allclass_mod)/num_cls):45.09909494498817
aos_mAP(sigma(allclass_mod)/num_cls):1.184890112807607

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:66.60, 64.12, 61.78
bev  AP:64.76, 60.69, 57.85
3d   AP:53.67, 48.79, 45.80
aos  AP:0.59, 1.25, 2.30
Van coco AP@0.50:0.05:0.95:
bbox AP:39.96, 29.02, 25.01
bev  AP:38.03, 27.89, 23.76
3d   AP:28.77, 20.03, 17.19
aos  AP:0.49, 0.61, 0.90

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:89.58, 86.03, 79.49
bev  AP:88.04, 84.27, 78.04
3d   AP:79.17, 64.82, 62.45
aos  AP:0.96, 1.90, 3.22
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:89.58, 86.03, 79.49
bev  AP:90.29, 89.05, 88.10
3d   AP:90.24, 88.72, 87.29
aos  AP:0.96, 1.90, 3.22
Car bbox_mAP(sigma(all_difficulties)/3):@85.03
Car bev_mAP(sigma(all_difficulties)/3):@83.45
Car 3d_mAP(sigma(all_difficulties)/3):@68.81
Car aos_mAP(sigma(all_difficulties)/3):@2.02
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:55.90, 37.73, 31.87
bev  AP:38.86, 27.00, 23.41
3d   AP:16.31, 11.90, 10.54
aos  AP:0.90, 0.92, 1.37
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:55.90, 37.73, 31.87
bev  AP:58.46, 42.02, 36.19
3d   AP:55.95, 40.18, 34.50
aos  AP:0.90, 0.92, 1.37
Van bbox_mAP(sigma(all_difficulties)/3):@41.84
Van bev_mAP(sigma(all_difficulties)/3):@29.76
Van 3d_mAP(sigma(all_difficulties)/3):@12.92
Van aos_mAP(sigma(all_difficulties)/3):@1.06
bbox_mAP(sigma(allclass_mod)/num_cls):61.87980514895851
bev_mAP(sigma(allclass_mod)/num_cls):55.63614640516189
3d_mAP(sigma(allclass_mod)/num_cls):38.35891464527321
aos_mAP(sigma(allclass_mod)/num_cls):1.4094969716894288

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:66.04, 62.35, 60.03
bev  AP:64.89, 61.49, 58.72
3d   AP:53.16, 48.48, 46.11
aos  AP:0.70, 1.45, 2.56
Van coco AP@0.50:0.05:0.95:
bbox AP:37.72, 26.67, 22.66
bev  AP:29.15, 21.05, 18.07
3d   AP:21.50, 14.81, 12.71
aos  AP:0.61, 0.69, 1.03

eval.kitti.official.Car.bbox@0.70=[89.58, 86.03, 79.49], eval.kitti.official.Car.bev@0.70=[88.04, 84.27, 78.04], eval.kitti.official.Car.3d@0.70=[79.17, 64.82, 62.45], eval.kitti.official.Car.aos=[0.9563, 1.898, 3.217], eval.kitti.official.Car.bev@0.50=[90.29, 89.05, 88.1], eval.kitti.official.Car.3d@0.50=[90.24, 88.72, 87.29], eval.kitti.official.Car.bbox_mAP@0.70=85.03, eval.kitti.official.Car.bev_mAP@0.70=83.45, eval.kitti.official.Car.3d_mAP@0.70=68.81, eval.kitti.official.Car.aos_mAP=2.024, eval.kitti.official.Van.bbox@0.70=[55.9, 37.73, 31.87], eval.kitti.official.Van.bev@0.70=[38.86, 27.0, 23.41], eval.kitti.official.Van.3d@0.70=[16.31, 11.9, 10.54], eval.kitti.official.Van.aos=[0.9017, 0.9209, 1.369], eval.kitti.official.Van.bev@0.50=[58.46, 42.02, 36.19], eval.kitti.official.Van.3d@0.50=[55.95, 40.18, 34.5], eval.kitti.official.Van.bbox_mAP@0.70=41.84, eval.kitti.official.Van.bev_mAP@0.70=29.76, eval.kitti.official.Van.3d_mAP@0.70=12.92, eval.kitti.official.Van.aos_mAP=1.064, eval.kitti.official.mAP_mod.bbox=61.88, eval.kitti.official.mAP_mod.bev=55.64, eval.kitti.official.mAP_mod.3d=38.36, eval.kitti.official.mAP_mod.aos=1.409, eval.kitti.coco.Car.bbox=[66.04, 62.35, 60.03], eval.kitti.coco.Car.bev=[64.89, 61.49, 58.72], eval.kitti.coco.Car.3d=[53.16, 48.48, 46.11], eval.kitti.coco.Car.aos=[0.6972, 1.448, 2.558], eval.kitti.coco.Van.bbox=[37.72, 26.67, 22.66], eval.kitti.coco.Van.bev=[29.15, 21.05, 18.07], eval.kitti.coco.Van.3d=[21.5, 14.81, 12.71], eval.kitti.coco.Van.aos=[0.6111, 0.6902, 1.034]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:89.89, 86.29, 79.41
bev  AP:89.09, 79.17, 78.20
3d   AP:75.42, 65.11, 63.07
aos  AP:0.60, 2.20, 3.43
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:89.89, 86.29, 79.41
bev  AP:90.58, 89.39, 88.63
3d   AP:90.58, 89.19, 88.19
aos  AP:0.60, 2.20, 3.43
Car bbox_mAP(sigma(all_difficulties)/3):@85.20
Car bev_mAP(sigma(all_difficulties)/3):@82.15
Car 3d_mAP(sigma(all_difficulties)/3):@67.87
Car aos_mAP(sigma(all_difficulties)/3):@2.08
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:42.27, 37.61, 32.63
bev  AP:42.89, 37.77, 32.84
3d   AP:30.69, 23.74, 19.79
aos  AP:0.53, 0.53, 1.07
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:42.27, 37.61, 32.63
bev  AP:44.08, 39.93, 36.74
3d   AP:43.78, 39.45, 36.23
aos  AP:0.53, 0.53, 1.07
Van bbox_mAP(sigma(all_difficulties)/3):@37.50
Van bev_mAP(sigma(all_difficulties)/3):@37.83
Van 3d_mAP(sigma(all_difficulties)/3):@24.74
Van aos_mAP(sigma(all_difficulties)/3):@0.71
bbox_mAP(sigma(allclass_mod)/num_cls):61.95022820304695
bev_mAP(sigma(allclass_mod)/num_cls):58.470460773013144
3d_mAP(sigma(allclass_mod)/num_cls):44.425155966262594
aos_mAP(sigma(allclass_mod)/num_cls):1.3659045867516673

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:63.53, 60.09, 58.65
bev  AP:61.83, 58.38, 56.87
3d   AP:51.74, 47.55, 45.92
aos  AP:0.41, 1.56, 2.69
Van coco AP@0.50:0.05:0.95:
bbox AP:28.73, 25.97, 22.80
bev  AP:29.75, 26.09, 23.55
3d   AP:22.03, 19.14, 16.87
aos  AP:0.37, 0.38, 0.77

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.31, 86.77, 79.80
bev  AP:89.72, 85.56, 78.67
3d   AP:77.06, 66.38, 64.24
aos  AP:0.78, 2.47, 3.96
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.31, 86.77, 79.80
bev  AP:90.66, 89.41, 88.56
3d   AP:90.64, 89.19, 88.15
aos  AP:0.78, 2.47, 3.96
Car bbox_mAP(sigma(all_difficulties)/3):@85.63
Car bev_mAP(sigma(all_difficulties)/3):@84.65
Car 3d_mAP(sigma(all_difficulties)/3):@69.22
Car aos_mAP(sigma(all_difficulties)/3):@2.40
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:35.11, 31.80, 27.54
bev  AP:36.28, 32.18, 27.33
3d   AP:24.23, 19.63, 15.96
aos  AP:0.20, 0.31, 0.72
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:35.11, 31.80, 27.54
bev  AP:39.46, 36.47, 34.64
3d   AP:39.21, 35.87, 31.31
aos  AP:0.20, 0.31, 0.72
Van bbox_mAP(sigma(all_difficulties)/3):@31.48
Van bev_mAP(sigma(all_difficulties)/3):@31.93
Van 3d_mAP(sigma(all_difficulties)/3):@19.94
Van aos_mAP(sigma(all_difficulties)/3):@0.41
bbox_mAP(sigma(allclass_mod)/num_cls):59.28090107108349
bev_mAP(sigma(allclass_mod)/num_cls):58.868622134800795
3d_mAP(sigma(allclass_mod)/num_cls):43.003335545526724
aos_mAP(sigma(allclass_mod)/num_cls):1.385769601264989

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:65.12, 61.79, 59.96
bev  AP:65.28, 61.29, 59.19
3d   AP:53.47, 49.23, 47.24
aos  AP:0.56, 1.74, 3.03
Van coco AP@0.50:0.05:0.95:
bbox AP:24.93, 22.67, 20.04
bev  AP:25.37, 22.77, 19.92
3d   AP:19.37, 16.69, 14.19
aos  AP:0.12, 0.22, 0.53

eval.kitti.official.Car.bbox@0.70=[90.31, 86.77, 79.8], eval.kitti.official.Car.bev@0.70=[89.72, 85.56, 78.67], eval.kitti.official.Car.3d@0.70=[77.06, 66.38, 64.24], eval.kitti.official.Car.aos=[0.784, 2.466, 3.959], eval.kitti.official.Car.bev@0.50=[90.66, 89.41, 88.56], eval.kitti.official.Car.3d@0.50=[90.64, 89.19, 88.15], eval.kitti.official.Car.bbox_mAP@0.70=85.63, eval.kitti.official.Car.bev_mAP@0.70=84.65, eval.kitti.official.Car.3d_mAP@0.70=69.22, eval.kitti.official.Car.aos_mAP=2.403, eval.kitti.official.Van.bbox@0.70=[35.11, 31.8, 27.54], eval.kitti.official.Van.bev@0.70=[36.28, 32.18, 27.33], eval.kitti.official.Van.3d@0.70=[24.23, 19.63, 15.96], eval.kitti.official.Van.aos=[0.1975, 0.3051, 0.7226], eval.kitti.official.Van.bev@0.50=[39.46, 36.47, 34.64], eval.kitti.official.Van.3d@0.50=[39.21, 35.87, 31.31], eval.kitti.official.Van.bbox_mAP@0.70=31.48, eval.kitti.official.Van.bev_mAP@0.70=31.93, eval.kitti.official.Van.3d_mAP@0.70=19.94, eval.kitti.official.Van.aos_mAP=0.4084, eval.kitti.official.mAP_mod.bbox=59.28, eval.kitti.official.mAP_mod.bev=58.87, eval.kitti.official.mAP_mod.3d=43.0, eval.kitti.official.mAP_mod.aos=1.386, eval.kitti.coco.Car.bbox=[65.12, 61.79, 59.96], eval.kitti.coco.Car.bev=[65.28, 61.29, 59.19], eval.kitti.coco.Car.3d=[53.47, 49.23, 47.24], eval.kitti.coco.Car.aos=[0.5613, 1.741, 3.029], eval.kitti.coco.Van.bbox=[24.93, 22.67, 20.04], eval.kitti.coco.Van.bev=[25.37, 22.77, 19.92], eval.kitti.coco.Van.3d=[19.37, 16.69, 14.19], eval.kitti.coco.Van.aos=[0.1198, 0.2218, 0.5279]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.30, 87.18, 80.21
bev  AP:89.46, 85.14, 78.87
3d   AP:83.43, 67.79, 66.79
aos  AP:1.80, 2.38, 3.13
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.30, 87.18, 80.21
bev  AP:90.48, 88.94, 88.28
3d   AP:90.48, 88.80, 87.76
aos  AP:1.80, 2.38, 3.13
Car bbox_mAP(sigma(all_difficulties)/3):@85.90
Car bev_mAP(sigma(all_difficulties)/3):@84.49
Car 3d_mAP(sigma(all_difficulties)/3):@72.67
Car aos_mAP(sigma(all_difficulties)/3):@2.44
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:42.26, 37.40, 32.74
bev  AP:42.62, 36.02, 32.20
3d   AP:30.36, 27.10, 23.52
aos  AP:0.02, 0.46, 0.81
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:42.26, 37.40, 32.74
bev  AP:46.49, 41.00, 37.90
3d   AP:46.39, 40.73, 37.19
aos  AP:0.02, 0.46, 0.81
Van bbox_mAP(sigma(all_difficulties)/3):@37.47
Van bev_mAP(sigma(all_difficulties)/3):@36.95
Van 3d_mAP(sigma(all_difficulties)/3):@26.99
Van aos_mAP(sigma(all_difficulties)/3):@0.43
bbox_mAP(sigma(allclass_mod)/num_cls):62.29013615903583
bev_mAP(sigma(allclass_mod)/num_cls):60.57991143914933
3d_mAP(sigma(allclass_mod)/num_cls):47.445147672299726
aos_mAP(sigma(allclass_mod)/num_cls):1.4204587688309762

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:69.73, 65.06, 63.84
bev  AP:65.62, 61.94, 59.44
3d   AP:55.45, 50.53, 49.11
aos  AP:1.33, 1.70, 2.51
Van coco AP@0.50:0.05:0.95:
bbox AP:29.62, 27.94, 25.31
bev  AP:31.57, 27.46, 25.27
3d   AP:23.00, 20.32, 18.34
aos  AP:0.01, 0.31, 0.74

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:89.54, 86.19, 79.82
bev  AP:88.05, 78.66, 78.32
3d   AP:74.00, 65.22, 64.33
aos  AP:1.91, 2.16, 3.23
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:89.54, 86.19, 79.82
bev  AP:89.89, 88.48, 87.79
3d   AP:89.86, 88.28, 87.30
aos  AP:1.91, 2.16, 3.23
Car bbox_mAP(sigma(all_difficulties)/3):@85.18
Car bev_mAP(sigma(all_difficulties)/3):@81.68
Car 3d_mAP(sigma(all_difficulties)/3):@67.85
Car aos_mAP(sigma(all_difficulties)/3):@2.43
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:45.62, 35.23, 31.70
bev  AP:44.98, 33.78, 31.14
3d   AP:15.88, 15.10, 14.51
aos  AP:0.06, 0.56, 1.13
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:45.62, 35.23, 31.70
bev  AP:49.19, 37.65, 36.47
3d   AP:49.10, 37.33, 36.05
aos  AP:0.06, 0.56, 1.13
Van bbox_mAP(sigma(all_difficulties)/3):@37.52
Van bev_mAP(sigma(all_difficulties)/3):@36.63
Van 3d_mAP(sigma(all_difficulties)/3):@15.16
Van aos_mAP(sigma(all_difficulties)/3):@0.59
bbox_mAP(sigma(allclass_mod)/num_cls):60.713075190486784
bev_mAP(sigma(allclass_mod)/num_cls):56.21896494793886
3d_mAP(sigma(allclass_mod)/num_cls):40.1587984422409
aos_mAP(sigma(allclass_mod)/num_cls):1.3604354450151233

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:66.57, 63.52, 62.39
bev  AP:63.21, 59.04, 57.54
3d   AP:52.43, 48.75, 47.14
aos  AP:1.34, 1.56, 2.59
Van coco AP@0.50:0.05:0.95:
bbox AP:29.79, 23.74, 22.14
bev  AP:30.06, 23.11, 21.99
3d   AP:19.88, 15.79, 14.53
aos  AP:0.04, 0.39, 0.76

eval.kitti.official.Car.bbox@0.70=[89.54, 86.19, 79.82], eval.kitti.official.Car.bev@0.70=[88.05, 78.66, 78.32], eval.kitti.official.Car.3d@0.70=[74.0, 65.22, 64.33], eval.kitti.official.Car.aos=[1.911, 2.161, 3.227], eval.kitti.official.Car.bev@0.50=[89.89, 88.48, 87.79], eval.kitti.official.Car.3d@0.50=[89.86, 88.28, 87.3], eval.kitti.official.Car.bbox_mAP@0.70=85.18, eval.kitti.official.Car.bev_mAP@0.70=81.68, eval.kitti.official.Car.3d_mAP@0.70=67.85, eval.kitti.official.Car.aos_mAP=2.433, eval.kitti.official.Van.bbox@0.70=[45.62, 35.23, 31.7], eval.kitti.official.Van.bev@0.70=[44.98, 33.78, 31.14], eval.kitti.official.Van.3d@0.70=[15.88, 15.1, 14.51], eval.kitti.official.Van.aos=[0.06424, 0.56, 1.135], eval.kitti.official.Van.bev@0.50=[49.19, 37.65, 36.47], eval.kitti.official.Van.3d@0.50=[49.1, 37.33, 36.05], eval.kitti.official.Van.bbox_mAP@0.70=37.52, eval.kitti.official.Van.bev_mAP@0.70=36.63, eval.kitti.official.Van.3d_mAP@0.70=15.16, eval.kitti.official.Van.aos_mAP=0.5862, eval.kitti.official.mAP_mod.bbox=60.71, eval.kitti.official.mAP_mod.bev=56.22, eval.kitti.official.mAP_mod.3d=40.16, eval.kitti.official.mAP_mod.aos=1.36, eval.kitti.coco.Car.bbox=[66.57, 63.52, 62.39], eval.kitti.coco.Car.bev=[63.21, 59.04, 57.54], eval.kitti.coco.Car.3d=[52.43, 48.75, 47.14], eval.kitti.coco.Car.aos=[1.339, 1.56, 2.594], eval.kitti.coco.Van.bbox=[29.79, 23.74, 22.14], eval.kitti.coco.Van.bev=[30.06, 23.11, 21.99], eval.kitti.coco.Van.3d=[19.88, 15.79, 14.53], eval.kitti.coco.Van.aos=[0.03808, 0.3875, 0.7554]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.51, 88.12, 86.82
bev  AP:89.58, 85.31, 79.08
3d   AP:85.42, 74.26, 68.46
aos  AP:1.41, 2.52, 3.86
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.51, 88.12, 86.82
bev  AP:90.61, 89.07, 88.29
3d   AP:90.61, 88.97, 87.92
aos  AP:1.41, 2.52, 3.86
Car bbox_mAP(sigma(all_difficulties)/3):@88.48
Car bev_mAP(sigma(all_difficulties)/3):@84.66
Car 3d_mAP(sigma(all_difficulties)/3):@76.05
Car aos_mAP(sigma(all_difficulties)/3):@2.59
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:39.60, 35.24, 31.08
bev  AP:40.13, 33.81, 30.41
3d   AP:27.55, 23.82, 20.02
aos  AP:0.86, 0.64, 1.15
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:39.60, 35.24, 31.08
bev  AP:46.09, 41.62, 37.99
3d   AP:45.23, 40.37, 36.78
aos  AP:0.86, 0.64, 1.15
Van bbox_mAP(sigma(all_difficulties)/3):@35.31
Van bev_mAP(sigma(all_difficulties)/3):@34.78
Van 3d_mAP(sigma(all_difficulties)/3):@23.80
Van aos_mAP(sigma(all_difficulties)/3):@0.88
bbox_mAP(sigma(allclass_mod)/num_cls):61.68223782395469
bev_mAP(sigma(allclass_mod)/num_cls):59.561848004059186
3d_mAP(sigma(allclass_mod)/num_cls):49.03775129151091
aos_mAP(sigma(allclass_mod)/num_cls):1.578637517722662

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:69.58, 65.59, 64.14
bev  AP:68.67, 64.04, 62.32
3d   AP:59.06, 53.32, 50.54
aos  AP:1.06, 1.81, 2.86
Van coco AP@0.50:0.05:0.95:
bbox AP:27.49, 26.13, 23.53
bev  AP:29.73, 26.39, 23.65
3d   AP:21.99, 20.21, 17.87
aos  AP:0.63, 0.44, 0.80

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:88.88, 84.58, 78.47
bev  AP:88.31, 78.38, 77.65
3d   AP:68.17, 58.97, 54.50
aos  AP:1.08, 2.26, 3.63
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:88.88, 84.58, 78.47
bev  AP:90.66, 88.99, 88.09
3d   AP:90.66, 88.78, 87.44
aos  AP:1.08, 2.26, 3.63
Car bbox_mAP(sigma(all_difficulties)/3):@83.98
Car bev_mAP(sigma(all_difficulties)/3):@81.45
Car 3d_mAP(sigma(all_difficulties)/3):@60.55
Car aos_mAP(sigma(all_difficulties)/3):@2.32
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:30.66, 27.13, 24.17
bev  AP:30.92, 27.67, 24.69
3d   AP:17.04, 14.31, 12.32
aos  AP:0.77, 1.07, 1.29
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:30.66, 27.13, 24.17
bev  AP:39.31, 36.46, 34.07
3d   AP:37.29, 35.22, 32.34
aos  AP:0.77, 1.07, 1.29
Van bbox_mAP(sigma(all_difficulties)/3):@27.32
Van bev_mAP(sigma(all_difficulties)/3):@27.76
Van 3d_mAP(sigma(all_difficulties)/3):@14.56
Van aos_mAP(sigma(all_difficulties)/3):@1.04
bbox_mAP(sigma(allclass_mod)/num_cls):55.85847685225894
bev_mAP(sigma(allclass_mod)/num_cls):53.02868598775359
3d_mAP(sigma(allclass_mod)/num_cls):36.642697055498466
aos_mAP(sigma(allclass_mod)/num_cls):1.660614162717502

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:58.77, 56.97, 55.67
bev  AP:59.73, 56.80, 55.49
3d   AP:48.05, 44.86, 43.14
aos  AP:0.75, 1.66, 2.76
Van coco AP@0.50:0.05:0.95:
bbox AP:21.70, 19.59, 18.01
bev  AP:22.29, 20.05, 18.48
3d   AP:15.76, 13.88, 12.16
aos  AP:0.55, 0.75, 0.97

eval.kitti.official.Car.bbox@0.70=[88.88, 84.58, 78.47], eval.kitti.official.Car.bev@0.70=[88.31, 78.38, 77.65], eval.kitti.official.Car.3d@0.70=[68.17, 58.97, 54.5], eval.kitti.official.Car.aos=[1.075, 2.255, 3.629], eval.kitti.official.Car.bev@0.50=[90.66, 88.99, 88.09], eval.kitti.official.Car.3d@0.50=[90.66, 88.78, 87.44], eval.kitti.official.Car.bbox_mAP@0.70=83.98, eval.kitti.official.Car.bev_mAP@0.70=81.45, eval.kitti.official.Car.3d_mAP@0.70=60.55, eval.kitti.official.Car.aos_mAP=2.32, eval.kitti.official.Van.bbox@0.70=[30.66, 27.13, 24.17], eval.kitti.official.Van.bev@0.70=[30.92, 27.67, 24.69], eval.kitti.official.Van.3d@0.70=[17.04, 14.31, 12.32], eval.kitti.official.Van.aos=[0.7673, 1.066, 1.289], eval.kitti.official.Van.bev@0.50=[39.31, 36.46, 34.07], eval.kitti.official.Van.3d@0.50=[37.29, 35.22, 32.34], eval.kitti.official.Van.bbox_mAP@0.70=27.32, eval.kitti.official.Van.bev_mAP@0.70=27.76, eval.kitti.official.Van.3d_mAP@0.70=14.56, eval.kitti.official.Van.aos_mAP=1.041, eval.kitti.official.mAP_mod.bbox=55.86, eval.kitti.official.mAP_mod.bev=53.03, eval.kitti.official.mAP_mod.3d=36.64, eval.kitti.official.mAP_mod.aos=1.661, eval.kitti.coco.Car.bbox=[58.77, 56.97, 55.67], eval.kitti.coco.Car.bev=[59.73, 56.8, 55.49], eval.kitti.coco.Car.3d=[48.05, 44.86, 43.14], eval.kitti.coco.Car.aos=[0.7473, 1.658, 2.759], eval.kitti.coco.Van.bbox=[21.7, 19.59, 18.01], eval.kitti.coco.Van.bev=[22.29, 20.05, 18.48], eval.kitti.coco.Van.3d=[15.76, 13.88, 12.16], eval.kitti.coco.Van.aos=[0.5457, 0.7463, 0.9684]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.46, 87.43, 87.41
bev  AP:89.28, 85.86, 79.29
3d   AP:76.68, 67.36, 66.42
aos  AP:0.65, 1.64, 2.71
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.46, 87.43, 87.41
bev  AP:90.70, 89.61, 89.00
3d   AP:90.70, 89.45, 88.64
aos  AP:0.65, 1.64, 2.71
Car bbox_mAP(sigma(all_difficulties)/3):@88.44
Car bev_mAP(sigma(all_difficulties)/3):@84.81
Car 3d_mAP(sigma(all_difficulties)/3):@70.15
Car aos_mAP(sigma(all_difficulties)/3):@1.67
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:44.56, 35.89, 31.28
bev  AP:43.49, 31.91, 30.03
3d   AP:33.63, 23.50, 21.15
aos  AP:1.17, 0.51, 1.30
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:44.56, 35.89, 31.28
bev  AP:46.16, 37.61, 33.57
3d   AP:45.83, 37.28, 33.20
aos  AP:1.17, 0.51, 1.30
Van bbox_mAP(sigma(all_difficulties)/3):@37.24
Van bev_mAP(sigma(all_difficulties)/3):@35.14
Van 3d_mAP(sigma(all_difficulties)/3):@26.09
Van aos_mAP(sigma(all_difficulties)/3):@0.99
bbox_mAP(sigma(allclass_mod)/num_cls):61.66345677873616
bev_mAP(sigma(allclass_mod)/num_cls):58.8884724079113
3d_mAP(sigma(allclass_mod)/num_cls):45.42775417437302
aos_mAP(sigma(allclass_mod)/num_cls):1.0701984738566923

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:67.68, 64.30, 63.51
bev  AP:65.02, 61.72, 59.92
3d   AP:53.12, 49.37, 47.89
aos  AP:0.47, 1.19, 2.06
Van coco AP@0.50:0.05:0.95:
bbox AP:30.76, 24.81, 21.60
bev  AP:31.63, 24.78, 21.81
3d   AP:24.20, 18.58, 16.25
aos  AP:0.87, 0.37, 0.89

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.36, 88.02, 86.98
bev  AP:89.60, 85.81, 79.35
3d   AP:75.66, 66.64, 65.65
aos  AP:0.59, 1.41, 2.59
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.36, 88.02, 86.98
bev  AP:90.71, 89.69, 89.14
3d   AP:90.71, 89.56, 88.91
aos  AP:0.59, 1.41, 2.59
Car bbox_mAP(sigma(all_difficulties)/3):@88.45
Car bev_mAP(sigma(all_difficulties)/3):@84.92
Car 3d_mAP(sigma(all_difficulties)/3):@69.31
Car aos_mAP(sigma(all_difficulties)/3):@1.53
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:27.93, 28.23, 25.38
bev  AP:28.31, 27.91, 25.39
3d   AP:18.67, 20.36, 19.58
aos  AP:0.92, 1.25, 2.58
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:27.93, 28.23, 25.38
bev  AP:29.86, 29.52, 29.71
3d   AP:29.79, 29.40, 29.62
aos  AP:0.92, 1.25, 2.58
Van bbox_mAP(sigma(all_difficulties)/3):@27.18
Van bev_mAP(sigma(all_difficulties)/3):@27.21
Van 3d_mAP(sigma(all_difficulties)/3):@19.54
Van aos_mAP(sigma(all_difficulties)/3):@1.58
bbox_mAP(sigma(allclass_mod)/num_cls):58.12825631587352
bev_mAP(sigma(allclass_mod)/num_cls):56.859377999751416
3d_mAP(sigma(allclass_mod)/num_cls):43.500858091040996
aos_mAP(sigma(allclass_mod)/num_cls):1.3270500923409172

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:66.05, 63.01, 61.95
bev  AP:66.46, 63.08, 60.87
3d   AP:51.56, 48.15, 47.20
aos  AP:0.42, 1.06, 1.96
Van coco AP@0.50:0.05:0.95:
bbox AP:18.77, 18.67, 18.02
bev  AP:19.24, 18.95, 18.31
3d   AP:14.49, 14.60, 14.04
aos  AP:0.65, 0.84, 1.87

eval.kitti.official.Car.bbox@0.70=[90.36, 88.02, 86.98], eval.kitti.official.Car.bev@0.70=[89.6, 85.81, 79.35], eval.kitti.official.Car.3d@0.70=[75.66, 66.64, 65.65], eval.kitti.official.Car.aos=[0.5944, 1.408, 2.585], eval.kitti.official.Car.bev@0.50=[90.71, 89.69, 89.14], eval.kitti.official.Car.3d@0.50=[90.71, 89.56, 88.91], eval.kitti.official.Car.bbox_mAP@0.70=88.45, eval.kitti.official.Car.bev_mAP@0.70=84.92, eval.kitti.official.Car.3d_mAP@0.70=69.31, eval.kitti.official.Car.aos_mAP=1.529, eval.kitti.official.Van.bbox@0.70=[27.93, 28.23, 25.38], eval.kitti.official.Van.bev@0.70=[28.31, 27.91, 25.39], eval.kitti.official.Van.3d@0.70=[18.67, 20.36, 19.58], eval.kitti.official.Van.aos=[0.9189, 1.246, 2.58], eval.kitti.official.Van.bev@0.50=[29.86, 29.52, 29.71], eval.kitti.official.Van.3d@0.50=[29.79, 29.4, 29.62], eval.kitti.official.Van.bbox_mAP@0.70=27.18, eval.kitti.official.Van.bev_mAP@0.70=27.21, eval.kitti.official.Van.3d_mAP@0.70=19.54, eval.kitti.official.Van.aos_mAP=1.582, eval.kitti.official.mAP_mod.bbox=58.13, eval.kitti.official.mAP_mod.bev=56.86, eval.kitti.official.mAP_mod.3d=43.5, eval.kitti.official.mAP_mod.aos=1.327, eval.kitti.coco.Car.bbox=[66.05, 63.01, 61.95], eval.kitti.coco.Car.bev=[66.46, 63.08, 60.87], eval.kitti.coco.Car.3d=[51.56, 48.15, 47.2], eval.kitti.coco.Car.aos=[0.4206, 1.058, 1.961], eval.kitti.coco.Van.bbox=[18.77, 18.67, 18.02], eval.kitti.coco.Van.bev=[19.24, 18.95, 18.31], eval.kitti.coco.Van.3d=[14.49, 14.6, 14.04], eval.kitti.coco.Van.aos=[0.6457, 0.8427, 1.867]Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.57, 86.87, 80.26
bev  AP:89.15, 79.60, 78.72
3d   AP:77.45, 67.04, 65.28
aos  AP:0.48, 1.39, 2.34
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.57, 86.87, 80.26
bev  AP:90.79, 89.63, 88.66
3d   AP:90.77, 89.43, 87.91
aos  AP:0.48, 1.39, 2.34
Car bbox_mAP(sigma(all_difficulties)/3):@85.90
Car bev_mAP(sigma(all_difficulties)/3):@82.49
Car 3d_mAP(sigma(all_difficulties)/3):@69.92
Car aos_mAP(sigma(all_difficulties)/3):@1.40
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:47.42, 34.44, 28.97
bev  AP:47.25, 34.27, 28.70
3d   AP:34.70, 23.21, 19.01
aos  AP:1.01, 1.14, 1.55
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:47.42, 34.44, 28.97
bev  AP:50.56, 36.80, 34.76
3d   AP:50.33, 36.42, 34.38
aos  AP:1.01, 1.14, 1.55
Van bbox_mAP(sigma(all_difficulties)/3):@36.94
Van bev_mAP(sigma(all_difficulties)/3):@36.74
Van 3d_mAP(sigma(all_difficulties)/3):@25.64
Van aos_mAP(sigma(all_difficulties)/3):@1.24
bbox_mAP(sigma(allclass_mod)/num_cls):60.654068764418916
bev_mAP(sigma(allclass_mod)/num_cls):56.93631694703167
3d_mAP(sigma(allclass_mod)/num_cls):45.12650595866624
aos_mAP(sigma(allclass_mod)/num_cls):1.2648038945581552

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:67.31, 63.52, 61.58
bev  AP:66.03, 61.41, 59.54
3d   AP:53.72, 49.02, 47.06
aos  AP:0.33, 1.03, 1.87
Van coco AP@0.50:0.05:0.95:
bbox AP:32.66, 25.31, 22.67
bev  AP:33.20, 24.39, 21.81
3d   AP:25.14, 19.14, 16.58
aos  AP:0.65, 0.76, 1.07

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:89.87, 80.14, 79.59
bev  AP:87.45, 78.97, 78.19
3d   AP:72.37, 62.17, 61.09
aos  AP:0.84, 1.45, 2.45
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:89.87, 80.14, 79.59
bev  AP:90.72, 89.39, 88.45
3d   AP:90.72, 89.16, 87.65
aos  AP:0.84, 1.45, 2.45
Car bbox_mAP(sigma(all_difficulties)/3):@83.20
Car bev_mAP(sigma(all_difficulties)/3):@81.54
Car 3d_mAP(sigma(all_difficulties)/3):@65.21
Car aos_mAP(sigma(all_difficulties)/3):@1.58
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:47.52, 33.44, 28.09
bev  AP:46.93, 32.84, 27.50
3d   AP:33.11, 22.37, 18.10
aos  AP:0.43, 0.61, 0.91
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:47.52, 33.44, 28.09
bev  AP:51.27, 39.94, 34.32
3d   AP:50.61, 39.38, 33.78
aos  AP:0.43, 0.61, 0.91
Van bbox_mAP(sigma(all_difficulties)/3):@36.35
Van bev_mAP(sigma(all_difficulties)/3):@35.75
Van 3d_mAP(sigma(all_difficulties)/3):@24.53
Van aos_mAP(sigma(all_difficulties)/3):@0.65
bbox_mAP(sigma(allclass_mod)/num_cls):56.789249453324956
bev_mAP(sigma(allclass_mod)/num_cls):55.90096517992854
3d_mAP(sigma(allclass_mod)/num_cls):42.273022084380855
aos_mAP(sigma(allclass_mod)/num_cls):1.0290997471527852

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:61.96, 58.37, 57.81
bev  AP:61.38, 58.17, 56.42
3d   AP:49.13, 45.43, 44.03
aos  AP:0.58, 1.13, 2.02
Van coco AP@0.50:0.05:0.95:
bbox AP:33.27, 25.36, 22.04
bev  AP:35.34, 25.93, 22.36
3d   AP:26.81, 19.01, 16.14
aos  AP:0.32, 0.44, 0.68

eval.kitti.official.Car.bbox@0.70=[89.87, 80.14, 79.59], eval.kitti.official.Car.bev@0.70=[87.45, 78.97, 78.19], eval.kitti.official.Car.3d@0.70=[72.37, 62.17, 61.09], eval.kitti.official.Car.aos=[0.8352, 1.451, 2.455], eval.kitti.official.Car.bev@0.50=[90.72, 89.39, 88.45], eval.kitti.official.Car.3d@0.50=[90.72, 89.16, 87.65], eval.kitti.official.Car.bbox_mAP@0.70=83.2, eval.kitti.official.Car.bev_mAP@0.70=81.54, eval.kitti.official.Car.3d_mAP@0.70=65.21, eval.kitti.official.Car.aos_mAP=1.58, eval.kitti.official.Van.bbox@0.70=[47.52, 33.44, 28.09], eval.kitti.official.Van.bev@0.70=[46.93, 32.84, 27.5], eval.kitti.official.Van.3d@0.70=[33.11, 22.37, 18.1], eval.kitti.official.Van.aos=[0.4279, 0.6072, 0.9136], eval.kitti.official.Van.bev@0.50=[51.27, 39.94, 34.32], eval.kitti.official.Van.3d@0.50=[50.61, 39.38, 33.78], eval.kitti.official.Van.bbox_mAP@0.70=36.35, eval.kitti.official.Van.bev_mAP@0.70=35.75, eval.kitti.official.Van.3d_mAP@0.70=24.53, eval.kitti.official.Van.aos_mAP=0.6496, eval.kitti.official.mAP_mod.bbox=56.79, eval.kitti.official.mAP_mod.bev=55.9, eval.kitti.official.mAP_mod.3d=42.27, eval.kitti.official.mAP_mod.aos=1.029, eval.kitti.coco.Car.bbox=[61.96, 58.37, 57.81], eval.kitti.coco.Car.bev=[61.38, 58.17, 56.42], eval.kitti.coco.Car.3d=[49.13, 45.43, 44.03], eval.kitti.coco.Car.aos=[0.5812, 1.129, 2.016], eval.kitti.coco.Van.bbox=[33.27, 25.36, 22.04], eval.kitti.coco.Van.bev=[35.34, 25.93, 22.36], eval.kitti.coco.Van.3d=[26.81, 19.01, 16.14], eval.kitti.coco.Van.aos=[0.3172, 0.441, 0.6847]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.55, 87.00, 79.97
bev  AP:89.97, 86.41, 79.37
3d   AP:78.60, 67.83, 66.00
aos  AP:1.13, 1.94, 2.65
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.55, 87.00, 79.97
bev  AP:90.62, 89.32, 88.16
3d   AP:90.62, 89.15, 87.87
aos  AP:1.13, 1.94, 2.65
Car bbox_mAP(sigma(all_difficulties)/3):@85.84
Car bev_mAP(sigma(all_difficulties)/3):@85.25
Car 3d_mAP(sigma(all_difficulties)/3):@70.81
Car aos_mAP(sigma(all_difficulties)/3):@1.91
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:52.46, 38.00, 32.43
bev  AP:51.60, 37.38, 32.37
3d   AP:40.57, 26.48, 22.72
aos  AP:3.39, 1.96, 2.77
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:52.46, 38.00, 32.43
bev  AP:54.77, 40.42, 38.43
3d   AP:54.63, 40.12, 34.45
aos  AP:3.39, 1.96, 2.77
Van bbox_mAP(sigma(all_difficulties)/3):@40.97
Van bev_mAP(sigma(all_difficulties)/3):@40.45
Van 3d_mAP(sigma(all_difficulties)/3):@29.93
Van aos_mAP(sigma(all_difficulties)/3):@2.71
bbox_mAP(sigma(allclass_mod)/num_cls):62.502699057260855
bev_mAP(sigma(allclass_mod)/num_cls):61.89473430967147
3d_mAP(sigma(allclass_mod)/num_cls):47.159629735045456
aos_mAP(sigma(allclass_mod)/num_cls):1.951288494989482

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:67.32, 63.65, 61.64
bev  AP:67.10, 63.54, 61.89
3d   AP:54.00, 49.65, 47.33
aos  AP:0.82, 1.40, 2.13
Van coco AP@0.50:0.05:0.95:
bbox AP:37.99, 28.00, 24.86
bev  AP:38.78, 27.52, 25.11
3d   AP:29.55, 20.68, 17.73
aos  AP:2.35, 1.41, 2.02

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:89.83, 86.09, 78.76
bev  AP:89.51, 79.90, 78.81
3d   AP:72.20, 62.48, 55.77
aos  AP:1.00, 1.69, 2.44
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:89.83, 86.09, 78.76
bev  AP:90.50, 89.22, 88.09
3d   AP:90.49, 88.93, 87.81
aos  AP:1.00, 1.69, 2.44
Car bbox_mAP(sigma(all_difficulties)/3):@84.89
Car bev_mAP(sigma(all_difficulties)/3):@82.74
Car 3d_mAP(sigma(all_difficulties)/3):@63.48
Car aos_mAP(sigma(all_difficulties)/3):@1.71
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:51.83, 36.92, 32.42
bev  AP:50.15, 35.99, 32.01
3d   AP:34.52, 23.27, 21.42
aos  AP:3.04, 1.84, 3.01
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:51.83, 36.92, 32.42
bev  AP:54.85, 39.06, 34.25
3d   AP:51.85, 37.91, 33.51
aos  AP:3.04, 1.84, 3.01
Van bbox_mAP(sigma(all_difficulties)/3):@40.39
Van bev_mAP(sigma(all_difficulties)/3):@39.38
Van 3d_mAP(sigma(all_difficulties)/3):@26.40
Van aos_mAP(sigma(all_difficulties)/3):@2.63
bbox_mAP(sigma(allclass_mod)/num_cls):61.50574713591932
bev_mAP(sigma(allclass_mod)/num_cls):57.94799999841152
3d_mAP(sigma(allclass_mod)/num_cls):42.87419780721875
aos_mAP(sigma(allclass_mod)/num_cls):1.7654887803350654

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:61.40, 58.69, 56.06
bev  AP:65.19, 61.26, 59.42
3d   AP:48.05, 44.89, 42.32
aos  AP:0.65, 1.17, 1.86
Van coco AP@0.50:0.05:0.95:
bbox AP:38.04, 27.47, 23.98
bev  AP:35.14, 25.40, 22.53
3d   AP:26.57, 19.14, 17.02
aos  AP:2.06, 1.29, 1.98

eval.kitti.official.Car.bbox@0.70=[89.83, 86.09, 78.76], eval.kitti.official.Car.bev@0.70=[89.51, 79.9, 78.81], eval.kitti.official.Car.3d@0.70=[72.2, 62.48, 55.77], eval.kitti.official.Car.aos=[0.9963, 1.686, 2.435], eval.kitti.official.Car.bev@0.50=[90.5, 89.22, 88.09], eval.kitti.official.Car.3d@0.50=[90.49, 88.93, 87.81], eval.kitti.official.Car.bbox_mAP@0.70=84.89, eval.kitti.official.Car.bev_mAP@0.70=82.74, eval.kitti.official.Car.3d_mAP@0.70=63.48, eval.kitti.official.Car.aos_mAP=1.706, eval.kitti.official.Van.bbox@0.70=[51.83, 36.92, 32.42], eval.kitti.official.Van.bev@0.70=[50.15, 35.99, 32.01], eval.kitti.official.Van.3d@0.70=[34.52, 23.27, 21.42], eval.kitti.official.Van.aos=[3.042, 1.845, 3.01], eval.kitti.official.Van.bev@0.50=[54.85, 39.06, 34.25], eval.kitti.official.Van.3d@0.50=[51.85, 37.91, 33.51], eval.kitti.official.Van.bbox_mAP@0.70=40.39, eval.kitti.official.Van.bev_mAP@0.70=39.38, eval.kitti.official.Van.3d_mAP@0.70=26.4, eval.kitti.official.Van.aos_mAP=2.632, eval.kitti.official.mAP_mod.bbox=61.51, eval.kitti.official.mAP_mod.bev=57.95, eval.kitti.official.mAP_mod.3d=42.87, eval.kitti.official.mAP_mod.aos=1.765, eval.kitti.coco.Car.bbox=[61.4, 58.69, 56.06], eval.kitti.coco.Car.bev=[65.19, 61.26, 59.42], eval.kitti.coco.Car.3d=[48.05, 44.89, 42.32], eval.kitti.coco.Car.aos=[0.6544, 1.17, 1.861], eval.kitti.coco.Van.bbox=[38.04, 27.47, 23.98], eval.kitti.coco.Van.bev=[35.14, 25.4, 22.53], eval.kitti.coco.Van.3d=[26.57, 19.14, 17.02], eval.kitti.coco.Van.aos=[2.065, 1.294, 1.984]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.53, 88.60, 86.47
bev  AP:89.79, 85.46, 79.70
3d   AP:84.44, 73.42, 67.77
aos  AP:0.45, 1.54, 2.37
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.53, 88.60, 86.47
bev  AP:90.64, 89.76, 88.98
3d   AP:90.64, 89.67, 88.69
aos  AP:0.45, 1.54, 2.37
Car bbox_mAP(sigma(all_difficulties)/3):@88.53
Car bev_mAP(sigma(all_difficulties)/3):@84.98
Car 3d_mAP(sigma(all_difficulties)/3):@75.21
Car aos_mAP(sigma(all_difficulties)/3):@1.45
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:32.57, 32.89, 28.84
bev  AP:32.38, 30.17, 29.13
3d   AP:27.89, 25.72, 21.58
aos  AP:1.52, 0.97, 1.85
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:32.57, 32.89, 28.84
bev  AP:33.29, 34.63, 31.33
3d   AP:33.28, 34.39, 31.18
aos  AP:1.52, 0.97, 1.85
Van bbox_mAP(sigma(all_difficulties)/3):@31.43
Van bev_mAP(sigma(all_difficulties)/3):@30.56
Van 3d_mAP(sigma(all_difficulties)/3):@25.06
Van aos_mAP(sigma(all_difficulties)/3):@1.44
bbox_mAP(sigma(allclass_mod)/num_cls):60.74647603454311
bev_mAP(sigma(allclass_mod)/num_cls):57.81622040658986
3d_mAP(sigma(allclass_mod)/num_cls):49.56814020166489
aos_mAP(sigma(allclass_mod)/num_cls):1.25530449382038

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:70.17, 66.74, 64.52
bev  AP:68.55, 64.73, 62.95
3d   AP:57.64, 52.40, 50.75
aos  AP:0.33, 1.14, 1.80
Van coco AP@0.50:0.05:0.95:
bbox AP:22.76, 23.94, 21.26
bev  AP:23.50, 23.37, 21.04
3d   AP:18.64, 18.23, 16.27
aos  AP:1.09, 0.72, 1.20

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.38, 86.43, 79.97
bev  AP:89.34, 79.55, 78.71
3d   AP:76.98, 66.58, 64.53
aos  AP:0.74, 1.66, 2.53
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.38, 86.43, 79.97
bev  AP:90.64, 89.70, 88.80
3d   AP:90.64, 89.58, 88.25
aos  AP:0.74, 1.66, 2.53
Car bbox_mAP(sigma(all_difficulties)/3):@85.60
Car bev_mAP(sigma(all_difficulties)/3):@82.54
Car 3d_mAP(sigma(all_difficulties)/3):@69.36
Car aos_mAP(sigma(all_difficulties)/3):@1.64
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:31.25, 30.69, 29.49
bev  AP:30.89, 30.23, 29.20
3d   AP:26.04, 21.34, 17.36
aos  AP:0.48, 1.12, 1.95
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:31.25, 30.69, 29.49
bev  AP:31.57, 34.19, 30.99
3d   AP:31.55, 33.90, 30.71
aos  AP:0.48, 1.12, 1.95
Van bbox_mAP(sigma(all_difficulties)/3):@30.48
Van bev_mAP(sigma(all_difficulties)/3):@30.11
Van 3d_mAP(sigma(all_difficulties)/3):@21.58
Van aos_mAP(sigma(all_difficulties)/3):@1.18
bbox_mAP(sigma(allclass_mod)/num_cls):58.56011671042141
bev_mAP(sigma(allclass_mod)/num_cls):54.88998909248741
3d_mAP(sigma(allclass_mod)/num_cls):43.95971373409386
aos_mAP(sigma(allclass_mod)/num_cls):1.3864407999449941

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:64.40, 61.32, 59.20
bev  AP:61.99, 58.80, 56.98
3d   AP:51.94, 48.02, 46.01
aos  AP:0.52, 1.22, 2.04
Van coco AP@0.50:0.05:0.95:
bbox AP:21.46, 22.27, 19.83
bev  AP:22.10, 22.74, 20.38
3d   AP:17.27, 16.97, 15.03
aos  AP:0.34, 0.80, 1.15

eval.kitti.official.Car.bbox@0.70=[90.38, 86.43, 79.97], eval.kitti.official.Car.bev@0.70=[89.34, 79.55, 78.71], eval.kitti.official.Car.3d@0.70=[76.98, 66.58, 64.53], eval.kitti.official.Car.aos=[0.7384, 1.658, 2.534], eval.kitti.official.Car.bev@0.50=[90.64, 89.7, 88.8], eval.kitti.official.Car.3d@0.50=[90.64, 89.58, 88.25], eval.kitti.official.Car.bbox_mAP@0.70=85.6, eval.kitti.official.Car.bev_mAP@0.70=82.54, eval.kitti.official.Car.3d_mAP@0.70=69.36, eval.kitti.official.Car.aos_mAP=1.643, eval.kitti.official.Van.bbox@0.70=[31.25, 30.69, 29.49], eval.kitti.official.Van.bev@0.70=[30.89, 30.23, 29.2], eval.kitti.official.Van.3d@0.70=[26.04, 21.34, 17.36], eval.kitti.official.Van.aos=[0.4775, 1.115, 1.953], eval.kitti.official.Van.bev@0.50=[31.57, 34.19, 30.99], eval.kitti.official.Van.3d@0.50=[31.55, 33.9, 30.71], eval.kitti.official.Van.bbox_mAP@0.70=30.48, eval.kitti.official.Van.bev_mAP@0.70=30.11, eval.kitti.official.Van.3d_mAP@0.70=21.58, eval.kitti.official.Van.aos_mAP=1.182, eval.kitti.official.mAP_mod.bbox=58.56, eval.kitti.official.mAP_mod.bev=54.89, eval.kitti.official.mAP_mod.3d=43.96, eval.kitti.official.mAP_mod.aos=1.386, eval.kitti.coco.Car.bbox=[64.4, 61.32, 59.2], eval.kitti.coco.Car.bev=[61.99, 58.8, 56.98], eval.kitti.coco.Car.3d=[51.94, 48.02, 46.01], eval.kitti.coco.Car.aos=[0.5246, 1.217, 2.037], eval.kitti.coco.Van.bbox=[21.46, 22.27, 19.83], eval.kitti.coco.Van.bev=[22.1, 22.74, 20.38], eval.kitti.coco.Van.3d=[17.27, 16.97, 15.03], eval.kitti.coco.Van.aos=[0.3419, 0.8028, 1.152]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.46, 87.51, 80.46
bev  AP:89.78, 80.14, 79.41
3d   AP:83.86, 73.75, 67.53
aos  AP:1.15, 2.37, 3.53
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.46, 87.51, 80.46
bev  AP:90.62, 89.60, 88.83
3d   AP:90.62, 89.51, 88.43
aos  AP:1.15, 2.37, 3.53
Car bbox_mAP(sigma(all_difficulties)/3):@86.14
Car bev_mAP(sigma(all_difficulties)/3):@83.11
Car 3d_mAP(sigma(all_difficulties)/3):@75.05
Car aos_mAP(sigma(all_difficulties)/3):@2.35
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:51.84, 37.62, 32.30
bev  AP:50.49, 37.03, 31.87
3d   AP:45.07, 30.53, 24.37
aos  AP:3.51, 1.51, 2.04
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:51.84, 37.62, 32.30
bev  AP:52.08, 38.84, 36.96
3d   AP:52.04, 38.76, 36.71
aos  AP:3.51, 1.51, 2.04
Van bbox_mAP(sigma(all_difficulties)/3):@40.58
Van bev_mAP(sigma(all_difficulties)/3):@39.80
Van 3d_mAP(sigma(all_difficulties)/3):@33.32
Van aos_mAP(sigma(all_difficulties)/3):@2.35
bbox_mAP(sigma(allclass_mod)/num_cls):62.56230808641179
bev_mAP(sigma(allclass_mod)/num_cls):58.58305245752497
3d_mAP(sigma(allclass_mod)/num_cls):52.139805847405
aos_mAP(sigma(allclass_mod)/num_cls):1.942181134987274

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:68.94, 65.04, 63.67
bev  AP:65.99, 62.36, 60.75
3d   AP:56.12, 51.74, 49.64
aos  AP:0.86, 1.78, 2.82
Van coco AP@0.50:0.05:0.95:
bbox AP:37.77, 28.03, 24.53
bev  AP:38.84, 28.27, 25.21
3d   AP:32.05, 22.93, 19.73
aos  AP:2.54, 1.10, 1.42

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:89.95, 87.18, 80.11
bev  AP:89.32, 79.92, 79.30
3d   AP:75.79, 66.42, 65.40
aos  AP:0.84, 2.02, 3.13
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:89.95, 87.18, 80.11
bev  AP:90.45, 89.32, 88.41
3d   AP:90.44, 89.19, 88.23
aos  AP:0.84, 2.02, 3.13
Car bbox_mAP(sigma(all_difficulties)/3):@85.75
Car bev_mAP(sigma(all_difficulties)/3):@82.85
Car 3d_mAP(sigma(all_difficulties)/3):@69.20
Car aos_mAP(sigma(all_difficulties)/3):@2.00
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:43.66, 32.49, 29.11
bev  AP:45.45, 33.91, 30.40
3d   AP:32.65, 23.49, 19.95
aos  AP:2.09, 1.05, 1.64
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:43.66, 32.49, 29.11
bev  AP:46.48, 35.51, 32.48
3d   AP:46.29, 34.91, 31.66
aos  AP:2.09, 1.05, 1.64
Van bbox_mAP(sigma(all_difficulties)/3):@35.09
Van bev_mAP(sigma(all_difficulties)/3):@36.59
Van 3d_mAP(sigma(all_difficulties)/3):@25.37
Van aos_mAP(sigma(all_difficulties)/3):@1.60
bbox_mAP(sigma(allclass_mod)/num_cls):59.836474389029
bev_mAP(sigma(allclass_mod)/num_cls):56.91508616235585
3d_mAP(sigma(allclass_mod)/num_cls):44.95383101013651
aos_mAP(sigma(allclass_mod)/num_cls):1.5339550582479964

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:66.05, 63.02, 60.95
bev  AP:64.85, 61.10, 59.11
3d   AP:51.99, 48.72, 46.83
aos  AP:0.60, 1.45, 2.43
Van coco AP@0.50:0.05:0.95:
bbox AP:29.05, 22.08, 19.85
bev  AP:32.18, 24.19, 21.75
3d   AP:23.13, 17.11, 15.06
aos  AP:1.53, 0.73, 1.17

eval.kitti.official.Car.bbox@0.70=[89.95, 87.18, 80.11], eval.kitti.official.Car.bev@0.70=[89.32, 79.92, 79.3], eval.kitti.official.Car.3d@0.70=[75.79, 66.42, 65.4], eval.kitti.official.Car.aos=[0.8368, 2.015, 3.134], eval.kitti.official.Car.bev@0.50=[90.45, 89.32, 88.41], eval.kitti.official.Car.3d@0.50=[90.44, 89.19, 88.23], eval.kitti.official.Car.bbox_mAP@0.70=85.75, eval.kitti.official.Car.bev_mAP@0.70=82.85, eval.kitti.official.Car.3d_mAP@0.70=69.2, eval.kitti.official.Car.aos_mAP=1.995, eval.kitti.official.Van.bbox@0.70=[43.66, 32.49, 29.11], eval.kitti.official.Van.bev@0.70=[45.45, 33.91, 30.4], eval.kitti.official.Van.3d@0.70=[32.65, 23.49, 19.95], eval.kitti.official.Van.aos=[2.092, 1.052, 1.644], eval.kitti.official.Van.bev@0.50=[46.48, 35.51, 32.48], eval.kitti.official.Van.3d@0.50=[46.29, 34.91, 31.66], eval.kitti.official.Van.bbox_mAP@0.70=35.09, eval.kitti.official.Van.bev_mAP@0.70=36.59, eval.kitti.official.Van.3d_mAP@0.70=25.37, eval.kitti.official.Van.aos_mAP=1.596, eval.kitti.official.mAP_mod.bbox=59.84, eval.kitti.official.mAP_mod.bev=56.92, eval.kitti.official.mAP_mod.3d=44.95, eval.kitti.official.mAP_mod.aos=1.534, eval.kitti.coco.Car.bbox=[66.05, 63.02, 60.95], eval.kitti.coco.Car.bev=[64.85, 61.1, 59.11], eval.kitti.coco.Car.3d=[51.99, 48.72, 46.83], eval.kitti.coco.Car.aos=[0.6015, 1.446, 2.433], eval.kitti.coco.Van.bbox=[29.05, 22.08, 19.85], eval.kitti.coco.Van.bev=[32.18, 24.19, 21.75], eval.kitti.coco.Van.3d=[23.13, 17.11, 15.06], eval.kitti.coco.Van.aos=[1.526, 0.7279, 1.173]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.29, 86.68, 80.11
bev  AP:89.40, 79.47, 79.02
3d   AP:84.79, 73.32, 67.37
aos  AP:0.56, 1.42, 2.34
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.29, 86.68, 80.11
bev  AP:90.59, 89.24, 88.85
3d   AP:90.58, 89.13, 88.48
aos  AP:0.56, 1.42, 2.34
Car bbox_mAP(sigma(all_difficulties)/3):@85.69
Car bev_mAP(sigma(all_difficulties)/3):@82.63
Car 3d_mAP(sigma(all_difficulties)/3):@75.16
Car aos_mAP(sigma(all_difficulties)/3):@1.44
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:50.71, 36.73, 31.34
bev  AP:50.75, 38.00, 31.89
3d   AP:42.83, 29.06, 23.96
aos  AP:0.01, 0.11, 0.65
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:50.71, 36.73, 31.34
bev  AP:52.48, 42.56, 38.01
3d   AP:52.29, 41.45, 36.78
aos  AP:0.01, 0.11, 0.65
Van bbox_mAP(sigma(all_difficulties)/3):@39.59
Van bev_mAP(sigma(all_difficulties)/3):@40.21
Van 3d_mAP(sigma(all_difficulties)/3):@31.95
Van aos_mAP(sigma(all_difficulties)/3):@0.26
bbox_mAP(sigma(allclass_mod)/num_cls):61.706112953936156
bev_mAP(sigma(allclass_mod)/num_cls):58.73739927728869
3d_mAP(sigma(allclass_mod)/num_cls):51.18863967655691
aos_mAP(sigma(allclass_mod)/num_cls):0.7679408801568763

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:67.64, 63.82, 62.23
bev  AP:66.11, 61.27, 60.14
3d   AP:57.02, 51.33, 49.20
aos  AP:0.40, 1.02, 1.85
Van coco AP@0.50:0.05:0.95:
bbox AP:38.20, 29.29, 25.75
bev  AP:37.58, 28.84, 25.10
3d   AP:31.07, 23.01, 19.81
aos  AP:0.01, 0.08, 0.41

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.14, 87.54, 87.20
bev  AP:89.91, 86.30, 79.74
3d   AP:84.85, 73.80, 67.82
aos  AP:1.24, 1.82, 2.93
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.14, 87.54, 87.20
bev  AP:90.52, 89.06, 88.66
3d   AP:90.50, 88.91, 88.21
aos  AP:1.24, 1.82, 2.93
Car bbox_mAP(sigma(all_difficulties)/3):@88.29
Car bev_mAP(sigma(all_difficulties)/3):@85.32
Car 3d_mAP(sigma(all_difficulties)/3):@75.49
Car aos_mAP(sigma(all_difficulties)/3):@2.00
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:50.15, 36.99, 31.32
bev  AP:50.01, 37.71, 32.00
3d   AP:36.60, 26.75, 20.87
aos  AP:0.02, 0.10, 0.71
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:50.15, 36.99, 31.32
bev  AP:51.07, 41.57, 37.15
3d   AP:50.86, 40.58, 35.90
aos  AP:0.02, 0.10, 0.71
Van bbox_mAP(sigma(all_difficulties)/3):@39.49
Van bev_mAP(sigma(all_difficulties)/3):@39.91
Van 3d_mAP(sigma(all_difficulties)/3):@28.07
Van aos_mAP(sigma(all_difficulties)/3):@0.28
bbox_mAP(sigma(allclass_mod)/num_cls):62.2643795679904
bev_mAP(sigma(allclass_mod)/num_cls):62.008020791952816
3d_mAP(sigma(allclass_mod)/num_cls):50.27507637273087
aos_mAP(sigma(allclass_mod)/num_cls):0.9617989151725372

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:70.31, 65.91, 64.55
bev  AP:65.76, 62.60, 61.57
3d   AP:56.15, 51.15, 49.50
aos  AP:0.86, 1.33, 2.15
Van coco AP@0.50:0.05:0.95:
bbox AP:35.90, 27.71, 24.04
bev  AP:34.40, 27.18, 23.64
3d   AP:27.92, 20.98, 17.68
aos  AP:0.01, 0.07, 0.51

eval.kitti.official.Car.bbox@0.70=[90.14, 87.54, 87.2], eval.kitti.official.Car.bev@0.70=[89.91, 86.3, 79.74], eval.kitti.official.Car.3d@0.70=[84.85, 73.8, 67.82], eval.kitti.official.Car.aos=[1.241, 1.819, 2.932], eval.kitti.official.Car.bev@0.50=[90.52, 89.06, 88.66], eval.kitti.official.Car.3d@0.50=[90.5, 88.91, 88.21], eval.kitti.official.Car.bbox_mAP@0.70=88.29, eval.kitti.official.Car.bev_mAP@0.70=85.32, eval.kitti.official.Car.3d_mAP@0.70=75.49, eval.kitti.official.Car.aos_mAP=1.997, eval.kitti.official.Van.bbox@0.70=[50.15, 36.99, 31.32], eval.kitti.official.Van.bev@0.70=[50.01, 37.71, 32.0], eval.kitti.official.Van.3d@0.70=[36.6, 26.75, 20.87], eval.kitti.official.Van.aos=[0.01799, 0.1049, 0.7122], eval.kitti.official.Van.bev@0.50=[51.07, 41.57, 37.15], eval.kitti.official.Van.3d@0.50=[50.86, 40.58, 35.9], eval.kitti.official.Van.bbox_mAP@0.70=39.49, eval.kitti.official.Van.bev_mAP@0.70=39.91, eval.kitti.official.Van.3d_mAP@0.70=28.07, eval.kitti.official.Van.aos_mAP=0.2784, eval.kitti.official.mAP_mod.bbox=62.26, eval.kitti.official.mAP_mod.bev=62.01, eval.kitti.official.mAP_mod.3d=50.28, eval.kitti.official.mAP_mod.aos=0.9618, eval.kitti.coco.Car.bbox=[70.31, 65.91, 64.55], eval.kitti.coco.Car.bev=[65.76, 62.6, 61.57], eval.kitti.coco.Car.3d=[56.15, 51.15, 49.5], eval.kitti.coco.Car.aos=[0.8615, 1.327, 2.146], eval.kitti.coco.Van.bbox=[35.9, 27.71, 24.04], eval.kitti.coco.Van.bev=[34.4, 27.18, 23.64], eval.kitti.coco.Van.3d=[27.92, 20.98, 17.68], eval.kitti.coco.Van.aos=[0.01216, 0.07396, 0.5056]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.55, 88.46, 87.13
bev  AP:89.95, 86.11, 79.74
3d   AP:86.19, 74.42, 68.67
aos  AP:0.27, 1.21, 2.09
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.55, 88.46, 87.13
bev  AP:90.69, 89.57, 89.12
3d   AP:90.69, 89.48, 88.91
aos  AP:0.27, 1.21, 2.09
Car bbox_mAP(sigma(all_difficulties)/3):@88.71
Car bev_mAP(sigma(all_difficulties)/3):@85.27
Car 3d_mAP(sigma(all_difficulties)/3):@76.43
Car aos_mAP(sigma(all_difficulties)/3):@1.19
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:38.56, 36.12, 31.19
bev  AP:37.95, 35.96, 31.38
3d   AP:31.84, 27.13, 22.34
aos  AP:0.53, 0.47, 0.83
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:38.56, 36.12, 31.19
bev  AP:39.44, 37.98, 35.92
3d   AP:39.31, 37.84, 35.58
aos  AP:0.53, 0.47, 0.83
Van bbox_mAP(sigma(all_difficulties)/3):@35.29
Van bev_mAP(sigma(all_difficulties)/3):@35.09
Van 3d_mAP(sigma(all_difficulties)/3):@27.10
Van aos_mAP(sigma(all_difficulties)/3):@0.61
bbox_mAP(sigma(allclass_mod)/num_cls):62.289750284014936
bev_mAP(sigma(allclass_mod)/num_cls):61.03325716238281
3d_mAP(sigma(allclass_mod)/num_cls):50.77463807181173
aos_mAP(sigma(allclass_mod)/num_cls):0.8413956413732088

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:71.19, 66.77, 65.04
bev  AP:68.83, 64.82, 63.23
3d   AP:58.24, 53.17, 51.26
aos  AP:0.20, 0.87, 1.56
Van coco AP@0.50:0.05:0.95:
bbox AP:28.24, 26.62, 23.59
bev  AP:27.49, 25.46, 23.04
3d   AP:22.70, 20.42, 17.59
aos  AP:0.36, 0.35, 0.58

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.37, 87.45, 86.61
bev  AP:89.63, 85.71, 79.43
3d   AP:84.54, 73.44, 67.56
aos  AP:0.75, 1.52, 2.40
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.37, 87.45, 86.61
bev  AP:90.65, 89.45, 89.04
3d   AP:90.64, 89.34, 88.79
aos  AP:0.75, 1.52, 2.40
Car bbox_mAP(sigma(all_difficulties)/3):@88.14
Car bev_mAP(sigma(all_difficulties)/3):@84.92
Car 3d_mAP(sigma(all_difficulties)/3):@75.18
Car aos_mAP(sigma(all_difficulties)/3):@1.56
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:32.67, 31.46, 28.36
bev  AP:31.33, 30.30, 28.30
3d   AP:23.89, 20.87, 17.79
aos  AP:1.00, 1.78, 1.64
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:32.67, 31.46, 28.36
bev  AP:33.36, 33.51, 30.13
3d   AP:33.24, 33.25, 29.90
aos  AP:1.00, 1.78, 1.64
Van bbox_mAP(sigma(all_difficulties)/3):@30.83
Van bev_mAP(sigma(all_difficulties)/3):@29.98
Van 3d_mAP(sigma(all_difficulties)/3):@20.85
Van aos_mAP(sigma(all_difficulties)/3):@1.47
bbox_mAP(sigma(allclass_mod)/num_cls):59.45763109687975
bev_mAP(sigma(allclass_mod)/num_cls):58.00419446384673
3d_mAP(sigma(allclass_mod)/num_cls):47.15262582822835
aos_mAP(sigma(allclass_mod)/num_cls):1.6518682608274697

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:68.51, 64.16, 63.13
bev  AP:67.08, 63.32, 61.79
3d   AP:56.92, 51.96, 50.70
aos  AP:0.55, 1.13, 1.83
Van coco AP@0.50:0.05:0.95:
bbox AP:23.08, 22.62, 20.52
bev  AP:21.68, 21.43, 19.74
3d   AP:17.18, 16.69, 14.81
aos  AP:0.73, 1.28, 1.15

eval.kitti.official.Car.bbox@0.70=[90.37, 87.45, 86.61], eval.kitti.official.Car.bev@0.70=[89.63, 85.71, 79.43], eval.kitti.official.Car.3d@0.70=[84.54, 73.44, 67.56], eval.kitti.official.Car.aos=[0.7534, 1.519, 2.4], eval.kitti.official.Car.bev@0.50=[90.65, 89.45, 89.04], eval.kitti.official.Car.3d@0.50=[90.64, 89.34, 88.79], eval.kitti.official.Car.bbox_mAP@0.70=88.14, eval.kitti.official.Car.bev_mAP@0.70=84.92, eval.kitti.official.Car.3d_mAP@0.70=75.18, eval.kitti.official.Car.aos_mAP=1.557, eval.kitti.official.Van.bbox@0.70=[32.67, 31.46, 28.36], eval.kitti.official.Van.bev@0.70=[31.33, 30.3, 28.3], eval.kitti.official.Van.3d@0.70=[23.89, 20.87, 17.79], eval.kitti.official.Van.aos=[0.9957, 1.785, 1.64], eval.kitti.official.Van.bev@0.50=[33.36, 33.51, 30.13], eval.kitti.official.Van.3d@0.50=[33.24, 33.25, 29.9], eval.kitti.official.Van.bbox_mAP@0.70=30.83, eval.kitti.official.Van.bev_mAP@0.70=29.98, eval.kitti.official.Van.3d_mAP@0.70=20.85, eval.kitti.official.Van.aos_mAP=1.473, eval.kitti.official.mAP_mod.bbox=59.46, eval.kitti.official.mAP_mod.bev=58.0, eval.kitti.official.mAP_mod.3d=47.15, eval.kitti.official.mAP_mod.aos=1.652, eval.kitti.coco.Car.bbox=[68.51, 64.16, 63.13], eval.kitti.coco.Car.bev=[67.08, 63.32, 61.79], eval.kitti.coco.Car.3d=[56.92, 51.96, 50.7], eval.kitti.coco.Car.aos=[0.5507, 1.129, 1.832], eval.kitti.coco.Van.bbox=[23.08, 22.62, 20.52], eval.kitti.coco.Van.bev=[21.68, 21.43, 19.74], eval.kitti.coco.Van.3d=[17.18, 16.69, 14.81], eval.kitti.coco.Van.aos=[0.7342, 1.285, 1.152]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.50, 88.92, 87.71
bev  AP:89.62, 86.21, 79.67
3d   AP:85.44, 75.36, 68.59
aos  AP:0.68, 1.44, 2.59
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.50, 88.92, 87.71
bev  AP:90.62, 89.45, 89.00
3d   AP:90.61, 89.38, 88.87
aos  AP:0.68, 1.44, 2.59
Car bbox_mAP(sigma(all_difficulties)/3):@89.04
Car bev_mAP(sigma(all_difficulties)/3):@85.16
Car 3d_mAP(sigma(all_difficulties)/3):@76.46
Car aos_mAP(sigma(all_difficulties)/3):@1.57
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:38.22, 37.77, 35.60
bev  AP:38.16, 37.42, 35.32
3d   AP:35.18, 29.92, 24.99
aos  AP:0.00, 0.71, 0.59
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:38.22, 37.77, 35.60
bev  AP:38.55, 40.97, 37.50
3d   AP:38.49, 40.79, 36.81
aos  AP:0.00, 0.71, 0.59
Van bbox_mAP(sigma(all_difficulties)/3):@37.20
Van bev_mAP(sigma(all_difficulties)/3):@36.97
Van 3d_mAP(sigma(all_difficulties)/3):@30.03
Van aos_mAP(sigma(all_difficulties)/3):@0.43
bbox_mAP(sigma(allclass_mod)/num_cls):63.34366100913549
bev_mAP(sigma(allclass_mod)/num_cls):61.812356277204884
3d_mAP(sigma(allclass_mod)/num_cls):52.64103356284749
aos_mAP(sigma(allclass_mod)/num_cls):1.0716776425025643

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:74.47, 70.65, 68.66
bev  AP:67.09, 63.61, 62.27
3d   AP:58.44, 53.80, 51.88
aos  AP:0.52, 1.08, 1.96
Van coco AP@0.50:0.05:0.95:
bbox AP:28.19, 29.33, 26.37
bev  AP:27.94, 28.02, 25.58
3d   AP:22.93, 22.51, 19.74
aos  AP:0.00, 0.52, 0.42

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.51, 88.63, 87.73
bev  AP:89.74, 86.71, 79.93
3d   AP:85.56, 75.73, 68.79
aos  AP:0.61, 1.44, 2.44
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.51, 88.63, 87.73
bev  AP:90.64, 89.54, 89.01
3d   AP:90.63, 89.48, 88.84
aos  AP:0.61, 1.44, 2.44
Car bbox_mAP(sigma(all_difficulties)/3):@88.96
Car bev_mAP(sigma(all_difficulties)/3):@85.46
Car 3d_mAP(sigma(all_difficulties)/3):@76.69
Car aos_mAP(sigma(all_difficulties)/3):@1.50
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:34.72, 35.65, 31.47
bev  AP:35.57, 36.20, 34.76
3d   AP:28.03, 27.94, 23.73
aos  AP:0.00, 0.56, 0.45
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:34.72, 35.65, 31.47
bev  AP:35.93, 39.85, 36.86
3d   AP:35.93, 39.47, 35.82
aos  AP:0.00, 0.56, 0.45
Van bbox_mAP(sigma(all_difficulties)/3):@33.95
Van bev_mAP(sigma(all_difficulties)/3):@35.51
Van 3d_mAP(sigma(all_difficulties)/3):@26.57
Van aos_mAP(sigma(all_difficulties)/3):@0.34
bbox_mAP(sigma(allclass_mod)/num_cls):62.142115268108824
bev_mAP(sigma(allclass_mod)/num_cls):61.454768206684335
3d_mAP(sigma(allclass_mod)/num_cls):51.8375170144953
aos_mAP(sigma(allclass_mod)/num_cls):0.9984074337823545

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:71.89, 68.08, 66.24
bev  AP:68.83, 64.81, 63.47
3d   AP:58.29, 53.76, 51.76
aos  AP:0.47, 1.10, 1.82
Van coco AP@0.50:0.05:0.95:
bbox AP:23.99, 27.65, 24.98
bev  AP:26.10, 27.65, 25.62
3d   AP:19.36, 20.33, 18.06
aos  AP:0.00, 0.40, 0.35

eval.kitti.official.Car.bbox@0.70=[90.51, 88.63, 87.73], eval.kitti.official.Car.bev@0.70=[89.74, 86.71, 79.93], eval.kitti.official.Car.3d@0.70=[85.56, 75.73, 68.79], eval.kitti.official.Car.aos=[0.6137, 1.441, 2.438], eval.kitti.official.Car.bev@0.50=[90.64, 89.54, 89.01], eval.kitti.official.Car.3d@0.50=[90.63, 89.48, 88.84], eval.kitti.official.Car.bbox_mAP@0.70=88.96, eval.kitti.official.Car.bev_mAP@0.70=85.46, eval.kitti.official.Car.3d_mAP@0.70=76.69, eval.kitti.official.Car.aos_mAP=1.498, eval.kitti.official.Van.bbox@0.70=[34.72, 35.65, 31.47], eval.kitti.official.Van.bev@0.70=[35.57, 36.2, 34.76], eval.kitti.official.Van.3d@0.70=[28.03, 27.94, 23.73], eval.kitti.official.Van.aos=[0.004236, 0.5561, 0.453], eval.kitti.official.Van.bev@0.50=[35.93, 39.85, 36.86], eval.kitti.official.Van.3d@0.50=[35.93, 39.47, 35.82], eval.kitti.official.Van.bbox_mAP@0.70=33.95, eval.kitti.official.Van.bev_mAP@0.70=35.51, eval.kitti.official.Van.3d_mAP@0.70=26.57, eval.kitti.official.Van.aos_mAP=0.3378, eval.kitti.official.mAP_mod.bbox=62.14, eval.kitti.official.mAP_mod.bev=61.45, eval.kitti.official.mAP_mod.3d=51.84, eval.kitti.official.mAP_mod.aos=0.9984, eval.kitti.coco.Car.bbox=[71.89, 68.08, 66.24], eval.kitti.coco.Car.bev=[68.83, 64.81, 63.47], eval.kitti.coco.Car.3d=[58.29, 53.76, 51.76], eval.kitti.coco.Car.aos=[0.4725, 1.101, 1.816], eval.kitti.coco.Van.bbox=[23.99, 27.65, 24.98], eval.kitti.coco.Van.bev=[26.1, 27.65, 25.62], eval.kitti.coco.Van.3d=[19.36, 20.33, 18.06], eval.kitti.coco.Van.aos=[0.002881, 0.3989, 0.3513]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.79, 89.46, 88.26
bev  AP:90.47, 88.25, 87.31
3d   AP:86.37, 76.49, 68.79
aos  AP:0.51, 1.52, 2.29
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.79, 89.46, 88.26
bev  AP:90.84, 90.07, 89.49
3d   AP:90.84, 90.01, 89.33
aos  AP:0.51, 1.52, 2.29
Car bbox_mAP(sigma(all_difficulties)/3):@89.50
Car bev_mAP(sigma(all_difficulties)/3):@88.68
Car 3d_mAP(sigma(all_difficulties)/3):@77.22
Car aos_mAP(sigma(all_difficulties)/3):@1.44
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:51.09, 41.43, 35.72
bev  AP:51.31, 40.84, 35.28
3d   AP:44.80, 31.55, 29.27
aos  AP:0.01, 0.28, 0.90
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:51.09, 41.43, 35.72
bev  AP:54.64, 42.63, 36.45
3d   AP:54.59, 42.52, 36.36
aos  AP:0.01, 0.28, 0.90
Van bbox_mAP(sigma(all_difficulties)/3):@42.74
Van bev_mAP(sigma(all_difficulties)/3):@42.48
Van 3d_mAP(sigma(all_difficulties)/3):@35.21
Van aos_mAP(sigma(all_difficulties)/3):@0.39
bbox_mAP(sigma(allclass_mod)/num_cls):65.4420697624414
bev_mAP(sigma(allclass_mod)/num_cls):64.54607486551586
3d_mAP(sigma(allclass_mod)/num_cls):54.023502766096136
aos_mAP(sigma(allclass_mod)/num_cls):0.9002755965068285

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:70.15, 67.18, 65.00
bev  AP:69.78, 66.06, 64.75
3d   AP:59.30, 55.18, 52.33
aos  AP:0.36, 1.05, 1.66
Van coco AP@0.50:0.05:0.95:
bbox AP:38.55, 29.50, 25.41
bev  AP:40.29, 30.82, 26.21
3d   AP:31.90, 23.92, 20.72
aos  AP:0.01, 0.19, 0.59

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.78, 89.32, 88.24
bev  AP:90.45, 87.89, 80.17
3d   AP:85.14, 74.63, 68.02
aos  AP:0.62, 1.60, 2.51
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.78, 89.32, 88.24
bev  AP:90.85, 90.07, 89.43
3d   AP:90.85, 90.01, 89.21
aos  AP:0.62, 1.60, 2.51
Car bbox_mAP(sigma(all_difficulties)/3):@89.45
Car bev_mAP(sigma(all_difficulties)/3):@86.17
Car 3d_mAP(sigma(all_difficulties)/3):@75.93
Car aos_mAP(sigma(all_difficulties)/3):@1.58
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:48.62, 40.69, 34.85
bev  AP:49.15, 40.69, 34.75
3d   AP:42.74, 31.82, 26.15
aos  AP:0.01, 0.19, 1.53
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:48.62, 40.69, 34.85
bev  AP:50.02, 42.08, 35.83
3d   AP:49.83, 41.86, 35.68
aos  AP:0.01, 0.19, 1.53
Van bbox_mAP(sigma(all_difficulties)/3):@41.39
Van bev_mAP(sigma(all_difficulties)/3):@41.53
Van 3d_mAP(sigma(all_difficulties)/3):@33.57
Van aos_mAP(sigma(all_difficulties)/3):@0.58
bbox_mAP(sigma(allclass_mod)/num_cls):65.00457101572577
bev_mAP(sigma(allclass_mod)/num_cls):64.28966879268614
3d_mAP(sigma(allclass_mod)/num_cls):53.22690350630021
aos_mAP(sigma(allclass_mod)/num_cls):0.8937338931954609

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:69.72, 65.73, 64.92
bev  AP:68.59, 64.66, 63.14
3d   AP:56.60, 51.80, 50.29
aos  AP:0.41, 1.10, 1.81
Van coco AP@0.50:0.05:0.95:
bbox AP:33.31, 27.69, 23.60
bev  AP:37.02, 30.14, 25.53
3d   AP:27.70, 22.14, 18.86
aos  AP:0.00, 0.13, 0.98

eval.kitti.official.Car.bbox@0.70=[90.78, 89.32, 88.24], eval.kitti.official.Car.bev@0.70=[90.45, 87.89, 80.17], eval.kitti.official.Car.3d@0.70=[85.14, 74.63, 68.02], eval.kitti.official.Car.aos=[0.621, 1.599, 2.513], eval.kitti.official.Car.bev@0.50=[90.85, 90.07, 89.43], eval.kitti.official.Car.3d@0.50=[90.85, 90.01, 89.21], eval.kitti.official.Car.bbox_mAP@0.70=89.45, eval.kitti.official.Car.bev_mAP@0.70=86.17, eval.kitti.official.Car.3d_mAP@0.70=75.93, eval.kitti.official.Car.aos_mAP=1.578, eval.kitti.official.Van.bbox@0.70=[48.62, 40.69, 34.85], eval.kitti.official.Van.bev@0.70=[49.15, 40.69, 34.75], eval.kitti.official.Van.3d@0.70=[42.74, 31.82, 26.15], eval.kitti.official.Van.aos=[0.007244, 0.1884, 1.533], eval.kitti.official.Van.bev@0.50=[50.02, 42.08, 35.83], eval.kitti.official.Van.3d@0.50=[49.83, 41.86, 35.68], eval.kitti.official.Van.bbox_mAP@0.70=41.39, eval.kitti.official.Van.bev_mAP@0.70=41.53, eval.kitti.official.Van.3d_mAP@0.70=33.57, eval.kitti.official.Van.aos_mAP=0.5763, eval.kitti.official.mAP_mod.bbox=65.0, eval.kitti.official.mAP_mod.bev=64.29, eval.kitti.official.mAP_mod.3d=53.23, eval.kitti.official.mAP_mod.aos=0.8937, eval.kitti.coco.Car.bbox=[69.72, 65.73, 64.92], eval.kitti.coco.Car.bev=[68.59, 64.66, 63.14], eval.kitti.coco.Car.3d=[56.6, 51.8, 50.29], eval.kitti.coco.Car.aos=[0.4134, 1.096, 1.81], eval.kitti.coco.Van.bbox=[33.31, 27.69, 23.6], eval.kitti.coco.Van.bev=[37.02, 30.14, 25.53], eval.kitti.coco.Van.3d=[27.7, 22.14, 18.86], eval.kitti.coco.Van.aos=[0.004781, 0.1287, 0.9808]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.78, 89.61, 88.75
bev  AP:89.97, 87.29, 79.78
3d   AP:87.17, 77.23, 75.49
aos  AP:0.51, 1.05, 1.67
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.78, 89.61, 88.75
bev  AP:90.80, 89.86, 89.39
3d   AP:90.80, 89.83, 89.31
aos  AP:0.51, 1.05, 1.67
Car bbox_mAP(sigma(all_difficulties)/3):@89.71
Car bev_mAP(sigma(all_difficulties)/3):@85.68
Car 3d_mAP(sigma(all_difficulties)/3):@79.97
Car aos_mAP(sigma(all_difficulties)/3):@1.08
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:61.94, 45.79, 39.63
bev  AP:62.11, 45.75, 39.92
3d   AP:58.71, 38.34, 32.19
aos  AP:0.14, 0.68, 1.54
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:61.94, 45.79, 39.63
bev  AP:63.17, 48.02, 42.12
3d   AP:63.16, 47.53, 42.04
aos  AP:0.14, 0.68, 1.54
Van bbox_mAP(sigma(all_difficulties)/3):@49.12
Van bev_mAP(sigma(all_difficulties)/3):@49.26
Van 3d_mAP(sigma(all_difficulties)/3):@43.08
Van aos_mAP(sigma(all_difficulties)/3):@0.79
bbox_mAP(sigma(allclass_mod)/num_cls):67.70095954360131
bev_mAP(sigma(allclass_mod)/num_cls):66.52149460140745
3d_mAP(sigma(allclass_mod)/num_cls):57.78703747741048
aos_mAP(sigma(allclass_mod)/num_cls):0.8688172327359608

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:73.66, 69.88, 68.00
bev  AP:70.17, 65.99, 64.23
3d   AP:60.59, 55.67, 54.08
aos  AP:0.39, 0.75, 1.28
Van coco AP@0.50:0.05:0.95:
bbox AP:47.52, 34.32, 29.99
bev  AP:48.81, 35.48, 30.88
3d   AP:40.73, 28.50, 24.53
aos  AP:0.10, 0.46, 1.10

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.78, 89.51, 88.63
bev  AP:89.95, 86.60, 79.65
3d   AP:84.87, 75.29, 68.13
aos  AP:0.43, 1.05, 1.80
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.78, 89.51, 88.63
bev  AP:90.82, 89.87, 89.44
3d   AP:90.82, 89.83, 89.31
aos  AP:0.43, 1.05, 1.80
Car bbox_mAP(sigma(all_difficulties)/3):@89.64
Car bev_mAP(sigma(all_difficulties)/3):@85.40
Car 3d_mAP(sigma(all_difficulties)/3):@76.10
Car aos_mAP(sigma(all_difficulties)/3):@1.09
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:61.68, 42.73, 39.46
bev  AP:61.81, 45.10, 39.14
3d   AP:58.52, 37.91, 31.73
aos  AP:0.01, 0.94, 1.37
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:61.68, 42.73, 39.46
bev  AP:62.53, 46.72, 41.47
3d   AP:62.52, 46.44, 41.27
aos  AP:0.01, 0.94, 1.37
Van bbox_mAP(sigma(all_difficulties)/3):@47.96
Van bev_mAP(sigma(all_difficulties)/3):@48.68
Van 3d_mAP(sigma(all_difficulties)/3):@42.72
Van aos_mAP(sigma(all_difficulties)/3):@0.77
bbox_mAP(sigma(allclass_mod)/num_cls):66.118870146916
bev_mAP(sigma(allclass_mod)/num_cls):65.85075924387272
3d_mAP(sigma(allclass_mod)/num_cls):56.602287180589826
aos_mAP(sigma(allclass_mod)/num_cls):0.9935272673749431

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:72.54, 68.90, 67.65
bev  AP:68.65, 64.72, 63.21
3d   AP:58.31, 54.05, 51.67
aos  AP:0.33, 0.76, 1.39
Van coco AP@0.50:0.05:0.95:
bbox AP:46.09, 32.81, 28.35
bev  AP:48.66, 34.43, 29.83
3d   AP:40.95, 28.01, 24.18
aos  AP:0.01, 0.67, 0.92

eval.kitti.official.Car.bbox@0.70=[90.78, 89.51, 88.63], eval.kitti.official.Car.bev@0.70=[89.95, 86.6, 79.65], eval.kitti.official.Car.3d@0.70=[84.87, 75.29, 68.13], eval.kitti.official.Car.aos=[0.4277, 1.051, 1.798], eval.kitti.official.Car.bev@0.50=[90.82, 89.87, 89.44], eval.kitti.official.Car.3d@0.50=[90.82, 89.83, 89.31], eval.kitti.official.Car.bbox_mAP@0.70=89.64, eval.kitti.official.Car.bev_mAP@0.70=85.4, eval.kitti.official.Car.3d_mAP@0.70=76.1, eval.kitti.official.Car.aos_mAP=1.092, eval.kitti.official.Van.bbox@0.70=[61.68, 42.73, 39.46], eval.kitti.official.Van.bev@0.70=[61.81, 45.1, 39.14], eval.kitti.official.Van.3d@0.70=[58.52, 37.91, 31.73], eval.kitti.official.Van.aos=[0.01003, 0.9363, 1.372], eval.kitti.official.Van.bev@0.50=[62.53, 46.72, 41.47], eval.kitti.official.Van.3d@0.50=[62.52, 46.44, 41.27], eval.kitti.official.Van.bbox_mAP@0.70=47.96, eval.kitti.official.Van.bev_mAP@0.70=48.68, eval.kitti.official.Van.3d_mAP@0.70=42.72, eval.kitti.official.Van.aos_mAP=0.7728, eval.kitti.official.mAP_mod.bbox=66.12, eval.kitti.official.mAP_mod.bev=65.85, eval.kitti.official.mAP_mod.3d=56.6, eval.kitti.official.mAP_mod.aos=0.9935, eval.kitti.coco.Car.bbox=[72.54, 68.9, 67.65], eval.kitti.coco.Car.bev=[68.65, 64.72, 63.21], eval.kitti.coco.Car.3d=[58.31, 54.05, 51.67], eval.kitti.coco.Car.aos=[0.3325, 0.7576, 1.392], eval.kitti.coco.Van.bbox=[46.09, 32.81, 28.35], eval.kitti.coco.Van.bev=[48.66, 34.43, 29.83], eval.kitti.coco.Van.3d=[40.95, 28.01, 24.18], eval.kitti.coco.Van.aos=[0.007394, 0.6746, 0.918]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.68, 89.22, 87.97
bev  AP:90.25, 87.58, 86.51
3d   AP:88.45, 78.09, 75.79
aos  AP:0.29, 1.21, 2.25
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.68, 89.22, 87.97
bev  AP:90.76, 89.77, 89.32
3d   AP:90.76, 89.71, 89.16
aos  AP:0.29, 1.21, 2.25
Car bbox_mAP(sigma(all_difficulties)/3):@89.29
Car bev_mAP(sigma(all_difficulties)/3):@88.11
Car 3d_mAP(sigma(all_difficulties)/3):@80.78
Car aos_mAP(sigma(all_difficulties)/3):@1.25
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:60.41, 41.49, 37.58
bev  AP:61.86, 43.64, 37.97
3d   AP:56.62, 38.28, 31.71
aos  AP:0.91, 0.39, 0.86
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:60.41, 41.49, 37.58
bev  AP:62.84, 46.18, 40.73
3d   AP:62.83, 45.93, 40.51
aos  AP:0.91, 0.39, 0.86
Van bbox_mAP(sigma(all_difficulties)/3):@46.49
Van bev_mAP(sigma(all_difficulties)/3):@47.82
Van 3d_mAP(sigma(all_difficulties)/3):@42.20
Van aos_mAP(sigma(all_difficulties)/3):@0.72
bbox_mAP(sigma(allclass_mod)/num_cls):65.35320316123561
bev_mAP(sigma(allclass_mod)/num_cls):65.60683132157328
3d_mAP(sigma(allclass_mod)/num_cls):58.183692054464146
aos_mAP(sigma(allclass_mod)/num_cls):0.8014633190131368

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:71.57, 68.10, 66.26
bev  AP:70.51, 66.28, 65.06
3d   AP:61.52, 56.51, 54.75
aos  AP:0.21, 0.90, 1.72
Van coco AP@0.50:0.05:0.95:
bbox AP:46.57, 32.71, 28.42
bev  AP:48.93, 34.17, 29.80
3d   AP:40.94, 28.25, 24.15
aos  AP:0.65, 0.30, 0.59

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.73, 89.27, 87.92
bev  AP:90.38, 87.80, 86.66
3d   AP:88.20, 78.00, 75.72
aos  AP:0.58, 1.43, 2.49
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.73, 89.27, 87.92
bev  AP:90.80, 89.86, 89.36
3d   AP:90.80, 89.80, 89.24
aos  AP:0.58, 1.43, 2.49
Car bbox_mAP(sigma(all_difficulties)/3):@89.31
Car bev_mAP(sigma(all_difficulties)/3):@88.28
Car 3d_mAP(sigma(all_difficulties)/3):@80.64
Car aos_mAP(sigma(all_difficulties)/3):@1.50
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:62.97, 41.86, 38.22
bev  AP:63.18, 41.87, 38.28
3d   AP:60.63, 38.68, 32.51
aos  AP:0.45, 0.17, 1.02
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:62.97, 41.86, 38.22
bev  AP:63.63, 45.65, 40.16
3d   AP:63.62, 45.21, 40.06
aos  AP:0.45, 0.17, 1.02
Van bbox_mAP(sigma(all_difficulties)/3):@47.68
Van bev_mAP(sigma(all_difficulties)/3):@47.78
Van 3d_mAP(sigma(all_difficulties)/3):@43.94
Van aos_mAP(sigma(all_difficulties)/3):@0.55
bbox_mAP(sigma(allclass_mod)/num_cls):65.56397865792782
bev_mAP(sigma(allclass_mod)/num_cls):64.83334942902125
3d_mAP(sigma(allclass_mod)/num_cls):58.33937042765081
aos_mAP(sigma(allclass_mod)/num_cls):0.8008292033809753

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:71.18, 67.84, 66.02
bev  AP:70.13, 66.54, 64.69
3d   AP:60.99, 56.07, 54.18
aos  AP:0.44, 1.05, 1.87
Van coco AP@0.50:0.05:0.95:
bbox AP:48.53, 32.55, 28.30
bev  AP:48.46, 33.65, 29.76
3d   AP:40.56, 27.43, 23.75
aos  AP:0.35, 0.14, 0.69

eval.kitti.official.Car.bbox@0.70=[90.73, 89.27, 87.92], eval.kitti.official.Car.bev@0.70=[90.38, 87.8, 86.66], eval.kitti.official.Car.3d@0.70=[88.2, 78.0, 75.72], eval.kitti.official.Car.aos=[0.5791, 1.431, 2.488], eval.kitti.official.Car.bev@0.50=[90.8, 89.86, 89.36], eval.kitti.official.Car.3d@0.50=[90.8, 89.8, 89.24], eval.kitti.official.Car.bbox_mAP@0.70=89.31, eval.kitti.official.Car.bev_mAP@0.70=88.28, eval.kitti.official.Car.3d_mAP@0.70=80.64, eval.kitti.official.Car.aos_mAP=1.5, eval.kitti.official.Van.bbox@0.70=[62.97, 41.86, 38.22], eval.kitti.official.Van.bev@0.70=[63.18, 41.87, 38.28], eval.kitti.official.Van.3d@0.70=[60.63, 38.68, 32.51], eval.kitti.official.Van.aos=[0.4498, 0.1702, 1.017], eval.kitti.official.Van.bev@0.50=[63.63, 45.65, 40.16], eval.kitti.official.Van.3d@0.50=[63.62, 45.21, 40.06], eval.kitti.official.Van.bbox_mAP@0.70=47.68, eval.kitti.official.Van.bev_mAP@0.70=47.78, eval.kitti.official.Van.3d_mAP@0.70=43.94, eval.kitti.official.Van.aos_mAP=0.5457, eval.kitti.official.mAP_mod.bbox=65.56, eval.kitti.official.mAP_mod.bev=64.83, eval.kitti.official.mAP_mod.3d=58.34, eval.kitti.official.mAP_mod.aos=0.8008, eval.kitti.coco.Car.bbox=[71.18, 67.84, 66.02], eval.kitti.coco.Car.bev=[70.13, 66.54, 64.69], eval.kitti.coco.Car.3d=[60.99, 56.07, 54.18], eval.kitti.coco.Car.aos=[0.4368, 1.046, 1.871], eval.kitti.coco.Van.bbox=[48.53, 32.55, 28.3], eval.kitti.coco.Van.bev=[48.46, 33.65, 29.76], eval.kitti.coco.Van.3d=[40.56, 27.43, 23.75], eval.kitti.coco.Van.aos=[0.3506, 0.1368, 0.688]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.82, 89.77, 88.52
bev  AP:90.29, 88.08, 86.60
3d   AP:88.24, 78.32, 76.25
aos  AP:0.56, 1.35, 2.20
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.82, 89.77, 88.52
bev  AP:90.86, 90.06, 89.52
3d   AP:90.86, 90.02, 89.40
aos  AP:0.56, 1.35, 2.20
Car bbox_mAP(sigma(all_difficulties)/3):@89.70
Car bev_mAP(sigma(all_difficulties)/3):@88.33
Car 3d_mAP(sigma(all_difficulties)/3):@80.94
Car aos_mAP(sigma(all_difficulties)/3):@1.37
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:61.26, 42.11, 38.62
bev  AP:60.99, 42.17, 38.89
3d   AP:58.21, 38.09, 32.45
aos  AP:0.30, 0.12, 1.15
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:61.26, 42.11, 38.62
bev  AP:61.39, 45.17, 40.30
3d   AP:61.33, 45.05, 39.89
aos  AP:0.30, 0.12, 1.15
Van bbox_mAP(sigma(all_difficulties)/3):@47.33
Van bev_mAP(sigma(all_difficulties)/3):@47.35
Van 3d_mAP(sigma(all_difficulties)/3):@42.92
Van aos_mAP(sigma(all_difficulties)/3):@0.52
bbox_mAP(sigma(allclass_mod)/num_cls):65.93962120205579
bev_mAP(sigma(allclass_mod)/num_cls):65.12437078243133
3d_mAP(sigma(allclass_mod)/num_cls):58.20833641123001
aos_mAP(sigma(allclass_mod)/num_cls):0.7331796170217979

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:73.72, 69.53, 67.91
bev  AP:69.62, 66.51, 65.07
3d   AP:61.02, 56.33, 54.44
aos  AP:0.44, 0.98, 1.66
Van coco AP@0.50:0.05:0.95:
bbox AP:46.59, 32.59, 28.73
bev  AP:48.56, 34.09, 29.87
3d   AP:40.03, 27.11, 23.76
aos  AP:0.22, 0.09, 0.72

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.77, 89.67, 88.30
bev  AP:90.35, 87.99, 86.71
3d   AP:88.06, 78.31, 76.13
aos  AP:0.66, 1.39, 2.35
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.77, 89.67, 88.30
bev  AP:90.85, 90.06, 89.50
3d   AP:90.85, 90.01, 89.36
aos  AP:0.66, 1.39, 2.35
Car bbox_mAP(sigma(all_difficulties)/3):@89.58
Car bev_mAP(sigma(all_difficulties)/3):@88.35
Car 3d_mAP(sigma(all_difficulties)/3):@80.83
Car aos_mAP(sigma(all_difficulties)/3):@1.47
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:61.93, 41.63, 35.33
bev  AP:63.18, 42.16, 38.46
3d   AP:59.53, 38.06, 32.15
aos  AP:0.34, 0.27, 1.36
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:61.93, 41.63, 35.33
bev  AP:63.57, 43.19, 39.69
3d   AP:63.54, 42.98, 39.29
aos  AP:0.34, 0.27, 1.36
Van bbox_mAP(sigma(all_difficulties)/3):@46.30
Van bev_mAP(sigma(all_difficulties)/3):@47.94
Van 3d_mAP(sigma(all_difficulties)/3):@43.25
Van aos_mAP(sigma(all_difficulties)/3):@0.65
bbox_mAP(sigma(allclass_mod)/num_cls):65.65142502515424
bev_mAP(sigma(allclass_mod)/num_cls):65.07572404185038
3d_mAP(sigma(allclass_mod)/num_cls):58.18972294560053
aos_mAP(sigma(allclass_mod)/num_cls):0.8302629360058997

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:72.78, 69.09, 67.53
bev  AP:69.83, 66.47, 65.02
3d   AP:61.07, 56.23, 54.35
aos  AP:0.51, 1.06, 1.81
Van coco AP@0.50:0.05:0.95:
bbox AP:46.54, 31.14, 27.28
bev  AP:49.08, 32.56, 29.06
3d   AP:40.49, 26.27, 23.04
aos  AP:0.25, 0.21, 0.96

eval.kitti.official.Car.bbox@0.70=[90.77, 89.67, 88.3], eval.kitti.official.Car.bev@0.70=[90.35, 87.99, 86.71], eval.kitti.official.Car.3d@0.70=[88.06, 78.31, 76.13], eval.kitti.official.Car.aos=[0.6557, 1.395, 2.345], eval.kitti.official.Car.bev@0.50=[90.85, 90.06, 89.5], eval.kitti.official.Car.3d@0.50=[90.85, 90.01, 89.36], eval.kitti.official.Car.bbox_mAP@0.70=89.58, eval.kitti.official.Car.bev_mAP@0.70=88.35, eval.kitti.official.Car.3d_mAP@0.70=80.83, eval.kitti.official.Car.aos_mAP=1.465, eval.kitti.official.Van.bbox@0.70=[61.93, 41.63, 35.33], eval.kitti.official.Van.bev@0.70=[63.18, 42.16, 38.46], eval.kitti.official.Van.3d@0.70=[59.53, 38.06, 32.15], eval.kitti.official.Van.aos=[0.3389, 0.2656, 1.36], eval.kitti.official.Van.bev@0.50=[63.57, 43.19, 39.69], eval.kitti.official.Van.3d@0.50=[63.54, 42.98, 39.29], eval.kitti.official.Van.bbox_mAP@0.70=46.3, eval.kitti.official.Van.bev_mAP@0.70=47.94, eval.kitti.official.Van.3d_mAP@0.70=43.25, eval.kitti.official.Van.aos_mAP=0.655, eval.kitti.official.mAP_mod.bbox=65.65, eval.kitti.official.mAP_mod.bev=65.08, eval.kitti.official.mAP_mod.3d=58.19, eval.kitti.official.mAP_mod.aos=0.8303, eval.kitti.coco.Car.bbox=[72.78, 69.09, 67.53], eval.kitti.coco.Car.bev=[69.83, 66.47, 65.02], eval.kitti.coco.Car.3d=[61.07, 56.23, 54.35], eval.kitti.coco.Car.aos=[0.5122, 1.061, 1.811], eval.kitti.coco.Van.bbox=[46.54, 31.14, 27.28], eval.kitti.coco.Van.bev=[49.08, 32.56, 29.06], eval.kitti.coco.Van.3d=[40.49, 26.27, 23.04], eval.kitti.coco.Van.aos=[0.2512, 0.205, 0.9572]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.83, 89.65, 88.77
bev  AP:90.47, 88.24, 86.87
3d   AP:89.17, 78.76, 77.41
aos  AP:0.32, 1.12, 1.76
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.83, 89.65, 88.77
bev  AP:90.85, 89.99, 89.48
3d   AP:90.85, 89.94, 89.39
aos  AP:0.32, 1.12, 1.76
Car bbox_mAP(sigma(all_difficulties)/3):@89.75
Car bev_mAP(sigma(all_difficulties)/3):@88.53
Car 3d_mAP(sigma(all_difficulties)/3):@81.78
Car aos_mAP(sigma(all_difficulties)/3):@1.07
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:62.95, 42.55, 38.70
bev  AP:62.35, 44.99, 39.00
3d   AP:60.14, 39.08, 32.75
aos  AP:0.64, 0.79, 1.02
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:62.95, 42.55, 38.70
bev  AP:63.06, 46.02, 40.52
3d   AP:63.05, 46.00, 40.41
aos  AP:0.64, 0.79, 1.02
Van bbox_mAP(sigma(all_difficulties)/3):@48.07
Van bev_mAP(sigma(all_difficulties)/3):@48.78
Van 3d_mAP(sigma(all_difficulties)/3):@43.99
Van aos_mAP(sigma(all_difficulties)/3):@0.82
bbox_mAP(sigma(allclass_mod)/num_cls):66.09979816869392
bev_mAP(sigma(allclass_mod)/num_cls):66.61464575670837
3d_mAP(sigma(allclass_mod)/num_cls):58.91731977381589
aos_mAP(sigma(allclass_mod)/num_cls):0.9506371264191498

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:73.18, 69.13, 67.66
bev  AP:71.61, 67.57, 66.14
3d   AP:62.51, 57.80, 55.88
aos  AP:0.25, 0.80, 1.31
Van coco AP@0.50:0.05:0.95:
bbox AP:48.50, 33.39, 29.21
bev  AP:48.68, 34.14, 30.05
3d   AP:40.89, 27.91, 24.16
aos  AP:0.48, 0.55, 0.70

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.84, 89.70, 88.76
bev  AP:90.53, 88.39, 86.99
3d   AP:89.51, 79.10, 77.70
aos  AP:0.45, 1.16, 1.76
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.84, 89.70, 88.76
bev  AP:90.84, 90.02, 89.50
3d   AP:90.84, 89.99, 89.40
aos  AP:0.45, 1.16, 1.76
Car bbox_mAP(sigma(all_difficulties)/3):@89.77
Car bev_mAP(sigma(all_difficulties)/3):@88.64
Car 3d_mAP(sigma(all_difficulties)/3):@82.11
Car aos_mAP(sigma(all_difficulties)/3):@1.13
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:64.63, 42.81, 39.03
bev  AP:64.42, 42.62, 39.04
3d   AP:62.65, 39.83, 33.12
aos  AP:0.62, 0.49, 1.07
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:64.63, 42.81, 39.03
bev  AP:64.62, 46.06, 40.21
3d   AP:64.62, 45.99, 39.98
aos  AP:0.62, 0.49, 1.07
Van bbox_mAP(sigma(all_difficulties)/3):@48.82
Van bev_mAP(sigma(all_difficulties)/3):@48.69
Van 3d_mAP(sigma(all_difficulties)/3):@45.20
Van aos_mAP(sigma(all_difficulties)/3):@0.73
bbox_mAP(sigma(allclass_mod)/num_cls):66.2585797297689
bev_mAP(sigma(allclass_mod)/num_cls):65.50231611745143
3d_mAP(sigma(allclass_mod)/num_cls):59.467842334663054
aos_mAP(sigma(allclass_mod)/num_cls):0.8289922972797599

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:72.62, 68.80, 67.37
bev  AP:71.29, 67.22, 65.79
3d   AP:62.66, 57.47, 55.52
aos  AP:0.35, 0.86, 1.33
Van coco AP@0.50:0.05:0.95:
bbox AP:50.12, 33.55, 29.07
bev  AP:51.66, 34.89, 30.47
3d   AP:42.99, 28.28, 24.45
aos  AP:0.47, 0.35, 0.73

eval.kitti.official.Car.bbox@0.70=[90.84, 89.7, 88.76], eval.kitti.official.Car.bev@0.70=[90.53, 88.39, 86.99], eval.kitti.official.Car.3d@0.70=[89.51, 79.1, 77.7], eval.kitti.official.Car.aos=[0.4502, 1.165, 1.76], eval.kitti.official.Car.bev@0.50=[90.84, 90.02, 89.5], eval.kitti.official.Car.3d@0.50=[90.84, 89.99, 89.4], eval.kitti.official.Car.bbox_mAP@0.70=89.77, eval.kitti.official.Car.bev_mAP@0.70=88.64, eval.kitti.official.Car.3d_mAP@0.70=82.11, eval.kitti.official.Car.aos_mAP=1.125, eval.kitti.official.Van.bbox@0.70=[64.63, 42.81, 39.03], eval.kitti.official.Van.bev@0.70=[64.42, 42.62, 39.04], eval.kitti.official.Van.3d@0.70=[62.65, 39.83, 33.12], eval.kitti.official.Van.aos=[0.6213, 0.4931, 1.072], eval.kitti.official.Van.bev@0.50=[64.62, 46.06, 40.21], eval.kitti.official.Van.3d@0.50=[64.62, 45.99, 39.98], eval.kitti.official.Van.bbox_mAP@0.70=48.82, eval.kitti.official.Van.bev_mAP@0.70=48.69, eval.kitti.official.Van.3d_mAP@0.70=45.2, eval.kitti.official.Van.aos_mAP=0.7287, eval.kitti.official.mAP_mod.bbox=66.26, eval.kitti.official.mAP_mod.bev=65.5, eval.kitti.official.mAP_mod.3d=59.47, eval.kitti.official.mAP_mod.aos=0.829, eval.kitti.coco.Car.bbox=[72.62, 68.8, 67.37], eval.kitti.coco.Car.bev=[71.29, 67.22, 65.79], eval.kitti.coco.Car.3d=[62.66, 57.47, 55.52], eval.kitti.coco.Car.aos=[0.3456, 0.8574, 1.327], eval.kitti.coco.Van.bbox=[50.12, 33.55, 29.07], eval.kitti.coco.Van.bev=[51.66, 34.89, 30.47], eval.kitti.coco.Van.3d=[42.99, 28.28, 24.45], eval.kitti.coco.Van.aos=[0.4692, 0.3486, 0.7278]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.83, 89.75, 88.97
bev  AP:90.55, 88.27, 86.92
3d   AP:89.43, 79.06, 77.73
aos  AP:0.31, 1.19, 1.80
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.83, 89.75, 88.97
bev  AP:90.84, 89.97, 89.48
3d   AP:90.84, 89.94, 89.41
aos  AP:0.31, 1.19, 1.80
Car bbox_mAP(sigma(all_difficulties)/3):@89.85
Car bev_mAP(sigma(all_difficulties)/3):@88.58
Car 3d_mAP(sigma(all_difficulties)/3):@82.08
Car aos_mAP(sigma(all_difficulties)/3):@1.10
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:65.55, 45.77, 39.60
bev  AP:65.24, 45.48, 39.54
3d   AP:63.22, 41.12, 34.40
aos  AP:0.63, 0.70, 1.16
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:65.55, 45.77, 39.60
bev  AP:65.57, 47.10, 41.33
3d   AP:65.56, 46.45, 41.24
aos  AP:0.63, 0.70, 1.16
Van bbox_mAP(sigma(all_difficulties)/3):@50.30
Van bev_mAP(sigma(all_difficulties)/3):@50.09
Van 3d_mAP(sigma(all_difficulties)/3):@46.25
Van aos_mAP(sigma(all_difficulties)/3):@0.83
bbox_mAP(sigma(allclass_mod)/num_cls):67.75858613004709
bev_mAP(sigma(allclass_mod)/num_cls):66.87629609208346
3d_mAP(sigma(allclass_mod)/num_cls):60.0902016546593
aos_mAP(sigma(allclass_mod)/num_cls):0.9479850618227156

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:74.65, 70.97, 69.58
bev  AP:71.30, 67.35, 65.95
3d   AP:62.41, 57.86, 55.94
aos  AP:0.24, 0.85, 1.36
Van coco AP@0.50:0.05:0.95:
bbox AP:51.25, 35.54, 30.58
bev  AP:50.44, 34.62, 30.42
3d   AP:42.68, 28.46, 24.67
aos  AP:0.48, 0.54, 0.86

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.84, 89.76, 88.91
bev  AP:90.59, 88.39, 87.02
3d   AP:89.43, 79.11, 77.73
aos  AP:0.31, 1.15, 1.74
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.84, 89.76, 88.91
bev  AP:90.85, 90.00, 89.49
3d   AP:90.85, 89.98, 89.41
aos  AP:0.31, 1.15, 1.74
Car bbox_mAP(sigma(all_difficulties)/3):@89.83
Car bev_mAP(sigma(all_difficulties)/3):@88.66
Car 3d_mAP(sigma(all_difficulties)/3):@82.09
Car aos_mAP(sigma(all_difficulties)/3):@1.07
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:66.19, 46.99, 40.16
bev  AP:66.13, 46.96, 40.24
3d   AP:63.83, 41.61, 34.61
aos  AP:0.44, 0.52, 1.07
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:66.19, 46.99, 40.16
bev  AP:66.17, 46.84, 41.15
3d   AP:66.17, 47.38, 41.11
aos  AP:0.44, 0.52, 1.07
Van bbox_mAP(sigma(all_difficulties)/3):@51.11
Van bev_mAP(sigma(all_difficulties)/3):@51.11
Van 3d_mAP(sigma(all_difficulties)/3):@46.68
Van aos_mAP(sigma(all_difficulties)/3):@0.68
bbox_mAP(sigma(allclass_mod)/num_cls):68.37394778134743
bev_mAP(sigma(allclass_mod)/num_cls):67.67469901736594
3d_mAP(sigma(allclass_mod)/num_cls):60.35745178114084
aos_mAP(sigma(allclass_mod)/num_cls):0.8339845226162884

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:74.56, 71.05, 69.50
bev  AP:71.34, 67.41, 65.97
3d   AP:62.33, 57.81, 55.82
aos  AP:0.24, 0.83, 1.35
Van coco AP@0.50:0.05:0.95:
bbox AP:52.15, 35.88, 30.38
bev  AP:50.51, 35.05, 30.57
3d   AP:42.88, 29.11, 25.12
aos  AP:0.35, 0.38, 0.75

eval.kitti.official.Car.bbox@0.70=[90.84, 89.76, 88.91], eval.kitti.official.Car.bev@0.70=[90.59, 88.39, 87.02], eval.kitti.official.Car.3d@0.70=[89.43, 79.11, 77.73], eval.kitti.official.Car.aos=[0.3129, 1.147, 1.744], eval.kitti.official.Car.bev@0.50=[90.85, 90.0, 89.49], eval.kitti.official.Car.3d@0.50=[90.85, 89.98, 89.41], eval.kitti.official.Car.bbox_mAP@0.70=89.83, eval.kitti.official.Car.bev_mAP@0.70=88.66, eval.kitti.official.Car.3d_mAP@0.70=82.09, eval.kitti.official.Car.aos_mAP=1.068, eval.kitti.official.Van.bbox@0.70=[66.19, 46.99, 40.16], eval.kitti.official.Van.bev@0.70=[66.13, 46.96, 40.24], eval.kitti.official.Van.3d@0.70=[63.83, 41.61, 34.61], eval.kitti.official.Van.aos=[0.4415, 0.5206, 1.065], eval.kitti.official.Van.bev@0.50=[66.17, 46.84, 41.15], eval.kitti.official.Van.3d@0.50=[66.17, 47.38, 41.11], eval.kitti.official.Van.bbox_mAP@0.70=51.11, eval.kitti.official.Van.bev_mAP@0.70=51.11, eval.kitti.official.Van.3d_mAP@0.70=46.68, eval.kitti.official.Van.aos_mAP=0.6758, eval.kitti.official.mAP_mod.bbox=68.37, eval.kitti.official.mAP_mod.bev=67.67, eval.kitti.official.mAP_mod.3d=60.36, eval.kitti.official.mAP_mod.aos=0.834, eval.kitti.coco.Car.bbox=[74.56, 71.05, 69.5], eval.kitti.coco.Car.bev=[71.34, 67.41, 65.97], eval.kitti.coco.Car.3d=[62.33, 57.81, 55.82], eval.kitti.coco.Car.aos=[0.2421, 0.826, 1.345], eval.kitti.coco.Van.bbox=[52.15, 35.88, 30.38], eval.kitti.coco.Van.bev=[50.51, 35.05, 30.57], eval.kitti.coco.Van.3d=[42.88, 29.11, 25.12], eval.kitti.coco.Van.aos=[0.3493, 0.3817, 0.7513]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.85, 89.72, 88.88
bev  AP:90.65, 88.41, 87.12
3d   AP:89.61, 79.21, 77.91
aos  AP:0.15, 1.12, 1.72
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.85, 89.72, 88.88
bev  AP:90.85, 89.98, 89.53
3d   AP:90.85, 89.95, 89.45
aos  AP:0.15, 1.12, 1.72
Car bbox_mAP(sigma(all_difficulties)/3):@89.82
Car bev_mAP(sigma(all_difficulties)/3):@88.73
Car 3d_mAP(sigma(all_difficulties)/3):@82.24
Car aos_mAP(sigma(all_difficulties)/3):@1.00
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:62.99, 43.91, 40.07
bev  AP:62.54, 43.65, 39.81
3d   AP:60.30, 40.75, 33.66
aos  AP:0.63, 0.66, 1.39
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:62.99, 43.91, 40.07
bev  AP:63.22, 47.36, 41.66
3d   AP:63.20, 47.30, 41.56
aos  AP:0.63, 0.66, 1.39
Van bbox_mAP(sigma(all_difficulties)/3):@48.99
Van bev_mAP(sigma(all_difficulties)/3):@48.67
Van 3d_mAP(sigma(all_difficulties)/3):@44.90
Van aos_mAP(sigma(all_difficulties)/3):@0.89
bbox_mAP(sigma(allclass_mod)/num_cls):66.81612736038076
bev_mAP(sigma(allclass_mod)/num_cls):66.03004754225012
3d_mAP(sigma(allclass_mod)/num_cls):59.978324391197006
aos_mAP(sigma(allclass_mod)/num_cls):0.8886875861684159

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:74.52, 70.70, 69.29
bev  AP:71.97, 67.79, 66.40
3d   AP:63.26, 58.42, 56.48
aos  AP:0.12, 0.81, 1.31
Van coco AP@0.50:0.05:0.95:
bbox AP:49.46, 34.69, 30.19
bev  AP:50.41, 35.48, 30.92
3d   AP:42.99, 29.12, 24.79
aos  AP:0.48, 0.48, 0.97

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.86, 89.75, 88.85
bev  AP:90.65, 88.44, 87.17
3d   AP:89.60, 79.31, 78.14
aos  AP:0.35, 1.01, 1.74
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.86, 89.75, 88.85
bev  AP:90.86, 89.98, 89.53
3d   AP:90.86, 89.94, 89.45
aos  AP:0.35, 1.01, 1.74
Car bbox_mAP(sigma(all_difficulties)/3):@89.82
Car bev_mAP(sigma(all_difficulties)/3):@88.75
Car 3d_mAP(sigma(all_difficulties)/3):@82.35
Car aos_mAP(sigma(all_difficulties)/3):@1.03
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:65.18, 43.75, 40.56
bev  AP:65.21, 43.69, 40.51
3d   AP:63.81, 41.82, 34.64
aos  AP:0.87, 0.74, 1.41
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:65.18, 43.75, 40.56
bev  AP:65.26, 47.16, 41.45
3d   AP:65.25, 47.09, 40.94
aos  AP:0.87, 0.74, 1.41
Van bbox_mAP(sigma(all_difficulties)/3):@49.83
Van bev_mAP(sigma(all_difficulties)/3):@49.81
Van 3d_mAP(sigma(all_difficulties)/3):@46.76
Van aos_mAP(sigma(all_difficulties)/3):@1.01
bbox_mAP(sigma(allclass_mod)/num_cls):66.74768913304635
bev_mAP(sigma(allclass_mod)/num_cls):66.06548281865312
3d_mAP(sigma(allclass_mod)/num_cls):60.5680379678502
aos_mAP(sigma(allclass_mod)/num_cls):0.878660900847916

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:74.10, 70.34, 68.94
bev  AP:71.93, 68.37, 66.43
3d   AP:63.63, 58.00, 56.11
aos  AP:0.29, 0.76, 1.34
Van coco AP@0.50:0.05:0.95:
bbox AP:51.09, 34.50, 30.01
bev  AP:51.90, 36.04, 31.24
3d   AP:43.63, 29.34, 25.22
aos  AP:0.69, 0.58, 0.98

eval.kitti.official.Car.bbox@0.70=[90.86, 89.75, 88.85], eval.kitti.official.Car.bev@0.70=[90.65, 88.44, 87.17], eval.kitti.official.Car.3d@0.70=[89.6, 79.31, 78.14], eval.kitti.official.Car.aos=[0.3532, 1.013, 1.735], eval.kitti.official.Car.bev@0.50=[90.86, 89.98, 89.53], eval.kitti.official.Car.3d@0.50=[90.86, 89.94, 89.45], eval.kitti.official.Car.bbox_mAP@0.70=89.82, eval.kitti.official.Car.bev_mAP@0.70=88.75, eval.kitti.official.Car.3d_mAP@0.70=82.35, eval.kitti.official.Car.aos_mAP=1.034, eval.kitti.official.Van.bbox@0.70=[65.18, 43.75, 40.56], eval.kitti.official.Van.bev@0.70=[65.21, 43.69, 40.51], eval.kitti.official.Van.3d@0.70=[63.81, 41.82, 34.64], eval.kitti.official.Van.aos=[0.8721, 0.7439, 1.415], eval.kitti.official.Van.bev@0.50=[65.26, 47.16, 41.45], eval.kitti.official.Van.3d@0.50=[65.25, 47.09, 40.94], eval.kitti.official.Van.bbox_mAP@0.70=49.83, eval.kitti.official.Van.bev_mAP@0.70=49.81, eval.kitti.official.Van.3d_mAP@0.70=46.76, eval.kitti.official.Van.aos_mAP=1.01, eval.kitti.official.mAP_mod.bbox=66.75, eval.kitti.official.mAP_mod.bev=66.07, eval.kitti.official.mAP_mod.3d=60.57, eval.kitti.official.mAP_mod.aos=0.8787, eval.kitti.coco.Car.bbox=[74.1, 70.34, 68.94], eval.kitti.coco.Car.bev=[71.93, 68.37, 66.43], eval.kitti.coco.Car.3d=[63.63, 58.0, 56.11], eval.kitti.coco.Car.aos=[0.2862, 0.7556, 1.339], eval.kitti.coco.Van.bbox=[51.09, 34.5, 30.01], eval.kitti.coco.Van.bev=[51.9, 36.04, 31.24], eval.kitti.coco.Van.3d=[43.63, 29.34, 25.22], eval.kitti.coco.Van.aos=[0.6926, 0.5788, 0.9837]
Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.84, 89.70, 88.86
bev  AP:90.62, 88.37, 87.11
3d   AP:89.57, 79.18, 77.87
aos  AP:0.18, 1.09, 1.72
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.84, 89.70, 88.86
bev  AP:90.85, 89.96, 89.51
3d   AP:90.85, 89.93, 89.42
aos  AP:0.18, 1.09, 1.72
Car bbox_mAP(sigma(all_difficulties)/3):@89.80
Car bev_mAP(sigma(all_difficulties)/3):@88.70
Car 3d_mAP(sigma(all_difficulties)/3):@82.21
Car aos_mAP(sigma(all_difficulties)/3):@1.00
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:62.54, 43.19, 39.81
bev  AP:62.18, 43.05, 39.68
3d   AP:60.30, 39.96, 33.37
aos  AP:0.98, 0.80, 1.56
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:62.54, 43.19, 39.81
bev  AP:62.76, 46.60, 41.27
3d   AP:62.75, 46.78, 41.09
aos  AP:0.98, 0.80, 1.56
Van bbox_mAP(sigma(all_difficulties)/3):@48.52
Van bev_mAP(sigma(all_difficulties)/3):@48.31
Van 3d_mAP(sigma(all_difficulties)/3):@44.54
Van aos_mAP(sigma(all_difficulties)/3):@1.11
bbox_mAP(sigma(allclass_mod)/num_cls):66.4457730245238
bev_mAP(sigma(allclass_mod)/num_cls):65.71023519286885
3d_mAP(sigma(allclass_mod)/num_cls):59.56843473525467
aos_mAP(sigma(allclass_mod)/num_cls):0.9462278263944526

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:74.34, 70.44, 69.27
bev  AP:72.07, 67.88, 66.50
3d   AP:63.23, 58.34, 56.42
aos  AP:0.15, 0.80, 1.33
Van coco AP@0.50:0.05:0.95:
bbox AP:49.01, 34.26, 29.98
bev  AP:49.73, 34.98, 30.66
3d   AP:41.80, 28.25, 24.18
aos  AP:0.76, 0.62, 1.09

Evaluation official
Car AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:90.85, 89.73, 88.84
bev  AP:90.63, 88.43, 87.19
3d   AP:89.46, 79.18, 77.99
aos  AP:0.41, 1.12, 1.76
Car AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:90.85, 89.73, 88.84
bev  AP:90.86, 89.98, 89.54
3d   AP:90.86, 89.96, 89.44
aos  AP:0.41, 1.12, 1.76
Car bbox_mAP(sigma(all_difficulties)/3):@89.81
Car bev_mAP(sigma(all_difficulties)/3):@88.75
Car 3d_mAP(sigma(all_difficulties)/3):@82.21
Car aos_mAP(sigma(all_difficulties)/3):@1.10
Van AP(Average Precision)@0.70, 0.70, 0.70:
bbox AP:64.64, 43.13, 39.95
bev  AP:64.58, 43.13, 39.88
3d   AP:63.14, 40.85, 34.01
aos  AP:0.87, 0.60, 0.93
Van AP(Average Precision)@0.70, 0.50, 0.50:
bbox AP:64.64, 43.13, 39.95
bev  AP:64.67, 46.37, 41.25
3d   AP:64.66, 46.62, 40.96
aos  AP:0.87, 0.60, 0.93
Van bbox_mAP(sigma(all_difficulties)/3):@49.24
Van bev_mAP(sigma(all_difficulties)/3):@49.20
Van 3d_mAP(sigma(all_difficulties)/3):@46.00
Van aos_mAP(sigma(all_difficulties)/3):@0.80
bbox_mAP(sigma(allclass_mod)/num_cls):66.4303845497695
bev_mAP(sigma(allclass_mod)/num_cls):65.77557634101247
3d_mAP(sigma(allclass_mod)/num_cls):60.01836933463959
aos_mAP(sigma(allclass_mod)/num_cls):0.8583623840109932

Evaluation coco
Car coco AP@0.50:0.05:0.95:
bbox AP:73.84, 69.99, 68.79
bev  AP:71.99, 67.74, 66.37
3d   AP:63.12, 58.09, 56.16
aos  AP:0.34, 0.83, 1.37
Van coco AP@0.50:0.05:0.95:
bbox AP:50.27, 34.05, 29.81
bev  AP:51.57, 35.65, 31.05
3d   AP:43.40, 29.36, 25.05
aos  AP:0.68, 0.48, 0.68

eval.kitti.official.Car.bbox@0.70=[90.85, 89.73, 88.84], eval.kitti.official.Car.bev@0.70=[90.63, 88.43, 87.19], eval.kitti.official.Car.3d@0.70=[89.46, 79.18, 77.99], eval.kitti.official.Car.aos=[0.4091, 1.118, 1.765], eval.kitti.official.Car.bev@0.50=[90.86, 89.98, 89.54], eval.kitti.official.Car.3d@0.50=[90.86, 89.96, 89.44], eval.kitti.official.Car.bbox_mAP@0.70=89.81, eval.kitti.official.Car.bev_mAP@0.70=88.75, eval.kitti.official.Car.3d_mAP@0.70=82.21, eval.kitti.official.Car.aos_mAP=1.097, eval.kitti.official.Van.bbox@0.70=[64.64, 43.13, 39.95], eval.kitti.official.Van.bev@0.70=[64.58, 43.13, 39.88], eval.kitti.official.Van.3d@0.70=[63.14, 40.85, 34.01], eval.kitti.official.Van.aos=[0.8669, 0.5989, 0.9337], eval.kitti.official.Van.bev@0.50=[64.67, 46.37, 41.25], eval.kitti.official.Van.3d@0.50=[64.66, 46.62, 40.96], eval.kitti.official.Van.bbox_mAP@0.70=49.24, eval.kitti.official.Van.bev_mAP@0.70=49.2, eval.kitti.official.Van.3d_mAP@0.70=46.0, eval.kitti.official.Van.aos_mAP=0.7999, eval.kitti.official.mAP_mod.bbox=66.43, eval.kitti.official.mAP_mod.bev=65.78, eval.kitti.official.mAP_mod.3d=60.02, eval.kitti.official.mAP_mod.aos=0.8584, eval.kitti.coco.Car.bbox=[73.84, 69.99, 68.79], eval.kitti.coco.Car.bev=[71.99, 67.74, 66.37], eval.kitti.coco.Car.3d=[63.12, 58.09, 56.16], eval.kitti.coco.Car.aos=[0.3354, 0.8334, 1.37], eval.kitti.coco.Van.bbox=[50.27, 34.05, 29.81], eval.kitti.coco.Van.bev=[51.57, 35.65, 31.05], eval.kitti.coco.Van.3d=[43.4, 29.36, 25.05], eval.kitti.coco.Van.aos=[0.6778, 0.4804, 0.6813]