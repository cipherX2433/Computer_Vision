import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# img = cv.imread('photos/cat.jpg')
# cv.imshow('Cat', img)

# #1. Paint the image a certain color
# # blank[200:300, 300:400] = 0,0,255
# # cv.imshow('Red', blank)

#2. Draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

#3.Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40 ,(0,0,255), thickness=cv.LINE_AA)
cv.imshow('Circle', blank)

#Draw a line
cv.line(blank, (0,0), (255,255), (255,255,255), thickness=3)
cv.imshow('Line', blank)    

#WRITE TEXT ON IMAGE
cv.putText(blank, 'Hello', (200,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)