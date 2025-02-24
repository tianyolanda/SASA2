import numpy as np
from mayavi import mlab

# 生成 20,000 个点的示例数据
N = 50
points = np.random.rand(N, 4)  # [x, y, z, intensity]

# 创建 mayavi 3D 散点图
mlab.figure(bgcolor=(1, 1, 1))  # 设置背景为白色
mlab.points3d(
    points[:, 0], points[:, 1], points[:, 2],  # x, y, z
    points[:, 3],  # intensity 作为颜色
    scale_factor=0.02,  # 点的大小
    colormap='viridis'  # 颜色映射
)

# 显示图形
mlab.show()