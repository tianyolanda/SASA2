# DENSE Snow Test Results With Van

Evaluation split: `test_snow` from `dense_infos_test_snow.pkl`.

Metrics are 3D AP_R40 over four classes: Car, Pedestrian, Cyclist, and Van.

- Strict thresholds: Car/Van `0.70`, Pedestrian/Cyclist `0.50`
- Loose thresholds: Car/Van `0.50`, Pedestrian/Cyclist `0.25`
- Mean mod is the average of moderate AP_R40 over Car, Pedestrian, Cyclist, and Van.

## Strict

| Model | Epoch | Samples | Mean mod | Car easy | Car mod | Car hard | Ped easy | Ped mod | Ped hard | Cyc easy | Cyc mod | Cyc hard | Van easy | Van mod | Van hard | Log |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| DSASA fixed r025 ns12 sasa e79 last sden | 79 | 3916 | 24.3581 | 41.1042 | 39.0436 | 35.0788 | 18.4978 | 18.1497 | 17.1112 | 30.0117 | 28.4242 | 27.3317 | 12.7021 | 11.8148 | 10.3527 | DSASA_fixed_r025_ns12_sasa_e79_last_sden_test_snow_console.log |
| DSASA fixed r025 ns12 sasa e80 last sden | 80 | 3916 | 24.2199 | 41.2390 | 40.0121 | 35.2993 | 18.3664 | 18.1604 | 17.0366 | 29.4856 | 28.0337 | 27.0089 | 11.1097 | 10.6736 | 9.6690 | DSASA_fixed_r025_ns12_sasa_e80_last_sden_test_snow_console.log |
| DSASA r025 gated sasa e80 last sden | 80 | 3916 | 23.9981 | 41.8878 | 40.6845 | 36.3493 | 18.5057 | 18.1302 | 17.0336 | 28.5663 | 27.3291 | 26.5675 | 10.7483 | 9.8487 | 9.2006 | DSASA_r025_gated_sasa_e80_last_sden_test_snow_console.log |
| SASA baseline e80 | 80 | 3916 | 23.9912 | 41.6655 | 40.4123 | 35.4838 | 18.3128 | 18.0063 | 16.9884 | 27.0904 | 26.0609 | 25.7045 | 11.8524 | 11.4853 | 9.9989 | SASA_baseline_e80_test_snow_console.log |
| DSASA r025 gated e74 | 74 | 3916 | 23.9351 | 42.2810 | 40.9241 | 35.8707 | 17.7607 | 17.4237 | 16.4436 | 28.1109 | 26.9601 | 25.9076 | 11.0340 | 10.4325 | 9.5949 | DSASA_r025_gated_e74_test_snow_console.log |
| DSASA r025 gated sasa e79 last sden | 79 | 3916 | 23.9038 | 41.0292 | 38.9768 | 34.9849 | 18.9068 | 18.3662 | 17.2385 | 29.3601 | 27.8485 | 26.7972 | 12.2068 | 10.4238 | 9.7809 | DSASA_r025_gated_sasa_e79_last_sden_test_snow_console.log |
| SASA baseline e74 | 74 | 3916 | 23.4591 | 41.9912 | 40.4664 | 35.6468 | 17.6310 | 16.8860 | 16.2581 | 26.6377 | 25.8392 | 24.9269 | 11.5265 | 10.6447 | 9.6763 | SASA_baseline_e74_test_snow_console.log |
| DSASA fixed r025 ns12 e74 | 74 | 3916 | 23.2249 | 41.9474 | 40.6665 | 35.7347 | 17.1952 | 16.5813 | 15.8984 | 26.8426 | 25.5889 | 24.5292 | 10.7567 | 10.0631 | 8.9022 | DSASA_fixed_r025_ns12_e74_test_snow_console.log |
| 3DSSD baseline e80 | 80 | 3916 | 22.3864 | 41.0494 | 39.5908 | 35.0044 | 17.5802 | 16.8050 | 15.7447 | 23.1348 | 22.6692 | 22.0636 | 10.6027 | 10.4804 | 9.1349 | 3DSSD_baseline_e80_test_snow_console.log |
| PV-RCNN baseline e76 | 76 | 3916 | 22.1505 | 38.9935 | 37.8990 | 34.2432 | 19.3853 | 18.8193 | 17.8206 | 23.7314 | 23.6138 | 23.0464 | 9.1850 | 8.2699 | 7.4985 | PV-RCNN_baseline_e76_test_snow_console.log |
| PV-RCNN baseline e80 | 80 | 3916 | 22.0855 | 38.8325 | 37.8120 | 34.2288 | 19.2987 | 18.6553 | 17.6273 | 23.0531 | 23.0777 | 22.5121 | 10.0665 | 8.7971 | 7.7760 | PV-RCNN_baseline_e80_test_snow_console.log |
| SECOND baseline e80 | 80 | 3916 | 17.5150 | 36.1869 | 34.9918 | 31.1699 | 14.4841 | 14.1856 | 13.5551 | 18.3868 | 18.4521 | 18.5067 | 2.3879 | 2.4306 | 2.1175 | SECOND_baseline_e80_test_snow_console.log |
| PointPillars baseline e80 | 80 | 3916 | 15.6024 | 32.3701 | 31.1442 | 27.6345 | 10.9148 | 10.8023 | 10.2983 | 17.3616 | 16.9869 | 16.2713 | 3.0945 | 3.4763 | 3.1222 | PointPillars_baseline_e80_test_snow_console.log |

## Loose

| Model | Epoch | Samples | Mean mod | Car easy | Car mod | Car hard | Ped easy | Ped mod | Ped hard | Cyc easy | Cyc mod | Cyc hard | Van easy | Van mod | Van hard | Log |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| DSASA fixed r025 ns12 sasa e79 last sden | 79 | 3916 | 56.1198 | 77.5155 | 75.6448 | 70.3060 | 51.6785 | 50.2653 | 48.3734 | 56.6727 | 54.1413 | 52.3413 | 46.8544 | 44.4278 | 39.9708 | DSASA_fixed_r025_ns12_sasa_e79_last_sden_test_snow_console.log |
| SASA baseline e74 | 74 | 3916 | 56.0937 | 77.7844 | 75.8375 | 70.3993 | 51.4395 | 50.0472 | 48.1981 | 54.9743 | 52.6608 | 50.7652 | 47.5622 | 45.8293 | 40.7992 | SASA_baseline_e74_test_snow_console.log |
| DSASA r025 gated sasa e79 last sden | 79 | 3916 | 55.8910 | 77.4607 | 75.5872 | 70.2899 | 51.5878 | 50.1834 | 48.3313 | 56.6157 | 54.0196 | 52.2070 | 46.5150 | 43.7739 | 39.2071 | DSASA_r025_gated_sasa_e79_last_sden_test_snow_console.log |
| DSASA fixed r025 ns12 sasa e80 last sden | 80 | 3916 | 55.7127 | 77.4283 | 75.5944 | 70.2844 | 51.2694 | 49.9805 | 48.0443 | 55.0241 | 52.2575 | 50.4866 | 47.0948 | 45.0184 | 40.5773 | DSASA_fixed_r025_ns12_sasa_e80_last_sden_test_snow_console.log |
| SASA baseline e80 | 80 | 3916 | 55.6683 | 77.4905 | 75.5763 | 70.2609 | 51.0907 | 49.8722 | 47.9098 | 56.3155 | 53.8021 | 52.1235 | 45.3253 | 43.4226 | 39.2888 | SASA_baseline_e80_test_snow_console.log |
| DSASA r025 gated e74 | 74 | 3916 | 55.5892 | 77.8622 | 75.9561 | 70.5371 | 51.6129 | 50.2620 | 48.3727 | 55.1426 | 52.7842 | 51.2707 | 44.9214 | 43.3544 | 39.3367 | DSASA_r025_gated_e74_test_snow_console.log |
| DSASA r025 gated sasa e80 last sden | 80 | 3916 | 55.3454 | 77.6125 | 75.6666 | 70.3576 | 51.2265 | 49.9152 | 47.9614 | 54.2116 | 52.0369 | 50.3674 | 45.4401 | 43.7629 | 39.0053 | DSASA_r025_gated_sasa_e80_last_sden_test_snow_console.log |
| DSASA fixed r025 ns12 e74 | 74 | 3916 | 55.3163 | 77.6243 | 75.7287 | 70.3526 | 51.4701 | 50.1274 | 48.1937 | 54.3478 | 52.3444 | 51.0188 | 44.7188 | 43.0645 | 38.4164 | DSASA_fixed_r025_ns12_e74_test_snow_console.log |
| PV-RCNN baseline e76 | 76 | 3916 | 53.9227 | 76.5384 | 74.8352 | 69.6182 | 53.2253 | 51.7991 | 50.7191 | 52.3860 | 50.7431 | 49.4640 | 40.9663 | 38.3133 | 34.3069 | PV-RCNN_baseline_e76_test_snow_console.log |
| PV-RCNN baseline e80 | 80 | 3916 | 53.7155 | 76.0448 | 74.5156 | 69.4177 | 53.0495 | 52.1452 | 50.5246 | 52.9549 | 51.3508 | 50.2890 | 40.4752 | 36.8502 | 33.0426 | PV-RCNN_baseline_e80_test_snow_console.log |
| 3DSSD baseline e80 | 80 | 3916 | 53.4620 | 77.5341 | 75.6060 | 70.1240 | 48.1338 | 46.8291 | 45.1471 | 53.7309 | 51.4273 | 49.5392 | 42.7440 | 39.9857 | 36.3933 | 3DSSD_baseline_e80_test_snow_console.log |
| SECOND baseline e80 | 80 | 3916 | 44.9601 | 74.7556 | 72.9237 | 67.0905 | 45.1793 | 44.7657 | 43.5000 | 46.1378 | 44.4675 | 43.6617 | 17.1459 | 17.6834 | 16.1313 | SECOND_baseline_e80_test_snow_console.log |
| PointPillars baseline e80 | 80 | 3916 | 41.3929 | 73.1657 | 71.1594 | 65.5222 | 37.1067 | 37.1456 | 36.2482 | 36.3118 | 34.3843 | 34.0698 | 19.5228 | 22.8823 | 20.7180 | PointPillars_baseline_e80_test_snow_console.log |
