'''
这里包括的按位操作有： AND， OR， NOT， XOR 等。当我们提取图像的
一部分，选择非矩形 ROI 时这些操作会很有用

我想把 OpenCV 的标志放到另一幅图像上。如果我使用加法，颜色会改
变，如果使用混合，会得到透明效果，但是我不想要透明。如果他是矩形我可
以象上一章那样使用 ROI。但是他不是矩形。但是我们可以通过下面的按位运
算实现

'''
import cv2
import numpy as np

img1=cv2.imread(r'D:/Python/OpenCV Tutorial/images/mountain.png')
img2=cv2.imread(r'D:/Python/OpenCV Tutorial/images/logo.png')

rows,cols,channels=img2.shape

# 获得 img1 的左上矩形区域
# 与 img2 的大小一致
roi=img1[0:rows,0:cols]

# 将 img2 转换为 灰度图像
img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

cv2.imshow('img2gray',img2gray)
cv2.waitKey(0)

# 小于等于175的设置为 0，大于175的设置为255
# ret 是我们设置阈值
# mask 是二值化后的图像
ret,mask=cv2.threshold(img2gray,175,255,cv2.THRESH_BINARY)

cv2.imshow('mask',mask)
cv2.waitKey(0)

# 将当前像素的值与 255 相减，然后取绝对值
# 取反操作
mask_inv=cv2.bitwise_not(mask)

cv2.imshow('mask_inv',mask_inv)
cv2.waitKey(0)
# mask 参数  8-bit single channel array, that specifies elements of the output array to be changed
# 获得 roi 中除了 logo 的区域像素
# 255 像素当做透明
# 0 像素盖在上面
# 将 0 与 一个像素 & 操作，结果还是 0
# 将 255 与一个 像素操作，结果还是原来的那个像素
img1_bg=cv2.bitwise_and(roi,roi,mask=mask)

cv2.imshow('img1_bg',img1_bg)
cv2.waitKey(0)

# 获得 img2 中 logo 区域的像素
# 黑色图像盖在上面，白色的透明
# 将 0 与 一个像素 & 操作，结果还是 0
# 将 255 与一个 像素操作，结果还是原来的那个像素
img2_fg=cv2.bitwise_and(img2,img2,mask=mask_inv)

cv2.imshow('img2_fg',img2_fg)
cv2.waitKey(0)

# 合并图像
# 此处使用像素相加
# OpenCV 中的加法 # 250+10=260 => 255
# 所以与黑色区域相加的都保留下来了
dst=cv2.add(img1_bg,img2_fg)

# 最后将原图像中的像素用新的值替换
img1[0:rows,0:cols]=dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()



