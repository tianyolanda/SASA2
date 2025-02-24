import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 假设 points 是一个 [N, 4] 的 numpy 数组
# points[:, 0] 是 x 坐标
# points[:, 1] 是 y 坐标
# points[:, 2] 是 z 坐标
# points[:, 3] 是 intensity（强度）

# 生成一些示例数据
N = 100
points = np.random.rand(N, 4)  # 随机生成 [N, 4] 的数据

# 创建 3D 图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制散点图，使用 intensity 作为颜色
scatter = ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=points[:, 3], cmap='viridis')

# 添加颜色条
cbar = fig.colorbar(scatter)
cbar.set_label('Intensity')

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 显示图形
plt.show()