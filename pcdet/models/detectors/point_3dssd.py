import torch
import time
from .detector3d_template import Detector3DTemplate
from ...ops.iou3d_nms import iou3d_nms_utils
from ...ops.roiaware_pool3d import roiaware_pool3d_utils
from pcdet.utils.density_calculation import cnt_ball_points

class Point3DSSD(Detector3DTemplate):
    def __init__(self, model_cfg, num_class, dataset):
        super().__init__(model_cfg=model_cfg, num_class=num_class, dataset=dataset)
        self.module_list = self.build_networks()
        self.time_list= []

    def forward(self, batch_dict):
        # print(batch_dict['points'].shape)  #torch.Size([16384, 5])
        # print(batch_dict['frame_id'])
        time1 = time.time()
        density_idx_cnt = cnt_ball_points(radius=0.5, max_nsample=500, points=batch_dict['points'])
        # print(density_idx_cnt.size())
        # density_idx_cnt = torch.zeros([1,16384])
        time2 = time.time()
        self.time_list.append(time2-time1)

        density_idx_cnt = density_idx_cnt.transpose(1, 0).contiguous()
        # print(idx_cnt.type) tensor
        batch_dict['density'] = density_idx_cnt
        # print(batch_dict['density'].shape)
        # print(batch_dict['points'].shape)
        for cur_module in self.module_list:
            # print('cur_module',cur_module)

            time1 = time.time()
            batch_dict = cur_module(batch_dict)
            time2 = time.time()
            self.time_list.append(time2-time1)

        if self.training:
            loss, tb_dict, disp_dict = self.get_training_loss()

            ret_dict = {
                'loss': loss
            }
            return ret_dict, tb_dict, disp_dict
        else:
            time1 = time.time()
            pred_dicts, recall_dicts = self.post_processing(batch_dict)
            time2 = time.time()
            self.time_list.append(time2-time1)
            recall_dicts['time_density_calculation'] = self.time_list[0]
            recall_dicts['time_PointNet2FSMSG'] = self.time_list[1]
            recall_dicts['time_PointHeadVote'] = self.time_list[2]
            recall_dicts['time_post_processing'] = self.time_list[3]
            return pred_dicts, recall_dicts

    def get_training_loss(self):
        disp_dict = {}
        loss_point, tb_dict = self.point_head.get_loss()

        loss = loss_point
        return loss, tb_dict, disp_dict
    
    def init_recall_record(self, metric, **kwargs):
        # initialize gt_num for all classes
        for cur_cls in range(len(self.class_names)):
            metric['gt_num[%s]' % self.class_names[cur_cls]] = 0

        # initialize statistics of all sampling segments
        npoint_list = self.model_cfg.BACKBONE_3D.SA_CONFIG.NPOINT_LIST
        for cur_layer in range(len(npoint_list)):
            for cur_seg in range(len(npoint_list[cur_layer])):
                metric['positive_point_L%dS%d' % (cur_layer, cur_seg)] = 0
                metric['recall_point_L%dS%d' % (cur_layer, cur_seg)] = 0
                metric['positive_num_point_in_far_boxes_L%dS%d' % (cur_layer, cur_seg)] = 0
                metric['positive_num_point_in_mid_boxes_L%dS%d' % (cur_layer, cur_seg)] = 0
                metric['positive_num_point_in_close_boxes_L%dS%d' % (cur_layer, cur_seg)] = 0
                metric['recall_gt_box_of_far_boxes_L%dS%d' % (cur_layer, cur_seg)] = 0
                metric['recall_gt_box_of_mid_boxes_L%dS%d' % (cur_layer, cur_seg)] = 0
                metric['recall_gt_box_of_close_boxes_L%dS%d' % (cur_layer, cur_seg)] = 0
                for cur_cls in range(self.num_class):
                    metric['recall_point_L%dS%d[%s]' \
                        % (cur_layer, cur_seg, self.class_names[cur_cls])] = 0

        # initialize statistics of the vote layer
        metric['positive_point_candidate'] = 0
        metric['recall_point_candidate'] = 0
        metric['positive_point_vote'] = 0
        metric['recall_point_vote'] = 0

        for cur_cls in range(len(self.class_names)):
            metric['recall_point_candidate[%s]' % self.class_names[cur_cls]] = 0
            metric['recall_point_vote[%s]' % self.class_names[cur_cls]] = 0

        # record processing time
        metric['time_density_calculation'] = 0
        metric['time_PointNet2FSMSG'] = 0
        metric['time_PointHeadVote'] = 0
        metric['time_post_processing'] = 0

    def generate_recall_record(self, box_preds, recall_dict, batch_index, data_dict=None, thresh_list=None):
        if 'gt_boxes' not in data_dict:
            return recall_dict

        # point_coords format: (N1 + N2 + N3 + ..., 4) [bs_idx, x, y, z]
        point_list = data_dict['point_coords_list']  # ignore raw point input
        npoint_list = self.model_cfg.BACKBONE_3D.SA_CONFIG.NPOINT_LIST
        assert len(point_list) == len(npoint_list)

        cur_points_list = []
        for cur_layer in range(npoint_list.__len__()):
            cur_points = point_list[cur_layer]
            bs_idx = cur_points[:, 0]
            bs_mask = (bs_idx == batch_index)
            cur_points = cur_points[bs_mask][:, 1:4]
            cur_points_list.append(cur_points.split(npoint_list[cur_layer], dim=0))

        base_points = data_dict['point_candidate_coords']
        vote_points = data_dict['point_vote_coords']
        bs_idx = base_points[:, 0]
        bs_mask = (bs_idx == batch_index)
        base_points = base_points[bs_mask][:, 1:4]
        vote_points = vote_points[bs_mask][:, 1:4]

        rois = data_dict['rois'][batch_index] if 'rois' in data_dict else None
        gt_boxes = data_dict['gt_boxes'][batch_index]

        # initialize recall_dict
        if recall_dict.__len__() == 0:
            recall_dict = {'gt_num': 0}
            for cur_thresh in thresh_list:
                recall_dict['recall_roi_%s' % (str(cur_thresh))] = 0
                recall_dict['recall_rcnn_%s' % (str(cur_thresh))] = 0
            self.init_recall_record(recall_dict)  # init customized statistics

        cur_gt = gt_boxes
        k = cur_gt.__len__() - 1
        while k > 0 and cur_gt[k].sum() == 0:
            k -= 1
        cur_gt = cur_gt[:k + 1]

        if cur_gt.shape[0] > 0:
            # backbone
            for cur_layer in range(len(npoint_list)):
                for cur_seg in range(len(npoint_list[cur_layer])):
                    points_in_far_boxes = 0  # (50, :)
                    points_in_mid_boxes = 0  # (20,50)
                    points_in_close_boxes = 0  # (0, 20)
                    close_boxes = 0
                    mid_boxes = 0
                    far_boxes =0

                    box_idxs_of_pts = roiaware_pool3d_utils.points_in_boxes_gpu(
                        cur_points_list[cur_layer][cur_seg].unsqueeze(dim=0),
                        cur_gt[None, :, :7].contiguous()
                    ).long().squeeze(dim=0)
                    box_fg_flag = (box_idxs_of_pts >= 0)
                    recall_dict['positive_point_L%dS%d' % (cur_layer, cur_seg)] += box_fg_flag.long().sum().item()
                    fg_points_num = box_fg_flag.long().sum().item()

                    box_recalled = box_idxs_of_pts[box_fg_flag].unique()
                    recall_dict['recall_point_L%dS%d' % (cur_layer, cur_seg)] += box_recalled.size(0)
                    box_recalled_cls = cur_gt[box_recalled, -1]
                    for cur_cls in range(self.num_class):
                        recall_dict['recall_point_L%dS%d[%s]' % (cur_layer, cur_seg, self.class_names[cur_cls])] += \
                            (box_recalled_cls == (cur_cls + 1)).sum().item()

                    num_of_gts = box_idxs_of_pts.max()
                    for i in range(num_of_gts+1):
                        flag_of_current_gt = (box_idxs_of_pts == i)
                        point_num_of_current_gt = flag_of_current_gt.long().sum().item()
                        x = cur_gt[i][0]
                        y = cur_gt[i][1]
                        distance_of_cur_gt =  x*x +y*y
                        if distance_of_cur_gt < 400:
                            recall_dict['positive_num_point_in_close_boxes_L%dS%d' % (cur_layer, cur_seg)] += point_num_of_current_gt
                            points_in_close_boxes += point_num_of_current_gt
                        elif distance_of_cur_gt < 2500:
                            recall_dict['positive_num_point_in_mid_boxes_L%dS%d' % (cur_layer, cur_seg)] += point_num_of_current_gt
                            points_in_mid_boxes += point_num_of_current_gt
                        else:
                            recall_dict['positive_num_point_in_far_boxes_L%dS%d' % (cur_layer, cur_seg)] += point_num_of_current_gt
                            points_in_far_boxes += point_num_of_current_gt

                    for i in range(num_of_gts+1):
                        flag_of_current_gt = (box_idxs_of_pts == i)
                        point_num_of_current_gt = flag_of_current_gt.long().sum().item()
                        if point_num_of_current_gt >0:
                            x = cur_gt[i][0]
                            y = cur_gt[i][1]
                            distance_of_cur_gt =  x*x +y*y
                            if distance_of_cur_gt < 400:
                                recall_dict['recall_gt_box_of_close_boxes_L%dS%d' % (cur_layer, cur_seg)] += 1
                                close_boxes += 1
                            elif distance_of_cur_gt < 2500:
                                recall_dict['recall_gt_box_of_mid_boxes_L%dS%d' % (cur_layer, cur_seg)] += 1
                                mid_boxes += 1
                            else:
                                recall_dict['recall_gt_box_of_far_boxes_L%dS%d' % (cur_layer, cur_seg)] += 1
                                far_boxes += 1

                        # print(cur_layer, cur_seg, i, point_num_of_current_gt, close_boxes, mid_boxes, far_boxes)


                    # all_points_num = points_in_close_boxes+ points_in_mid_boxes+ points_in_far_boxes,
                    # print(num_of_gts, points_in_close_boxes, points_in_mid_boxes, points_in_far_boxes,all_points_num,fg_points_num)
                    # a = 'positive_num_point_in_close_boxes_L%dS%d' % (cur_layer, cur_seg)
                    # print(a,recall_dict['positive_num_point_in_close_boxes_L%dS%d' % (cur_layer, cur_seg)])
                    # b = 'positive_num_point_in_mid_boxes_L%dS%d' % (cur_layer, cur_seg)
                    # print(b,recall_dict['positive_num_point_in_mid_boxes_L%dS%d' % (cur_layer, cur_seg)])
                    # c = 'positive_num_point_in_far_boxes_L%dS%d' % (cur_layer, cur_seg)
                    # print(c,recall_dict['positive_num_point_in_far_boxes_L%dS%d' % (cur_layer, cur_seg)])
                    # d= 'recall_point_L%dS%d' % (cur_layer, cur_seg)
                    # print(d, recall_dict['recall_point_L%dS%d' % (cur_layer, cur_seg)])
                    # print('******')

            # candidate points
            box_idxs_of_pts = roiaware_pool3d_utils.points_in_boxes_gpu(
                base_points.unsqueeze(dim=0), cur_gt[None, :, :7]
            ).long().squeeze(dim=0)
            box_fg_flag = (box_idxs_of_pts >= 0)
            recall_dict['positive_point_candidate'] += box_fg_flag.long().sum().item()
            box_recalled = box_idxs_of_pts[box_fg_flag].unique()
            recall_dict['recall_point_candidate'] += box_recalled.size(0)

            box_recalled_cls = cur_gt[box_recalled, -1]
            for cur_cls in range(self.num_class):
                recall_dict['recall_point_candidate[%s]' % self.class_names[cur_cls]] += \
                    (box_recalled_cls == (cur_cls + 1)).sum().item()

            # vote points
            box_idxs_of_pts = roiaware_pool3d_utils.points_in_boxes_gpu(
                vote_points.unsqueeze(dim=0), cur_gt[None, :, :7]
            ).long().squeeze(dim=0)
            box_fg_flag = (box_idxs_of_pts >= 0)
            recall_dict['positive_point_vote'] += box_fg_flag.long().sum().item()
            box_recalled = box_idxs_of_pts[box_fg_flag].unique()
            recall_dict['recall_point_vote'] += box_recalled.size(0)

            box_recalled_cls = cur_gt[box_recalled, -1]
            for cur_cls in range(self.num_class):
                recall_dict['recall_point_vote[%s]' % self.class_names[cur_cls]] += \
                    (box_recalled_cls == (cur_cls + 1)).sum().item()

            if box_preds.shape[0] > 0:
                iou3d_rcnn = iou3d_nms_utils.boxes_iou3d_gpu(box_preds[:, 0:7], cur_gt[:, 0:7])
            else:
                iou3d_rcnn = torch.zeros((0, cur_gt.shape[0]))

            if rois is not None:
                iou3d_roi = iou3d_nms_utils.boxes_iou3d_gpu(rois[:, 0:7], cur_gt[:, 0:7])

            for cur_thresh in thresh_list:
                if iou3d_rcnn.shape[0] == 0:
                    recall_dict['recall_rcnn_%s' % str(cur_thresh)] += 0
                else:
                    rcnn_recalled = (iou3d_rcnn.max(dim=0)[0] > cur_thresh).sum().item()
                    recall_dict['recall_rcnn_%s' % str(cur_thresh)] += rcnn_recalled
                if rois is not None:
                    roi_recalled = (iou3d_roi.max(dim=0)[0] > cur_thresh).sum().item()
                    recall_dict['recall_roi_%s' % str(cur_thresh)] += roi_recalled

            cur_gt_class = cur_gt[:, -1]
            for cur_cls in range(self.num_class):
                cur_cls_gt_num = (cur_gt_class == cur_cls + 1).sum().item()
                recall_dict['gt_num'] += cur_cls_gt_num
                recall_dict['gt_num[%s]' % self.class_names[cur_cls]] += cur_cls_gt_num

        # record processing time
        # recall_dict['time_density_calculation'] = self.time_list[0]
        # recall_dict['time_PointNet2FSMSG'] = self.time_list[1]
        # recall_dict['time_PointHeadVote'] = self.time_list[2]
        # recall_dict['time_post_processing'] = self.time_list[3]


        return recall_dict
    
    def disp_recall_record(self, metric, logger, sample_num, **kwargs):

        gt_num = metric['gt_num']
        gt_num_cls = [metric['gt_num[%s]' % cur_cls] for cur_cls in self.class_names]

        # backbone
        for k in metric.keys():
            if 'positive_point_' in k:  # count the number of positive points
                # cur_positive_point = metric[k] / sample_num  # sample num 3769
                cur_positive_point = metric[k]   # sample num 3769
                logger.info(k + (': %d' % cur_positive_point))
            elif 'positive_num_point_in_far_boxes_' in k:  # count the number of positive points
                cur_positive_point = metric[k]
                logger.info(k + (': %d' % cur_positive_point))
            elif 'positive_num_point_in_mid_boxes_' in k:  # count the number of positive points
                cur_positive_point = metric[k]
                logger.info(k + (': %d' % cur_positive_point))
            elif 'positive_num_point_in_close_boxes_' in k:  # count the number of positive points
                cur_positive_point = metric[k]
                logger.info(k + (': %d' % cur_positive_point))
            elif 'recall_gt_box_of_far_boxes_' in k:  # count the number of positive points
                cur_recall_point = metric[k]
                logger.info(k + (': %d' % cur_recall_point))
            elif 'recall_gt_box_of_mid_boxes_' in k:  # count the number of positive points
                cur_recall_point = metric[k]
                logger.info(k + (': %d' % cur_recall_point))
            elif 'recall_gt_box_of_close_boxes_' in k:  # count the number of positive points
                cur_recall_point = metric[k]
                logger.info(k + (': %d' % cur_recall_point))

            elif 'recall_point_' in k and not any(cur_cls in k for cur_cls in self.class_names):
                cur_recall_point = metric[k] / max(gt_num, 1)
                logger.info(k + (': %f' % cur_recall_point))
                for cur_cls in range(len(self.class_names)):
                    cur_recall_point_cls = metric[k + '[%s]' % self.class_names[cur_cls]] / max(gt_num_cls[cur_cls], 1)
                    logger.info('\t- ' + self.class_names[cur_cls] + ': %f' % cur_recall_point_cls)

        # candidate points
        positive_point_candidate = metric['positive_point_candidate'] / sample_num
        logger.info('positive_point_candidate: %f' % positive_point_candidate)
        recall_point_candidate = metric['recall_point_candidate'] / max(gt_num, 1)
        logger.info('recall_point_candidate: %f' % recall_point_candidate)
        for cur_cls in range(len(self.class_names)):
            cur_recall_point_cls = metric['recall_point_candidate' + '[%s]' % self.class_names[cur_cls]] / max(gt_num_cls[cur_cls], 1)
            logger.info('\t- ' + self.class_names[cur_cls] + ': %f' % cur_recall_point_cls)

        # vote points
        positive_point_vote = metric['positive_point_vote'] / sample_num
        logger.info('positive_point_vote: %f' % positive_point_vote)
        recall_point_vote = metric['recall_point_vote'] / max(gt_num, 1)
        logger.info('recall_point_vote: %f' % recall_point_vote)
        for cur_cls in range(len(self.class_names)):
            cur_recall_point_cls = metric['recall_point_vote' + '[%s]' % self.class_names[cur_cls]] / max(gt_num_cls[cur_cls], 1)
            logger.info('\t- ' + self.class_names[cur_cls] + ': %f' % cur_recall_point_cls)

        # record processing time
        temp_1 = metric['time_density_calculation']/3769
        logger.info('time_density_calculation: %f' % temp_1)
        print('metric[time_density_calculation]',metric['time_density_calculation'],temp_1)

        temp_2 = metric['time_PointNet2FSMSG']/3769
        logger.info('time_PointNet2FSMSG: %f' % temp_2)
        print('metric[time_PointNet2FSMSG]',metric['time_PointNet2FSMSG'],temp_2)

        temp_3 = metric['time_PointHeadVote']/3769
        logger.info('time_PointHeadVote: %f' % temp_3)
        print('metric[time_PointHeadVote]',metric['time_PointHeadVote'],temp_3)

        temp_4 = metric['time_post_processing']/3769
        logger.info('time_post_processing: %f' % temp_4)
        print('metric[time_post_processing]',metric['time_post_processing'],temp_4)
