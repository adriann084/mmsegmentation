_base_ = './fcn_r50-d8_4xb2-google_ign.py'
model = dict(
    pretrained='torchvision://resnet101',
    backbone=dict(type='ResNet', depth=101))