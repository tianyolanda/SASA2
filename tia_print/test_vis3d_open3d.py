import open3d as o3d
import numpy as np

# 生成示例点云数据 [N, 4]，N=20000
N = 20000
points = np.random.rand(N, 4)  # [x, y, z, intensity]

# 提取 x, y, z 坐标
xyz = points[:, :3]

# 提取 intensity 作为颜色（归一化到 [0, 1]）
intensity = points[:, 3]
intensity_normalized = (intensity - intensity.min()) / (intensity.max() - intensity.min())

# 将 intensity 映射到颜色（使用 matplotlib 的 colormap）
import matplotlib.pyplot as plt
cmap = plt.get_cmap("viridis")  # 使用 viridis 颜色映射
colors = cmap(intensity_normalized)[:, :3]  # 取 RGB 值，忽略 alpha 通道

# 创建 Open3D 点云对象
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(xyz)  # 设置点云坐标
pcd.colors = o3d.utility.Vector3dVector(colors)  # 设置点云颜色

# 可视化点云
o3d.visualization.draw_geometries([pcd])