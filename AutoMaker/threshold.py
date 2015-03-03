import cv2
import numpy as np
img=cv2.imread('chamber.png',0)
ret1,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imwrite('chamber.png',th1)