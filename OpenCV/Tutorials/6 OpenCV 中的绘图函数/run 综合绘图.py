'''
代码
上面所有的这些绘图函数需要设置下面这些参数：
• img：你想要绘制图形的那幅图像。
• color：形状的颜色。以 RGB 为例，需要传入一个元组，例如：（ 255,0,0）代表蓝色。对于灰度图只需要传入灰度值。
• thickness：线条的粗细。如果给一个闭合图形设置为 -1，那么这个图形就会被填充。默认值是 1.

• linetype：线条的类型 
	8 (or omitted) - 8-connected line.
	4 - 4-connected line.
	CV_AA - antialiased line. 【cv2.CV_AA==16】抗锯齿
'''

import cv2
import numpy as np

# 创建一个 512x512 的黑色图片
# 3 通道
img=np.zeros((512,512,3),np.uint8)

# 白色图片
#img[:]=255 or img[...]=255


'''
img – Image.
pt1 – First point of the line segment.
pt2 – Second point of the line segment.
color – Line color.
thickness – Line thickness.
lineType –
	Type of the line:

	8 (or omitted) - 8-connected line.
	4 - 4-connected line.
	cv2.CV_AA - antialiased line. 【cv2.CV_AA==16】抗锯齿
shift – Number of fractional bits in the point coordinates.
'''
# line(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> None
cv2.line(img,(0,0),(511,511),(255,0,0),5,4)

# 以左上角为(0,0)起点计算
# 第一个点是左上，第二个点是右下
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# circle(img, center, radius, color[, thickness[, lineType[, shift]]]) -> None
# thickness=-1 表示闭合
cv2.circle(img,(447,63),63,(0,0,255),-1)

'''
画椭圆比较复杂，我们要多输入几个参数。一个参数是中心点的位置坐标。
下一个参数是长轴和短轴的长度。椭圆沿逆时针方向旋转的角度。椭圆弧演
顺时针方向起始的角度和结束角度，如果是 0 很 360，就是整个椭圆。查看
cv2.ellipse() 可以得到更多信息。下面的例子是在图片的中心绘制半个椭圆。
ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]]) -> None  or  ellipse(img, box, color[, thickness[, lineType]]) -> None
'''
cv2. ellipse(img,( 256, 256),( 100, 50), 0, 0, 180, 255, - 1)

'''
要在图片上绘制文字，你需要设置下列参数：
• 你要绘制的文字
• 你要绘制的位置
• 字体类型（通过查看 cv2.putText() 的文档找到支持的字体）
• 字体的大小
• 文字的一般属性如颜色，粗细，线条的类型等。为了更好看一点推荐使用
linetype=cv2.CV_AA
在图像上绘制白色的 OpenCV
'''
font=cv2.FONT_HERSHEY_SIMPLEX
#putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) -> None
cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),2,cv2.CV_AA) # cv2.CV_AA==16，表示抗锯齿

# 画多变形
# polylines(img, pts, isClosed, color[, thickness[, lineType[, shift]]]) -> None

# 点的类型一定要 np.int32
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
'''
# 多边形的  thickness 不能设置为 -1 
cv2.polylines(img,pts,True,(0,0,255),1,16)

winname='example'
cv2.namedWindow(winname)
cv2.imshow(winname,img)
cv2.waitKey(0)
cv2.destroyAllWindows()
