# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 17:04:04 2020
    Press button "o" to get frame xyz & uv info
    Press button "q" to quite the application
@author: hj823
"""
print(__doc__)
#視2角點間距離為1
import cv2
import numpy as np
import os
import glob #方便找圖片->找相似檔案

objp = np.zeros((6*7,3),np.float32) #[42x3]
#T 轉置 reshape 至兩行
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2) #[42x3]的前兩行

#存取角點座標 以及 影像角點位置
objpoints = [] #3d
imgpoints = [] #2d

winSize = (11,11)
zeroZone = (-1,-1)
criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,30,0.001)



cap = cv2.VideoCapture(0)
i = 0
while True:
    rev, frame = cap.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if cv2.waitKey(20) & 0xFF == ord('o'):
        print("pressed o")
        #dir_name = os.getcwd()
        #direct = dir_name+"\\tmp\\chess%d.jpg"%i
        #rev = cv2.imwrite(direct,frame)
        #print(rev)
        #i = i+1
        img = frame
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret,corners = cv2.findChessboardCorners(gray,(7,6))
        if ret == True:
            corners2 = cv2.cornerSubPix(gray, corners, winSize, zeroZone, criteria)
            objpoints.append(objp)
            imgpoints.append(corners2)
            
            #draw and display
            img = cv2.drawChessboardCorners(img, (7,6), corners2, ret)
            cv2.imshow("img",img)
            cv2.waitKey(100)
cap.release()