# -*- coding: utf-8 -*-
"""
Created on Tue May 26 13:04:42 2020

@author: hj823
"""
import cv2
import numpy as np

def pick_color(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = image[y,x]
        print(x,y)
        #you might want to adjust the ranges(+-10, etc):
        upper =  np.array([pixel[0] + 20, pixel[1] + 50, pixel[2] + 50])
        lower =  np.array([pixel[0] - 20, pixel[1] - 50, pixel[2] - 50])
        #print(pixel, lower, upper)
        image_mask = cv2.inRange(image,lower,upper)
        cv2.imshow("mask",image_mask)
image = cv2.imread("qr0526_1.jpg")
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', pick_color)
cv2.imshow("Image",image)

