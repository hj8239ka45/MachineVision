# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 04:23:17 2020

@author: hj823
"""

import numpy as np
import matplotlib.pyplot as plt
theta = np.linspace(0,90,100)
theta_i = theta/180*np.pi
n1 = 1
n2 = np.linspace(1.3,1.7,100)
Theta_i,N2 = np.meshgrid(theta_i,n2)
#formula
Rp_up_1 = n1*(1-(n1/N2*np.sin(Theta_i))**2)**0.5
Rp_up_2 = N2*np.cos(Theta_i)
Rp_up = Rp_up_1 - Rp_up_2
Rp_down = Rp_up_1 + Rp_up_2
Rp = (Rp_up/Rp_down)**2

#label
plt.title("HW3: Rp")
plt.xlabel("theta")
plt.ylabel("n2")
#print("Reflection rate(Rp): ",Rp)
plt.imshow(Rp,cmap="rainbow")
#adjust the axis limit and display
plt.axis('auto')
plt.xlim(0,90)
plt.ylim(1.3,1.7)
#adjust the scale
xtick = np.linspace(0,90,5)
ytick = np.linspace(1.3,1.7,5)
plt.xticks(xtick)
plt.yticks(ytick)

plt.show()