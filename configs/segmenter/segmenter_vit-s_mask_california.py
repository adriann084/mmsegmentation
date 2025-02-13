_base_ = [
    '../_base_/models/segmenter_vit-b16_mask.py',
    '../_base_/datasets/california.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_40_epochs_california.py'
]
crop_size = (380, 380)
data_preprocessor = dict(size=crop_size)
checkpoint = 'https://download.openmmlab.com/mmsegmentation/v0.5/pretrain/segmenter/vit_small_p16_384_20220308-410f6037.pth'  # noqa

backbone_norm_cfg = dict(type='LN', eps=1e-6, requires_grad=True)
model = dict(
    data_preprocessor=data_preprocessor,
    pretrained=checkpoint,
    backbone=dict(
        img_size=(380, 380),
        embed_dims=384,
        num_heads=6,
    ),
    decode_head=dict(
        type='SegmenterMaskTransformerHead',
        in_channels=384,
        channels=384,
        num_classes=2,
        num_layers=2,
        num_heads=6,
        embed_dims=384,
        dropout_ratio=0.0,
        loss_decode=[dict(type='CrossEntropyLoss', loss_name='loss_ce', use_sigmoid=True, loss_weight=1.0),
                     dict(type='DiceLoss', loss_name='loss_dice', loss_weight=1.0)]))

optimizer = dict(lr=0.001, weight_decay=0.0)
optim_wrapper = dict(type='OptimWrapper', optimizer=optimizer)
train_dataloader = dict(
    # num_gpus: 8 -> batch_size: 8
    batch_size=2)
val_dataloader = dict(batch_size=2)
test_dataloader = dict(batch_size=2)
