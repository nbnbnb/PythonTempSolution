import cv2
import numpy as np

# 错误方式  
#green=np.uint8([0,255,0])
#(scn == 3 || scn == 4) && (depth == CV_8U || depth == CV_32F) in function cv::cvtColor

#正确方式
green=np.uint8([[[0,255,0]]])

hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)

print(hsv_green)