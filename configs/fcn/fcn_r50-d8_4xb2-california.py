_base_ = [
    '../_base_/models/fcn_r50-d8-2-classes-resnetV1c.py', '../_base_/datasets/california.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40_epochs_california.py'
]
crop_size = (380, 380)
data_preprocessor = dict(size=crop_size)
model = dict(data_preprocessor=data_preprocessor)