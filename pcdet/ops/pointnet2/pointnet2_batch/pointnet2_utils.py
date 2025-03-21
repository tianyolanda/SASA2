from typing import List, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Function, Variable

from . import pointnet2_batch_cuda as pointnet2


@torch.no_grad()
def calc_dist_matrix_for_sampling(xyz: torch.Tensor, features: torch.Tensor = None,
                                  gamma: float = 1.0):
    dist = torch.cdist(xyz, xyz)
    
    if features is not None:
        dist += torch.cdist(features, features) * gamma
    
    return dist


@torch.no_grad()
def furthest_point_sample(xyz: torch.Tensor, npoint: int) -> torch.Tensor:
    """
    Uses iterative furthest point sampling to select a set of npoint features that have the largest
    minimum distance
    :param ctx:
    :param xyz: (B, N, 3) where N > npoint
    :param npoint: int, number of features in the sampled set
    :return:
         output: (B, npoint) tensor containing the set
    """
    assert xyz.is_contiguous()

    B, N, _ = xyz.size()
    output = torch.cuda.IntTensor(B, npoint)
    temp = torch.cuda.FloatTensor(B, N).fill_(1e10)

    pointnet2.furthest_point_sampling_wrapper(B, N, npoint, xyz, temp, output)
    return output


@torch.no_grad()
def furthest_point_sample_matrix(matrix: torch.Tensor, npoint: int) -> torch.Tensor:
    """
    Uses iterative furthest point sampling to select a set of npoint features that have the largest
    minimum distance with a pairwise distance matrix
    :param matrix: (B, N, N) tensor of dist matrix
    :param npoint: int, number of features in the sampled set
    :return:
         output: (B, npoint) tensor containing the set
    """
    assert matrix.is_contiguous()

    B, N, _ = matrix.size()
    output = torch.cuda.IntTensor(B, npoint)
    temp = torch.cuda.FloatTensor(B, N).fill_(1e10)

    pointnet2.furthest_point_sampling_matrix_wrapper(B, N, npoint, matrix, temp, output)
    return output


@torch.no_grad()
def furthest_point_sample_weights(xyz: torch.Tensor, weights: torch.Tensor, npoint: int) -> torch.Tensor:
    """
    Uses iterative furthest point sampling to select a set of npoint features that have the largest
    minimum weighted distance
    Args:
        xyz: (B, N, 3), tensor of xyz coordinates
        weights: (B, N), tensor of point weights
        npoint: int, number of points in the sampled set
    Returns:
        output: (B, npoint) tensor containing the set
    """
    assert xyz.is_contiguous()
    assert weights.is_contiguous()

    B, N, _ = xyz.size()
    output = torch.cuda.IntTensor(B, npoint)
    temp = torch.cuda.FloatTensor(B, N).fill_(1e10)

    pointnet2.furthest_point_sampling_weights_wrapper(B, N, npoint, xyz, weights, temp, output)
    return output

@torch.no_grad()
def furthest_point_sample_weights_density(xyz: torch.Tensor, weights: torch.Tensor, density: torch.Tensor, npoint: int) -> torch.Tensor:
    """
    Uses iterative furthest point sampling to select a set of npoint features that have the largest
    minimum weighted distance
    Args:
        xyz: (B, N, 3), tensor of xyz coordinates
        weights: (B, N), tensor of point weights, sementic scores
        density: (B, N), tensor of point weights, density
        npoint: int, number of points in the sampled set
    Returns:
        output: (B, npoint) tensor containing the set
    """
    assert xyz.is_contiguous()
    assert weights.is_contiguous()
    assert density.is_contiguous()

    B, N, _ = xyz.size()
    output = torch.cuda.IntTensor(B, npoint)
    temp = torch.cuda.FloatTensor(B, N).fill_(1e10)

    pointnet2.furthest_point_sampling_weights_density_wrapper(B, N, npoint, xyz, weights, density, temp, output)
    return output

class GatherOperation(Function):

    @staticmethod
    def forward(ctx, features: torch.Tensor, idx: torch.Tensor) -> torch.Tensor:
        """
        :param ctx:
        :param features: (B, C, N)
        :param idx: (B, npoint) index tensor of the features to gather
        :return:
            output: (B, C, npoint)
        """
        assert features.is_contiguous()
        assert idx.is_contiguous()

        B, npoint = idx.size()
        _, C, N = features.size()
        output = torch.cuda.FloatTensor(B, C, npoint)

        pointnet2.gather_points_wrapper(B, C, N, npoint, features, idx, output)

        ctx.for_backwards = (idx, C, N)
        return output

    @staticmethod
    def backward(ctx, grad_out):
        idx, C, N = ctx.for_backwards
        B, npoint = idx.size()

        grad_features = Variable(torch.cuda.FloatTensor(B, C, N).zero_())
        grad_out_data = grad_out.data.contiguous()
        pointnet2.gather_points_grad_wrapper(B, C, N, npoint, grad_out_data, idx, grad_features.data)
        return grad_features, None


gather_operation = GatherOperation.apply


def three_nn(unknown: torch.Tensor, known: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Find the three nearest neighbors of unknown in known
        :param unknown: (B, N, 3)
        :param known: (B, M, 3)
        :return:
            dist: (B, N, 3) l2 distance to the three nearest neighbors
            idx: (B, N, 3) index of 3 nearest neighbors
        """
        assert unknown.is_contiguous()
        assert known.is_contiguous()

        B, N, _ = unknown.size()
        m = known.size(1)
        dist2 = torch.cuda.FloatTensor(B, N, 3)
        idx = torch.cuda.IntTensor(B, N, 3)

        pointnet2.three_nn_wrapper(B, N, m, unknown, known, dist2, idx)
        return torch.sqrt(dist2), idx


class ThreeInterpolate(Function):

    @staticmethod
    def forward(ctx, features: torch.Tensor, idx: torch.Tensor, weight: torch.Tensor) -> torch.Tensor:
        """
        Performs weight linear interpolation on 3 features
        :param ctx:
        :param features: (B, C, M) Features descriptors to be interpolated from
        :param idx: (B, n, 3) three nearest neighbors of the target features in features
        :param weight: (B, n, 3) weights
        :return:
            output: (B, C, N) tensor of the interpolated features
        """
        assert features.is_contiguous()
        assert idx.is_contiguous()
        assert weight.is_contiguous()

        B, c, m = features.size()
        n = idx.size(1)
        ctx.three_interpolate_for_backward = (idx, weight, m)
        output = torch.cuda.FloatTensor(B, c, n)

        pointnet2.three_interpolate_wrapper(B, c, m, n, features, idx, weight, output)
        return output

    @staticmethod
    def backward(ctx, grad_out: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """
        :param ctx:
        :param grad_out: (B, C, N) tensor with gradients of outputs
        :return:
            grad_features: (B, C, M) tensor with gradients of features
            None:
            None:
        """
        idx, weight, m = ctx.three_interpolate_for_backward
        B, c, n = grad_out.size()

        grad_features = Variable(torch.cuda.FloatTensor(B, c, m).zero_())
        grad_out_data = grad_out.data.contiguous()

        pointnet2.three_interpolate_grad_wrapper(B, c, n, m, grad_out_data, idx, weight, grad_features.data)
        return grad_features, None, None


three_interpolate = ThreeInterpolate.apply


class GroupingOperation(Function):

    @staticmethod
    def forward(ctx, features: torch.Tensor, idx: torch.Tensor) -> torch.Tensor:
        """
        :param ctx:
        :param features: (B, C, N) tensor of features to group
        :param idx: (B, npoint, nsample) tensor containing the indicies of features to group with
        :return:
            output: (B, C, npoint, nsample) tensor
        """
        assert features.is_contiguous()
        assert idx.is_contiguous()

        B, nfeatures, nsample = idx.size()
        _, C, N = features.size()
        output = torch.cuda.FloatTensor(B, C, nfeatures, nsample)

        pointnet2.group_points_wrapper(B, C, N, nfeatures, nsample, features, idx, output)

        ctx.for_backwards = (idx, N)
        return output

    @staticmethod
    def backward(ctx, grad_out: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        :param ctx:
        :param grad_out: (B, C, npoint, nsample) tensor of the gradients of the output from forward
        :return:
            grad_features: (B, C, N) gradient of the features
        """
        idx, N = ctx.for_backwards

        B, C, npoint, nsample = grad_out.size()
        grad_features = Variable(torch.cuda.FloatTensor(B, C, N).zero_())

        grad_out_data = grad_out.data.contiguous()
        pointnet2.group_points_grad_wrapper(B, C, N, npoint, nsample, grad_out_data, idx, grad_features.data)
        return grad_features, None


grouping_operation = GroupingOperation.apply


@torch.no_grad()
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


@torch.no_grad()
def ball_query_dilated(radius_in: float, radius_out: float, nsample: int, xyz: torch.Tensor, new_xyz: torch.Tensor):
    """
    :param radius_in: float, radius of the inner balls
    :param radius_out: float, radius of the outer balls
    :param nsample: int, maximum number of features in the balls 查询点数上限（多余的都不记录）
    :param xyz: (B, N, 3) xyz coordinates of the features
    :param new_xyz: (B, npoint, 3) centers of the ball query
    :return:
        idx_cnt: (B, npoint) tensor with the number of grouped points for each ball query　每个目标点的查询点数,共npoint个
        idx: (B, npoint, nsample) tensor with the indicies of the features that form the query balls
    """
    assert new_xyz.is_contiguous()
    assert xyz.is_contiguous()

    B, N, _ = xyz.size()
    npoint = new_xyz.size(1)
    idx_cnt = torch.cuda.IntTensor(B, npoint).zero_()
    idx = torch.cuda.IntTensor(B, npoint, nsample).zero_()

    pointnet2.ball_query_dilated_wrapper(B, N, npoint, radius_in, radius_out, nsample, new_xyz, xyz, idx_cnt, idx)
    # print('--------')
    # print('dilated')
    # print(B, N, npoint, radius_in, radius_out, nsample, idx_cnt)

    return idx_cnt, idx


class QueryAndGroup(nn.Module):
    def __init__(self, radius: float, nsample: int, use_xyz: bool = True):
        """
        :param radius: float, radius of ball
        :param nsample: int, maximum number of features to gather in the ball
        :param use_xyz:
        """
        super().__init__()
        self.radius, self.nsample, self.use_xyz = radius, nsample, use_xyz

    def forward(self, xyz: torch.Tensor, new_xyz: torch.Tensor, features: torch.Tensor = None):
        """
        :param xyz: (B, N, 3) xyz coordinates of the features
        :param new_xyz: (B, npoint, 3) centroids
        :param features: (B, C, N) descriptors of the features
        :return:
            idx_cnt: (B, npoint) tensor with the number of grouped points for each ball query
            new_features: (B, 3 + C, npoint, nsample)
        """
        idx_cnt, idx = ball_query(self.radius, self.nsample, xyz, new_xyz)
        xyz_trans = xyz.transpose(1, 2).contiguous()
        grouped_xyz = grouping_operation(xyz_trans, idx)  # (B, 3, npoint, nsample)
        grouped_xyz -= new_xyz.transpose(1, 2).unsqueeze(-1)

        if features is not None:
            grouped_features = grouping_operation(features, idx)
            if self.use_xyz:
                new_features = torch.cat([grouped_xyz, grouped_features], dim=1)  # (B, C + 3, npoint, nsample)
            else:
                new_features = grouped_features
        else:
            assert self.use_xyz, "Cannot have not features and not use xyz as a feature!"
            new_features = grouped_xyz

        return idx_cnt, new_features


class QueryAndGroupDilated(nn.Module):
    def __init__(self, radius_in: float, radius_out: float, nsample: int, use_xyz: bool = True):
        """
        :param radius_in: float, radius of inner ball
        :param radius_out: float, radius of outer ball
        :param nsample: int, maximum number of features to gather in the ball
        :param use_xyz:
        """
        super().__init__()
        self.radius_in, self.radius_out, self.nsample, self.use_xyz = radius_in, radius_out, nsample, use_xyz

    def forward(self, xyz: torch.Tensor, new_xyz: torch.Tensor, features: torch.Tensor = None):
        """
        :param xyz: (B, N, 3) xyz coordinates of the features
        :param new_xyz: (B, npoint, 3) centroids
        :param features: (B, C, N) descriptors of the features
        :return:
            new_features: (B, 3 + C, npoint, nsample)
            idx_cnt: (B, npoint) tensor with the number of grouped points for each ball query
        """
        idx_cnt, idx = ball_query_dilated(self.radius_in, self.radius_out, self.nsample, xyz, new_xyz)
        xyz_trans = xyz.transpose(1, 2).contiguous()
        grouped_xyz = grouping_operation(xyz_trans, idx)  # (B, 3, npoint, nsample)
        grouped_xyz -= new_xyz.transpose(1, 2).unsqueeze(-1)

        if features is not None:
            grouped_features = grouping_operation(features, idx)
            if self.use_xyz:
                new_features = torch.cat([grouped_xyz, grouped_features], dim=1)  # (B, C + 3, npoint, nsample)
            else:
                new_features = grouped_features
        else:
            assert self.use_xyz, "Cannot have not features and not use xyz as a feature!"
            new_features = grouped_xyz

        return idx_cnt, new_features


class GroupAll(nn.Module):
    def __init__(self, use_xyz: bool = True):
        super().__init__()
        self.use_xyz = use_xyz

    def forward(self, xyz: torch.Tensor, new_xyz: torch.Tensor, features: torch.Tensor = None):
        """
        :param xyz: (B, N, 3) xyz coordinates of the features
        :param new_xyz: ignored
        :param features: (B, C, N) descriptors of the features
        :return:
            idx_cnt: (B, 1)
            new_features: (B, C + 3, 1, N)
        """
        grouped_xyz = xyz.transpose(1, 2).unsqueeze(2)
        if features is not None:
            grouped_features = features.unsqueeze(2)
            if self.use_xyz:
                new_features = torch.cat([grouped_xyz, grouped_features], dim=1)  # (B, 3 + C, 1, N)
            else:
                new_features = grouped_features
        else:
            new_features = grouped_xyz
        
        idx_cnt = new_features.new_ones(new_features.size(0), 1)
        return idx_cnt, new_features
