# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:30:03 2020

@author: hj823
"""

import numpy as np
import cv2


global mask;

cap = cv2.VideoCapture(0)
upper = np.array([120,136,255])
lower = np.array([80,36,141])
while True:
    ret, frame = cap.read()
    w, h, _ = frame.shape
    
    w_c = int(w/2)
    h_c = int(h/2)
    
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    k = np.ones((3,3))
    
    mask = cv2.inRange(frame,lower,upper)
    eroded = cv2.erode(mask,k,iterations = 1)
    dilated = cv2.dilate(eroded,k,iterations = 3)
    try:
        _, contours, _ = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnt_max = max(contours,key = cv2.contourArea)
        rect = cv2.minAreaRect(cnt_max)
        box = cv2.boxPoints(rect)
        #return 4*2 np vertex
        box = np.int0(box)
        
        cv2.drawContours(frame,[box],0,(0,0,255),2)
    
        f = 600 #pixel
        A = int( rect[0][1])*-1 + w_c
        B = int( rect[0][0]) - h_c
        
        alpha = B/f*180/np.pi
        beta  = A/f*180/np.pi
        print('Alpha',alpha)
        print('Beta',beta)
        cv2.putText(frame,"(Alpha,Beta)=(%0.2f,%0.2f)"%(alpha,beta),
                    (400,465),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255))#,cv2.LINE_AA
        cv2.imshow("Image",frame)
    except:
        print("Adjust the mask range")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cv2.destroyAllWindows()
cap.release()
