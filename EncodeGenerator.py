import cv2 as cv
import face_recognition
import pickle
import os

#importing student images
folderImages = 'Files/Images'
imagePathList = os.listdir(folderImages)
# print(imagePathList)
imageList = []
studentIds = []

for path in imagePathList:
    imageList.append(cv.imread(os.path.join(folderImages, path)))
    studentIds.append(os.path.splitext(path)[0])

print(len(imageList))
print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]    
        encodeList.append(encode)

    return encodeList

print("Encoding Started...")
encodeListKnown = findEncodings(imageList)
print("Encoding Completed")