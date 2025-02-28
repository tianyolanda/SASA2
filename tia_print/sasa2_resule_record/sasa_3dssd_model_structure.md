Point3DSSD
├── backbone_3d (PointNet2FSMSG)
│   ├── SA_modules (ModuleList)
│   │   ├── PointnetSAModuleFSMSG 1
│   │   │   ├── groupers (QueryAndGroupDilated)
│   │   │   ├── mlps (Sequential: Conv2d + BN + ReLU)
│   │   │   ├── aggregation_mlp (Sequential: Conv1d + BN + ReLU)
│   │   │   └── confidence_mlp (Sequential: Conv1d + BN + ReLU + Conv1d)
│   │   ├── PointnetSAModuleFSMSG 2
│   │   └── PointnetSAModuleFSMSG 3
│   └── ...
├── point_head (PointHeadVote)
│   ├── vote_layers (Sequential: Conv1d + BN + ReLU + Conv1d)
│   ├── SA_module (PointnetSAModuleFSMSG)
│   ├── shared_fc_layer (Sequential: Conv1d + BN + ReLU)
│   ├── cls_layers (Sequential: Conv1d + BN + ReLU + Conv1d)
│   └── reg_layers (Sequential: Conv1d + BN + ReLU + Conv1d)
└── ...

Point3DSSD(
  (vfe): None
  (backbone_3d): PointNet2FSMSG(
    (SA_modules): ModuleList(
      (0): PointnetSAModuleFSMSG(
        (groupers): ModuleList(
          (0): QueryAndGroupDilated()
          (1): QueryAndGroupDilated()
          (2): QueryAndGroupDilated()
        )
        (mlps): ModuleList(
          (0): Sequential(
            (0): Conv2d(4, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (1): BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (2): ReLU()
            (3): Conv2d(16, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (4): BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (5): ReLU()
            (6): Conv2d(16, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (7): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (8): ReLU()
          )
          (1): Sequential(
            (0): Conv2d(4, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (1): BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (2): ReLU()
            (3): Conv2d(16, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (4): BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (5): ReLU()
            (6): Conv2d(16, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (7): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (8): ReLU()
          )
          (2): Sequential(
            (0): Conv2d(4, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (1): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (2): ReLU()
            (3): Conv2d(32, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (4): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (5): ReLU()
            (6): Conv2d(32, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (7): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (8): ReLU()
          )
        )
        (aggregation_mlp): Sequential(
          (0): Conv1d(128, 64, kernel_size=(1,), stride=(1,), bias=False)
          (1): BatchNorm1d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          (2): ReLU()
        )
        (confidence_mlp): Sequential(
          (0): Conv1d(64, 32, kernel_size=(1,), stride=(1,), bias=False)
          (1): BatchNorm1d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          (2): ReLU()
          (3): Conv1d(32, 1, kernel_size=(1,), stride=(1,))
        )
      )
      (1): PointnetSAModuleFSMSG(
        (groupers): ModuleList(
          (0): QueryAndGroupDilated()
          (1): QueryAndGroupDilated()
          (2): QueryAndGroupDilated()
        )
        (mlps): ModuleList(
          (0): Sequential(
            (0): Conv2d(67, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (1): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (2): ReLU()
            (3): Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (4): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (5): ReLU()
            (6): Conv2d(64, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (7): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (8): ReLU()
          )
          (1): Sequential(
            (0): Conv2d(67, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (1): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (2): ReLU()
            (3): Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (4): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (5): ReLU()
            (6): Conv2d(64, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (7): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (8): ReLU()
          )
          (2): Sequential(
            (0): Conv2d(67, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (1): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (2): ReLU()
            (3): Conv2d(64, 96, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (4): BatchNorm2d(96, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (5): ReLU()
            (6): Conv2d(96, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (7): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (8): ReLU()
          )
        )
        (aggregation_mlp): Sequential(
          (0): Conv1d(384, 128, kernel_size=(1,), stride=(1,), bias=False)
          (1): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          (2): ReLU()
        )
        (confidence_mlp): Sequential(
          (0): Conv1d(128, 64, kernel_size=(1,), stride=(1,), bias=False)
          (1): BatchNorm1d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          (2): ReLU()
          (3): Conv1d(64, 1, kernel_size=(1,), stride=(1,))
        )
      )
      (2): PointnetSAModuleFSMSG(
        (groupers): ModuleList(
          (0): QueryAndGroupDilated()
          (1): QueryAndGroupDilated()
          (2): QueryAndGroupDilated()
        )
        (mlps): ModuleList(
          (0): Sequential(
            (0): Conv2d(131, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (1): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (2): ReLU()
            (3): Conv2d(128, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (4): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (5): ReLU()
            (6): Conv2d(128, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (7): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (8): ReLU()
          )
          (1): Sequential(
            (0): Conv2d(131, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (1): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (2): ReLU()
            (3): Conv2d(128, 196, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (4): BatchNorm2d(196, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (5): ReLU()
            (6): Conv2d(196, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (7): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (8): ReLU()
          )
          (2): Sequential(
            (0): Conv2d(131, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (1): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (2): ReLU()
            (3): Conv2d(128, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (4): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (5): ReLU()
            (6): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
            (7): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
            (8): ReLU()
          )
        )
        (aggregation_mlp): Sequential(
          (0): Conv1d(768, 256, kernel_size=(1,), stride=(1,), bias=False)
          (1): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          (2): ReLU()
        )
      )
    )
  )
  (map_to_bev_module): None
  (pfe): None
  (backbone_2d): None
  (dense_head): None
  (point_head): PointHeadVote(
    (cls_loss_func): WeightedBinaryCrossEntropyLoss()
    (reg_loss_func): WeightedSmoothL1Loss()
    (loss_point_sasa): PointSASALoss(
      (loss_func): WeightedBinaryCrossEntropyLoss()
    )
    (vote_layers): Sequential(
      (0): Conv1d(256, 128, kernel_size=(1,), stride=(1,), bias=False)
      (1): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (2): ReLU()
      (3): Conv1d(128, 3, kernel_size=(1,), stride=(1,))
    )
    (SA_module): PointnetSAModuleFSMSG(
      (groupers): ModuleList(
        (0): QueryAndGroup()
        (1): QueryAndGroup()
      )
      (mlps): ModuleList(
        (0): Sequential(
          (0): Conv2d(259, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (1): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          (2): ReLU()
          (3): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (4): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          (5): ReLU()
          (6): Conv2d(256, 512, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (7): BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          (8): ReLU()
        )
        (1): Sequential(
          (0): Conv2d(259, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (1): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          (2): ReLU()
          (3): Conv2d(256, 512, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (4): BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          (5): ReLU()
          (6): Conv2d(512, 1024, kernel_size=(1, 1), stride=(1, 1), bias=False)
          (7): BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          (8): ReLU()
        )
      )
    )
    (shared_fc_layer): Sequential(
      (0): Conv1d(1536, 512, kernel_size=(1,), stride=(1,), bias=False)
      (1): BatchNorm1d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (2): ReLU()
      (3): Conv1d(512, 256, kernel_size=(1,), stride=(1,), bias=False)
      (4): BatchNorm1d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (5): ReLU()
    )
    (cls_layers): Sequential(
      (0): Conv1d(256, 128, kernel_size=(1,), stride=(1,), bias=False)
      (1): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (2): ReLU()
      (3): Conv1d(128, 1, kernel_size=(1,), stride=(1,))
    )
    (reg_layers): Sequential(
      (0): Conv1d(256, 128, kernel_size=(1,), stride=(1,), bias=False)
      (1): BatchNorm1d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (2): ReLU()
      (3): Conv1d(128, 30, kernel_size=(1,), stride=(1,))
    )
  )
  (roi_head): None
)
