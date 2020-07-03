# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 23:07:43 2020
HW5
@author: hj823
"""

import cv2
import numpy as np
img = np.zeros([300,300,3])
img[:][:] = [255,255,255]
center = [100,100]
radius = 140 #radius<150
x = np.linspace(-radius,radius,80000)
for i in x:
    j = (radius**2 - i**2)**0.5
    if i >299 or j>299:
        break;
    img[int(i)+150,int(j)+150] = [0,0,255]
    img[int(i)+150,-int(j)+150] = [0,0,255]
cv2.imshow("img",img)