'''
有时我们需要构建一个椭圆形/圆形的核
使用 cv2.getStructingElement() 可以实现这种要求
'''

import cv2

# 正矩形核
print(cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)))
'''
[[1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]]
'''
print('----------')

# 椭圆形核
print(cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))
'''
[[0 0 1 0 0]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [0 0 1 0 0]]
 '''
print('----------')
# 圆形核
print(cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5)))
'''
[[0 0 1 0 0]
 [0 0 1 0 0]
 [1 1 1 1 1]
 [0 0 1 0 0]
 [0 0 1 0 0]]
'''

raw_input('')