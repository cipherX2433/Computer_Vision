import cv2 as cv

img = cv.imread('photos/park.jpg')
cv.imshow('Park', img)

# #converting to grayscale    
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# #how to blur a image
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)
   
# #how to Edge Casscade
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

# #Dilating the image
# dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# #resize
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

#Cropping-->>
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)