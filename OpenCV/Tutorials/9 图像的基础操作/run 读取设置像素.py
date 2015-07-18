# 所有的这些操作都与 numpy 有很大的关系

import cv2
import numpy as np

img=cv2.imread(r'D:/Python/OpenCV Tutorial/images/mountain.jpg')

'''
你可以根据像素的行和列的坐标获取他的像素值。对 BGR 图像而言
返回值为 B， G， R 的值。对灰度图像而言，会返回他的灰度值
'''

px=img[100,100]  # 返回 BGR 值
print(px)

blue=img[100,100,0] # 返回 B(lue) 值
print(blue)

# 修改像素的值

img[100,100]=[255,255,255]
print(img[100,100])

'''
Numpy 是经过优化了的进行快速矩阵运算的软件包。所以我们不推荐
逐个获取像素值并修改，这样会很慢，能有矩阵运算就不要用循环。
'''

# 获取像素值及修改的更好方法

print(img.item(10,10,2)) # 获取 R(ed) 像素的值
img.itemset((10,10,2),100) # 修改 R(ed) 像素的值
print(img.item(10,10,2))














