# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:45:02 2020
find d#(micrometer)
@author: hj823
"""

import cv2
import numpy as np

d = 100#(micrometer)
L = 10#(cm)

img1 = cv2.imread("p1.jpg",0)
img2 = cv2.imread("p2.jpg",0)

strong_1D_img1 = img1[0][:]
strong_1D_img2 = img2[0][:]

Peak1 = []
Peak2 = []
peak_center_1 = []
peak_center_2 = []
tmp1 = 0
tmp2 = 0
for i in range(0,len(strong_1D_img1)):
    if(strong_1D_img1[i]>240):
        if i == tmp1+1:
            Peak1.append(i)
        elif Peak1!=[]:
            p1 = np.sum(Peak1)/len(Peak1)
            print(Peak1)
            peak_center_1.append(p1)
            Peak1 = []
        if Peak1 == []:
            Peak1.append(i)
        tmp1 = i
        
    if(strong_1D_img2[i]>240):
        if i == tmp2+1:
            Peak2.append(i)
        elif Peak1!=[]:
            p2 = np.sum(Peak2)/len(Peak2)
            peak_center_2.append(p2)
            Peak2 = []
        if Peak2 == []:
            Peak2.append(i)
        tmp2 = i
delta_y_1 = (peak_center_1[3] - peak_center_1[2])#亮紋距離
delta_y_2 = (peak_center_2[3] - peak_center_2[2])#亮紋距離

x = d*delta_y_1/delta_y_2
print(x,'micrometer')