'''
图像的属性包括：行，列，通道，图像数据类型，像素数目等
img.shape 可以获取图像的形状，他的返回值是一个包含行数，列数，通道数的元组。
'''

import cv2
import numpy as np

img=cv2.imread(r'D:/Python/OpenCV Tutorial/images/mountain.jpg')

print(type(img))

print(img.shape) # 返回的是一个元组 (1200, 1920, 3) 3 通道 BGR

# 如果图像是灰度图，返回值仅有行数和列数。所以通过检查这个返回值就可以知道加载的是灰度图还是彩色图。

print(img.size) #  返回图像的像素数目 行*列*通道

#注意：在除虫（ debug）时 img.dtype 非常重要。因为在 OpenCVPython 代码中经常出现数据类型的不一致。
print(img.dtype) # 返回图像的数据类型 #uint8
