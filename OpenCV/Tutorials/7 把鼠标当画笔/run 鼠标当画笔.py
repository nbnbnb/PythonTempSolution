'''
将要学习的函数是： cv2.setMouseCallback()


'''
import cv2
import numpy as np
# 查看所有被支持的鼠标事件
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

# 所有的鼠标事件回调函数都有一个统一的格式，他们所不同的地方仅仅是被调用后的功能。

# 回调格式的参数都是一致的
def draw_circle(event,x,y,flags,param):
	if event==cv2.EVENT_LBUTTONDBLCLK:  # 鼠标左键双击事件
		cv2.circle(img,(x,y),100,(255,0,0),-1)

img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while True:
	cv2.imshow('image',img)
	if cv2.waitKey(20)&0xFF==27:  # ESC
		break

cv2.destroyAllWindows()		
		