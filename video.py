import cv2
import numpy as np
cap=cv2.VideoCapture("C:\\Users\KESHAV TRIKHA\\OneDrive\\Desktop\\TWD\\Rick.mp4")
face_cascade=cv2.CascadeClassifier("D:\\Anaconda\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
while(True):
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 255, 0), 3)
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
