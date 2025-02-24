import pcl
import numpy as np

# 生成示例点云数据 [N, 4]，N=20000
N = 20000
points = np.random.rand(N, 4).astype(np.float32)  # [x, y, z, intensity]

# 将 numpy 数组转换为 PCL 点云
cloud = pcl.PointCloud_PointXYZI()
cloud.from_array(points)

# 创建 PCL 可视化器
viewer = pcl.Visualizer()
viewer.addPointCloud(cloud, "cloud")  # 添加点云

# 设置点云颜色映射（根据 intensity）
viewer.setPointCloudRenderingProperties(0, 1, "cloud")  # 0: 点大小, 1: 颜色

# 启动可视化
while not viewer.wasStopped():
    viewer.spinOnce(100)