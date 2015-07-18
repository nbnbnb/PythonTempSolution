'''
目标
• 学习使用不同的低通滤波器对图像进行模糊
• 使用自定义的滤波器对图像进行卷积（ 2D 卷积）

与一维信号一样，我们也可以对 2D 图像实施低通滤波【LPF】或高通滤波【HPF】
LPF 帮助我们去除噪音
HPF 帮助我们找到图像的边缘

使用低通滤波器可以达到模糊的目的，这对祛除噪音很有帮助
OpenCV 提供了4种模糊技术
	平均
	高斯
	中值
	双边

OpenCV 提供的函数 cv.filter2D() 可以让我们对一幅图像进行卷积操作

平均滤波器
	将卷积核放在图像的一个像素 A 上，求与核对应的图像上的 25(5x5) 个像素的和，再取平均值
	最后用这个值代替像素 A 的值。重复以上操作，直到将图像上的每一个像素都更新一遍
	
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('..\images\logo.png')

kernel=np.ones((5,5),dtype=np.float32)/25

'''
http://docs.opencv.org/2.4.10/modules/imgproc/doc/filtering.html?highlight=filter2d#cv2.filter2D

Python: cv2.filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]]) → dst

Parameters:	
src – input image.
dst – output image of the same size and the same number of channels as src.

ddepth –
	desired depth of the destination image; if it is negative, it will be the same as src.depth(); the following combinations of src.depth() and ddepth are supported:
	src.depth() = CV_8U, ddepth = -1/CV_16S/CV_32F/CV_64F
	src.depth() = CV_16U/CV_16S, ddepth = -1/CV_32F/CV_64F
	src.depth() = CV_32F, ddepth = -1/CV_32F/CV_64F
	src.depth() = CV_64F, ddepth = -1/CV_64F

when ddepth=-1, the output image will have the same depth as the source.

kernel – convolution kernel (or rather a correlation kernel), a single-channel floating point matrix; if you want to apply different kernels to different channels, split the image into separate color planes using split() and process them individually.
anchor – anchor of the kernel that indicates the relative position of a filtered point within the kernel; the anchor should lie within the kernel; default value (-1,-1) means that the anchor is at the kernel center.
delta – optional value added to the filtered pixels before storing them in dst.
borderType – pixel extrapolation method (see borderInterpolate() for details).
'''
dst=cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging'),plt.xticks([]),plt.yticks([])

plt.show()



