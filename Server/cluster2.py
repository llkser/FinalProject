import cv2
import numpy as np
from sklearn.cluster import KMeans
import random

def kMeans(k,points):
    result=[]
    rand = random.sample(points, k)
    centers=[]
    for i in rand:
        centers.append(i[2])
    while True:
        result.clear()
        for i in range(k):
            result.append([])
        for point in points:
            dis=[]
            for i in range(k):
                dis.append(abs(point[2]-centers[i]))
            result[dis.index(min(dis))].append(point)
        newCenters=[]
        for i in range(k):
            sum=0
            for point in result[i]:
                sum+=point[2]
            newCenters.append(sum/len(result[i]))
        loss=0
        for i in range(k):
            loss+=abs(centers[i]-newCenters[i])
        if loss<=0.01:
            break
        centers=newCenters
    return result

def setSelect(s):
    flag=[]
    for x in s:
        center=[0,0]
        for point in x:
            center[0]+=point[0]
            center[1]+=point[1]
        center=[center[0]//len(x),center[1]//len(x)]
        dis=0
        for point in x:
            dis+=abs(center[0]-point[0])+abs(center[1]-point[1])
        dis=dis//len(x)
        flag.append(dis)
    return s[flag.index(min(flag))]

def exFeatures(s,img):
    print("Area = %d points."%len(s))
    avR=0
    avG=0
    avB=0
    for point in s:
        avR+=img[point[0]][point[1]][0]
        avG+=img[point[0]][point[1]][1]
        avB+=img[point[0]][point[1]][2]
    avR=int(avR/len(s))
    avG=int(avG/len(s))
    avB=int(avB/len(s))
    print("R = %d."%avR)
    print("G = %d."%avG)
    print("B = %d."%avB)
    for i in s:
        img[i[0]][i[1]][0]=0
        img[i[0]][i[1]][1]=0
        img[i[0]][i[1]][2]=0

    cv2.namedWindow('feature', cv2.WINDOW_KEEPRATIO)
    cv2.imshow('feature',img)

points = []

fi = open("points4.txt", "r+")
while True:
     line = fi.readline()
     if not line:      
        break
     points.append(eval(line[0:-1]))
     
print(len(points))
fi.close()
result=kMeans(3,points)
img1=cv2.imread("Images/Nickle4.jpg")
exFeatures(setSelect(result),img1)

'''
for k in range(3):
    img=cv2.imread("Images/Nickle4.jpg")
    for i in result[k]:
        img[i[0]][i[1]][0]=0
        img[i[0]][i[1]][1]=0
        img[i[0]][i[1]][2]=0

    cv2.namedWindow('img'+str(k), cv2.WINDOW_KEEPRATIO)
    cv2.imshow('img'+str(k),img)
'''

cv2.waitKey(0)
cv2.destroyAllWindows()

