'''
• 学习对图像进行各种几个变换，例如移动，旋转，仿射变换等。
• 将要学到的函数有： cv2.getPerspectiveTransform

perspective：远景
affine：仿射
interpolation：篡改，插入

OpenCV 提供了两个变换函数， cv2.warpAffine 和 cv2.warpPerspective，
使用这两个函数你可以实现所有类型的变换。 
cv2.warpAffine 接收的参数是2 × 3 的变换矩阵
cv2.warpPerspective 接收的参数是 3 × 3 的变换矩阵
'''

# 扩展缩放 改变图像的尺寸大小
'''
OpenCV 提供的函数 cv2.resize()可以实现这个功能
图像的尺寸可以自己手动设置，你也可以指定缩放因子，我们可以选择使用不同的插值方法
在缩放时我们推荐使用 cv2.INTER_AREA
在扩展时我们推荐使用 v2.INTER_CUBIC（慢) 和 v2.INTER_LINEAR。
默认情况下所有改变图像尺寸大小的操作使用的插值方法都是 cv2.INTER_LINEAR
'''

import cv2
import numpy as np

img=cv2.imread(r'D:/Python/OpenCV Tutorial/images/mountain.png')



height,width=img.shape[:2]

# 戏码的两种方式都是将图像放大一倍

# 下面的 None 本应该是输出图像的尺寸，但是因为后边我们设置了缩放因子
# 因此这里为 None
res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

# 显式指定宽度和高度
#res=cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)

cv2.imshow('img',img)
cv2.imshow('res',res)


cv2.waitKey(0)

cv2.destroyAllWindows()
	
	

