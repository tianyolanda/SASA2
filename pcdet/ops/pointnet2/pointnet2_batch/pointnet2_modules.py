from typing import List

import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


from . import pointnet2_utils
from pcdet.utils.density_calculation import vis3d_pyvista

def min_max_normalize(tensor, min_vals=0, max_vals=500):
    # 最大-最小归一化（对每个 batch 分别计算 max 和 min）

    # 沿着第1维（batch 维度）计算每个 batch 的 min 和 max
    # min_vals = tensor.min(dim=2, keepdim=True).values  # 形状: [2, 1, 1]
    # min_vals = 0  # 形状: [2, 1, 1]
    # max_vals = tensor.max(dim=2, keepdim=True).values  # 形状: [2, 1, 1]
    # max_vals = 10  # 形状: [2, 1, 1]
    # 对每个 batch 进行归一化
    normalized_tensor = (tensor - min_vals) / (max_vals - min_vals)  # 形状: [2, 1, 4096]
    return normalized_tensor

def density_factor_calculation(density, weight):
    '''
    written by tiatia 2025/2/25
    sampling algorithm ranking strategy:
    ranking = (score ** weight_gamma) * (1 + density ** weight_beta )/2
    this function aims to calculate the second multiplier(called density_factor): (1 + density ** weight_beta )/2
    :param density: density of each point (B,1,N)?
    :param weight: weight_beta
    :return: density_factor
    '''

    weight = 0.1
    density = 1-density # (0~1)
    # density_factor = (1 + density ** weight)/2
    density_factor =  density ** weight
    return density_factor

def sigmoid_normalize(tensor):
    return tensor.sigmoid()

def vis_weight_distribution(value_before_weight, value_after_weight):
    '''
    written by tiatia 2025/2/25
    this function is to visiualize value distribution, can compare two values' distribution
    :param value_before_weight: value 1 (B,1,N)?
    :param value_after_weight:  value 2 (B,1,N)?
    :return:
    '''
    # 加权前的数值分布
    value_before_weight = value_before_weight.cpu().flatten().numpy()

    # 加权后的数值分布
    value_after_weight = value_after_weight.cpu().flatten().numpy()

    print('-----here')

    # 绘制加权前后的数值分布图
    plt.figure(figsize=(12, 6))

    # 加权前的分布图
    plt.subplot(1, 2, 1)
    plt.hist(value_before_weight, bins=50, color='blue', alpha=0.7)
    plt.title('Distribution 1: semantic_score')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    # 加权后的分布图
    plt.subplot(1, 2, 2)
    plt.hist(value_after_weight, bins=50, color='red', alpha=0.7)
    plt.title('Distribution 2: semantic_score * density_factor')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()


class _PointnetSAModuleBase(nn.Module):

    def __init__(self):
        super().__init__()
        self.npoint = None
        self.groupers = None
        self.mlps = None
        self.pool_method = 'max_pool'

    def forward(self, xyz: torch.Tensor, features: torch.Tensor = None, new_xyz=None) -> (torch.Tensor, torch.Tensor):
        """
        :param xyz: (B, N, 3) tensor of the xyz coordinates of the features
        :param features: (B, C, N) tensor of the descriptors of the the features
        :param new_xyz: (B, npoint, 3) tensor of the xyz coordinates of the grouping centers if specified
        :return:
            new_xyz: (B, npoint, 3) tensor of the new features' xyz
            new_features: (B, npoint, \sum_k(mlps[k][-1])) tensor of the new_features descriptors
        """
        new_features_list = []

        xyz_flipped = xyz.transpose(1, 2).contiguous()
        if new_xyz is None:
            new_xyz = pointnet2_utils.gather_operation(
                xyz_flipped,
                pointnet2_utils.furthest_point_sample(xyz, self.npoint)
            ).transpose(1, 2).contiguous() if self.npoint is not None else None

        for i in range(len(self.groupers)):
            idx_cnt, new_features = self.groupers[i](xyz, new_xyz, features)  # (B, C, npoint, nsample)

            new_features = self.mlps[i](new_features)  # (B, mlp[-1], npoint, nsample)
            idx_cnt_mask = (idx_cnt > 0).float()
            idx_cnt_mask = idx_cnt_mask.unsqueeze(dim=1).unsqueeze(dim=-1)
            # new_features *= idx_cnt_mask
            new_features = new_features * idx_cnt_mask
            '''
                allow_unreachable=True, accumulate_grad=True)  # allow_unreachable flag
RuntimeError: one of the variables needed for gradient computation has been modified by an inplace operation: [torch.cuda.FloatTensor [256, 512, 1, 32]], which is output 0 of ReluBackward0, is at version 1; expected version 0 instead. Hint: the backtrace further above shows the operation that failed to compute its gradient. The variable in question was changed in there or anywhere later. Good luck!

            '''
            if self.pool_method == 'max_pool':
                new_features = F.max_pool2d(
                    new_features, kernel_size=[1, new_features.size(3)]
                )  # (B, mlp[-1], npoint, 1)
            elif self.pool_method == 'avg_pool':
                new_features = F.avg_pool2d(
                    new_features, kernel_size=[1, new_features.size(3)]
                )  # (B, mlp[-1], npoint, 1)
            else:
                raise NotImplementedError

            new_features = new_features.squeeze(-1)  # (B, mlp[-1], npoint)
            new_features_list.append(new_features)

        return new_xyz, torch.cat(new_features_list, dim=1)


class PointnetSAModuleMSG(_PointnetSAModuleBase):
    """Pointnet set abstraction layer with multiscale grouping"""

    def __init__(self, *, npoint: int, radii: List[float], nsamples: List[int], mlps: List[List[int]], bn: bool = True,
                 use_xyz: bool = True, pool_method='max_pool'):
        """
        :param npoint: int
        :param radii: list of float, list of radii to group with
        :param nsamples: list of int, number of samples in each ball query
        :param mlps: list of list of int, spec of the pointnet before the global pooling for each scale
        :param bn: whether to use batchnorm
        :param use_xyz:
        :param pool_method: max_pool / avg_pool
        """
        super().__init__()

        assert len(radii) == len(nsamples) == len(mlps)

        self.npoint = npoint
        self.groupers = nn.ModuleList()
        self.mlps = nn.ModuleList()
        for i in range(len(radii)):
            radius = radii[i]
            nsample = nsamples[i]
            self.groupers.append(
                pointnet2_utils.QueryAndGroup(radius, nsample, use_xyz=use_xyz)
                if npoint is not None else pointnet2_utils.GroupAll(use_xyz)
            )
            mlp_spec = mlps[i]
            if use_xyz:
                mlp_spec[0] += 3

            shared_mlps = []
            for k in range(len(mlp_spec) - 1):
                shared_mlps.extend([
                    nn.Conv2d(mlp_spec[k], mlp_spec[k + 1], kernel_size=1, bias=False),
                    nn.BatchNorm2d(mlp_spec[k + 1]),
                    nn.ReLU()
                ])
            self.mlps.append(nn.Sequential(*shared_mlps))

        self.pool_method = pool_method


class PointnetSAModule(PointnetSAModuleMSG):
    """Pointnet set abstraction layer"""

    def __init__(self, *, mlp: List[int], npoint: int = None, radius: float = None, nsample: int = None,
                 bn: bool = True, use_xyz: bool = True, pool_method='max_pool'):
        """
        :param mlp: list of int, spec of the pointnet before the global max_pool
        :param npoint: int, number of features
        :param radius: float, radius of ball
        :param nsample: int, number of samples in the ball query
        :param bn: whether to use batchnorm
        :param use_xyz:
        :param pool_method: max_pool / avg_pool
        """
        super().__init__(
            mlps=[mlp], npoint=npoint, radii=[radius], nsamples=[nsample], bn=bn, use_xyz=use_xyz,
            pool_method=pool_method
        )


class _PointnetSAModuleFSBase(nn.Module):

    def __init__(self):
        super().__init__()
        self.groupers = None
        self.mlps = None
        self.npoint_list = []
        self.sample_range_list = [[0, -1]]
        self.sample_method_list = ['d-fps']
        self.radii = []

        self.pool_method = 'max_pool'
        self.dilated_radius_group = False
        self.weight_gamma = 1.0
        self.skip_connection = False

        self.aggregation_mlp = None
        self.confidence_mlp = None

    def forward(self,
                xyz: torch.Tensor,
                features: torch.Tensor = None,
                new_xyz=None,
                scores=None):
        """
        :param xyz: (B, N, 3) tensor of the xyz coordinates of the features
               xyz: torch.Size([4, 16384, 3])

        :param features: (B, C, N) tensor of the descriptors of the features
               features: torch.Size([4, 1, 16384])

        :param new_xyz:
               new_xyz: None
        :param scores: (B, N) tensor of confidence scores of points, required when using s-fps
               scores: 在第一个PointnetSAModuleFSMSG()里是None
        :return:
            new_xyz: (B, npoint, 3) tensor of the new features' xyz
            new_features: (B, npoint, \sum_k(mlps[k][-1])) tensor of the new_features descriptors
        """
        #　self.npoint_list: <class 'list'>: [4096]
        #　self.sample_range_list: <class 'list'>: [[0, 16384]]

        new_features_list = []
        xyz_flipped = xyz.transpose(1, 2).contiguous()  #　torch.Size([4, 3, 16384])
        if new_xyz is None:
            assert len(self.npoint_list) == len(self.sample_range_list) == len(self.sample_method_list)
            sample_idx_list = []
            for i in range(len(self.sample_method_list)): # 循环不同的sample方式
                xyz_slice = xyz[:, self.sample_range_list[i][0]:self.sample_range_list[i][1], :].contiguous() # torch.Size([4, 16384, 3])
                if self.sample_method_list[i] == 'd-fps':
                    sample_idx = pointnet2_utils.furthest_point_sample(xyz_slice, self.npoint_list[i])
                elif self.sample_method_list[i] == 'f-fps':
                    features_slice = features[:, :, self.sample_range_list[i][0]:self.sample_range_list[i][1]]
                    dist_matrix = pointnet2_utils.calc_dist_matrix_for_sampling(xyz_slice,
                                                                                features_slice.permute(0, 2, 1),
                                                                                self.weight_gamma)
                    sample_idx = pointnet2_utils.furthest_point_sample_matrix(dist_matrix, self.npoint_list[i])
                elif self.sample_method_list[i] == 's-fps':
                    assert scores is not None
                    scores_slice = \
                        scores[:, self.sample_range_list[i][0]:self.sample_range_list[i][1]].contiguous()
                    scores_slice = scores_slice.sigmoid() ** self.weight_gamma
                    sample_idx = pointnet2_utils.furthest_point_sample_weights(
                        xyz_slice,
                        scores_slice,
                        self.npoint_list[i]
                    )
                else:
                    raise NotImplementedError

                # 第一个循环:
                # sample_method_list: <class 'list'>: ['d-fps']
                # sample_idx: torch.Size([4, 4096])
                sample_idx_list.append(sample_idx + self.sample_range_list[i][0])

            sample_idx = torch.cat(sample_idx_list, dim=-1) # torch.Size([4, 4096]) , torch.Size([4, 512])
            new_xyz = pointnet2_utils.gather_operation(
                xyz_flipped,
                sample_idx
            ).transpose(1, 2).contiguous()  # (B, npoint, 3) torch.Size([4, 512, 3])
            
            if self.skip_connection: 
                old_features = pointnet2_utils.gather_operation(
                    features,
                    sample_idx
                ) if features is not None else None  # (B, C, npoint)

        for i in range(len(self.groupers)):
            idx_cnt, new_features = self.groupers[i](xyz, new_xyz, features)  # (B, C, npoint, nsample)
            new_features = self.mlps[i](new_features)  # (B, mlp[-1], npoint, nsample)
            idx_cnt_mask = (idx_cnt > 0).float()  # (B, npoint)
            idx_cnt_mask = idx_cnt_mask.unsqueeze(1).unsqueeze(-1)  # (B, 1, npoint, 1)
            # new_features *= idx_cnt_mask
            '''
        RuntimeError: one of the variables needed for gradient computation has been modified by an inplace operation: [torch.cuda.FloatTensor [256, 512, 1, 32]], which is output 0 of ReluBackward0, is at version 1; expected version 0 instead. Hint: the backtrace further above shows the operation that failed to compute its gradient. The variable in question was changed in there or anywhere later. Good luck!
            '''
            new_features = new_features * idx_cnt_mask
            if self.pool_method == 'max_pool':
                pooled_features = F.max_pool2d(
                    new_features, kernel_size=[1, new_features.size(3)]
                )  # (B, mlp[-1], npoint, 1)
            elif self.pool_method == 'avg_pool':
                pooled_features = F.avg_pool2d(
                    new_features, kernel_size=[1, new_features.size(3)]
                )  # (B, mlp[-1], npoint, 1)
            else:
                raise NotImplementedError
            
            new_features_list.append(pooled_features.squeeze(-1))  # (B, mlp[-1], npoint)

        if self.skip_connection and old_features is not None:
            new_features_list.append(old_features)

        new_features = torch.cat(new_features_list, dim=1)
        if self.aggregation_mlp is not None:
            new_features = self.aggregation_mlp(new_features)

        if self.confidence_mlp is not None:
            new_scores = self.confidence_mlp(new_features)
            new_scores = new_scores.squeeze(1)  # (B, npoint)
            return new_xyz, new_features, new_scores

        return new_xyz, new_features, None


class PointnetSAModuleFSMSG(_PointnetSAModuleFSBase):
    """Pointnet set abstraction layer with fusion sampling and multiscale grouping"""

    def __init__(self, *,
                 npoint_list: List[int] = None,
                 sample_range_list: List[List[int]] = None,
                 sample_method_list: List[str] = None,
                 radii: List[float],
                 nsamples: List[int],
                 mlps: List[List[int]],
                 bn: bool = True,
                 use_xyz: bool = True,
                 pool_method='max_pool',
                 dilated_radius_group: bool = False,
                 skip_connection: bool = False,
                 weight_gamma: float = 1.0,
                 aggregation_mlp: List[int] = None,
                 confidence_mlp: List[int] = None):
        """
        :param npoint_list: list of int, number of samples for every sampling method
        :param sample_range_list: list of list of int, sample index range [left, right] for every sampling method
        :param sample_method_list: list of str, list of used sampling method, d-fps or f-fps
        :param radii: list of float, list of radii to group with
        :param nsamples: list of int, number of samples in each ball query
        :param mlps: list of list of int, spec of the pointnet before the global pooling for each scale
        :param bn: whether to use batchnorm
        :param use_xyz:
        :param pool_method: max_pool / avg_pool
        :param dilated_radius_group: whether to use radius dilated group
        :param skip_connection: whether to add skip connection
        :param weight_gamma: gamma for s-fps, default: 1.0
        :param aggregation_mlp: list of int, spec aggregation mlp
        :param confidence_mlp: list of int, spec confidence mlp
        """
        super().__init__()

        assert npoint_list is None or len(npoint_list) == len(sample_range_list) == len(sample_method_list)
        assert len(radii) == len(nsamples) == len(mlps)

        self.npoint_list = npoint_list
        self.sample_range_list = sample_range_list
        self.sample_method_list = sample_method_list
        self.radii = radii
        self.groupers = nn.ModuleList()
        self.mlps = nn.ModuleList()

        former_radius = 0.0
        in_channels, out_channels = 0, 0
        for i in range(len(radii)):
            radius = radii[i]
            nsample = nsamples[i]
            if dilated_radius_group:
                self.groupers.append(
                    pointnet2_utils.QueryAndGroupDilated(former_radius, radius, nsample, use_xyz=use_xyz)
                )
            else:
                self.groupers.append(
                    pointnet2_utils.QueryAndGroup(radius, nsample, use_xyz=use_xyz)
                )
            former_radius = radius
            mlp_spec = mlps[i]
            if use_xyz:
                # print('here,mlp_spec[0]',mlp_spec[0])
                mlp_spec[0] = mlp_spec[0] + 3

            shared_mlp = []
            for k in range(len(mlp_spec) - 1):
                shared_mlp.extend([
                    nn.Conv2d(mlp_spec[k], mlp_spec[k + 1], kernel_size=1, bias=False),
                    nn.BatchNorm2d(mlp_spec[k + 1]),
                    nn.ReLU()
                ])
            self.mlps.append(nn.Sequential(*shared_mlp))
            in_channels = mlp_spec[0] - 3 if use_xyz else mlp_spec[0]
            out_channels = out_channels + mlp_spec[-1]

        self.pool_method = pool_method
        self.dilated_radius_group = dilated_radius_group
        self.skip_connection = skip_connection
        self.weight_gamma = weight_gamma

        if skip_connection:
            out_channels = out_channels + in_channels

        if aggregation_mlp is not None:
            shared_mlp = []
            for k in range(len(aggregation_mlp)):
                shared_mlp.extend([
                    nn.Conv1d(out_channels, aggregation_mlp[k], kernel_size=1, bias=False),
                    nn.BatchNorm1d(aggregation_mlp[k]),
                    nn.ReLU()
                ])
                out_channels = aggregation_mlp[k]
            self.aggregation_mlp = nn.Sequential(*shared_mlp)
        else:
            self.aggregation_mlp = None

        if confidence_mlp is not None:
            shared_mlp = []
            for k in range(len(confidence_mlp)):
                shared_mlp.extend([
                    nn.Conv1d(out_channels, confidence_mlp[k], kernel_size=1, bias=False),
                    nn.BatchNorm1d(confidence_mlp[k]),
                    nn.ReLU()
                ])
                out_channels = confidence_mlp[k]
            shared_mlp.append(
                nn.Conv1d(out_channels, 1, kernel_size=1, bias=True),
            )
            self.confidence_mlp = nn.Sequential(*shared_mlp)
        else:
            self.confidence_mlp = None


class PointnetSAModuleFS(PointnetSAModuleFSMSG):
    """Pointnet set abstraction layer with fusion sampling"""

    def __init__(self, *,
                 mlp: List[int],
                 npoint_list: List[int] = None,
                 sample_range_list: List[List[int]] = None,
                 sample_method_list: List[str] = None,
                 radius: float = None,
                 nsample: int = None,
                 bn: bool = True,
                 use_xyz: bool = True,
                 pool_method='max_pool',
                 dilated_radius_group: bool = False,
                 skip_connection: bool = False,
                 weight_gamma: float = 1.0,
                 aggregation_mlp: List[int] = None,
                 confidence_mlp: List[int] = None):
        """
        :param mlp: list of int, spec of the pointnet before the global max_pool
        :param npoint_list: list of int, number of samples for every sampling method
        :param sample_range_list: list of list of int, sample index range [left, right] for every sampling method
        :param sample_method_list: list of str, list of used sampling method, d-fps, f-fps or c-fps
        :param radius: float, radius of ball
        :param nsample: int, number of samples in the ball query
        :param bn: whether to use batchnorm
        :param use_xyz:
        :param pool_method: max_pool / avg_pool
        :param dilated_radius_group: whether to use radius dilated group
        :param skip_connection: whether to add skip connection
        :param weight_gamma: gamma for s-fps, default: 1.0
        :param aggregation_mlp: list of int, spec aggregation mlp
        :param confidence_mlp: list of int, spec confidence mlp
        """
        super().__init__(
            mlps=[mlp], npoint_list=npoint_list, sample_range_list=sample_range_list,
            sample_method_list=sample_method_list, radii=[radius], nsamples=[nsample],
            bn=bn, use_xyz=use_xyz, pool_method=pool_method, dilated_radius_group=dilated_radius_group,
            skip_connection=skip_connection, weight_gamma=weight_gamma,
            aggregation_mlp=aggregation_mlp, confidence_mlp=confidence_mlp
        )

class PointnetFPModule(nn.Module):
    r"""Propigates the features of one set to another"""

    def __init__(self, *, mlp: List[int], bn: bool = True):
        """
        :param mlp: list of int
        :param bn: whether to use batchnorm
        """
        super().__init__()

        shared_mlps = []
        for k in range(len(mlp) - 1):
            shared_mlps.extend([
                nn.Conv2d(mlp[k], mlp[k + 1], kernel_size=1, bias=False),
                nn.BatchNorm2d(mlp[k + 1]),
                nn.ReLU()
            ])
        self.mlp = nn.Sequential(*shared_mlps)

    def forward(
            self, unknown: torch.Tensor, known: torch.Tensor, unknow_feats: torch.Tensor, known_feats: torch.Tensor
    ) -> torch.Tensor:
        """
        :param unknown: (B, n, 3) tensor of the xyz positions of the unknown features
        :param known: (B, m, 3) tensor of the xyz positions of the known features
        :param unknow_feats: (B, C1, n) tensor of the features to be propigated to
        :param known_feats: (B, C2, m) tensor of features to be propigated
        :return:
            new_features: (B, mlp[-1], n) tensor of the features of the unknown features
        """
        if known is not None:
            dist, idx = pointnet2_utils.three_nn(unknown, known)
            dist_recip = 1.0 / (dist + 1e-8)
            norm = torch.sum(dist_recip, dim=2, keepdim=True)
            weight = dist_recip / norm

            interpolated_feats = pointnet2_utils.three_interpolate(known_feats, idx, weight)
        else:
            interpolated_feats = known_feats.expand(*known_feats.size()[0:2], unknown.size(1))

        if unknow_feats is not None:
            new_features = torch.cat([interpolated_feats, unknow_feats], dim=1)  # (B, C2 + C1, n)
        else:
            new_features = interpolated_feats

        new_features = new_features.unsqueeze(-1)
        new_features = self.mlp(new_features)

        return new_features.squeeze(-1)

# wD = with Density
class _PointnetSAModuleFSBasewD(nn.Module):

    def __init__(self):
        super().__init__()
        self.groupers = None
        self.mlps = None
        self.npoint_list = []
        self.sample_range_list = [[0, -1]]
        self.sample_method_list = ['d-fps']
        self.radii = []

        self.pool_method = 'max_pool'
        self.dilated_radius_group = False
        self.weight_gamma = 1.0
        self.weight_beta = 1.0
        self.skip_connection = False

        self.aggregation_mlp = None
        self.confidence_mlp = None

    def forward(self,
                xyz: torch.Tensor,
                features: torch.Tensor = None,
                density: torch.Tensor = None,
                new_xyz=None,
                scores=None):
        """
        :param xyz: (B, N, 3) tensor of the xyz coordinates of the features
               xyz: torch.Size([4, 16384, 3])

        :param features: (B, C, N) tensor of the descriptors of the features
               features: torch.Size([4, 1, 16384])

        :param density: (B, C, N) tensor of the descriptors of the density
                        和feature一样维度
               density: torch.Size([4, 1, 16384])

        :param new_xyz:
               new_xyz: None
        :param scores: (B, N) tensor of confidence scores of points, required when using s-fps
               scores: 在第一个PointnetSAModuleFSMSG()里是None
        :return:
            new_xyz: (B, npoint, 3) tensor of the new features' xyz
            new_features: (B, npoint, \sum_k(mlps[k][-1])) tensor of the new_features descriptors
        """
        # 　self.npoint_list: <class 'list'>: [4096]
        # 　self.sample_range_list: <class 'list'>: [[0, 16384]]

        new_features_list = []
        xyz_flipped = xyz.transpose(1, 2).contiguous()  # torch.Size([4, 3, 16384])
        density_squeezed = density.squeeze(1).contiguous()  # torch.Size([4, 16384])
        if new_xyz is None:
            assert len(self.npoint_list) == len(self.sample_range_list) == len(self.sample_method_list)
            sample_idx_list = []
            for i in range(len(self.sample_method_list)):  # 循环不同的sample方式
                xyz_slice = xyz[:, self.sample_range_list[i][0]:self.sample_range_list[i][1],
                            :].contiguous()  # torch.Size([4, 16384, 3])
                if self.sample_method_list[i] == 'd-fps':
                    sample_idx = pointnet2_utils.furthest_point_sample(xyz_slice, self.npoint_list[i])
                elif self.sample_method_list[i] == 'f-fps':
                    features_slice = features[:, :, self.sample_range_list[i][0]:self.sample_range_list[i][1]]
                    dist_matrix = pointnet2_utils.calc_dist_matrix_for_sampling(xyz_slice,
                                                                                features_slice.permute(0, 2, 1),
                                                                                self.weight_gamma)
                    sample_idx = pointnet2_utils.furthest_point_sample_matrix(dist_matrix, self.npoint_list[i])
                elif self.sample_method_list[i] == 's-fps':
                    assert scores is not None
                    scores_slice = \
                        scores[:, self.sample_range_list[i][0]:self.sample_range_list[i][1]].contiguous()
                    scores_slice = scores_slice.sigmoid() ** self.weight_gamma
                    sample_idx = pointnet2_utils.furthest_point_sample_weights(
                        xyz_slice,
                        scores_slice,
                        self.npoint_list[i]
                    )
                elif self.sample_method_list[i] == 'sden-fps':
                    assert scores is not None
                    scores_slice_0 = \
                        scores[:, self.sample_range_list[i][0]:self.sample_range_list[i][1]].contiguous()
                    scores_slice = scores_slice_0.sigmoid() ** self.weight_gamma
                    density_slice = \
                        density_squeezed[:, self.sample_range_list[i][0]:self.sample_range_list[i][1]].contiguous()

                    density_norm = min_max_normalize(density_slice)
                    density_factor = density_factor_calculation(density_norm, self.weight_beta)
                    #
                    # # vis_weight_distribution(density_slice.detach(), density_factor.detach())
                    # # vis_weight_distribution(scores_slice_0.detach(), scores_slice.detach())
                    # show_aa = scores_slice.detach()
                    # show_bb = show_aa.clone()
                    # show_bb = show_bb*density_factor
                    # vis_weight_distribution(show_aa,show_bb)
                    #
                    # aa =density_factor.clone()*scores_slice.clone()
                    # # aa =scores_slice
                    # # aa =density_factor
                    # print(aa.shape)
                    # # torch.Size([2, 4096])
                    # # torch.Size([2, 512])
                    # print(xyz_slice.shape)
                    # vis3d_pyvista(xyz_slice.detach(), aa.detach())

                    sample_idx = pointnet2_utils.furthest_point_sample_weights_density(
                        xyz_slice,
                        scores_slice,
                        density_factor,
                        self.npoint_list[i]
                    )
                else:
                    raise NotImplementedError

                # 第一个循环:
                # sample_method_list: <class 'list'>: ['d-fps']
                # sample_idx: torch.Size([4, 4096])
                sample_idx_list.append(sample_idx + self.sample_range_list[i][0])

            sample_idx = torch.cat(sample_idx_list, dim=-1)  # torch.Size([4, 4096]) , torch.Size([4, 512])
            new_xyz = pointnet2_utils.gather_operation(
                xyz_flipped,
                sample_idx
            ).transpose(1, 2).contiguous()  # (B, npoint, 3) torch.Size([4, 512, 3])
            new_density = pointnet2_utils.gather_operation(
                density,
                sample_idx
            ).contiguous()  # (B, npoint, 3) torch.Size([4, 512, 3])

            if self.skip_connection:
                old_features = pointnet2_utils.gather_operation(
                    features,
                    sample_idx
                ) if features is not None else None  # (B, C, npoint)

        for i in range(len(self.groupers)):
            idx_cnt, new_features = self.groupers[i](xyz, new_xyz, features)  # (B, C, npoint, nsample)
            new_features = self.mlps[i](new_features)  # (B, mlp[-1], npoint, nsample)
            idx_cnt_mask = (idx_cnt > 0).float()  # (B, npoint)
            idx_cnt_mask = idx_cnt_mask.unsqueeze(1).unsqueeze(-1)  # (B, 1, npoint, 1)
            # new_features *= idx_cnt_mask
            '''
        RuntimeError: one of the variables needed for gradient computation has been modified by an inplace operation: [torch.cuda.FloatTensor [256, 512, 1, 32]], which is output 0 of ReluBackward0, is at version 1; expected version 0 instead. Hint: the backtrace further above shows the operation that failed to compute its gradient. The variable in question was changed in there or anywhere later. Good luck!
            '''
            new_features = new_features * idx_cnt_mask
            if self.pool_method == 'max_pool':
                pooled_features = F.max_pool2d(
                    new_features, kernel_size=[1, new_features.size(3)]
                )  # (B, mlp[-1], npoint, 1)
            elif self.pool_method == 'avg_pool':
                pooled_features = F.avg_pool2d(
                    new_features, kernel_size=[1, new_features.size(3)]
                )  # (B, mlp[-1], npoint, 1)
            else:
                raise NotImplementedError

            new_features_list.append(pooled_features.squeeze(-1))  # (B, mlp[-1], npoint)

        if self.skip_connection and old_features is not None:
            new_features_list.append(old_features)

        new_features = torch.cat(new_features_list, dim=1)
        if self.aggregation_mlp is not None:
            new_features = self.aggregation_mlp(new_features)

        if self.confidence_mlp is not None:
            new_scores = self.confidence_mlp(new_features)
            new_scores = new_scores.squeeze(1)  # (B, npoint)
            return new_xyz, new_features, new_density, new_scores

        return new_xyz, new_features, new_density, None

class PointnetSAModuleFSMSGwD(_PointnetSAModuleFSBasewD):
    """Pointnet set abstraction layer with fusion sampling and multiscale grouping"""

    def __init__(self, *,
                 npoint_list: List[int] = None,
                 sample_range_list: List[List[int]] = None,
                 sample_method_list: List[str] = None,
                 radii: List[float],
                 nsamples: List[int],
                 mlps: List[List[int]],
                 bn: bool = True,
                 use_xyz: bool = True,
                 pool_method='max_pool',
                 dilated_radius_group: bool = False,
                 skip_connection: bool = False,
                 weight_gamma: float = 1.0,
                 aggregation_mlp: List[int] = None,
                 confidence_mlp: List[int] = None):
        """
        :param npoint_list: list of int, number of samples for every sampling method
        :param sample_range_list: list of list of int, sample index range [left, right] for every sampling method
        :param sample_method_list: list of str, list of used sampling method, d-fps or f-fps
        :param radii: list of float, list of radii to group with
        :param nsamples: list of int, number of samples in each ball query
        :param mlps: list of list of int, spec of the pointnet before the global pooling for each scale
        :param bn: whether to use batchnorm
        :param use_xyz:
        :param pool_method: max_pool / avg_pool
        :param dilated_radius_group: whether to use radius dilated group
        :param skip_connection: whether to add skip connection
        :param weight_gamma: gamma for s-fps, default: 1.0
        :param aggregation_mlp: list of int, spec aggregation mlp
        :param confidence_mlp: list of int, spec confidence mlp
        """
        super().__init__()

        assert npoint_list is None or len(npoint_list) == len(sample_range_list) == len(sample_method_list)
        assert len(radii) == len(nsamples) == len(mlps)

        self.npoint_list = npoint_list
        self.sample_range_list = sample_range_list
        self.sample_method_list = sample_method_list
        self.radii = radii
        self.groupers = nn.ModuleList()
        self.mlps = nn.ModuleList()

        former_radius = 0.0
        in_channels, out_channels = 0, 0
        for i in range(len(radii)):
            radius = radii[i]
            nsample = nsamples[i]
            if dilated_radius_group:
                self.groupers.append(
                    pointnet2_utils.QueryAndGroupDilated(former_radius, radius, nsample, use_xyz=use_xyz)
                )
            else:
                self.groupers.append(
                    pointnet2_utils.QueryAndGroup(radius, nsample, use_xyz=use_xyz)
                )
            former_radius = radius
            mlp_spec = mlps[i]
            if use_xyz:
                # print('here,mlp_spec[0]',mlp_spec[0])
                mlp_spec[0] = mlp_spec[0] + 3

            shared_mlp = []
            for k in range(len(mlp_spec) - 1):
                shared_mlp.extend([
                    nn.Conv2d(mlp_spec[k], mlp_spec[k + 1], kernel_size=1, bias=False),
                    nn.BatchNorm2d(mlp_spec[k + 1]),
                    nn.ReLU()
                ])
            self.mlps.append(nn.Sequential(*shared_mlp))
            in_channels = mlp_spec[0] - 3 if use_xyz else mlp_spec[0]
            out_channels = out_channels + mlp_spec[-1]

        self.pool_method = pool_method
        self.dilated_radius_group = dilated_radius_group
        self.skip_connection = skip_connection
        self.weight_gamma = weight_gamma

        if skip_connection:
            out_channels = out_channels + in_channels

        if aggregation_mlp is not None:
            shared_mlp = []
            for k in range(len(aggregation_mlp)):
                shared_mlp.extend([
                    nn.Conv1d(out_channels, aggregation_mlp[k], kernel_size=1, bias=False),
                    nn.BatchNorm1d(aggregation_mlp[k]),
                    nn.ReLU()
                ])
                out_channels = aggregation_mlp[k]
            self.aggregation_mlp = nn.Sequential(*shared_mlp)
        else:
            self.aggregation_mlp = None

        if confidence_mlp is not None:
            shared_mlp = []
            for k in range(len(confidence_mlp)):
                shared_mlp.extend([
                    nn.Conv1d(out_channels, confidence_mlp[k], kernel_size=1, bias=False),
                    nn.BatchNorm1d(confidence_mlp[k]),
                    nn.ReLU()
                ])
                out_channels = confidence_mlp[k]
            shared_mlp.append(
                nn.Conv1d(out_channels, 1, kernel_size=1, bias=True),
            )
            self.confidence_mlp = nn.Sequential(*shared_mlp)
        else:
            self.confidence_mlp = None

class PointnetSAModuleFS(PointnetSAModuleFSMSGwD):
    """Pointnet set abstraction layer with fusion sampling"""

    def __init__(self, *,
                 mlp: List[int],
                 npoint_list: List[int] = None,
                 sample_range_list: List[List[int]] = None,
                 sample_method_list: List[str] = None,
                 radius: float = None,
                 nsample: int = None,
                 bn: bool = True,
                 use_xyz: bool = True,
                 pool_method='max_pool',
                 dilated_radius_group: bool = False,
                 skip_connection: bool = False,
                 weight_gamma: float = 1.0,
                 aggregation_mlp: List[int] = None,
                 confidence_mlp: List[int] = None):
        """
        :param mlp: list of int, spec of the pointnet before the global max_pool
        :param npoint_list: list of int, number of samples for every sampling method
        :param sample_range_list: list of list of int, sample index range [left, right] for every sampling method
        :param sample_method_list: list of str, list of used sampling method, d-fps, f-fps or c-fps
        :param radius: float, radius of ball
        :param nsample: int, number of samples in the ball query
        :param bn: whether to use batchnorm
        :param use_xyz:
        :param pool_method: max_pool / avg_pool
        :param dilated_radius_group: whether to use radius dilated group
        :param skip_connection: whether to add skip connection
        :param weight_gamma: gamma for s-fps, default: 1.0
        :param aggregation_mlp: list of int, spec aggregation mlp
        :param confidence_mlp: list of int, spec confidence mlp
        """
        super().__init__(
            mlps=[mlp], npoint_list=npoint_list, sample_range_list=sample_range_list,
            sample_method_list=sample_method_list, radii=[radius], nsamples=[nsample],
            bn=bn, use_xyz=use_xyz, pool_method=pool_method, dilated_radius_group=dilated_radius_group,
            skip_connection=skip_connection, weight_gamma=weight_gamma,
            aggregation_mlp=aggregation_mlp, confidence_mlp=confidence_mlp
        )


if __name__ == "__main__":
    pass
