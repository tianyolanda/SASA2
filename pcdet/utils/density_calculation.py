from ..ops.pointnet2.pointnet2_batch.pointnet2_utils import ball_query
import time
import torch
import matplotlib.pyplot as plt

def vis_weight_distribution_single(value, radius, max):
    '''
    written by tiatia 2025/2/25
    this function is to visiualize value distribution, can compare two values' distribution
    :param value_before_weight: value 1 (B,1,N)?
    :param value_after_weight:  value 2 (B,1,N)?
    :return:
    '''
    # 加权前的数值分布
    value = value.cpu().flatten().numpy()

    # 加权后的数值分布

    # 绘制加权前后的数值分布图
    plt.figure(figsize=(6, 6))

    # 加权前的分布图
    plt.hist(value, bins=50, color='blue', alpha=0.7)
    title_name = 'Distribution_of_radius_'+str(radius)+'_max_'+str(max)
    plt.title(title_name)
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()


# 这俩save只能save一帧的内容...
def tensor_save_to_txt(density_value_tensor, radius, max):
    # 打开文件并写入张量内容
    print(density_value_tensor.size())
    vis_weight_distribution_single(density_value_tensor, radius, max)
    txt_file_name = 'num_cnt_ball_points_'+'radius_'+str(radius)+'max_'+str(max)+'.txt'
    with open(txt_file_name, 'w') as f:
        for row in density_value_tensor:
            # 将每一行转换为字符串并写入文件
            row_str = ' '.join([f'{x:.2f}' for x in row.tolist()])
            f.write(row_str + '\n')
    print('successful save to ',txt_file_name)

def float_save_to_txt(floatx):
    # 打开文件并写入内容
    with open('time_cnt_ball_points_radius1.0_nsample500.txt', 'w') as f:
        row_str = ' '.join(f'{floatx:.6f}')
        f.write(row_str + '\n')


def vis3d_pyvista(points, feature):
    import pyvista as pv
    import numpy as np
    '''
    points: [1, N, D]
    
    '''
    # 创建 PyVista 点云对象
    if points.size(0) == 1:
        # points.unsqueeze(0)
        # print('points.size',points.size)
        points = points.cpu()
        points = points.numpy()
        points = np.squeeze(points,axis=0) # [N,D]
        # print('points.shape',points.shape)

        cloud = pv.PolyData(points[:, :3])  # 提取 x, y, z 坐标
        # cloud["intensity"] = points[:, 3]  # 添加 intensity 作为标量场
        print(feature.shape)
        cloud["intensity"] = feature.view(feature.size(1)).cpu()  # 添加 intensity 作为标量场
        # cloud["intensity"] = feature.cpu()  # 添加 intensity 作为标量场

        # 可视化点云
        plotter = pv.Plotter()
        # 设置背景颜色为白色
        plotter.set_background("white")
        plotter.add_mesh(cloud, scalars="intensity", cmap="YlOrBr", point_size=3)
        # plotter.add_mesh(cloud, scalars="intensity", cmap="viridis", point_size=1)
        # cmap change: https://matplotlib.org/stable/users/explain/colors/colormaps.html
        plotter.show()
    else:
        print('the shape of points is incorrect!')
def cnt_ball_points(radius, max_nsample, points=''):
    '''

    :param radius: 球半径
    :param nsample: 在球内最多找多少个点,算法停 (点数最大值,点数上限)
    :param points: 输入点云,numpy.ndarray
    当batch size>1 时, 多个输入点云会摞在一起
    example: 比如point的尺寸是[32768, 5]
            其中32768=2个16384的点云摞在一起
            5个特征表示:
            第一维是0/1,表示该点是属于第0个batch还是第1个batch
            第二维-第四维是xyz
            第五维是intensity
    :return:
    '''
    first_column = points[:, 0] # batch_id of each points
    # print('points.shape',points.shape) #　points.shape torch.Size([32768, 5])
    batch_num = torch.max(first_column).int()+1 # 计算出当前points是多少个点云图摞在一起的
    # print('batch_num',batch_num)
    idx_cnt_batch = ''
    for i in range(batch_num):
        # print('i',i)
        points_torch=torch.tensor(points[16384*i:16384*(i+1),1:4])
        points_intensity_torch=torch.tensor(points[16384*i:16384*(i+1),4])

        num_points = points_torch.size(0)
        # print('points_torch.shape',points_torch.shape)
        points_torch = points_torch.view([1,num_points,3])
        idx_cnt, idx = ball_query(radius, max_nsample, points_torch,points_torch)
        # record
        # vis3d_pyvista(points_torch, idx_cnt)
        # vis3d_pyvista(points_torch, points_intensity_torch)
        # tensor_save_to_txt(idx_cnt, radius, max_nsample)
        # float_save_to_txt(time2-time1)
        if i == 0:
            idx_cnt_batch = idx_cnt
        else:
            idx_cnt_batch = torch.cat((idx_cnt_batch, idx_cnt),dim=1)
        # print('idx_cnt_batch.size()',idx_cnt_batch.size())
    idx_cnt_batch_float = idx_cnt_batch.to(dtype=torch.float32)
    return idx_cnt_batch_float

'''
def ball_query(radius: float, nsample: int, xyz: torch.Tensor, new_xyz: torch.Tensor):
    """
    :param radius: float, radius of the balls
    :param nsample: int, maximum number of features in the balls
    :param xyz: (B, N, 3) xyz coordinates of the features
    :param new_xyz: (B, npoint, 3) centers of the ball query
    :return:
        idx_cnt: (B, npoint) tensor with the number of grouped points for each ball query
        idx: (B, npoint, nsample) tensor with the indicies of the features that form the query balls
    """
    assert new_xyz.is_contiguous()
    assert xyz.is_contiguous()

    B, N, _ = xyz.size()
    npoint = new_xyz.size(1)
    idx = torch.cuda.IntTensor(B, npoint, nsample).zero_()
    idx_cnt = torch.cuda.IntTensor(B, npoint).zero_()

    pointnet2.ball_query_wrapper(B, N, npoint, radius, nsample, new_xyz, xyz, idx_cnt, idx)
    # print('******')
    # print('ball query')
    # print(B, N, npoint, radius, nsample, idx_cnt)

    return idx_cnt, idx
'''

# vis3d_pyvista(points)
# cnt_ball_points(radius=0.2, nsample=64, points=points)
