import cv2
import numpy as np

# 当鼠标按下时为 True
drawing=False

# 如果 mode 为 True 绘制矩形
# 按下 m ,切换绘制曲线
mode=True

ix,iy=-1,-1

def draw_circle(event,x,y,flags,param):
	global ix,iy,drawing,mode
	
	# 按下鼠标左键
	if event==cv2.EVENT_LBUTTONDOWN:
		drawing=True
		ix,iy=x,y
	# 按下鼠标左键并移动
	elif event==cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:
		if drawing==True:
			# 下面的绘制过程是连续的
			# 在绘制矩形时察觉不出来，因为后一个里面会覆盖前一个矩形区域
			if mode==True:
				cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
			else:
				cv2.circle(img,(x,y),3,(0,0,255),-1)
	# 松开鼠标左键			
	elif event==cv2.EVENT_LBUTTONUP:
		drawing=False
	
		'''
		if mode==True:
				cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
		else:
			cv2.circle(img,(x,y),30,(0,0,255),-1)	
		'''
		
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while True:
	cv2.imshow('image',img)
	k=cv2.waitKey(1)&0xFF
	if k==ord('m'):
		mode=not mode
	elif k==27:
		break
		
cv2.destroyAllWindows()			