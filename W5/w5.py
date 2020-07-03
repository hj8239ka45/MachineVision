# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:01:45 2020

@author: hj823
"""

# =============================================================================
# import numpy as np
# 
# def reflective_fun(theta_i,n1,n2):
#     Rs_up_1 = n1*np.cos(theta_i)
#     Rs_up_2 = n2*(1-(n1/n2*np.sin(theta_i))**2)**0.5
#     Rs_up = Rs_up_1 - Rs_up_2
#     Rs_down = Rs_up_1 + Rs_up_2
#     Rs = (Rs_up/Rs_down)**2
# 
#     Rp_up_1 = n1*(1-(n1/n2*np.sin(theta_i))**2)**0.5
#     Rp_up_2 = n2*np.cos(theta_i)
#     Rp_up = Rp_up_1 - Rp_up_2
#     Rp_down = Rp_up_1 + Rp_up_2
#     Rp = (Rp_up/Rp_down)**2
# 
#     return Rs,Rp
# 
# print("cal. the reflective rate")
# theta = eval(input("input a injected angle: "))/180*np.pi
# n1 = eval(input("input a reflective coeffiction n1: "))
# n2 = eval(input("input a reflective coeffiction n2: "))
# 
# Rs,Rp = reflective_fun(theta,n1,n2)
# print("Rs:",Rs)
# print("Rp:",Rp)
# =============================================================================

# =============================================================================
# import random
# #sort from small to large
# def sort_num(x):
#     for i in range(len(x)):
#         for j in range(len(x)):
#             if x[i]<x[j]:
#                 tmp = x[j]
#                 x[j] = x[i]
#                 x[i] = tmp
#     return x
# a = [i for i in range(20)]
# random.shuffle(a)
# print(a)
# 
# sort_num(a)
# print(a)
# 
# =============================================================================



# =============================================================================
# import numpy as np
# def fun(alpha0):
#     A = np.array([[1,2],[0,3]])
#     B = np.array([[1,0],[2,1]])
#     C = np.array([[1,5],[0,1]])
#     Y0 = [1,alpha0]
#     Y = np.dot(np.dot(np.dot(A,B),C),Y0)
#     h = Y[0]
#     alpha = Y[1]
#     return h,alpha
# a = 2*(np.random.randn()-0.5)
# h,alpha = fun(a)
# print(h)
# print(alpha)
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
def trace(f=1,l0=2,h0=1,alpha0=0,l=2):
     A = np.array([[1,l0],[0,1]])
     B = np.array([[1,0],[-1/f,1]])
     C = np.array([[1,l],[0,1]])
     Y0 = [h0,alpha0]
     Y = np.dot(np.dot(np.dot(A,B),C),Y0)
     h = Y[0]
     alpha = Y[1]
     return h,alpha

if __name__ == "__main__":
    #不成像 h(alpha0)!=const.
    for i in range(1000):
        a = 2*(np.random.randn()-0.5)
        h,alpha = trace(alpha0 = a,l=4)
        plt.plot(h,alpha,'o')
    plt.xlabel("h")
    plt.ylabel("alpha")
    plt.show()
    