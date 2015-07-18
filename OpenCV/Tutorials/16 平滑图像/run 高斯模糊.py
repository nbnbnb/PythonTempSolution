'''
高斯滤波
	现在把卷积核换成高斯核【简单来说，原来方框内的值是相等的，现在里面的值复合高斯分布】
	高斯分布
		方框中心的值最大，其余值根据距离中心元素的值递减，构成一个高斯小山包
	
	原来的求平均数，现在变成求加权平均数，权值就是方框里的值	
	
	实现的函数是 cv2.GaussianBlur()
	需要指定的高斯核的宽和高必须是奇数，同时还是指定高斯函数沿 X,Y 方向的标准差
	如果只指定了 X 方向的标准差， Y 方向的也会取相同的值
	如果两个标准差都是 0 ，那么函数会根据核的大小自己计算
	
	高斯滤波可以有效的从图像中祛除高斯噪音
	
	如果愿意，可以使用函数 cv2.getGaussianKernel() 自己构建一个高斯核
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('..\images\logo.png')
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
dst=cv2.GaussianBlur(img,(5,5),0) # 两个标准差都是 0 ，那么函数会根据核的大小自己计算

plt.subplot(121),plt.imshow(img),plt.title('Original'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('GaussianBlur'),plt.xticks([]),plt.yticks([])

plt.show()