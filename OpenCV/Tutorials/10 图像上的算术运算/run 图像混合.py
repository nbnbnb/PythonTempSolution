import cv2
import numpy as np

img1=cv2.imread(r'D:/Python/OpenCV Tutorial/images/130-1.png')
img2=cv2.imread(r'D:/Python/OpenCV Tutorial/images/130-2.png')

# dst = α · img 1 + β · img 2 + γ
# 这里的 γ 取值为 0
# 第一幅图的权重取 0.7，第二幅图的权重取 0.3
dst=cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()