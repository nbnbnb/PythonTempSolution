import cv2
import numpy as np

'''
可以使用 cv2.add() 将两幅图像进行加法运算，或者使用 numpy
例如 res=img1 + img2，两幅图像的大小、类型必须一致，
或者第二个图像可以使用一个简单的标量值
'''

x=np.uint8([250])
y=np.uint8([10])

# OpenCV 加法
print(cv2.add(x,y)) # 250+10=260 => 255

# numpy 加法
print(x+y)  # 250+10=260%256=4

x=np.uint16([250])
y=np.uint16([10])

# 如果使用 uint16，就不会有溢出了
print(cv2.add(x,y)) 
print(x+y)

raw_input('')