'''
有时你需要对一幅图像的特定区域进行操作。例如我们要检测一副图像中
眼睛的位置，我们首先应该在图像中找到脸，再在脸的区域中找眼睛，而不是
直接在一幅图像中搜索。这样会提高程序的准确性和性能。
ROI 也是使用 Numpy 索引来获得的。
'''

import cv2
import numpy as np

img=cv2.imread(r'D:/Python/OpenCV Tutorial/images/mountain.jpg')

ball=img[280:340,330:390] # 获得一个矩形区域的像素【X 轴从 280 到 340，Y 轴从 330 到 390】
img[273:333,100:160]=ball # 这个区域大小要与上面选择的保持一致

cv2.imshow('image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()





