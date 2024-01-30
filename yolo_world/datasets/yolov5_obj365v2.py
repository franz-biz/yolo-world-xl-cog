# Copyright (c) Tencent Inc. All rights reserved.
from mmdet.datasets import Objects365V2Dataset
from mmyolo.registry import DATASETS

from .utils import RobustBatchShapePolicyDataset


@DATASETS.register_module()
class YOLOv5Objects365V2Dataset(RobustBatchShapePolicyDataset,
                                Objects365V2Dataset):
    """Dataset for YOLOv5 VOC Dataset.

    We only add `BatchShapePolicy` function compared with Objects365V1Dataset.
    See `mmyolo/datasets/utils.py#BatchShapePolicy` for details
    """
    pass
