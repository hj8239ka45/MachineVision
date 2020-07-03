# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:37:26 2020

@author: hj823
"""
import numpy as np
import cv2

'''數字
       筆電 -> 內建鏡頭
   影音檔
       抓取影片
'''
# =============================================================================
# cap = cv2.VideoCapture("test.mp4")
# while(True):
#     #擷取即時畫面
#     ret, frame = cap.read()
#     cv2.imshow("frame",frame)
#     #判斷按鍵，如果按鍵為q，退出迴圈
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break
#     
# cv2.waitKey(1000)
# #釋放資源
# cap.release()
# cv2.destroyAllWindows()
# 
# =============================================================================

'''
    absdiff : 影像相減 看畫面變化部分分析
    微分運算(平移量少) : 邊緣強度放大
'''

# =============================================================================
# img = cv2.imread("th.jpg")
# grey1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# grey2 = grey1.copy()
# d = 1
# 
# grey2[30:110,30:110] = grey1[30+d:110+d,30+d:110+d]
# diff = cv2.absdiff(grey1,grey2)
# cv2.imshow("dfv",diff)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# =============================================================================

# =============================================================================
# img = cv2.imread("lena.jpg")
# img2 = img.copy()
# w,h,a = img.shape
# d = 3
# 
# img[5:w,5:h,:] = img2[5-d:w-d,5-d:h-d,:]
# diff = cv2.absdiff(img,img2)
# cv2.imshow("dfv",diff)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 
# =============================================================================



# =============================================================================
# cap = cv2.VideoCapture("test.mp4")
# while(True):
#     #擷取即時畫面
#     ret, frame1 = cap.read()
#     cv2.waitKey(100)
#     #擷取即時畫面
#     ret, frame2 = cap.read()
#     diff = cv2.absdiff(frame1,frame2)
#     cv2.imshow("dfv",diff)
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break
# 
# cv2.destroyAllWindows()
# cap.release()
# =============================================================================

'''
    找出變異中心:
        1.差異轉灰階
        2.高斯模糊
        3.閥值
        4.偵測255找質量
'''
cap = cv2.VideoCapture(0)
while(True):
    #擷取即時畫面
    ret, frame1 = cap.read()
    cv2.waitKey(100)
    #擷取即時畫面
    ret, frame2 = cap.read()
    diff = cv2.absdiff(frame1,frame2)
    #gray
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    #blur
    blur = cv2.GaussianBlur(gray,(5,5),0)
    #threshold
    a,thresh = cv2.threshold(blur,10,255,cv2.THRESH_BINARY)
    b = np.where(thresh==255)
    #(X,Y)質量中心
    Y = int(np.average(b[0]))
    X = int(np.average(b[1]))

#    a,thresh = cv2.threshold(blur,10,255,cv2.THRESH_BINARY)    
#    cv2.imshow("dfv2",blur)
#    cv2.imshow("dfv",diff)
    cv2.circle(frame1,(X,Y),20,(255,0,0),5)
    cv2.imshow("frame",frame1)
    
    #未按鍵時 0xff = 255
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

