import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

Gimg=[]
for i in range(1,9):
    address="Images/Co"+str(i)+".jpg"
    img=cv2.imread(address)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    '''
    cv2.namedWindow(address, cv2.WINDOW_KEEPRATIO)
    cv2.imshow(address,img)
    '''
    Gimg.append(img)

table=[]
for i in Gimg:
    temp=[0]*256
    for x in range(0,i.shape[0]):
        for y in range(0,i.shape[1]):
            if i[x][y]!=0 and i[x][y]!=255:
                temp[i[x][y]]+=1
    table.append(temp)
'''
for i in table:
    plt.plot(range(0,256),i)
    plt.xlabel("Grey Value", fontsize=8)               
    plt.ylabel("Frequency", fontsize=8)
    plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

test=[0]*256
testImg=cv2.imread("Images/test1.jpg")
Gtest=cv2.cvtColor(testImg,cv2.COLOR_BGR2GRAY)

for x in range(0,Gtest.shape[0]):
    for y in range(0,Gtest.shape[1]):
        if Gtest[x][y]!=0 and Gtest[x][y]!=255:
            test[Gtest[x][y]]+=1

result=[]
for i in table:
    p=0
    X=0
    Y=0
    for j in range(256):
        p+=test[j]*i[j]
        X+=test[j]*test[j]
        Y+=i[j]*i[j]
    X=math.sqrt(X)
    Y=math.sqrt(Y)
    result.append(p/(X*Y))

print(result)