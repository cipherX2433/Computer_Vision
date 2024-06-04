import cv2 as cv
import numpy as np

img = cv.imread('photos/group 1.jpg')
cv.imshow('Group', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#Sobel
Sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(Sobelx, sobely)

cv.imshow('Sobel_x', Sobelx)
cv.imshow('Sobel_y', sobely)
cv.imshow('Combined', combined_sobel)

cv.waitKey(0)