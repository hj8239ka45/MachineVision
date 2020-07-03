# -*- coding: utf-8 -*-
"""
Created on Tue May  5 14:35:02 2020

@author: hj823
"""

import numpy as np
import cv2
cap = cv2.VideoCapture("viewFromME_video1.mp4")

while(True):
    #get fps to cal. sec.
    fps =cap.get(cv2.CAP_PROP_FPS)
    sec = 1/fps
    #print("fps:",fps)
    
    #get the frame in time
    ret, frame1 = cap.read()

    #blur preocess
    img1 = cv2.GaussianBlur(frame1,(9,9),0)
    #interval time
    cv2.waitKey(1)
    #get the frame in time
    ret, frame2 = cap.read()

    #blur preocess
    img2 = cv2.GaussianBlur(frame2,(9,9),0)

    
    #determine the video playing state:    playing or not
    if ret:
        #cal. the difference between frame1 & frame2
        diff = cv2.absdiff(img1,img2)
        #gray level
        gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)

        #use contour area to divivde the noise
        #if cv2.contourArea(c)<300:
        #   continue
# =============================================================================
#         low_threshold = 80
#         high_threshold = 150
#         img = cv2.Canny(gray, low_threshold, high_threshold)
# =============================================================================
        #threshold process
        a,thresh = cv2.threshold(gray,20,255,cv2.THRESH_BINARY)
    
        cv2.imshow("frame",thresh)
        kernel = np.ones((3,3))
        dilated = cv2.dilate(thresh,kernel,iterations = 5)
        _, contour, _ = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame2,contour,-1,(0,0,255),2)
        cv2.imshow("video",frame2)
        
    else:
        break
    #未按鍵時 0xff = 255
    if cv2.waitKey(int(1000*sec)) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()



