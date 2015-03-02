import cv2
import numpy as np
detectPointCount = 10
offset = 5
def isUp(list,start,cnt):    
    upCount = 1
    try:
        for i in range(cnt - 1):
            if list[start + i] <= list[start + i + 1]:
                upCount+=1
        return upCount == detectPointCount
    except IndexError:
        return False
def isLine(list,start,cnt):
    return len(set(list[start:start + cnt])) < 3
def getIndex(list,start):
    cnt = len(list)
    if isLine(list,start,detectPointCount):
        for i in range(detectPointCount - 1,cnt - start - 1):
            flag = i + start            
            try:
                if (list[flag - 1] != list[flag] and list[flag] != list[flag + 1] and list[flag - 1] != list[flag + 1]):
                    return flag + 1
            except IndexError: 
                return None
    else:
        up = isUp(list,start,detectPointCount)

        for i in range(cnt - start - 1):
            flag = i + start
            if isLine(list,flag,detectPointCount):
                return flag
            if up:
                if list[flag] > list[flag + 1]:
                    return flag
            else:
                if list[flag] < list[flag + 1]:
                    return flag
def pointCheck(list1,list2,file):
    res = []
    points = []
    index = 0
    while True:
        res.append(index)
        index = getIndex(list1,index)
        if index == None:
            break
    index = 0   
    while True:
        if not index in res:
            res.append(index)
        index = getIndex(list2,index)
        if index == None:
            break
    res.sort()
    for i in res:
        points.append([int(list1[i]),int(list2[i])])
    for point in filterPoints(points,5):
        file.write(str(point[0]) + ',' + str(point[1]) + '\n')
    file.write('--------------------\n')
def filterPoints(points,offset):
    res = []
    res.append(points[0])   
    for i in range(1,len(points)):
        if len([x for x in res if getOffset(x,points[i]) <= offset]) == 0:
            res.append(points[i])
    return res
def getOffset(p1,p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
def generateResult(fileName):
    img = cv2.imread(fileName,cv2.IMREAD_UNCHANGED)
    resFile = open('res.txt','w+')
    lower_red = np.array([0,0,200,255])
    upper_red = np.array([100,100,255,255])
    mask = cv2.inRange(img,lower_red,upper_red)
    contours,hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for points in contours:
        indexX = list(points[:,0][:,0].flat)
        indexY = list(points[:,0][:,1].flat)
        pointCheck(indexX,indexY,resFile)
    resFile.close()