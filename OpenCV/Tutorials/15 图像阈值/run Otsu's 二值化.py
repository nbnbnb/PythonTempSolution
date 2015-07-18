'''
使用全局阈值时，我们随便给了一个数来做阈值，那我怎么知道选取的这个数好坏呢？答案就是不停尝试
如果是一幅双峰图像【直方图中存在两个峰】，我们就应该在两个峰的峰谷中选一个值作为阈值，这就是 Otsu's 二值化要做的

定义：
	对一幅双峰图像自动根据其直方图计算出一个阈值【对于非双峰图像，这种方法得到的结果可能会很不理想】
	
这里用到的函数还是 cv2.threshold()，但是需要多传入一个参数【flag: cv2.THRESH_OTSU】
这时要把阈值设为 0，然后算法会找到最优阈值，这个最优阈值就是返回值 retVal
如果不使用 Otsu 二值化，返回的 retVal 值与设定的阈值相等
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('..\images\dave.png',0)

# 全局阈值
ret1,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Otsu's thresholding
ret2,th2=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# (5,5) 的高斯核大小，0 为标准差
blur=cv2.GaussianBlur(img,(5,5),0)

# 阈值一定要设置为 0
ret3,th3=cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

images=[img,0,th1,
		img,0,th2,
		blur,0,th3]

titles=[
		'Original Noisy Image','Histogram','Global Thresholding (v=127)',
		'Original Noisy Image','Histogram','Otsu''s Thresholding',
		'Gaussian filtered Image','Histogram','Otsu''s Thresholding'
		]
		
for i in range(3):
	plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],cmap='gray') # image[0,3,6]
	plt.title(titles[i*3]),plt.xticks([]),plt.yticks([])  # title[0,3,6]
	plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256) # image[0,3,6]
	plt.title(titles[i*3+1]),plt.xticks([]),plt.yticks([])  # title[1,4,7]
	plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],cmap='gray') # image[2,5,8]
	plt.title(titles[i*3+2]),plt.xticks([]),plt.yticks([]) # title[2,5,8]

plt.show()




