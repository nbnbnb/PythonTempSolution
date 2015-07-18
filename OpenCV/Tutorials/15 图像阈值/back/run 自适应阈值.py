'''
当像素值高于阈值时，我们给这个像素赋予一个新值（可能是白色）
否则我们给它赋予另外一种颜色（也许是黑色）
这个函数就是 cv2.threshhold()

这个函数的第一个参数就是原图像，原图
像应该是灰度图。第二个参数就是用来对像素值进行分类的阈值。第三个参数
就是当像素值高于（有时是小于）阈值时应该被赋予的新的像素值。OpenCV
提供了多种不同的阈值方法，这是有第四个参数来决定的。

• cv2.THRESH_BINARY
• cv2.THRESH_BINARY_INV
• cv2.THRESH_TRUNC
• cv2.THRESH_TOZERO
• cv2.THRESH_TOZERO_INV
'''