#import tkinter
import cv2
cam= cv2.VideoCapture(0)# indexing can be higher if more cams are there

while cam.isOpened():
    retrive,frame=cam.read()
    if cv2.waitKey(3)== ord('q'):# q will quit the program
      break
    cv2.imshow('My Cam',frame)
