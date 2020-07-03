# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 21:51:28 2020
    Mask & Display:
        https://www.luoow.com/dc_hk/106714937
    cv2.bitwise:
        https://blog.csdn.net/weixin_35732969/article/details/83748054
@author: hj823
"""
import cv2
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image
from PIL import ImageOps

# draw object in cv2
def draw_obj(frame, width, height, size, center):
    data = glReadPixels(0, 0, width, height, GL_RGBA, GL_UNSIGNED_BYTE)
    image = Image.frombytes("RGBA", (width, height), data)
    image = np.array(ImageOps.flip(image))
    image = cv2.cvtColor(image,cv2.COLOR_RGBA2BGRA)
    r,g,b,a = cv2.split(image)
    rgb_obj = cv2.merge((r,g,b))
    #cv2.imshow("obj",image)  
    copyframe = frame
    #print("s:",size)
    #print("c:",center)
    if size is None and center is None:
        print("no qr code")
    else:
        # 用alpha通道作為mask 
        mask = a
        mask_inv = cv2.bitwise_not(mask)
        (cx,cy) = (int(center[0]), int(center[1]))
        # 原圖ROI 
        dhx = int(size[0]/2)
        dhy = int(size[1]/2)
        try:
            bg_roi = copyframe[cy-dhy:cy+dhy,cx-dhx:cx+dhx]
            #print(bg_roi.shape)
            
            # 原圖ROI中提取放obj的區域 
            bg_roi = bg_roi.astype(float) 
            mask_inv = cv2.merge((mask_inv,mask_inv,mask_inv)) 
            alpha = mask_inv.astype(float)/255
            # 相乘之前保證兩者大小一致（可能會由於四捨五入原因不一致） 
            alpha = cv2.resize(alpha,(bg_roi.shape[1],bg_roi.shape[0]))
            #print("alpha size: ",alpha.shape)
            #print("bg_roi size: ",bg_roi.shape)
            bg = cv2.multiply(alpha, bg_roi)
            bg = bg.astype('uint8')

            cv2.imshow("bg",bg)
            
            # 提取obj區域 
            obj = cv2.bitwise_and(rgb_obj,rgb_obj,mask = mask)
            # 相加之前保證兩者大小一致（可能會由於四捨五入原因不一致） 
            im_obj = cv2.resize(obj,(bg_roi.shape[1],bg_roi.shape[0])) 
            # 兩個ROI區域相加 
            add_obj = cv2.add(bg,im_obj) 
            # cv2.imshow("add_hat",add_hat) 
            # 把添加好帽子的區域放回原圖
            copyframe[cy-dhy:cy+dhy,cx-dhx:cx+dhx] = add_obj
        except:
            print("boundary error")  
    cv2.imshow("copy",copyframe)
