import cv2
import numpy as np
import face_recognition

imgSundar = face_recognition.load_image_file('Train Images/sundarpichai.jpg')
imgSundar = cv2.cvtColor(imgSundar,cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('Test Images/sundarp.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgSundar)[0]
encodeSundar = face_recognition.face_encodings(imgSundar)[0]
cv2.rectangle(imgSundar,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeSundarTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

results = face_recognition.compare_faces([encodeSundar],encodeSundarTest)
faceDis = face_recognition.face_distance([encodeSundar],encodeSundarTest)
cv2.putText(imgTest,f'{results} {round(faceDis[0],3)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
print(results)


cv2.imshow('Sundar Pichai',imgSundar)
cv2.imshow('Test Sundar',imgTest)

cv2.waitKey(0)