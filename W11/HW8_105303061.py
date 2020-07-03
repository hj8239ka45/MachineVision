# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:21:44 2020
camera calibration & find the dist.
@author: hj823
"""

import numpy as np
import cv2

W = 10      # width of picture(cm)
p = -1.0    # width of pixel(init. value)
d = 50      # dist. between cam. & picture(cm)
f = p*d/W   # init. focal length
D = 0       # measure dist.

cap = cv2.VideoCapture(0)


def findfocal(rect,p,d,W):
    
    p = rect[1][0]
    f = p*d/W
    return f

while True:
    ret, frame1 = cap.read()
    img1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(img1,(5,5),0)
    a,thresh = cv2.threshold(blur,80,255,cv2.THRESH_BINARY_INV)
    #low thresh  high thresh recommend: 1:2<->1:3
    _,contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    try:
        cnt_max = max(contours,key = cv2.contourArea)#以key作為篩選
        rect = cv2.minAreaRect(cnt_max)
        #return tuple data
        box = cv2.boxPoints(rect)
        #return 4*2 np vertex
        box = np.int0(box)
        #float to integer
        cv2.drawContours(frame1,[box],0,(0,0,255),2)
        print("dist.",D)
    except:
        print("can't catch the contour")
    D = f*W/rect[1][0]
    #text
    cv2.putText(frame1,"dist. = %.2f cm"%D,(10,40),cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 255))#,cv2.LINE_AA
    cv2.imshow("frame",thresh)
    cv2.imshow("dfd",frame1)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    #calibration when d = 50cm, press button 'c'
    if cv2.waitKey(30) & 0xFF == ord('c'):
        f = findfocal(rect,p,d,W)
        Str = "calibrating..."
        cv2.putText(frame1,"%s"%Str,(10,80),cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 255))
        cv2.imshow("frame",thresh)
        cv2.imshow("dfd",frame1)
        cv2.waitKey(1000)

cv2.destroyAllWindows()
cap.release()
   
    
