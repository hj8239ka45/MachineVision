# -*- coding: utf-8 -*-
"""
Created on Tue May 26 12:55:07 2020

@author: hj823
"""

import numpy as np
import cv2
import pyzbar.pyzbar as zb
import os


img = cv2.imread("qr0526_1.jpg",1)
img = cv2.resize(img,(756,756))
r = zb.decode(img)
for i in range(len(r)):
    (x, y, w, h) = r[i].rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
    cv2.putText(img,"%d"%i,
                    (x, y),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255))#,cv2.LINE_AA
cv2.imshow("qr0526_1",img)


print(r[0])
# =============================================================================
# print(r[0].data)
# print(r[0].rect[0],r[0].rect[1])
# print(r[1].data)
# print(r[2].data)
# =============================================================================


# =============================================================================
# im0 = cv2.imread("Position1(z69cm)_Cam0.jpg")
# im1 = cv2.imread("Position1(z69cm)_Cam1.jpg")
# upper = np.array([107, 220, 298])
# lower = np.array([ 67, 120, 198] )
# l = 18
# a = []
# b = []
# for i in range(0,2):
#     if i==0:
#         img = im0
#     elif i==1:
#         img = im1
#     w, h, _ = img.shape
#     k = np.ones((3,3))
#     mask = cv2.inRange(img,lower,upper)
#     eroded = cv2.erode(mask,k,iterations = 1)
#     dilated = cv2.dilate(eroded,k,iterations = 3)
#     _, contours, _ = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#     cnt_max = max(contours,key = cv2.contourArea)
#     rect = cv2.minAreaRect(cnt_max)
#     box = cv2.boxPoints(rect)
#     #return 4*2 np vertex
#     box = np.int0(box)
#     
#     if i == 0:
#         cv2.drawContours(im0,[box],0,(0,0,255),2)
#         f = 593 #pixel
#     if i == 1:
#         cv2.drawContours(im1,[box],0,(0,0,255),2)
#         f = 675 #pixel
#     U = rect[0][0];V = rect[0][1]; 
#     cv2.circle(img,(int(U),int(V)),5,(255,0,0),-1)
#     u,v = U-h/2,-V+w/2
#     print(U)
#     print(V)
#     alpha = u/f
#     beta = v/f
#     a.append(alpha)
#     b.append(beta)
#     if i == 0:
#         cv2.putText(im0,"(Alpha,Beta)=(%0.3f,%0.3f)"%(alpha,beta),
#                     (400,465),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255))#,cv2.LINE_AA
#     if i == 1:
#         cv2.putText(im1,"(Alpha,Beta)=(%0.3f,%0.3f)"%(alpha,beta),
#                     (350,425),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255))#,cv2.LINE_AA
# 
# x = (l/2)*(np.tan(a[0])+np.tan(a[1]))/(np.tan(a[0]-np.tan(a[1])))
# z = l/(np.tan(a[0]-np.tan(a[1])))
# y = z*np.tan(b[0])
# 
# print('x',x)
# print('y',y)
# print('z',z)
# 
# cv2.imshow("Image0",im0)
# cv2.imshow("Image1",im1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 
# =============================================================================
