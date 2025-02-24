import pyvista as pv
import numpy as np

# 生成示例点云数据 [N, 4]，N=20000
N = 20000
points = np.random.rand(N, 4)  # [x, y, z, intensity]

# 创建 PyVista 点云对象
cloud = pv.PolyData(points[:, :3])  # 提取 x, y, z 坐标
cloud["intensity"] = points[:, 3]  # 添加 intensity 作为标量场

# 可视化点云
plotter = pv.Plotter()
plotter.add_mesh(cloud, scalars="intensity", cmap="viridis", point_size=2)
plotter.show()