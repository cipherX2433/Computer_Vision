import os
import numpy as np
import cv2 as cv

people = []

for i in os.listdir(r'C:\vs_files\OpenCV\myenv\faces'):
    people.append(i)

print(people)

DIR = r'C:\vs_files\OpenCV\myenv\faces'

feature = []
labels = []

haar_cascade = cv.CascadeClassifier('haar_face.xml')

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                feature.append(faces_roi)
                labels.append(label)

create_train()
print('Training Done---------->')


# print(f'Length os the features = {len(feature)}')
# print(f'Length os the labels = {len(labels)}')

feature = np.array(feature, dtype=object)
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Train the recognizer on the features list and labels list
face_recognizer.train(feature, labels)

face_recognizer.save('face_trained.yml')

np.save('feature npy', feature)
np.save('labels.npy', labels)