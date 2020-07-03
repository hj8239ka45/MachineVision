# -*- coding: utf-8 -*-
"""
Created on Sat May 30 14:27:23 2020
    先縮小圖檔 : 原圖檔太大
@author: hj823
"""
import numpy as np
import cv2
import pyzbar.pyzbar as zb

im0 = cv2.imread("qr0526_1.jpg")
im1 = cv2.imread("qr0526_2.jpg")
im0 = cv2.resize(im0,(756,756))
im1 = cv2.resize(im1,(756,756))
l = 4   #cm
a = []
b = []
f = 5000    #pixel
for i in range(0,2):
    if i==0:
        img = im0
    elif i==1:
        img = im1
    
    
    r = zb.decode(img)
    for j in range(len(r)):
        (x, y, w, h) = r[j].rect
        if i==0:
            cv2.rectangle(im0, (x, y), (x + w, y + h), (255, 255, 0), 2)
            cv2.putText(im0,"%d"%j,
                            (x, y),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255))#,cv2.LINE_AA
        elif i==1:
            cv2.rectangle(im1, (x, y), (x + w, y + h), (255, 255, 0), 2)
            cv2.putText(im1,"%d"%j,
                            (x, y),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255))#,cv2.LINE_AA

        
        center_qr = (int((x+x+w)/2), int((y+y+h)/2))
        cv2.circle(img,center_qr,5,(255,0,0),-1)
        
        U = center_qr[0];V = center_qr[1]
        img_w, img_h, _ = img.shape
        u,v = U-img_h/2,-V+img_w/2
        print(U)
        print(V)
        alpha = u/f
        beta = v/f
        a.append(alpha)
        b.append(beta)

for i in range(len(r)):
    x = (l/2)*(np.tan(a[i])+np.tan(a[i+len(r)]))/(np.tan(a[i]-np.tan(a[i+len(r)])))
    z = l/(np.tan(a[i]-np.tan(a[i+len(r)])))
    y = z*np.tan(b[i])
    print("QR CODE %d"%i)
    print('(x,y,z)=(%0.2f\t,\t%0.2f\t,\t%0.2f)'%(x,y,z))
cv2.imshow("Image0",im0)
cv2.imshow("Image1",im1)
cv2.waitKey(0)
cv2.destroyAllWindows()