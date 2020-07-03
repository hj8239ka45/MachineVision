# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:19:35 2020
HW6
105303061 
using the rolling ball video
tracking the ball & cal. the velocity

the vel. in the beginning & end is not accuracy
@author: hj823
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

tmp1 = 0
tmp2 = 0
cap = cv2.VideoCapture("34781t.mp4")
ball_radius = 2.5#cm (Default)
print(__doc__)
vel = []
while(True):
    #get fps to cal. sec.
    fps =cap.get(cv2.CAP_PROP_FPS)
    sec = 1/fps
    #print("fps:",fps)
    
    #get the frame in time
    ret, frame1 = cap.read()
    #interval time
    cv2.waitKey(int(1000*sec))
    #get the frame in time
    ret, frame2 = cap.read()
    
    #determine the video playing state:    playing or not
    if ret:
        #cal. the difference between frame1 & frame2
        diff = cv2.absdiff(frame1,frame2)
        #gray level
        gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
        #blur preocess
        blur = cv2.GaussianBlur(gray,(15,15),0)
        #threshold process
        a,thresh = cv2.threshold(blur,10,255,cv2.THRESH_BINARY)
        b = np.where(thresh==255)
        #print(b)
        
        #void data b is NaN, which is occured due to unnoticeable difference or low strength data
        #first: using try and except to record the last time and keep from the error
        #because the difference is too small, you can use the data of last time as one of this time
        #second: find high contrast condition
        try:
            #(X,Y)mass center
            Y = int(np.average(b[0]))
            X = int(np.average(b[1]))
            tmpx = X
            tmpy = Y
            
            #cal. ball radius in the cap.
            cap_radius = ((b[1].max()-b[1].min())**2+(b[0].max()-b[0].min()))**0.5        
            #print("r:",cap_radius)
        except:
            print("====== small diff. or low contrast ======")
            X = tmpx
            Y = tmpy
    
        #this time - last time 
        diff_x = (X-tmp1)/2
        diff_y = (Y-tmp2)/2
        
        #scale (cm/pixel)
        scale = ball_radius/cap_radius
        #distance (cm)
        dist = ((diff_x*scale)**2+(diff_y*scale)**2)**0.5
        #velocity (m/s)
        vel.append(dist/sec/100)
        print("vel:",vel[-1],"m/s",len(vel))
        
    #    a,thresh = cv2.threshold(blur,10,255,cv2.THRESH_BINARY)    
    #    cv2.imshow("dfv2",blur)
    #    cv2.imshow("dfv",diff)
        cv2.circle(frame2,(X,Y),20,(255,0,0),5)
        cv2.imshow("frame",frame2)
        
        
        #未按鍵時 0xff = 255
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cv2.destroyAllWindows()
cap.release()

#index 50 ~ 90 : release the ball
plt.plot(vel[50:90])
plt.xlabel("data index")
plt.ylabel("vel. (m/s)")
plt.show()
