#!/bin/bash
python /home/ubuntu/caffe_ssd/scripts/create_annoset.py --anno-type detection --label-map-file /home/ubuntu/caffe_ssd/data/face_data/labelmap_face.prototxt --min-dim 0 --max-dim 0 --resize-width 0 --resize-height 0 --check-label --label-type txt --backend lmdb --encode-type jpg --encoded --shuffle --root /home/ubuntu/caffe_ssd/data/face_data --listfile /home/ubuntu/caffe_ssd/data/face_data/wider_all_data.txt --outdir /home/ubuntu/caffe_ssd/data/face_data/wider_trainval_lmdb --exampledir /home/ubuntu/caffe_ssd/data/face_data/wider_all


#    --label-map-file /home/ubuntu/caffe_ssd/data/face_data/labelmap_face.prototxt    \
#    --min-dim 0 --max-dim 0   \
#    --resize-width 0 --resize-height 0 \
#    --check-label \
#    --label-type txt --backend lmdb \
#    --encode-type jpg --encoded \
#    	--shuffle \
#    --root /home/ubuntu/caffe_ssd/data/face_data \
#    --listfile /home/ubuntu/caffe_ssd/data/face_data/wider_all_data.txt \
#    --outdir /home/ubuntu/caffe_ssd/data/face_data/wider_train_lmdb \
#    --exampledir /home/ubuntu/caffe_ssd/data/face_data/wider_all
