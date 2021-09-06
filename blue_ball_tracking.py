import cv2
    2 import numpy as np
    3 
    4 cap = cv2.VideoCapture(0)
    5 
    6 while(1):
    7 
    8     # Take each frame
    9     _, frame = cap.read()
   10 
   11     # Convert BGR to HSV
   12     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   13 
   14     # define range of blue color in HSV
   15     lower_blue = np.array([110,50,50])
   16     upper_blue = np.array([130,255,255])
   17 
   18     # Threshold the HSV image to get only blue colors
   19     mask = cv2.inRange(hsv, lower_blue, upper_blue)
   20 
   21     # Bitwise-AND mask and original image
   22     res = cv2.bitwise_and(frame,frame, mask= mask)
   23 
   24     cv2.imshow('frame',frame)
   25     cv2.imshow('mask',mask)
   26     cv2.imshow('res',res)
   27     k = cv2.waitKey(5) & 0xFF
   28     if k == 27:
   29         break
   30 
   31 cv2.destroyAllWindows()
