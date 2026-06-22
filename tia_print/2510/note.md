# nuscene v1.0-trainval


# train - 单GPU
python tools/train.py --cfg_file cfgs/nuscenes_models/3dssd.yaml




# train - 多GPU运行(out of memory)
sh scripts/dist_train2.sh tia_exp 2 --cfg_file /cfgs/nuscenes_models/3dssd.yaml


# make dataset v1.0-trainval

python -m pcdet.datasets.nuscenes.nuscenes_dataset --func create_nuscenes_infos --cfg_file tools/cfgs/dataset_configs/nuscenes_dataset.yaml --version v1.0-trainval