# 使用 cv2.copyMakeBorder()函数
# 这经常在卷积运算或 0 填充时被用到

import cv2
import numpy as np
from matplotlib import pyplot as plt

#Python: cv2.copyMakeBorder(src, top, bottom, left, right, borderType[, dst[, value]]) → dst

'''
• src 输入图像
• top, bottom, left, right 对应边界的像素数目。
• borderType 要添加那种类型的边界，类型如下
– cv2.BORDER_CONSTANT 添加有颜色的常数值边界，还需要
下一个参数（ value）。
– cv2.BORDER_REFLECT 边界元素的镜像。比如: fedcba|abcdefgh|hgfedcb
– cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT
跟上面一样，但稍作改动。例如: gfedcb|abcdefgh|gfedcba
– cv2.BORDER_REPLICATE 重复最后一个元素。例如: aaaaaa|
abcdefgh|hhhhhhh
– cv2.BORDER_WRAP 不知道怎么说了, 就像这样: cdefgh|abcdefgh|abcdefg
• value 边界颜色，如果边界的类型是 cv2.BORDER_CONSTANT
'''
BLUE=[255,0,0]

img=cv2.imread(r'D:/Python/OpenCV Tutorial/images/logo.png')

# 重复最后一个元素
# 重复最后的一行像素
replicate=cv2.copyMakeBorder(img,50,20,10,10,cv2.BORDER_REPLICATE)

# 边界元素值的镜像
#fedcba|abcdefgh|hgfedcb 完全的镜像【连接处都是重复的】
reflect=cv2.copyMakeBorder(img,30,40,10,10,cv2.BORDER_REFLECT)
# 与上面的类式，有点小改动
# gfedcb|abcdefgh|gfedcba【连接处，进行了合并】
reflect101=cv2.copyMakeBorder(img,30,40,10,10,cv2.BORDER_REFLECT101)

# 将下面的像素复制一份给上面【上面添加底部的 20 像素】
# 将上面的像素复制一份给下面【下面添加上面的 40 像素】
# 左右同理
wrap=cv2.copyMakeBorder(img,20,40,10,10,cv2.BORDER_WRAP)

# 添加边框时，将会扩大图像
constant=cv2.copyMakeBorder(img,100,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL'),plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE'),plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT'),plt.xticks([]), plt.yticks([])
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT101'),plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP'),plt.xticks([]), plt.yticks([])
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT'),plt.xticks([]), plt.yticks([])

plt.show()



