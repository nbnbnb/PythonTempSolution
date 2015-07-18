'''
目标
• 学习不同的形态学操作，例如腐蚀，膨胀，开运算，闭运算等
• 我们要学习的函数有： cv2.erode()， cv2.dilate()， cv2.morphologyEx()等

原理
	形态学操作是根据图像形状进行的简单操作。
	一般情况下对二值化图像进行的操作。
	需要输入两个参数，一个是原始图像，第二个被称为结构化元素或核，它是用来决定操作的性质的。
	两个基本的形态学操作是腐蚀和膨胀。他们的变体构成了开运算，闭运算，梯度等。我们会以下图为例逐一介绍它们
	
腐蚀：
	就像土壤腐蚀一样，这个操作会把前景物体的边界腐蚀掉【但是前景仍然是白色】
	步骤
		卷积核沿着图像滑动，如果与卷积核对应的原图像的“所有像素值”都是 1
		那么中心元素就保持原来的像素值，否则就变为 0 
		最终的结果就是将部分的像素变为了 0【图像的白边缘减少】
		
		解释：
			此处可以这样理解，卷积值与像素值用 & 二进制操作，得到为 1，就保留
			
		
	产生的影响
		根据卷积核的大小，靠近前景的所有像素都会被腐蚀掉【变为 0】
		所以前景物体会变小，整幅图像的白色区域会减少
		
作用：
	对于祛除白噪声很有用，也可以用来断开两个连在一块的物体等	
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

 #小于等于阈值的设置为 0【黑】 ，大于阈值的设置指定值  255【可以设置为 188 试试】
ret,img=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

erosion=cv2.erode(img,kernel,iterations=1) # iterations 表示腐蚀的数量

cv2.imshow('origin',img)
cv2.imshow('erosion',erosion)

cv2.waitKey(0)

cv2.destroyAllWindows()

