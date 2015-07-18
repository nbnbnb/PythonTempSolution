import cv2
import numpy as np

cap=cv2.VideoCapture(0)

'''
FourCC 就是一个 4 字节码，用来确定视频的编码格式。可用的编码列表
可以从fourcc.org查到。这是平台依赖的。下面这些编码器对我来说是有用个。
• In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is
more preferable. MJPG results in high size video. X264 gives
very small size video)
• In Windows: DIVX (More to be tested and added)
• In OSX : (I don’ t have access to OSX. Can some one fill this?)
'''

# 使用 Windows 自带的解码器
fourcc=cv2.cv.CV_FOURCC('I','4','2','0')

# 下面为备用解码器
#cv2.cv.FOURCC(*'XVID')

out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while(cap.isOpened()):
	ret,frame=cap.read()
	if ret==True:
		frame=cv2.flip(frame,0) # 水平方向旋转
		
		out.write(frame)
		
		cv2.imshow('frame',frame)
		
		if cv2.waitKey(1)&0xFF==ord('q'):
			break
	else:
		break
		
cap.release()
out.release()
cv2.destroyAllWindows()		