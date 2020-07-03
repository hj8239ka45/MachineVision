# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:12:01 2020

@author: hj823
"""

import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    weight, height, _ = frame.shape
    w_c = int(weight/2)
    h_c = int(height/2)
    
    cv2.line(frame,(h_c,0),(h_c,weight-1),(0,255,0),2)#綠色，3個畫素寬度
    cv2.line(frame,(0,w_c),(height-1,w_c),(0,255,0),2)#綠色，3個畫素寬度
    cv2.circle(frame,(h_c,w_c),10,(0,0,255),2)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()



# =============================================================================
# import numpy as np
# import cv2
# img = cv2.imread("practice0519.png")
# img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 
# weight, height, _ = img.shape
# w_c = int(weight/2)
# h_c = int(height/2)
# 
# blur = cv2.GaussianBlur(img1,(5,5),0)
# a,thresh = cv2.threshold(blur,80,255,cv2.THRESH_BINARY_INV)
# b = np.where(thresh==255)
# A = int( (b[0][-1]-b[0][0])/2 + b[0][0] )*-1 + w_c
# B = int( (b[1][-1]-b[1][0])/2 + b[1][0] ) - h_c
# 
# 
# cv2.line(img,(h_c,0),(h_c,weight-1),(0,255,0),2)#綠色，3個畫素寬度
# cv2.line(img,(0,w_c),(height-1,w_c),(0,255,0),2)#綠色，3個畫素寬度
# cv2.circle(img,(h_c,w_c),10,(0,0,255),2)
# cv2.imshow("frame",img)
# 
# f = 600 #pixel
# length =  (A**2 + B**2)**0.5
# alpha = B/f*180/np.pi
# 
# print('alpha:%0.2f'%alpha,'degree')
# 
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# =============================================================================


# =============================================================================
# import numpy as np
# import cv2
# img = cv2.imread("practice0519.png")
# img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 
# weight, height, _ = img.shape
# w_c = int(weight/2)
# h_c = int(height/2)
# 
# blur = cv2.GaussianBlur(img1,(5,5),0)
# a,thresh = cv2.threshold(blur,80,255,cv2.THRESH_BINARY_INV)
# 
# _,contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# cnt_max = max(contours,key = cv2.contourArea)#以key作為篩選
# rect = cv2.minAreaRect(cnt_max)
# #return tuple data
# 
# box = cv2.boxPoints(rect)
# #return 4*2 np vertex
# box = np.int0(box)
# #float to integer
# cv2.drawContours(img,[box],0,(0,0,255),2)
#     
# b = np.where(thresh==255)
# # =============================================================================
# # A = int( (b[0][-1]-b[0][0])/2 + b[0][0] )*-1 + w_c
# # B = int( (b[1][-1]-b[1][0])/2 + b[1][0] ) - h_c
# # =============================================================================
# 
# A = int(rect[0][1])*-1 + w_c
# B = int(rect[0][0]) - h_c
# 
# 
# cv2.line(img,(h_c,0),(h_c,weight-1),(0,255,0),2)#綠色，3個畫素寬度
# cv2.line(img,(0,w_c),(height-1,w_c),(0,255,0),2)#綠色，3個畫素寬度
# cv2.circle(img,(h_c,w_c),10,(0,0,255),2)
# cv2.imshow("frame",img)
# 
# f = 600 #pixel
# length =  (A**2 + B**2)**0.5
# alpha = B/f*180/np.pi
# 
# print('alpha:%0.2f'%alpha,'degree')
# 
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# =============================================================================

# =============================================================================
# import numpy as np
# import cv2
# 
# img = cv2.imread("picture.jpg")
# L_red = np.array([20,20,40])
# U_red = np.array([230,230,250])
# mask = cv2.inRange(img,L_red,U_red)#圖 下限 上限
# cv2.imshow('mask',mask)
# k = np.ones((3,3))
# 
# eroded = cv2.erode(mask,k,iterations = 1)
# dilated = cv2.dilate(eroded,k,iterations = 3)
# cv2.imshow("c2",dilated)
# _,contours,_ = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img,contours,-1,(0,255,0),2)
# cv2.imshow("frame",img)
# =============================================================================




