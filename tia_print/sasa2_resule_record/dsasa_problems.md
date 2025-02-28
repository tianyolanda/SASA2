## 2025下阶段目标
1. - [x] 使用ROR的方法进行点云周围点计数(密度=邻域近点数)(完成)
'''
代码详见:pcdet/utils/density_calculation.py的Vcnt_ball_points()
[注]补充:
1.1 ROR中的两个参数需要确定: 
- radius:在多大的范围内 
- min_pts:少于多少个点,则该点被认为是噪点(外点)
- 我们的目的并不是要去噪,而是想计算[每个点的密度d],[d=一定范围内的点数目]
因此cnt_ball_points(radius=1, nsample=500, points='')只有两个超参
radius:半径
nsample:点数最大值(上限)
2. - [x] 可视化确认计数结果准确(完成)
2.1 可视化代码 完成 vis3d_pyvista(points)
3. - [x] 安插到SASA中,在训练开始之初,对点云图的每个点,计算其密度(完成)
具体详见代码
作为新的键值对,加入到字典batch_dict['density']中,是一个[1,16834*BATCH_SIZE]的tensor
4. - [x] 在SASA中修改s-fps,加入密度考量(sden-fps)
4.1 已改完
主要在class _PointnetSAModuleFSBasewD(nn.Module):
pointnet2的cuda代码也有改动
改完后需要重新编译(在SASA目录下): python setup.py develop
4.2 统计density分布
vis_weight_distribution(),可以对比两个特征值的分布
4.3 设计密度因子计算方法:
ranking = (score ** weight_gamma) * (1 + density_factor ** weight_beta )/2
sden-fps: 每次采样选择最远点, 远 = distance*ranking
其中,
score_factor = (score ** weight_gamma) 是写在外面
density_factor = (1 + density_factor ** weight_beta )/2 为密度因子, 由函数density_factor_calculation()计算
将score_factor和density_factor送入cuda代码中, 将score_factor*density_factor作为ranking依据(代码里不是叫这个名字哈)
5. 训练看结果
5.0 - [ ] 训练过程中参数监视
可视化sementic score,可以训练结束后可视化
5.1 kitti数据集
- [x] 3dssd_dsasa 略有提升, 一个点左右. 
radius=1, nsample=500
- [ ] pointrcnn_dsasa 正在训练.训练结束后,修改roi数目,测试 
radius=0.5, nsample=500
- [ ] density radius,npoints,可以不训练直接测试!
epoch 79: radius=0.5, nsample=500, 某一个值positive point比原来多,其他ap没原来好 (训练上了)
epoch 79: radius=0.5, nsample=100, max_vals = 100, 都没原来好
epoch 79: radius=2, nsample=500, max_vals = 500, 都没原来好
5.2 使用雪数据集CADC/hanner

*****一些idea & 未完成部分******
1. 计算density前是否应该去除地面点?
2. FP_MLPS关于density的部分没实现(pointrcnn_sasa会用到)
3. 计算density时可以按照距离归一化,类似fpn里面的尺度
4. density相关参数(weight/)放在yaml文件中
5. density的归一化:(1)整个数据集 (2) 当前场景 (3) 按照距离


# 编写density部分
# 2.25
完成全部代码并训练
# 2.21
1. 实现了计算一定半径内的点数目
density_calculation.py
目前调用是在网络一开始时, Point3DSSD的forward里
2. 实现了将上述点数目作为feature,可视化

# 2.20
1. 打印sasa中ror的参数
- 环形的dilated ror: 前面层的降采样16384 -> 4096 -> 1024 -> 512, radius=0.2/0.4/0.8米,点数目在32/64以内.
- 球形的原始ror: 后2层的降采样 512 -> 256, radius=4.8/6.4米, 点数目在48/64以内.
- DA3DSSD,对初始点云计算density, radius=0.5/1(选中)/2米, 点数目在500以内, 做了归一化
# 2.19 进度
1. 从train.py开始,看sasa代码,并整理了代码思路
2. 发现sasa代码中自带ror计数!

# 2.18 进度
1. ROR点云去除,已实现
使用pcl库,c++
2. SASA的本体,已训练
baseline: 3dssd,pointrcnn
+sa模块后,AP均有提升
有曲线



# 2024年底进度
进行radius point calculate 
可以调用点云库的ROR/SOR
- SASA本体:Python,
编译:原版需要编译spconv1.2,但只能在ubuntu16上编译.如使用高版本ubuntu,需要自己改代码.
调用:可训练,精度确有提升
- PCL库:c++,
编译:ubuntu16仅支持低版本1.7.2
调用:低版本官网无example,但可以看代码自己写.ror可以运行,但是去除效果未知,需要用viwer看结果,但viwer编译不过
高版本的有example,没有测试过
- Open3D库:Python,
编译:ubuntu16只能安装低版本0.10.0,装不上啊
调用:
example运行时报错,OSError: /lib/x86_64-linux-gnu/libm.so.6: version `GLIBC_2.27' not found (required by /home/ubuntu/anaconda3/envs/sasa2/lib/python3.7/site-packages/open3d/cpu/pybind.cpython-37m-x86_64-linux-gnu.so)
GLIBC库与ubuntu内核版本强相关,ubuntu16无,可以尝试降低open3d的版本到0.10.0

-
