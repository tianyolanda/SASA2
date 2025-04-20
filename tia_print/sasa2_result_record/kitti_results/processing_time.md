每个记录5次
求平均值
# 3dssd 
python test.py --batch_size=1 --cfg_file='cfgs/kitti_models/car/3dssd.yaml' --ckpt='../output/kitti_models/car/3dssd/default/ckpt/checkpoint_epoch_80.pth'

## 1
2025-04-13 16:20:02,440   INFO  time_density_calculation: 0.000078
metric[time_density_calculation] 0.2947406768798828 7.82012939453125e-05
2025-04-13 16:20:02,441   INFO  time_PointNet2FSMSG: 0.095911
metric[time_PointNet2FSMSG] 361.48775839805603 0.09591078758239746
2025-04-13 16:20:02,441   INFO  time_PointHeadVote: 0.005390
metric[time_PointHeadVote] 20.313743114471436 0.005389690399169922
2025-04-13 16:20:02,441   INFO  time_post_processing: 0.041483
metric[time_post_processing] 156.3482472896576 0.04148268699645996

# 2
2025-04-13 17:11:43,960   INFO  time_density_calculation: 0.000075
metric[time_density_calculation] 0.28395748138427734 7.534027099609375e-05
2025-04-13 17:11:43,960   INFO  time_PointNet2FSMSG: 0.074902
metric[time_PointNet2FSMSG] 282.3040580749512 0.07490158081054688
2025-04-13 17:11:43,960   INFO  time_PointHeadVote: 0.010764
metric[time_PointHeadVote] 40.56997585296631 0.010764122009277344
2025-04-13 17:11:43,960   INFO  time_post_processing: 0.015272
metric[time_post_processing] 57.56069755554199 0.015272140502929688

# 3
2025-04-13 17:22:52,073   INFO  time_density_calculation: 0.000089
metric[time_density_calculation] 0.3351776599884033 8.893013000488281e-05
2025-04-13 17:22:52,073   INFO  time_PointNet2FSMSG: 0.060906
metric[time_PointNet2FSMSG] 229.55626010894775 0.060906410217285156
2025-04-13 17:22:52,073   INFO  time_PointHeadVote: 0.018529
metric[time_PointHeadVote] 69.83556842803955 0.01852893829345703
2025-04-13 17:22:52,073   INFO  time_post_processing: 0.015078
metric[time_post_processing] 56.82923746109009 0.015078067779541016

# 4
2025-04-13 17:29:47,155   INFO  time_density_calculation: 0.000091
metric[time_density_calculation] 0.3441636562347412 9.131431579589844e-05
2025-04-13 17:29:47,155   INFO  time_PointNet2FSMSG: 0.066546
metric[time_PointNet2FSMSG] 250.81353282928467 0.06654644012451172
2025-04-13 17:29:47,155   INFO  time_PointHeadVote: 0.023880
metric[time_PointHeadVote] 90.00553560256958 0.023880481719970703
2025-04-13 17:29:47,155   INFO  time_post_processing: 0.019698
metric[time_post_processing] 74.24230098724365 0.019698143005371094

# 5

2025-04-13 17:37:27,960   INFO  time_density_calculation: 0.000080
metric[time_density_calculation] 0.30103087425231934 7.987022399902344e-05
2025-04-13 17:37:27,960   INFO  time_PointNet2FSMSG: 0.094479
metric[time_PointNet2FSMSG] 356.09256625175476 0.09447932243347168
2025-04-13 17:37:27,960   INFO  time_PointHeadVote: 0.016419
metric[time_PointHeadVote] 61.882063150405884 0.0164186954498291
2025-04-13 17:37:27,960   INFO  time_post_processing: 0.015358
metric[time_post_processing] 57.88509202003479 0.015358209609985352

# 3dssd_sasa
python test.py --batch_size=1 --cfg_file='cfgs/kitti_models/car/3dssd_sasa.yaml' --ckpt='../output/kitti_models/car/3dssd_sasa/default/ckpt/checkpoint_epoch_80.pth'
## 1
2025-04-13 16:32:11,394   INFO  time_density_calculation: 0.000080
metric[time_density_calculation] 0.30103087425231934 7.987022399902344e-05
2025-04-13 16:32:11,394   INFO  time_PointNet2FSMSG: 0.105319
metric[time_PointNet2FSMSG] 396.94739818573 0.10531902313232422
2025-04-13 16:32:11,394   INFO  time_PointHeadVote: 0.005731
metric[time_PointHeadVote] 21.601436376571655 0.005731344223022461
2025-04-13 16:32:11,394   INFO  time_post_processing: 0.029503
metric[time_post_processing] 111.19810914993286 0.029503345489501953

## 2
2025-04-13 16:39:22,032   INFO  time_density_calculation: 0.000084
metric[time_density_calculation] 0.31630706787109375 8.392333984375e-05
2025-04-13 16:39:22,032   INFO  time_PointNet2FSMSG: 0.050227
metric[time_PointNet2FSMSG] 189.30618572235107 0.05022716522216797
2025-04-13 16:39:22,032   INFO  time_PointHeadVote: 0.032619
metric[time_PointHeadVote] 122.94280624389648 0.032619476318359375
2025-04-13 16:39:22,032   INFO  time_post_processing: 0.026529
metric[time_post_processing] 99.98897743225098 0.026529312133789062

##　3
2025-04-13 16:46:41,410   INFO  time_density_calculation: 0.000097
metric[time_density_calculation] 0.36573004722595215 9.703636169433594e-05
2025-04-13 16:46:41,410   INFO  time_PointNet2FSMSG: 0.049705
metric[time_PointNet2FSMSG] 187.33825254440308 0.04970502853393555
2025-04-13 16:46:41,410   INFO  time_PointHeadVote: 0.030287
metric[time_PointHeadVote] 114.15090751647949 0.030286788940429688
2025-04-13 16:46:41,410   INFO  time_post_processing: 0.015750
metric[time_post_processing] 59.36238980293274 0.01575016975402832

## 4
2025-04-13 16:54:55,677   INFO  time_density_calculation: 0.000078
metric[time_density_calculation] 0.293842077255249 7.796287536621094e-05
2025-04-13 16:54:55,677   INFO  time_PointNet2FSMSG: 0.056051
metric[time_PointNet2FSMSG] 211.25448155403137 0.05605053901672363
2025-04-13 16:54:55,677   INFO  time_PointHeadVote: 0.029455
metric[time_PointHeadVote] 111.0156934261322 0.029454946517944336
2025-04-13 16:54:55,677   INFO  time_post_processing: 0.012865
metric[time_post_processing] 48.487537145614624 0.012864828109741211

## 5
2025-04-13 17:03:36,342   INFO  time_density_calculation: 0.000092
metric[time_density_calculation] 0.345062255859375 9.1552734375e-05
2025-04-13 17:03:36,342   INFO  time_PointNet2FSMSG: 0.053922
metric[time_PointNet2FSMSG] 203.23268270492554 0.053922176361083984
2025-04-13 17:03:36,343   INFO  time_PointHeadVote: 0.028242
metric[time_PointHeadVote] 106.44271993637085 0.028241634368896484
2025-04-13 17:03:36,343   INFO  time_post_processing: 0.015652
metric[time_post_processing] 58.99216675758362 0.015651941299438477

# 3dssd_dsasa

python test.py --batch_size=1 --cfg_file='cfgs/kitti_models/car/3dssd_dsasa.yaml' --ckpt='../output/kitti_models/car/3dssd_dsasa_0.5/default/ckpt/checkpoint_epoch_80.pth'

##radius=0.5
##1
2025-04-13 17:49:33,976   INFO  time_density_calculation: 0.003473
metric[time_density_calculation] 13.088103532791138 0.003472566604614258
2025-04-13 17:49:33,976   INFO  time_PointNet2FSMSG: 0.075698
metric[time_PointNet2FSMSG] 285.30627942085266 0.0756981372833252
2025-04-13 17:49:33,976   INFO  time_PointHeadVote: 0.020880
metric[time_PointHeadVote] 78.69755792617798 0.02088022232055664
2025-04-13 17:49:33,976   INFO  time_post_processing: 0.041448
metric[time_post_processing] 156.21615314483643 0.04144763946533203

## 2
2025-04-13 17:58:20,447   INFO  time_density_calculation: 0.002731
metric[time_density_calculation] 10.293458700180054 0.0027310848236083984
2025-04-13 17:58:20,447   INFO  time_PointNet2FSMSG: 0.111033
metric[time_PointNet2FSMSG] 418.48503398895264 0.11103343963623047
2025-04-13 17:58:20,447   INFO  time_PointHeadVote: 0.014363
metric[time_PointHeadVote] 54.134337186813354 0.01436305046081543
2025-04-13 17:58:20,447   INFO  time_post_processing: 0.016253
metric[time_post_processing] 61.2575364112854 0.016252994537353516

## 3
2025-04-13 18:05:03,295   INFO  time_density_calculation: 0.002743
metric[time_density_calculation] 10.339287281036377 0.002743244171142578
2025-04-13 18:05:03,295   INFO  time_PointNet2FSMSG: 0.101444
metric[time_PointNet2FSMSG] 382.342458486557 0.10144400596618652
2025-04-13 18:05:03,295   INFO  time_PointHeadVote: 0.009499
metric[time_PointHeadVote] 35.80290484428406 0.009499311447143555
2025-04-13 18:05:03,295   INFO  time_post_processing: 0.022085
metric[time_post_processing] 83.23908042907715 0.022085189819335938

## 4
2025-04-13 18:39:46,157   INFO  time_density_calculation: 0.002689
metric[time_density_calculation] 10.135305166244507 0.0026891231536865234
2025-04-13 18:39:46,157   INFO  time_PointNet2FSMSG: 0.061393
metric[time_PointNet2FSMSG] 231.39030194282532 0.061393022537231445
2025-04-13 18:39:46,157   INFO  time_PointHeadVote: 0.028503
metric[time_PointHeadVote] 107.42668652534485 0.028502702713012695
2025-04-13 18:39:46,157   INFO  time_post_processing: 0.015690
metric[time_post_processing] 59.135942697525024 0.015690088272094727

## 5
2025-04-13 18:50:48,132   INFO  time_density_calculation: 0.003226
metric[time_density_calculation] 12.157154321670532 0.003225564956665039
2025-04-13 18:50:48,132   INFO  time_PointNet2FSMSG: 0.053867
metric[time_PointNet2FSMSG] 203.02330899238586 0.05386662483215332
2025-04-13 18:50:48,132   INFO  time_PointHeadVote: 0.027028
metric[time_PointHeadVote] 101.8670506477356 0.027027606964111328
2025-04-13 18:50:48,133   INFO  time_post_processing: 0.013731
metric[time_post_processing] 51.75214958190918 0.013731002807617188

## 6
metric[time_density_calculation] 10.675363540649414 0.0028324127197265625
2025-04-13 22:20:14,397   INFO  time_PointNet2FSMSG: 0.066103
metric[time_PointNet2FSMSG] 249.1412389278412 0.06610274314880371
2025-04-13 22:20:14,397   INFO  time_PointHeadVote: 0.023844
metric[time_PointHeadVote] 89.86894845962524 0.023844242095947266
2025-04-13 22:20:14,397   INFO  time_post_processing: 0.015206
metric[time_post_processing] 57.309988260269165 0.015205621719360352


## radius=1

## 1
2025-04-13 18:58:42,979   INFO  time_density_calculation: 0.004094
metric[time_density_calculation] 15.429854154586792 0.00409388542175293
2025-04-13 18:58:42,979   INFO  time_PointNet2FSMSG: 0.080069
metric[time_PointNet2FSMSG] 301.7803063392639 0.08006906509399414
2025-04-13 18:58:42,979   INFO  time_PointHeadVote: 0.025294
metric[time_PointHeadVote] 95.33423137664795 0.02529430389404297
2025-04-13 18:58:42,979   INFO  time_post_processing: 0.011915
metric[time_post_processing] 44.90751624107361 0.011914968490600586

## 2
2025-04-13 19:08:02,618   INFO  time_density_calculation: 0.002608
metric[time_density_calculation] 9.828882694244385 0.0026078224182128906
2025-04-13 19:08:02,618   INFO  time_PointNet2FSMSG: 0.080648
metric[time_PointNet2FSMSG] 303.9612076282501 0.08064770698547363
2025-04-13 19:08:02,618   INFO  time_PointHeadVote: 0.013253
metric[time_PointHeadVote] 49.9495587348938 0.013252735137939453
2025-04-13 19:08:02,618   INFO  time_post_processing: 0.020777
metric[time_post_processing] 78.30666708946228 0.02077651023864746

## 3
2025-04-13 19:17:36,280   INFO  time_density_calculation: 0.002662
metric[time_density_calculation] 10.034662008285522 0.0026624202728271484
2025-04-13 19:17:36,280   INFO  time_PointNet2FSMSG: 0.072890
metric[time_PointNet2FSMSG] 274.72167444229126 0.07288980484008789
2025-04-13 19:17:36,280   INFO  time_PointHeadVote: 0.021263
metric[time_PointHeadVote] 80.14160752296448 0.02126336097717285
2025-04-13 19:17:36,281   INFO  time_post_processing: 0.017019
metric[time_post_processing] 64.14473700523376 0.017019033432006836

## 4
2025-04-13 21:14:20,332   INFO  time_density_calculation: 0.002935
metric[time_density_calculation] 11.062659978866577 0.002935171127319336
2025-04-13 21:14:20,332   INFO  time_PointNet2FSMSG: 0.113220
metric[time_PointNet2FSMSG] 426.7278883457184 0.1132204532623291
2025-04-13 21:14:20,332   INFO  time_PointHeadVote: 0.021341
metric[time_PointHeadVote] 80.43275380134583 0.021340608596801758
2025-04-13 21:14:20,332   INFO  time_post_processing: 0.019657
metric[time_post_processing] 74.08594465255737 0.019656658172607422

3d   AP:91.4445, 84.6761, 80.5560

## 5
2025-04-13 21:34:55,682   INFO  time_density_calculation: 0.002823
metric[time_density_calculation] 10.640318155288696 0.0028231143951416016
2025-04-13 21:34:55,682   INFO  time_PointNet2FSMSG: 0.078055
metric[time_PointNet2FSMSG] 294.19073390960693 0.07805538177490234
2025-04-13 21:34:55,682   INFO  time_PointHeadVote: 0.024334
metric[time_PointHeadVote] 91.71557068824768 0.024334192276000977
2025-04-13 21:34:55,682   INFO  time_post_processing: 0.009414
metric[time_post_processing] 35.482104778289795 0.009414196014404297

## 6
2025-04-13 21:41:30,390   INFO  time_density_calculation: 0.003341
metric[time_density_calculation] 12.592076539993286 0.0033409595489501953
2025-04-13 21:41:30,390   INFO  time_PointNet2FSMSG: 0.076519
metric[time_PointNet2FSMSG] 288.40105652809143 0.07651925086975098
2025-04-13 21:41:30,390   INFO  time_PointHeadVote: 0.015510
metric[time_PointHeadVote] 58.455702781677246 0.015509605407714844
2025-04-13 21:41:30,390   INFO  time_post_processing: 0.015043
metric[time_post_processing] 56.698041915893555 0.015043258666992188

3d   AP:91.7196, 84.8136, 80.6593



## radius = 2
## 1
2025-04-13 20:13:48,432   INFO  time_density_calculation: 0.005599
metric[time_density_calculation] 21.102713584899902 0.005599021911621094
2025-04-13 20:13:48,432   INFO  time_PointNet2FSMSG: 0.067968
metric[time_PointNet2FSMSG] 256.1700851917267 0.06796765327453613
2025-04-13 20:13:48,432   INFO  time_PointHeadVote: 0.029988
metric[time_PointHeadVote] 113.02496218681335 0.02998805046081543
2025-04-13 20:13:48,432   INFO  time_post_processing: 0.013620
metric[time_post_processing] 51.3325035572052 0.013619661331176758

## 2

python test.py --batch_size=1 --cfg_file='cfgs/kitti_models/car/3dssd_dsasa.yaml' --ckpt='../output/kitti_models/car/3dssd_dsasa_0.5/default/ckpt/checkpoint_epoch_79.pth'

2025-04-13 20:21:07,594   INFO  time_density_calculation: 0.013706
metric[time_density_calculation] 51.65779662132263 0.013705968856811523
2025-04-13 20:21:07,594   INFO  time_PointNet2FSMSG: 0.063592
metric[time_PointNet2FSMSG] 239.67718768119812 0.06359171867370605
2025-04-13 20:21:07,594   INFO  time_PointHeadVote: 0.027087
metric[time_PointHeadVote] 102.09259915351868 0.02708745002746582
2025-04-13 20:21:07,594   INFO  time_post_processing: 0.010679
metric[time_post_processing] 40.25097298622131 0.010679483413696289

## 3
metric[time_density_calculation] 16.037307500839233 0.004255056381225586
2025-04-13 20:33:07,691   INFO  time_PointNet2FSMSG: 0.074555
metric[time_PointNet2FSMSG] 280.9992914199829 0.0745553970336914
2025-04-13 20:33:07,691   INFO  time_PointHeadVote: 0.022611
metric[time_PointHeadVote] 85.22139120101929 0.022611141204833984
2025-04-13 20:33:07,691   INFO  time_post_processing: 0.014811
metric[time_post_processing] 55.82370448112488 0.014811277389526367

## 4
2025-04-13 20:40:45,367   INFO  time_density_calculation: 0.002881
metric[time_density_calculation] 10.857779264450073 0.0028808116912841797
2025-04-13 20:40:45,368   INFO  time_PointNet2FSMSG: 0.060946
metric[time_PointNet2FSMSG] 229.7036304473877 0.06094551086425781
2025-04-13 20:40:45,368   INFO  time_PointHeadVote: 0.027742
metric[time_PointHeadVote] 104.55925512313843 0.02774190902709961
2025-04-13 20:40:45,368   INFO  time_post_processing: 0.015544
metric[time_post_processing] 58.58420252799988 0.015543699264526367

## 5
2025-04-13 20:48:32,046   INFO  time_density_calculation: 0.002563
metric[time_density_calculation] 9.660844564437866 0.0025632381439208984
2025-04-13 20:48:32,046   INFO  time_PointNet2FSMSG: 0.086241
metric[time_PointNet2FSMSG] 325.0423548221588 0.08624100685119629
2025-04-13 20:48:32,046   INFO  time_PointHeadVote: 0.007706
metric[time_PointHeadVote] 29.042739868164062 0.0077056884765625
2025-04-13 20:48:32,046   INFO  time_post_processing: 0.016929
metric[time_post_processing] 63.80686354637146 0.01692938804626465

## 6
2025-04-13 21:07:26,955   INFO  time_density_calculation: 0.002551
metric[time_density_calculation] 9.615015983581543 0.0025510787963867188
2025-04-13 21:07:26,955   INFO  time_PointNet2FSMSG: 0.053281
metric[time_PointNet2FSMSG] 200.8172469139099 0.053281307220458984
2025-04-13 21:07:26,955   INFO  time_PointHeadVote: 0.026917
metric[time_PointHeadVote] 101.44830322265625 0.02691650390625
2025-04-13 21:07:26,955   INFO  time_post_processing: 0.015876
metric[time_post_processing] 59.83505320549011 0.015875577926635742

## 7
2025-04-13 22:28:34,623   INFO  time_density_calculation: 0.002902
metric[time_density_calculation] 10.938653230667114 0.0029022693634033203
2025-04-13 22:28:34,623   INFO  time_PointNet2FSMSG: 0.067560
metric[time_PointNet2FSMSG] 254.63527703285217 0.06756043434143066
2025-04-13 22:28:34,623   INFO  time_PointHeadVote: 0.026113
metric[time_PointHeadVote] 98.41822528839111 0.02611255645751953
2025-04-13 22:28:34,623   INFO  time_post_processing: 0.015431
metric[time_post_processing] 58.16006350517273 0.01543116569519043

## 8
2025-04-13 22:38:00,821   INFO  time_density_calculation: 0.002662
metric[time_density_calculation] 10.032864809036255 0.0026619434356689453
2025-04-13 22:38:00,821   INFO  time_PointNet2FSMSG: 0.088694
metric[time_PointNet2FSMSG] 334.28714776039124 0.08869385719299316
2025-04-13 22:38:00,821   INFO  time_PointHeadVote: 0.009558
metric[time_PointHeadVote] 36.02575755119324 0.009558439254760742
2025-04-13 22:38:00,821   INFO  time_post_processing: 0.017773
metric[time_post_processing] 66.98700761795044 0.017773151397705078
