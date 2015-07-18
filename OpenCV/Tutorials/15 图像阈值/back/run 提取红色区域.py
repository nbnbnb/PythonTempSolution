import cv2
import numpy as np

img=cv2.imread('test.png',cv2.IMREAD_UNCHANGED)

sk=cv2.imread('test.png')

# 将透明区域设置为

lower_red=np.array([0,0,255,255]) 
upper_red=np.array([0,0,255,255])

# 识别后的黑白区域
mask=cv2.inRange(img,lower_red,upper_red)

cv2.imshow('mask',mask)

cv2.imwrite('white-black.jpg',mask)

'''
函数 cv2.findContours() 有三个参数
	第一个是输入图像
	第二个是轮廓检索模式
	第三个是轮廓近似方法
返回值有三个
	第一个是图像
	第二个是轮廓
	第三个是（轮廓的）层析结构
轮廓（第二个返回值）是一个 Python列表，其中存储这图像中的所有轮廓
每一个轮廓都是一个 Numpy 数组，包含对象边界点（x，y）的坐标
'''
contours,hierarchy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

# 将坐标写入文本
open('res.txt','w').write(str(contours[0]))


cv2.waitKey(0)

cv2.destroyAllWindows()

