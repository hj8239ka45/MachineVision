# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 22:19:49 2020
HW1
學號:105303061
姓名:陳崴淇
# =============================================================================
# calculate the radius of coin in the water
# =============================================================================
@author: hj823
"""
import math
L = eval(input("L(dist.(cm) between eyes and water surface):"))
D = eval(input("D(depth(cm) of water):"))
theta = eval(input("theta(perspective):"))
n = eval(input("n(refractive index of water):"))
radius = L*math.tan(theta/2/180*math.pi) + D*math.tan(theta/2/n/180*math.pi)
diameter = radius*2
print("Diameter of coin:",diameter)