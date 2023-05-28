import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier(r"P:\DSA practice\images\haar_face.xml")

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

people = os.listdir('P:\DSA practice\Face recognizer')

img = cv.imread(r"P:\DSA practice\validation_image\OIP.jpg")
gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)


faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'label = {people[label]} with a confidence of {confidence}')
    sv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=1)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness = 1)
cvcv.imshow('Detected Face', img)

cv.waitKey(0)