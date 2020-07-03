# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# =============================================================================
# #3
# a = eval(input("input your score:"))
# condition1 = a>=90
# condition2 = a>=80
# condition3 = a>=70
# condition4 = a>=60
# 
# if condition1:
#     print("class A")
# elif condition2:
#     print("class B")
# elif condition3:
#     print("class C")
# elif condition4:
#     print("class D")
# else:
#     print("class F")
# =============================================================================

# =============================================================================
# #4
# temp = 0
# for i in range(1,101):
#     if (i%3==0 or i%5==0)and not i%15==0:
#         temp = i+temp
# print(temp)
# =============================================================================

# =============================================================================
# #5
# a = eval(input("input a number:"))
# temp = 1
# for i in range(1,a+1):
#     temp = temp*i
# print(a,'!  =',temp)
# =============================================================================

# =============================================================================
# #6
# import turtle as tu
# x = eval(input("input a number:"))
# tu.color("hotpink")
# tu.pensize(3)#畫筆粗細
# temp = 0#移動次數
# 
# while x!=1:
#     print(x)
#     temp = temp+1
#     if temp%2==0:
#         tu.left(x)
#     else:
#         tu.forward(x)#前進
#     if x%2==0:
#         x=x/2
#     else:
#         x=3*x+1
# tu.down()
# =============================================================================


# =============================================================================
# import time
# r = ""
# for i in range(1,10):#列
#     r1 = ""
#     for j in range(1,10):#行
#         r1 = r1 + str(i) + "*" + str(j) + "=" + str(i*j) + "\t"
#     r = r1 + "\n"
#     time.sleep(0.1)
#     print(r)
# =============================================================================

# =============================================================================
# #7
# import random as rd
# x = rd.randint(1,100)
# while True:
#     y = eval(input("input a number:"))
#     if x>y:
#         print("too small")
#     elif x<y:
#         print("too large")
#     else:
#         print("Right Anwser")
#         break
# =============================================================================

# =============================================================================
# #8
# import random as rd
# N = eval(input("Throw the coin N times:"))
# tmp = 0 #upper side times
# times = N #Number of remaining
# while times>0:
#     times = times-1
#     x = rd.randint(0,1)
#     if x:
#         tmp = tmp+1
# print("upper side:",tmp)
# print("back side:",N-tmp)
# =============================================================================

