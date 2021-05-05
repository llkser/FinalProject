import cv2
import numpy as np

img1=cv2.imread("Images_Co/Co1.jpg")
result=[0,0,0]
count=0

for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        if not (img1[i,j,0]==255 and img1[i,j,1]==255 and img1[i,j,2]==255):
            count+=1
            result[0]+=img1[i,j,0]
            result[1]+=img1[i,j,1]
            result[2]+=img1[i,j,2]
result[0]//=count
result[1]//=count
result[2]//=count
for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        img1[i,j]=result

img2=cv2.imread("Images_Co/Co5.jpg")
ans=20
for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        if abs(img2[i,j,0]-result[0])<ans and abs(img2[i,j,1]-result[1])<ans and abs(img2[i,j,2]-result[2])<ans:
            img2[i,j,0]=255
            img2[i,j,1]=255
            img2[i,j,2]=255

cv2.namedWindow('test', cv2.WINDOW_KEEPRATIO)
cv2.imshow('test',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()