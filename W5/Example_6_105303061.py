# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 15:51:47 2020
     EX6
@author: hj823
"""

import numpy as np
def trace(f=1,l0=2,h0=1,alpha0=0,l=2):
     A = np.array([[1,l0],[0,1]])
     B = np.array([[1,0],[-1/f,1]])
     C = np.array([[1,l],[0,1]])
     Y0 = [h0,alpha0]
     Y = np.dot(C,np.dot(B,np.dot(A,Y0)))
     h = Y[0]
     alpha = Y[1]
     return h,alpha

if __name__ == "__main__":
    #不成像 h(alpha0)!=const.
    A = np.linspace(-1,1,1000)
    H = np.linspace(1,1,1000)
    h,alpha = trace(alpha0 = A,h0 = H,l=3)
    count = np.count_nonzero((h<-2) & (h>-2.1))
    print("the height of light in the range of -2~-2.1: ",count," times")