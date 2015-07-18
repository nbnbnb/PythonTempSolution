# OpenCV 中有超过 150 种转换方法，经常使用的为 
# BGR - Gray 和 BGR - HSV
# 使用 cv.cvtColor(input_image,flag)，其中 flag 就是转换类型
# BGR -> Gray 使用的 flag 为 cv2.COLOR_BGR2GRAY
# BGR -> HSV 使用的 flag 为 cv2.COLOR_BGR2HSV

# 使用下面的命令，枚举出所有的标记
# flags=[i for i in dir(cv2) if i.startswith('COLOR_')]

# H(色彩/色度) S(饱和度) V(亮度)
# Hue Saturation Value
# OpenCV 中的取值访问为  H[0~179] S[0~255] V[0~255]

#当你需要拿 OpenCV 的 HSV 值与其他软件的 HSV 值进行对比时，一定要记得归一化。

# 使用场景
# 1，物体跟踪
# 在 HSV 颜色空间中要比在 BGR 空间中更容易表示一个特定颜色
# 例如要提取一个蓝色的物体
# a.从视频中获取每一帧图像
# b.将图像转换到 HSV 空间
# c.设置 HSV 阈值到蓝色范围
# d.获取蓝色物体，当然我们还可以做其他任何我们想做的事，比如：在蓝色物体周围画一个圈。

# 代码

import cv2
import numpy as np

cap=cv2.VideoCapture(0)

print(u'按 ESC 键退出')

while True:
	# 获取每一帧
	ret,frame=cap.read()
	
	# 转换到 HSV
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	
	# 设定蓝色的阈值
	lower_blue=np.array([110,50,50])
	upper_blue=np.array([130,255,255])
	
	# 根据阈值构建掩模
	mask=cv2.inRange(hsv,lower_blue,upper_blue)
	
	# 对原图像和掩模进行位运算
	res=cv2.bitwise_and(frame,frame,mask=mask)
	
	# 显示图像
	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	
	k=cv2.waitKey(5)&0xFF
	if k==27:  # ESC
		break
		
cv2.destroyAllWindows()	

'''	
这是物体跟踪中最简单的方法。当你学习了轮廓之后，你就会学到更多
相关知识，那是你就可以找到物体的重心，并根据重心来跟踪物体，仅仅在摄
像头前挥挥手就可以画出同的图形，或者其他更有趣的事。	
'''
	
