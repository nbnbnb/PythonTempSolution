'''
为了获取视频，你应该创建一个 VideoCapture 对象。他的参数可以是
设备的索引号，或者是一个视频文件
'''

import cv2
import numpy as np

cap=cv2.VideoCapture(0) # 参数可以是设备索引号或一个视频文件

# 视频默认的宽高为  640x480

# 此处需要两个值一起设置
# 并且还需要设置为原始的比例
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,320)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,240)

print(cap.get(3))
print(cap.get(4))

while(True):

	'''
	cap.read() 返回一个布尔值（ True/False）。如果帧读取的是正确的，
	就是 True。所以最后你可以通过检查他的返回值来查看视频文件是否已经到
	了结尾。
	
	有时 cap 可能不能成功的初始化摄像头设备。这种情况下上面的代码会报
	错。你可以使用 cap.isOpened()，来检查是否成功初始化了。如果返回值是
	True，那就没有问题。否则就要使用函数 cap.open()。

	你可以使用函数 cap.get(propId) 来获得视频的一些参数信息。这里
	propId 可以是 0 到 18 之间的任何整数。每一个数代表视频的一个属性

	其中的一些值可以使用 cap.set(propId,value) 来修改， value 就是
	你想要设置成的新值。
	例如，我可以使用 cap.get(3) 和 cap.get(4) 来查看每一帧的宽和高。
	默认情况下得到的值是 640X480。但是我可以使用 ret=cap.set(3,320)
	和 ret=cap.set(4,240) 来把宽和高改成 320X240。

	定义在 cv2.cv 中的常量信息

	CV_CAP_PROP_BRIGHTNESS = 10
	CV_CAP_PROP_CONTRAST = 11
	CV_CAP_PROP_CONVERT_RGB = 16
	CV_CAP_PROP_EXPOSURE = 15
	CV_CAP_PROP_FORMAT = 8
	CV_CAP_PROP_FOURCC = 6
	CV_CAP_PROP_FPS = 5
	CV_CAP_PROP_FRAME_COUNT = 7
	CV_CAP_PROP_FRAME_HEIGHT = 4 # 设置宽度
	CV_CAP_PROP_FRAME_WIDTH = 3  # 设置高度
	CV_CAP_PROP_GAIN = 14
	CV_CAP_PROP_HUE = 13
	CV_CAP_PROP_MODE = 9
	CV_CAP_PROP_OPENNI_BASELINE = 102
	CV_CAP_PROP_OPENNI_FOCAL_LENGTH = 103
	CV_CAP_PROP_OPENNI_FRAME_MAX_DEPTH = 101
	CV_CAP_PROP_OPENNI_OUTPUT_MODE = 100
	CV_CAP_PROP_OPENNI_REGISTRATION = 104
	CV_CAP_PROP_POS_AVI_RATIO = 2
	CV_CAP_PROP_POS_FRAMES = 1
	CV_CAP_PROP_POS_MSEC = 0
	CV_CAP_PROP_RECTIFICATION = 18
	CV_CAP_PROP_SATURATION = 12	

	'''

	ret,frame=cap.read() # 读取视频的一帧
	
	# 将图像转换为灰度图
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
	cv2.imshow('frame',gray)
	
	if cv2.waitKey(1)&0xFF==ord('q'):
		break
		
cap.release() # 释放摄像头
cv2.destroyAllWindows()	# 释放所有的窗口	 














