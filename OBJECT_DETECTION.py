# https://www.youtube.com/watch?v=1LCb1PVqzeY

import cv2
import numpy as np

net = cv2.dnn.readNet('yolov2-tiny.weights', 'yolov3.cfg')
classes = []
with open('coco.names', 'r') as f:
    classes = f.read().splitlines()

img = cv2.imread('image.png')
height, width, _ = img.shape

# prepare the image blob

# normalizaing the image with 1/255
# end result is black and white squares with
blob = cv2.dnn.blobFromImage(
    img, 1/255, (416, 416), (0, 0, 0), swapRB=True, crop=False)

for b in blob:
    for n, img_blob in enumerate(b):
        cv2.imshow(str(n), img_blob)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
