import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime


path = 'Train Images'
images = []
classList = []
myList = os.listdir(path)
print(myList)


for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classList.append(os.path.splitext(cls)[0])
print(classList)

def findEncode(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def MarkAttendance(name):
    with open('Attendance.csv','r+') as f:
        datalist = f.readlines()
        namelist = []
        for line in datalist:
            entry = line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstring}')



encodeList = findEncode(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    success,img  = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    currentFrame = face_recognition.face_locations(imgS)
    encode = face_recognition.face_encodings(imgS,currentFrame)

    for encodeFace,faceLoc in zip(encode,currentFrame):
        matches = face_recognition.compare_faces(encodeList,encodeFace)
        faceDis = face_recognition.face_distance(encodeList,encodeFace)

        print(faceDis)

        matchIndex = np.argmin(faceDis)
        if matches[matchIndex]:
            name = classList[matchIndex].upper()
            print(name)
            y1,x2,y2,x1 = faceLoc
            y1,x2,y2,x1 = 4*y1,4*x2,4*y2,4*x1
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            MarkAttendance(name)

    cv2.imshow('WebCam ', img)
    cv2.waitKey(1)


