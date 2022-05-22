import imgaug as ia
import imgaug.augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
import cv2
import os
import ast
import numpy as np
import shutil
import xml.etree.ElementTree as ET

in_pics = r'dataset/voc/VOCdevkit/VOC2021/JPEGImages/'
in_annotations = r'dataset/voc/VOCdevkit/VOC2021/Annotations/'
out_pics = r"dataset/voc/VOCdevkit/VOC2021/JPEGImages/"
out_annotations = r"dataset/voc/VOCdevkit/VOC2021/Annotations/"


def aug_pts_to_dict(bbs_aug):
    boxes = {}
    dict_idx = 1
    for i in range(len(bbs_aug)):
        boxes[dict_idx] = {}
        boxes[dict_idx]["xmin"] = bbs_aug[i].x1
        boxes[dict_idx]["xmax"] = bbs_aug[i].x2
        boxes[dict_idx]["ymin"] = bbs_aug[i].y1
        boxes[dict_idx]["ymax"] = bbs_aug[i].y2
        dict_idx += 1
    return boxes


def get_bbs(xml_file):
    # Retrieve the bounding boxes for this image
    tree = ET.parse(xml_file)
    root = tree.getroot()
    bbs = []
    for child in root:
        if child.tag == 'object':
            for c in child:
                if c.tag == 'bndbox':
                    xmin = int(c[0].text)
                    ymin = int(c[1].text)
                    xmax = int(c[2].text)
                    ymax = int(c[3].text)

                    bbs.append(BoundingBox(x1=xmin, y1=ymin, x2=xmax, y2=ymax))

    # Create the imgaug bounding box object to modify if necessary
    return BoundingBoxesOnImage(bbs, i.shape)


def write_new_files(name, op, image, bbs, apply_bbs_shift=True,
                    out_paths=[out_pics, out_annotations],
                    in_paths=[in_pics, in_annotations]):
    # Write the image
    cv2.imwrite(out_paths[0] + name + "_" + op + ".jpg", image)

    # Write the xml
    if apply_bbs_shift:
        shutil.copy(in_paths[1] + name + '.xml', out_paths[1] + name + '_' + op + '.xml')
        xml_file = out_paths[1] + name + '_' + op + '.xml'
        tree = ET.parse(xml_file)
        root = tree.getroot()

        boxes = aug_pts_to_dict(bbs)
        dict_key = 1
        for child in root:
            if child.tag == 'filename':
                child.text = name + "_" + op + ".jpg"

            if child.tag == 'object':
                for c in child:
                    if c.tag == 'bndbox':
                        c[0].text = str(int(boxes[dict_key]['xmin']))
                        c[1].text = str(int(boxes[dict_key]['ymin']))
                        c[2].text = str(int(boxes[dict_key]['xmax']))
                        c[3].text = str(int(boxes[dict_key]['ymax']))
                        dict_key += 1
        tree.write(xml_file, encoding='utf-8')

    else:
        shutil.copy(in_paths[1] + name + '.xml', out_paths[1] + name + '_' + op + '.xml')
        xml_file = out_paths[1] + name + '_' + op + '.xml'
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for child in root:
            if child.tag == 'filename':
                child.text = name + "_" + op + ".jpg"
        tree.write(xml_file, encoding='utf-8')


# Get the images
images_list = os.listdir(in_pics)  # should be the same as annotations

for img in images_list:
    print(img)
    name = img.split(".")[0]

    xml_file = name + '.xml'
    # Load imge for augment
    i = cv2.imread(in_pics + img)

    # Get bbs. Won't apply the transorms unless it's a spacial augment
    bbs_og = get_bbs(in_annotations + xml_file)

    # Rotating all images_list
    seq = iaa.Rot90(2)
    rot180, bbs = seq(image=i, bounding_boxes=bbs_og)
    write_new_files(name, 'rot180', rot180, bbs, True)

    # DARKENING IMAGE
    seq = iaa.Multiply((0.8, 1.2))
    darkened, _ = seq(image=i, bounding_boxes=bbs_og)
    write_new_files(name, 'darkened', darkened, _, False)

    seq = iaa.Fliplr(1)
    fliplr, bbs = seq(image=i, bounding_boxes=bbs_og)
    write_new_files(name, 'fliplr', fliplr, bbs, True)

    seq = iaa.Flipud(1)
    flipud, bbs = seq(image=i, bounding_boxes=bbs_og)
    write_new_files(name, 'flipud', flipud, bbs, True)

    # GREYSCALE IMAGE
    seq = iaa.color.ChangeColorspace("GRAY")
    grey, bbs = seq(image=i, bounding_boxes=bbs_og)
    write_new_files(name, 'grey', grey, _, False)

    seq = iaa.Rot90(2)
    darkened_rot180, bbs = seq(image=darkened, bounding_boxes=bbs_og)
    write_new_files(name, 'darkened_rot180', darkened_rot180, bbs, True)

    seq = iaa.Rot90(2)
    grey_rot180, bbs = seq(image=grey, bounding_boxes=bbs_og)
    write_new_files(name, 'grey_rot180', grey_rot180, bbs, True)

