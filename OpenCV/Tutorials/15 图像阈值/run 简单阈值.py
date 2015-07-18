'''
	当像素高于阈值时，我们给这个像素赋予一个新值，可能是白色
	否则我们给它赋予另外一种颜色，也许是黑色
	
	这个函数就是 cv2.threshold()
	http://docs.opencv.org/2.4.10/modules/imgproc/doc/miscellaneous_transformations.html?highlight=cv2.threshold#cv2.threshold
	
	第一个参数是原始图像，应该是灰度图【single-channel, 8-bit or 32-bit floating point】
	第二个参数就是我们用来对像素进行分类的阈值
	第三个参数当像素高于阈值时被赋予的新值【THRESH_BINARY 和 THRESH_BINARY_INV 才会用到】
	第四个参数是阈值类型
		cv2.THRESH_BINARY 
		cv2.THRESH_BINARY_INV 
		cv2.THRESH_TRUNC
		cv2.THRESH_TOZERO 
		cv2.THRESH_TOZERO_INV
		
	Python: cv2.threshold(src, thresh, maxval, type[, dst]) → retval, dst
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread(r'..\images\thresh.png',0)

ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY) # 小于等于阈值的设置为 0，大于阈值的设置为指定的值
cv2.imshow('1',thresh1)

ret,thresh2=cv2.threshold(img,127,100,cv2.THRESH_BINARY_INV) # 小于等于阈值的设置为指定值，大于阈值的设置0【黑】
cv2.imshow('2',thresh2)

ret,thresh3=cv2.threshold(img,100,255,cv2.THRESH_TRUNC) # 小于等于阈值的不变，大于阈值的设置为阈值，第三个参数无效
cv2.imshow('3',thresh3)

ret,thresh4=cv2.threshold(img,100,255,cv2.THRESH_TOZERO) # 小于等于阈值时，设置为 0，大于阈值时不变 ，第三个参数无效
cv2.imshow('4',thresh4)

ret,thresh5=cv2.threshold(img,100,5,cv2.THRESH_TOZERO_INV) # 小于等于阈值时不变，大于阈值时设置为 0 ，第三个参数无效
cv2.imshow('5',thresh5)

titles=['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images=[img,thresh1,thresh2,thresh3,thresh4,thresh5]

'''
for i in range(6):
	plt.subplot(2,3,i+1),plt.imshow(images[i],aspect='equal',cmap='gray')  # 以灰度图显式
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])
	
plt.show()	
'''

cv2.waitKey(0)
cv2.destroyAllWindows()







