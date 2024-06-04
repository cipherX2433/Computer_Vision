import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/park.jpg')
cv.imshow('Park', img)

# plt.imshow(img)
# plt.show()

# #BGR->
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# BGR TO HSV ->
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# # BGR TO L*a*b ->
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

# #BGR TO RGB
# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB', rgb)

#HSV TO BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV->BGR', hsv_bgr)
# hsv to gryscale
grayscale = cv.cvtColor(hsv_bgr, cv.COLOR_BGR2GRAY)
cv.imshow('HSV TO GRAYSCAL VIA BGR', grayscale)


# plt.imshow()
# plt.show()


cv.waitKey(0)