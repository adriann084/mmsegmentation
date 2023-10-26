_base_ = [
    '../_base_/models/fcn_r50-d8-2-classes-resnetV1c.py', '../_base_/datasets/google_ign.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_n_iterations_ign_france.py'
]
crop_size = (299, 299)
data_preprocessor = dict(size=crop_size)
model = dict(data_preprocessor=data_preprocessor)