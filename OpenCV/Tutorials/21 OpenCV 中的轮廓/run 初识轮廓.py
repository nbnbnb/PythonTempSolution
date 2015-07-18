'''
轮廓可以简单认为成将连续的点（连着边界）连在一起的曲线，具有相同的颜色或者灰度

• 为了更加准确，要使用二值化图像。在寻找轮廓之前，要进行阈值化处理或者 Canny 边界检测。
• 查找轮廓的函数会修改原始图像。如果你在找到轮廓之后还想使用原始图像的话，你应该将原始图像存储到其他变量中。
• 在 OpenCV 中，查找轮廓就像在黑色背景中超白色物体。你应该记住，要找的物体应该是白色而背景应该是黑色。



'''

import numpy as np
import cv2

img=cv2.imread('test.jpg')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,127,255,0)

'''
函数 cv2.findContours() 有三个参数
第一个是输入图像
第二个是轮廓检索模式
第三个是轮廓近似方法
第一个是轮廓，第二个是（轮廓的）层析结构
轮廓是一个 Python 列表，其中存储着图像中的所有轮廓
每一个轮廓都是一个 Numpy 数组，包含对象边界点（ x， y）的坐标
'''

# Python: cv2.findContours(image, mode, method[, contours[, hierarchy[, offset]]]) → contours, hierarchy
# cv2.CHAIN_APPROX_SIMPLE # 只保留连接的点
# cv2.CHAIN_APPROX_NONE # 保留所有的点

contours,hierarchy =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print(contours)

'''
第一个参数是图像
第二个参数是轮廓
第三个参数表示轮廓的索引【在轮廓列表中】 如果设置为负数，则表示绘制所有的轮廓
接下来是轮廓的颜色和厚度
Python: cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]]) → None

lineType
	8 (or omitted) - 8-connected line.
	4 - 4-connected line.
	CV_AA - antialiased line. 【cv2.CV_AA==16】抗锯齿
'''

# 虽说此处的轮廓只有4个点，但是还是会绘制成连接的线
cv2.drawContours(img,contours,-1,(0,255,0),3,16) # 直接修改 img

cv2.imshow('image',imgray)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()