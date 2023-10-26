# Copyright (c) OpenMMLab. All rights reserved.
from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset


@DATASETS.register_module()
class CaliforniaDataset(BaseSegDataset):
    """California dataset.

    The ``img_suffix`` is fixed to '.png' and ``seg_map_suffix`` is
    fixed to '.png' for Cityscapes dataset.
    """
    METAINFO = dict(
        classes=('solar-pv', 'background'),
        palette=[[0, 0, 0], [255, 255, 255]])

    def __init__(self,
                 img_suffix='.png',
                 seg_map_suffix='.png',
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
