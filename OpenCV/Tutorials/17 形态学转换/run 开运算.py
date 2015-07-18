'''
开运算
	先进行腐蚀，在进行膨胀操作
	可以用来祛除雪花点
'''

import cv2
import numpy as np

img=cv2.imread('..\images\opening.png',cv2.IMREAD_GRAYSCALE) 

#kernel=np.ones((5,5),np.uint8)
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

# 首先进行二值化
# 小于等于阈值的设置为 0【黑】大于阈值的设置指定值  255
ret,img=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

cv2.imshow('img',img)

'''
http://docs.opencv.org/2.4.10/modules/imgproc/doc/filtering.html?highlight=morphologyex#cv2.morphologyEx
Python: cv2.morphologyEx(src, op, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) → dst

Parameters:	
	src – Source image. The number of channels can be arbitrary. The depth should be one of CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
	dst – Destination image of the same size and type as src .
	element – Structuring element.
	op –
	Type of a morphological operation that can be one of the following:

		MORPH_OPEN - an opening operation
		MORPH_CLOSE - a closing operation
		MORPH_GRADIENT - a morphological gradient
		MORPH_TOPHAT - “top hat”
		MORPH_BLACKHAT - “black hat”
	iterations – Number of times erosion and dilation are applied.
	borderType – Pixel extrapolation method. See borderInterpolate() for details.
	borderValue – Border value in case of a constant border. The default value has a special meaning. See createMorphologyFilter() for details.
'''
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

cv2.imshow('opening',opening)

cv2.waitKey(0)

cv2.destroyAllWindows()