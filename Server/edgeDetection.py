import cv2
import numpy as np

def fourthCut(filename,copyname):
    img = cv2.imread(filename)
    for i in range(0,img.shape[0],2):
        for j in range(0,img.shape[1],2):
            img[i//2,j//2]=img[i,j]
    copy=img[0:img.shape[0]//2,0:img.shape[1]//2]
    cv2.imwrite(copyname, copy)

def imgEnhancement(img):
    kernel1 = np.array([[-1, -1, -1],
                    [-1, 9, -1],
                    [-1, -1, -1]])

    kernel2 = np.array([[0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]])

    dst = cv2.filter2D(img, -1, kernel2)
    return dst

#fourthCut("badApple.jpg","5.jpg")
img4=cv2.imread("badApple.jpg")
img5=cv2.imread("5.jpg")
#print(img4.shape,img5.shape)

img2=cv2.imread("Images_Co/Co4.jpg")
cv2.namedWindow('img', cv2.WINDOW_KEEPRATIO)
cv2.imshow('img',img2)
img2=imgEnhancement(img2)
img2=imgEnhancement(img2)
cv2.namedWindow('img2', cv2.WINDOW_KEEPRATIO)
cv2.imshow('img2',img2)
#blur = cv2.GaussianBlur(img2, (3, 3), 0)  
#cv2.imshow('blur',blur)
canny = cv2.Canny(img2, 50, 60)

img = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)
Scale_absX = cv2.convertScaleAbs(x)  
Scale_absY = cv2.convertScaleAbs(y)
sobel = cv2.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)

print(sobel.shape,canny.shape)

cv2.namedWindow('canny', cv2.WINDOW_KEEPRATIO)
cv2.imshow('canny',canny)
cv2.namedWindow('sobel', cv2.WINDOW_KEEPRATIO)
cv2.imshow('sobel',sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()