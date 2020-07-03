# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:34:34 2020
    HW4
@author: hj823
"""

import numpy as np
import matplotlib.pyplot as plt
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
    ## HW4
    count_data = []
    A = np.linspace(-1,1,1000)
    H = np.linspace(1,1,1000)
    h,alpha = trace(alpha0 = A,h0 = H,l=2.1)
    h_space = 11
    h_delta = 0.2
    Range = np.linspace(-2,0,h_space)
    for i in Range[:-1]:
        count = np.count_nonzero((h>i) & (h<i+h_delta))
        count_data.append(count)
    #let the data in the center of data range
    Range_data = (Range[:-1]+Range[1:])/2
    plt.plot(Range_data,count_data,'o--')
    plt.xlabel("h")
    plt.ylabel("num")
    xtick = np.linspace(-2,0,11)
    plt.xticks(xtick)    
    