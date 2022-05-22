#!/bin/bash

MODEL_NAME=ppyolo_mobilenet_v3_small
MODEL_TYPE=1 # 1 combined paddle fluid model
LABEL_NAME=labels/steel_list
IMAGE_NAME=steel_images/47.jpg
OUTPUT_IMAGE=47_result.jpg

TARGET_ARCH_ABI=armv7hf
if [ -n "$1" ]; then
    TARGET_ARCH_ABI=$1
fi

LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/plite/lib ./yolov3-test ${MODEL_NAME} ${MODEL_TYPE} ${LABEL_NAME} ${IMAGE_NAME} ${OUTPUT_IMAGE}

