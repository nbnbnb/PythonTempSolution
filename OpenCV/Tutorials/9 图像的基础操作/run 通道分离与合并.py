'''
有时你需要对一幅图像的特定区域进行操作。例如我们要检测一副图像中
眼睛的位置，我们首先应该在图像中找到脸，再在脸的区域中找眼睛，而不是
直接在一幅图像中搜索。这样会提高程序的准确性和性能。
ROI 也是使用 Numpy 索引来获得的。
'''

import cv2
import numpy as np

img=cv2.imread(r'D:/Python/OpenCV Tutorial/images/mountain.jpg')

# 分离通道
# cv2.split() 是一个比较耗时的操作。只有真正需要时才用它，能用Numpy 索引就尽量用。
b,g,r=cv2.split(img)

print(b)
print(g)
print(r)

# 获得通道值的等价方法
b=img[:,:,0]
g=img[:,:,1]
r=img[:,:,2]

# 合并通道
img=cv2.merge((b,g,r))

cv2.imshow('image',img)

cv2.waitKey(0)

# 将所有像素的红色通道值都设置为 0
#你不必先拆分再赋值。你可以直接使用 Numpy 索引，这会更快。
img[:,:,2]=0
cv2.imshow('image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()




