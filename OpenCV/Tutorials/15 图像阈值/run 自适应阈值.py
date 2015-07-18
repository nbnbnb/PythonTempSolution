'''
当一幅图像上的不同部分具有不同亮度时，我们需要采用自适应阈值
此时的阈值是根据图像上的每一小块区域计算与其对应的阈值
因此在一幅图像上的不同区域采用的是不同的阈值，从而是我们能在亮度不同的情况下得到更好的结果

Adaptive Method 自适应方式
	cv2.ADPTIVE_THRESH_MEAN_C：阈值取自相邻区域的平均值
	cv2.ADPTIVE_THRESH_GASUUIAN_C：阈值取自相邻区域的加权和，权重为一个高斯窗口
	
Block Size 邻域大小【用来计算阈值的区域大小】
	
C 一个常数，阈值就等于平均值或加权平均值减去这个参数	
	
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('..\images\dave.png',0)

# 中值滤波
# img=cv2.medianBlur(img,5)

ret,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# 11 为 Block Size, 2 为常数 C

# http://docs.opencv.org/2.4.10/modules/imgproc/doc/miscellaneous_transformations.html?highlight=adaptivethreshold#cv2.adaptiveThreshold
# Python: cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) → dst¶
# 貌似第二个参数有没有什么用
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

titles=['Original Image','Global Thresholding (v=127)','Adaptive Mean Thresholding','Adaptive Gaussian Thresholding']

images=[img,th1,th2,th3]

for i in range(4):
	plt.subplot(2,2,i+1),plt.imshow(images[i],cmap='gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])
	
plt.show()	


