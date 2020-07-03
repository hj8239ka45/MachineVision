# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:21:31 2020

@author: hj823
"""

#dilat 只針對有值的地方(白色處)擴張 -> 暗區侵蝕
import numpy as np
import cv2

# =============================================================================
# img = cv2.imread("img.png",0)
# a,th = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
# cv2.imshow("befor dilate",th)
# 
# kernel = np.ones((5,5))
# dilated = cv2.dilate(th,kernel,iterations = 10)
# cv2.imshow("after dilate",dilated)
# 
# added = cv2.addWeighted(th,0.5,dilated,0.5,0)
# cv2.imshow('add',added)
# =============================================================================

# =============================================================================
# import matplotlib.pyplot as plt
# 
# img = cv2.imread("img.png")
# imgg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# a,th = cv2.threshold(imgg,200,255,cv2.THRESH_BINARY_INV)
# 
# kernel = np.ones((3,3))
# dilated = cv2.dilate(th,kernel,iterations = 5)
# #cv2.imshow("after dilate",dilated)
# 
# #img,檢索模式,輪廓近似法
# _, contour, _ = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# 
# #抓到的contour數量
# print(len(contour))
# #contour內分別有 多少點紀錄,一維資料內,有xy資料 -> XXX,1,2
# print(contour[5].shape)
# 
# print(contour[0][5][0,1])#有點奇怪
# 
# #畫圖法1
# 
# # =============================================================================
# # for n in range(0,len(contour)):
# #     X = []
# #     Y = []
# #     for i in range(0,len(contour[n])):
# #         x = contour[n][i][0,0]
# #         y = -contour[n][i][0,1]#上下顛倒(+負號)
# #         X.append(x)
# #         Y.append(y)
# #     X.append(X[0])
# #     Y.append(Y[0])
# #     plt.plot(X,Y,'o-')
# # plt.show()
# # cv2.imshow("df",dilated)
# # =============================================================================
# 
# 
# #畫圖法2
# 
# #drawcontour 圖檔,輪廓,index(輪廓編號),color,[optional](粗度,線型...)
# cv2.drawContours(img,contour,0,(255,0,0),2)
# 
# cv2.imshow("ccc",img)
# =============================================================================





# =============================================================================
# import matplotlib.pyplot as plt
# 
# img = cv2.imread("google.png")
# imgg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("imgg",imgg)
# 
# #base on this img. i choose 100 to divide the color data
# a,th = cv2.threshold(imgg,100,255,cv2.THRESH_BINARY)
# 
# kernel = np.ones((3,3))
# dilated = cv2.dilate(th,kernel,iterations = 4)
# cv2.imshow("di",dilated)
# 
# _, contour, _ = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# 
# print(len(contour))
# cv2.drawContours(img,contour,-1,(0,0,255))
# print(contour[0].shape)
# X = contour[0][:,0,0]
# Y = contour[0][:,0,1]
# p = (int((X.max()-X.min())/2),int((Y.max()-Y.min())/2))
# cv2.circle(img,p,10,(255,0,255),-1)
# 
# cv2.imshow("contour img",img)
# =============================================================================

# =============================================================================
# cap = cv2.VideoCapture(0)
# #擷取即時畫面
# ret, frame1 = cap.read()
# cv2.waitKey(1000)
# #擷取即時畫面
# ret, frame2 = cap.read()
# diff = cv2.absdiff(frame1,frame2)
# #gray
# gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
# #blur
# blur = cv2.GaussianBlur(gray,(5,5),0)
# #threshold
# 
# a,th = cv2.threshold(blur,35,255,cv2.THRESH_BINARY)
# kernel = np.ones((3,3))
# dilated = cv2.dilate(th,kernel,iterations = 2)
# cv2.imshow("di",dilated)
# _, contour, _ = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(frame2,contour,-1,(0,0,255))
# cv2.imshow("frame",frame2)
# 
# #未按鍵時 0xff = 255
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cap.release()
# =============================================================================


# =============================================================================
# cap = cv2.VideoCapture("motionPattern_0506.mov")
# while(True):
#     #get fps to cal. sec.
#     fps =cap.get(cv2.CAP_PROP_FPS)
#     sec = 1/fps
#     #print("fps:",fps)
#     #擷取即時畫面
#     ret, frame = cap.read()
#     if ret:
#         #gray
#         gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         #blur
#         blur = cv2.GaussianBlur(gray,(5,5),0)
#         #threshold
#         a,th = cv2.threshold(blur,150,255,cv2.THRESH_BINARY_INV)
#         kernel = np.ones((3,3))
#         dilated = cv2.dilate(th,kernel,iterations = 10)
#         cv2.imshow("di",dilated)
#         _, contour, _ = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#         cv2.drawContours(frame,contour,-1,(0,0,255),2)
#         cv2.imshow("frame",frame)
#     else:
#         break
#     
#     #未按鍵時 0xff = 255
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cv2.destroyAllWindows()
# cap.release()
# =============================================================================

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("google.png")
imgg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("imgg",imgg)

#base on this img. i choose 100 to divide the color data
a,th = cv2.threshold(imgg,100,255,cv2.THRESH_BINARY)

kernel = np.ones((3,3))
dilated = cv2.dilate(th,kernel,iterations = 4)
#cv2.imshow("di",dilated)

_, contour, _ = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# =============================================================================
# #1
# for c in contour:
#     x0 = min(c[:,0,0])
#     y0 = min(c[:,0,1])
#     x1 = max(c[:,0,0])
#     y1 = max(c[:,0,1])
#     cv2.drawContours(img,contour,-1,(0,0,255),2)
#     cv2.rectangle(img,(x0,y0),(x1,y1),(0,0,255),1)
# cv2.imshow("rect",img)
# =============================================================================

# =============================================================================
# #2
# for c in contour:
#     (x,y,w,h) = cv2.boundingRect(c)
#     cv2.drawContours(img,contour,-1,(0,0,255),2)
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
# cv2.imshow("rect",img)
# =============================================================================

for c in contour:
    (x,y,w,h) = cv2.boundingRect(c)
    cv2.drawContours(img,contour,-1,(0,0,255),2)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
    print(int(cv2.arcLength(c,True)),cv2.contourArea(c))
cv2.imshow("rect",img)

    