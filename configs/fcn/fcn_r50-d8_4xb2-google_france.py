_base_ = [
    '../_base_/models/fcn_r50-d8-2-classes.py', '../_base_/datasets/google_france.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40_epochs_google_france.py'
]
crop_size = (380, 380)
data_preprocessor = dict(size=crop_size)
model = dict(data_preprocessor=data_preprocessor)