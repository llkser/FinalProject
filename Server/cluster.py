import cv2
import numpy as np
from sklearn.cluster import KMeans

img=cv2.imread("Images/Co8.jpg")

points = []
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if not (img[i][j][0]==255 and img[i][j][1]==255 and  img[i][j][2]==255) and not (img[i][j][0]==0 and img[i][j][1]==0 and img[i][j][2]==0):
            RGBdis=3*img[i][j][0]*img[i][j][0]+4*img[i][j][1]*img[i][j][1]+2*img[i][j][2]*img[i][j][2]
            points.append([i,j,RGBdis])

fi = open("points8.txt", "w+")
for i in points:
    img[i[0]][i[1]][0]=0
    img[i[0]][i[1]][1]=0
    img[i[0]][i[1]][2]=0
    
    fi.write(str(i)+'\n')
fi.close()

'''cv2.namedWindow('img', cv2.WINDOW_KEEPRATIO)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

