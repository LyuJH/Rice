#!/bin/bash
MODEL_NAME=/opt/ssd_mobilenet_v1   # 上传后的模型路径
MODEL_TYPE=1 # 1 combined paddle fluid model
LABEL_NAME=labels/pascalvoc_label_list  # 训练模型的类别列表
IMAGE_NAME=images/dog.jpg   # 推理图片
OUTPUT_IMAGE=dog_result.jpg  # 推理后的输出图片

TARGET_ARCH_ABI=armv7hf
if [ -n "$1" ]; then
    TARGET_ARCH_ABI=$1
fi

LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/plite/lib ./ssd_detection ${MODEL_NAME} ${MODEL_TYPE} ${LABEL_NAME} ${IMAGE_NAME} ${OUTPUT_IMAGE}
