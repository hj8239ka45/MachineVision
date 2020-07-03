# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 22:22:15 2020
HW2
學號:105303061
姓名:陳崴淇
# =============================================================================
# test the chance of Game Theory
# this code use jit funtion to accelerate the loop,
# so you can turn up the number of round in experiment.
# **** you need to install a package about numba by using "pip install numba" in the console ****
# =============================================================================
@author: hj823
"""
import random as rd
from matplotlib import pyplot as plt
from numba import jit
#use jit(just in time) mode to accelerate the while loop function
print(__doc__)
@jit
def fun(A,B,N):
    List = []
    Nround = N
    tmp = 0 #times of A earn to B
    while Nround>0:
        a = A
        Nround = Nround-1
        while a!=0 and a!=B:
            x = rd.randint(0,1)
            if x:
                a = a + 1
            else:
                a = a - 1
        if a==B:
            tmp = tmp + 1
        List.append(tmp/(N-Nround))
    print("the chance of success(In experiment)",tmp/N)#probability of practice
    print("the chance of success(In theory)",A/B)
    return List,tmp

Nround = eval(input("How many round do you to do:"))
N = Nround #total round
A = eval(input("How much money do you have:"))
B = eval(input("How much money do you want to get after playing:"))
print("test ",Nround,"round")
#get the data from fun of while loop
List,tmp = fun(A,B,N)

#數據可視化
print("Record the data of success and lose, and put it to the figure.")
plt.title("the chance of success")
plt.plot(range(1,N+1),List,label="In experiment")
plt.plot(range(1,N+1),[A/B for i in range(1,N+1)],label="In theory")
plt.xlabel("Nround(times)")
plt.ylabel("The chance")
plt.legend()
plt.show()

