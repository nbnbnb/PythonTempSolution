'''
双边模糊
	在保持边界清晰的情况下，能有效祛除噪音
	
这种操作与其他滤波器相比会比较慢	

高斯滤波器是要求中心点邻近区域像素的高斯加权平均值，它只考虑像素之间的空间关系
而不会考虑像素值之间的关系【像素的相似度】
所以，这种方法不会考虑一个像素是否位于边界，因此边界也会被模糊掉，而这不是我们想要的

双边滤波在同时使用 空间高斯权重 和 灰度值相似性高斯权重

空间高斯函数确保只有邻近区域的像素对中心点有影响
灰度相似性高斯函数确保只有与中心像素灰度值相近的才会被用来做【高斯】模糊运算
所以这种方法确保边界不会被模糊掉，因为边界处的灰度值变化比较大
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread(r'..\images\bilateral.png',cv2.IMREAD_UNCHANGED)
'''
http://docs.opencv.org/2.4.10/modules/imgproc/doc/filtering.html?highlight=bilatera#cv2.bilateralFilter
Python: cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]]) → dst

Parameters:	
src – Source 8-bit or floating-point, 1-channel or 3-channel image.
dst – Destination image of the same size and type as src .
d – Diameter of each pixel neighborhood that is used during filtering. If it is non-positive, it is computed from sigmaSpace .
sigmaColor – Filter sigma in the color space. A larger value of the parameter means that farther colors within the pixel neighborhood (see sigmaSpace ) will be mixed together, resulting in larger areas of semi-equal color.
sigmaSpace – Filter sigma in the coordinate space. A larger value of the parameter means that farther pixels will influence each other as long as their colors are close enough (see sigmaColor ). 
	When d>0 , it specifies the neighborhood size regardless of sigmaSpace . Otherwise, d is proportional to sigmaSpace .
'''

# 9 表示邻域直径
# 两个 75 表示空间高斯函数标准差和灰度值相似性高斯函数标准差

dst=cv2.bilateralFilter(img,9,75,75) 

cv2.imshow('img',img)
cv2.imshow('dst',dst)

plt.subplot(121),plt.imshow(img),plt.title('Original'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('BilateralFilter'),plt.xticks([]),plt.yticks([])

plt.show()