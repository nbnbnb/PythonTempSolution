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
print(u'按(s)保存 按(ESC)保存退出')

# 设置无限期等待键盘事件
# 如果你用的是 64 位系统，你需要将  k = cv2.waitKey(0) 这行改成 k = cv2.waitKey(0)&0xFF
whiteCodes=[27,ord('s'),ord('S')]
k = cv2.waitKey(0)&0xFF

while not k in whiteCodes:
	k = cv2.waitKey(0)&0xFF
	
if k==ord('s') or k==ord('s'):
	cv2.destroyAllWindows()

cv2.destroyAllWindows()











