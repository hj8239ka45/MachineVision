# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:16:55 2020
W11:
    dist. measure
針孔成像 : 使物體可以清楚成像於非像距
@author: hj823
"""
print(__doc__)

# =============================================================================
# import numpy as np
# import cv2
# im = cv2.imread("A4paper70cm.jpg")
# img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(img,(5,5),0)
# a,thresh = cv2.threshold(blur,150,255,cv2.THRESH_BINARY_INV)
# 
# #low thresh  high thresh 建議1:2<->1:3
# edged = cv2.Canny(thresh,35,125)
# _,contours,_ = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# 
# # =============================================================================
# # Alist = []
# # for c in contours:
# #     Alist.append(cv2.contourArea(c))
# # print("max area",max(Alist))
# # cv2.drawContours(im,contours,Alist.index(max(Alist)),(0,0,255),3)
# # =============================================================================
# cnt_max = max(contours,key = cv2.contourArea)#以key作為篩選
# cv2.drawContours(im,[cnt_max],0,(0,0,255),2)
# cv2.imshow("dfd",im)
# =============================================================================


# =============================================================================
# import numpy as np
# import cv2
# 
# def findMarker(img):
#     img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(img1,(5,5),0)
#     a,thresh = cv2.threshold(blur,150,255,cv2.THRESH_BINARY_INV)
#     #low thresh  high thresh 建議1:2<->1:3
#     edged = cv2.Canny(thresh,35,125)
#     _,contours,_ = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#     cnt_max = max(contours,key = cv2.contourArea)#以key作為篩選
#     return cnt_max
# if __name__ == "__main__":
#     img = cv2.imread("A4paper70cm.jpg")
#     contour = findMarker(img)
#     #最小外接矩形
#     rect = cv2.minAreaRect(contour)
#     #return tuple (中心)、(寬高)、旋轉角度
#     box = cv2.boxPoints(rect)
#     #return 4*2 np 矩陣頂點座標
#     box = np.int0(box)
#     #浮點轉整數
#     cv2.drawContours(img,[box],0,(0,0,255),2)
#     cv2.imshow("dfd",img)
# =============================================================================


# =============================================================================
# import numpy as np
# import cv2
# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame1 = cap.read()
#     img1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(img1,(5,5),0)
#     a,thresh = cv2.threshold(blur,80,255,cv2.THRESH_BINARY_INV)
#     #low thresh  high thresh 建議1:2<->1:3
#     _,contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#     cnt_max = max(contours,key = cv2.contourArea)#以key作為篩選
#     rect = cv2.minAreaRect(cnt_max)
#     #return tuple (中心)、(寬高)、旋轉角度
#     box = cv2.boxPoints(rect)
#     #return 4*2 np 矩陣頂點座標
#     box = np.int0(box)
#     #浮點轉整數
#     cv2.drawContours(frame1,[box],0,(0,0,255),2)
#     w = rect[1][0]
#     #text:string (座標) 字型 大小 顏色
#     cv2.putText(frame1,"w=%d"%w,(10,40),cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 255))#,cv2.LINE_AA
#     cv2.imshow("frame",thresh)
#     cv2.imshow("dfd",frame1)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     
# cv2.destroyAllWindows()
# cap.release()
# =============================================================================

import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame1 = cap.read()
    img1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(img1,(5,5),0)
    a,thresh = cv2.threshold(blur,80,255,cv2.THRESH_BINARY_INV)
    #low thresh  high thresh 建議1:2<->1:3
    _,contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnt_max = max(contours,key = cv2.contourArea)#以key作為篩選
    rect = cv2.minAreaRect(cnt_max)
    #return tuple (中心)、(寬高)、旋轉角度
    box = cv2.boxPoints(rect)
    #return 4*2 np 矩陣頂點座標
    box = np.int0(box)
    #浮點轉整數
    cv2.drawContours(frame1,[box],0,(0,0,255),2)
    w = rect[1][0]
    #text:string (座標) 字型 大小 顏色
    cv2.putText(frame1,"w=%d"%w,(10,40),cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 255))#,cv2.LINE_AA
    cv2.imshow("frame",thresh)
    cv2.imshow("dfd",frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
cap.release()




