import cv2 as cv
import pickle

img = cv.imread('carParkImg.png')

width, height = 107, 48

try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if event == cv.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)

while True:
    img = cv.imread('carParkImg.png')
    for pos in posList:
        cv.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv.imshow('Image', img)
    cv.setMouseCallback('Image', mouseClick)
    key = cv.waitKey(1)
    if key == 27:  # Press Esc to exit
        break

cv.destroyAllWindows()
