import cv2
import numpy as np

mask=np.zeros((500,500,3),np.uint8)

mask[:]=255
# 点的类型一定要 np.int32
'''
pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts=pts.reshape((1,4,2))
'''

# 最终的数组形状应该是这样的
pts=np.array([[
	[10,5],
	[20,30],
	[70,20],
	[50,10]
]]);

# polylines(img, pts, isClosed, color[, thickness[, lineType[, shift]]]) -> None
'''
lineType –
	Type of the line:

	8 (or omitted) - 8-connected line.
	4 - 4-connected line.
	CV_AA - antialiased line. 【cv2.CV_AA==16】
'''
cv2.polylines(mask,pts,True,(0,0,255),1,16)

cv2.imshow('mask',mask)

cv2.waitKey(0)

cv2.destroyAllWindows()