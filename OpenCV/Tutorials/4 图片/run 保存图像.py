import numpy as np
import cv2

# 文件一定要用 UTF-8 格式编码

# 第二个参数是要告诉应该如何读取这幅图片
# cv2.IMREAD_COLOR 读入一副彩色图像，图像的透明度会被忽略，这是默认值  1
# cv2.IMREAD_GRAYSCALE 以灰度模式读入图像  0
# cv2.IMREAD_UNCHANGED 读入一副图像，并且包括图像的 alpha 通道  -1
# cv2.IMREAD_ANYDEPTH 2
# cv2.IMREAD_ANYCOLOR 4

# 载入图像
img=cv2.imread(r'D:/Python/OpenCV Tutorial/images/logo.png',0)

# 就算图像的路径是错误的，OpenCV 也不会提醒你，但是当你使用命令 print img 时
# 得到的 是 None

#显示图像
# 窗口会自动调整为图像大小，第一个参数是窗口的名字
# 第二个参数是图像对象
# 可以创建多个窗口对象，只要给定不同的名称即可
cv2.imshow('image',img)

# 由于是以灰度图打开的,所以存储为灰度
cv2.imwrite('BTKing.png',img)

'''cv2.waitKey() 是一个键盘绑定函数。需要指出的是它的时间尺度是毫
秒级。函数等待特定的几毫秒，看是否有键盘输入。特定的几毫秒之内，如果
按下任意键，这个函数会返回按键的 ASCII 码值，程序将会继续运行。如果没
有键盘输入，返回值为 -1，如果我们设置这个函数的参数为 0，那它将会无限
期的等待键盘输入。'''

# 一定到带 u，要不然中文乱码
print(u'按任意键退出.')

# 设置无限期等待键盘事件
cv2.waitKey(0)

'''
 可以轻易删除任何我们建立的窗口。如果
你想删除特定的窗口可以使用 cv2.destroyWindow()，在括号内输入你想删
除的窗口名。'''
cv2.destroyAllWindows()











