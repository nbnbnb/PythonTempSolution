'''
将窗口向各个方向移动(u,v)，然后计算所有差异的总和

窗口可以是正常的矩形窗口，也可以是对每一个像素给予不同权重的高斯窗口
'''

import cv2
import numpy as np

filename=r'D:/Python/OpenCV Tutorial/images/pattern.png'

img=cv2.imread(filename)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 数据类型为 float32 的输入图像
gray=np.float32(gray)

'''
Open 中的函数 cv2.cornerHarris() 可以用来进行角点检测。参数如下：
• img - 数据类型为 float32 的输入图像。
• blockSize - 角点检测中要考虑的领域大小。
• ksize - Sobel 求导中使用的窗口大小
• k - Harris 角点检测方程中的自由参数，取值参数为 [0,04， 0.06]
'''
dst=cv2.cornerHarris(gray,2,3,0.04)

# 此处的值需要根据不同的图像进行设置
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',img)

cv2.waitKey(0)

cv2.destroyAllWindows()