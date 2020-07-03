# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# =============================================================================
# import numpy as np
# print(np.pi)
# print(np.sin(30/180*np.pi))
# print(np.sin(90/180*np.pi))
# 
# a = np.array([[1,2,3],[7,8,9]])
# print(a)
# 
# =============================================================================

# =============================================================================
# 入射波與s篇正垂直
# 入射波與p篇正平行
# =============================================================================

# Q1
# =============================================================================
# import numpy as np
# print("cal. the reflective rate")
# theta_i = eval(input("input a injected angle: "))/180*np.pi
# n1 = eval(input("input a reflective coeffiction n1: "))
# n2 = eval(input("input a reflective angle: "))
# 
# Rs_up_1 = n1*np.cos(theta_i)
# Rs_up_2 = n2*(1-(n1/n2*np.sin(theta_i))**2)**0.5
# Rs_up = Rs_up_1 - Rs_up_2
# Rs_down = Rs_up_1 + Rs_up_2
# Rs = (Rs_up/Rs_down)**2
# print("Reflection rate(Rs): ",Rs)
# 
# Rp_up_1 = n1*(1-(n1/n2*np.sin(theta_i))**2)**0.5
# Rp_up_2 = n2*np.cos(theta_i)
# Rp_up = Rp_up_1 - Rp_up_2
# Rp_down = Rp_up_1 + Rp_up_2
# Rp = (Rp_up/Rp_down)**2
# print("Reflection rate(Rp): ",Rp)
# =============================================================================


# =============================================================================
# import numpy as np
# x1 = [1,2]
# x2 = [3,4]
# y = x1+x2
# print(y)
# y = np.add(x1,x2)
# print(y)
# x1 = [1,2]
# x1 = [1,2]
# y = np.sin(x1)+np.sin(x2)
# print(y)
# x1 = np.array([1,2])
# x2 = np.array([3,4])
# y = x1+x2
# print(y)
# x1 = np.array([1,2])
# x2 = np.array([3,4])
# y = np.multiply(x1,x2)
# print(y)
# x1 = np.array([1,2])
# x2 = np.array([3,4])
# y = x1*x2
# print(y)
# x1 = np.array([[1],[2]])
# x2 = np.array([3,4])
# y = x1*x2
# print(y)
# x1 = np.array([[1],[2]])
# x2 = np.array([3,4])
# y = np.multiply(x1,x2)
# print(y)
# 
# =============================================================================

# Q2
# =============================================================================
# import numpy as np
# import matplotlib.pyplot as plt
# 
# xL = [1,2,3]
# yL = [4,5,6]
# 
# xn = np.array(xL)
# yn = np.sin(xn)
# 
# plt.title("fig")
# plt.plot(xL,yL,'o-r',xn,yn,'x-g')
# plt.show()
# 
# x = np.linspace(-10,10,1000)
# y = x**2 + x + 1
# plt.plot(x,y)
# plt.show()
# =============================================================================




