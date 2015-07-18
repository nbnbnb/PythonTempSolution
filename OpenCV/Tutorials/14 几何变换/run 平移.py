import cv2
import numpy as np

img=cv2.imread(r'D:/Python/OpenCV Tutorial/images/mountain.png')
	
# 高对应行 rows
# 宽对应列 cols
rows,cols=img.shape[:2]
	
M=np.mat([[1,0,100],[0,1,50]],dtype='float32')

# 需要的格式是 宽，高
dst=cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('dst',dst)

cv2.waitKey(0)

cv2.destroyAllWindows()
