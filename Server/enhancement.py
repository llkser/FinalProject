import cv2
import numpy as np

img=cv2.imread("Images_Co/Co2.jpg")

kernel = np.array([[-1, -1, -1],
                [-1, 9, -1],
                [-1, -1, -1]])

dst = cv2.filter2D(img, -1, kernel)

cv2.namedWindow('original', cv2.WINDOW_KEEPRATIO)
cv2.imshow('original', img)
cv2.namedWindow('dst', cv2.WINDOW_KEEPRATIO)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Mat h1_kernel = (Mat_<char>(3, 3) << -1, -1, -1, -1, 8, -1, -1, -1, -1);
Mat h2_kernel = (Mat_<char>(3, 3) << 0, -1, 0, -1, 5, -1, 0, -1, 0);

Mat h1_result,h2_result;
filter2D(input, h1_result, CV_32F, h1_kernel);
filter2D(input, h2_result, CV_32F, h2_kernel);
convertScaleAbs(h1_result, h1_result);
convertScaleAbs(h2_result, h2_result);

imshow("h1_result", h1_result);
imshow("h2_result", h2_result);
'''