# YOLO (You only look once) Object detection

Goal:
1. give yuumi bot eyes

Plan:
1. Can we train the object detection to see if our teammates are low on health
   1. By using a webcam pointing at the monitor and sending live feed to YOLO
   2. Once the low health status is detected
   3. Can we trigger the controller to press the heal button via localhost web server or something else
2. Getting training data:
   1. I can get training data from stream and youtube videos

Aside:
1. Can we have an list of champion icons of ADC champions for yuumi to auto detach onto. 
2. For Webcam, change cap = cv2.VideoCapture('resources/test.mp4') to cap = cv2.VideoCapture(0)
3. The higher the accuracy the slower the fps 

Credits:
1. [Python: Real Time Object Detection (Image, Webcam, Video files) with Yolov3 and OpenCV
](https://www.youtube.com/watch?v=1LCb1PVqzeY)