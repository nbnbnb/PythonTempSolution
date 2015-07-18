'''
顾名思义，就是用与卷积对应像素的“中值”来替代中心像素的值
这个滤波器经常用来祛除椒盐噪声

中值=中间值：方框内所有像素排序后的一个中间值

卷积核的大小也应该是一个奇数。
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('..\images\logo2.png')
'''
http://docs.opencv.org/2.4.10/modules/imgproc/doc/filtering.html?highlight=gaussianblur#cv2.GaussianBlur
Python: cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) → dst

Parameters:	
	src – input image; the image can have any number of channels, which are processed independently, but the depth should be CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
	dst – output image of the same size and type as src.
	ksize – Gaussian kernel size. ksize.width and ksize.height can differ but they both must be positive and odd. Or, they can be zero’s and then they are computed from sigma* .
	sigmaX – Gaussian kernel standard deviation in X direction.
	sigmaY – Gaussian kernel standard deviation in Y direction; if sigmaY is zero, it is set to be equal to sigmaX, if both sigmas are zeros, they are computed from ksize.width and ksize.height , respectively (see getGaussianKernel() for details); to fully control the result regardless of possible future modifications of all this semantics, it is recommended to specify all of ksize, sigmaX, and sigmaY.
	borderType – pixel extrapolation method (see borderInterpolate() for details).

'''
dst=cv2.medianBlur(img,5) # 卷积核的大小也应该是一个奇数

plt.subplot(121),plt.imshow(img),plt.title('Original'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('MedianBlur'),plt.xticks([]),plt.yticks([])

plt.show()