import numpy as np
import plotly.graph_objs as go
import plotly.express as px

# 生成 20,000 个点的示例数据
N = 50
points = np.random.rand(N, 4)  # [x, y, z, intensity]

# 创建 plotly 3D 散点图
fig = go.Figure(data=[go.Scatter3d(
    x=points[:, 0],
    y=points[:, 1],
    z=points[:, 2],
    mode='markers',
    marker=dict(
        size=2,
        color=points[:, 3],  # 使用 intensity 作为颜色
        colorscale='Viridis',  # 颜色映射
        opacity=0.8
    )
)])

# 设置布局
fig.update_layout(scene=dict(
    xaxis_title='X',
    yaxis_title='Y',
    zaxis_title='Z'
))

# 显示图形
fig.show()