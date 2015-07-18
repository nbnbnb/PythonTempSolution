'''
	与腐蚀相反，与卷积和对应的原图像的像素值只要有一个是 1 ，中心元素的值就是 1 
	
	用途：
		一般在去噪声时，先用腐蚀，再用膨胀
		因为腐蚀在去掉白噪声的同时，也会使前景对象变小
		所以我们再对他进行膨胀
		
		它也可以用来连接两个分开的物体
'''


import cv2
import numpy as np

img=cv2.imread('..\images\erode.png',cv2.IMREAD_GRAYSCALE) 

# 首先进行二值化
# 小于等于阈值的设置为 0【黑】大于阈值的设置指定值  255
ret,img=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

kernel=np.ones((5,5),np.uint8)

'''
http://docs.opencv.org/2.4.10/modules/imgproc/doc/filtering.html?highlight=cv2.erode#cv2.erode
Python: cv2.erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) → dst

Parameters:	
	src – input image; the number of channels can be arbitrary, but the depth should be one of CV_8U, CV_16U, CV_16S, CV_32F` or ``CV_64F.
	dst – output image of the same size and type as src.
	element – structuring element used for erosion; if element=Mat() , a 3 x 3 rectangular structuring element is used.
	anchor – position of the anchor within the element; default value (-1, -1) means that the anchor is at the element center.
	iterations – number of times erosion is applied.
	borderType – pixel extrapolation method (see borderInterpolate() for details).
	borderValue – border value in case of a constant border (see createMorphologyFilter() for details).
'''

erosion=cv2.erode(img,kernel,iterations=1) # iterations 表示腐蚀的数量

dilation=cv2.dilate(erosion,kernel,iterations=1)

cv2.imshow('origin',img)
cv2.imshow('erosion',erosion)
cv2.imshow('dilation',dilation)

cv2.waitKey(0)

cv2.destroyAllWindows()