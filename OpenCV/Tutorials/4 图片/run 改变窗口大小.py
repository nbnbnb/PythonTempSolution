import numpy as np
import cv2

# 文件一定要用 UTF-8 格式编码

# 第二个参数是要告诉应该如何读取这幅图片
# cv2.IMREAD_COLOR 读入一副彩色图像，图像的透明度会被忽略，这是默认值
# cv2.IMRWAD_GRAYSCALE 以灰度模式读入图像
# cv2.IMREAD_UNCHANGED 读入一副图像，并且包括图像的 alpha 通道

# 载入图像
img=cv2.imread(r'D:/Python/OpenCV Tutorial/images/logo.png',0)

# 就算图像的路径是错误的，OpenCV 也不会提醒你，但是当你使用命令 print img 时
# 得到的 是 None

# 显示图像
# 先创建一个窗口,然后加载图像
# cv2.WINDOW_NORMAL 可以拉动边框
# cv.WINDOW_AUTOSIZE 默认值,不可改动边框
cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)
# 传递窗口名称和图像对象
cv2.imshow('image',img)

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











