export CUDA_VISIBLE_DEVICES=0

python3 tools/train.py configs/fcn/fcn_r50-d8_4xb2-google_france.py --work-dir /home/ad084/ad084_media/mmsegmentation/outputs/GGE-France/FCN-GFr-WD-AA-RN50-last-test --resume