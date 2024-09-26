#!/bin/sh

cd $(dirname $0)

# wget -nc https://pjreddie.com/media/files/yolov3-tiny.weights
# wget -nc https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3-tiny.cfg
# wget -nc https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names

wget -nc https://github.com/pjreddie/darknet/raw/master/data/dog.jpg
wget -nc https://github.com/pjreddie/darknet/raw/master/data/eagle.jpg
wget -nc https://github.com/pjreddie/darknet/raw/master/data/giraffe.jpg

# node index.js
