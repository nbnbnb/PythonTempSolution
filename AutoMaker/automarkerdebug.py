import cv2
import numpy as np

# 设置探测点格式
# isUp 和 isLine 函数使用
detectPointCount = 5

# 过滤点的阈值
offset = 5

# 判断线是否为【斜】向上趋势
# 取一部分连续的点，只要前一个点大于后一个点，就认为是向上的斜线
def isUp(list,start,cnt):   
    upCount = 1
    try:
        for i in range(cnt - 1):
            if list[start + i] <= list[start + i + 1]:
                upCount+=1
        # 当所有的点满足条件时，表示这是一个向上的趋势
        # 否则就是一个向下的趋势
        # 直线趋势已经在 isUp 函数之前判断过
        return upCount == detectPointCount
    except IndexError: # 检测到了结尾
        return False # 此处随便返回一个值

# 判断是否为直线
# 只要他们的不同数小于2个，就认为他们是直线，否则为斜线
def isLine(list,start,cnt):
    return len(set(list[start:start + cnt])) < 3

# 核心算法
# 获取拐点
def getIndex(list,start):
    # 首先计算轮廓点的长度
    cnt = len(list)
    # 首先判断是否为直线
    if isLine(list,start,detectPointCount):
        # 由于已经有一部分数据判断过了
        # 此处从 detectPointCount - 1 开始进行循环判断
        for i in range(detectPointCount - 1,cnt - start - 1):
            flag = i + start            
            try:
                # 每次迭代，判断后续的点有没有可能是斜线
                # 如果是斜线，就肯定此处为一个拐点
                # 如果是直线的的话，不会有3个连续相等的情况
                if (list[flag - 1] != list[flag] and list[flag] != list[flag + 1] and list[flag - 1] != list[flag + 1]):
                    return flag + 1
            except IndexError: # 检测到了结尾
                return None
    else:
        # 首先判断了是否为直线
        # 此处就只用判断是否为【斜上】或【斜下】了
        up = isUp(list,start,detectPointCount)

        for i in range(cnt - start - 1):
            flag = i + start
            # 在每一次迭代之前，需要判断后续的点有没有可能为直线
            # 因为从斜线变为直线处，肯定就是一个拐点
            if isLine(list,flag,detectPointCount):
                return flag

            # 对于 805 805 806 807 808 808 809 809 这类的上升趋势
            # 应该如何应对
            # 判断趋势是否发生了明显的变化
            # 如果是，就直接返回当前点
            if up:
                if list[flag] > list[flag + 1]:
                    return flag
            else:
                if list[flag] < list[flag + 1]:
                    return flag

def pointCheck(list1,list2,file):
    # 存储 x 轴和 y 轴索引
    res = []

    # 存储索引对应的坐标点
    points = []

    index = 0
    # 将 x 轴的拐点加入集合
    while True:
        res.append(index)
        index = getIndex(list1,index)
        if index == None:
            break
    index = 0   

    # 将 y 轴的拐点加入集合
    while True:
        # 排除掉重复的点
        if not index in res:
            res.append(index)
        index = getIndex(list2,index)
        if index == None:
            break

    # 原始的轮廓点是按照顺序生成的
    # 此处也需要把点的索引进行排序
    res.sort()

    for i in res:
        # 将索引对应的点添加到坐标中
        points.append([int(list1[i]),int(list2[i])])

    # 过滤掉相邻的坐标点，得到最终的拐点
    for point in filterPoints(points,5):
        file.write(str(point[0]) + ',' + str(point[1]) + '\n')
    # 加入房间点分割线
    file.write('--------------------\n')

def filterPoints(points,offset):
    # 最终的拐点
    res = []
    # 第一个点总是一个拐点
    res.append(points[0])
    
    for i in range(1,len(points)):
        # 将所有的点与检测出来的拐点进行对比
        # 如果他们的 offset 大于一个指定的访问，认为这是一个最终的拐点
        # 此处通过点的来判断，如果没有脏点，则认为这是一个最终的拐点
        if len([x for x in res if getOffset(x,points[i]) <= offset]) == 0:
            res.append(points[i])

    return res

# 计算两个点的差和
def getOffset(p1,p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def generateResult(fileName):
    img = cv2.imread(fileName,cv2.IMREAD_UNCHANGED)
    resFile = open('res.txt','w+')
    lower_red = np.array([0,0,200,255])
    upper_red = np.array([100,100,255,255])
    mask = cv2.inRange(img,lower_red,upper_red)
    contours,hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    
    # 单点测试
    '''
    lines1 = list(contours[22][:,0][:,0].flat)
    lines2 = list(contours[22][:,0][:,1].flat)
    checkfilex = open('check-x.txt','w+')
    checkfilex.writelines([str(x) + '\n' for x in lines1])
    checkfiley = open('check-y.txt','w+')
    checkfiley.writelines([str(y) + '\n' for y in lines2])	  
    pointCheck(lines1,lines2,resFile)        
    

    '''

    for points in contours:
        indexX = list(points[:,0][:,0].flat)
        indexY = list(points[:,0][:,1].flat)
        pointCheck(indexX,indexY,resFile)
    
    resFile.close()