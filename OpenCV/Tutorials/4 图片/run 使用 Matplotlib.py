import numpy as np
import cv2
from matplotlib import pyplot as plt

# 需要安装 matplotlib 包
# pip install matplotlib

# 载入图像
img=cv2.imread(r'D:/Python/OpenCV Tutorial/images/logo.png',0)

plt.imshow(img,cmap='gray',interpolation='bicubic')

# 隐藏 x,y 轴的刻度
plt.xticks([]), plt.yticks([])

plt.show()