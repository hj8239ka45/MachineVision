## Q4
#import numpy as np
#import matplotlib.pyplot as plt
#print("cal. the reflective rate")
#n1 = eval(input("input a reflective coeffiction n1: "))
#n2 = eval(input("input a reflective coeffiction n2: "))
#theta_i_angle = np.linspace(0,90,1800)
#theta_i = theta_i_angle/180*np.pi
#Rs_up_1 = n1*np.cos(theta_i)
#Rs_up_2 = n2*(1-(n1/n2*np.sin(theta_i))**2)**0.5
#Rs_up = Rs_up_1 - Rs_up_2
#Rs_down = Rs_up_1 + Rs_up_2
#Rs = (Rs_up/Rs_down)**2
##print("Reflection rate(Rs): ",Rs)
##
#Rp_up_1 = n1*(1-(n1/n2*np.sin(theta_i))**2)**0.5
#Rp_up_2 = n2*np.cos(theta_i)
#Rp_up = Rp_up_1 - Rp_up_2
#Rp_down = Rp_up_1 + Rp_up_2
#Rp_1 = (Rp_up/Rp_down)**2
##print("Reflection rate(Rp): ",Rp)
#
#
#n2 = eval(input("input a reflective coeffiction n2: "))
#theta_i_angle = np.linspace(0,90,1800)
#theta_i = theta_i_angle/180*np.pi
#Rs_up_1 = n1*np.cos(theta_i)
#Rs_up_2 = n2*(1-(n1/n2*np.sin(theta_i))**2)**0.5
#Rs_up = Rs_up_1 - Rs_up_2
#Rs_down = Rs_up_1 + Rs_up_2
#Rs = (Rs_up/Rs_down)**2
##print("Reflection rate(Rs): ",Rs)
##
#Rp_up_1 = n1*(1-(n1/n2*np.sin(theta_i))**2)**0.5
#Rp_up_2 = n2*np.cos(theta_i)
#Rp_up = Rp_up_1 - Rp_up_2
#Rp_down = Rp_up_1 + Rp_up_2
#Rp = (Rp_up/Rp_down)**2
##print("Reflection rate(Rp): ",Rp)
#plt.plot(theta_i_angle,Rp,theta_i_angle,Rp_1)


##Q3
#import numpy as np
#import matplotlib.pyplot as plt
#delta = 0.05
#x = np.linspace(-10,10,1000)
#y = np.sin(x)
#y_derive = np.sin(x+delta)
#yd = (y_derive-y)/delta
#plt.plot(x,y,x,yd)
#plt.show()

## Q4
#import numpy as np
#import matplotlib.pyplot as plt
#x = np.linspace(-10,10,500)
#X,Y = np.meshgrid(x,x)
##Z = np.exp(-X**2-Y**2)
#Z = (np.sin(X)+np.cos(Y))
#plt.imshow(Z,cmap="rainbow")
#plt.show()



## convolution
#import numpy as np
#import matplotlib.pyplot as plt
#
#n = [1,1,1]
#x = np.linspace(1,100)
#y = np.random.rand(100)
#
#A = []
#for i in range(0,len(y)-2):
    #yc = (y[i]*n[0]+y[i+1]*n[1]+y[i+2]*n[2])/sum(n)
    #A = A+[yc]
#
#plt.plot(y)
#plt.plot(A)
#plt.show()


#import numpy as np
#import matplotlib.pyplot as plt
#
#x = np.linspace(0,10,100)
#y = np.random.randn(len(x))
#c = np.array([1,1,1])/3
#yc = np.convolve(y,c,"same")
#plt.plot(x,y,x,yc)
#plt.show()



import numpy as np
import matplotlib.pyplot as plt
theta = np.linspace(0,90,100)
theta_i = theta/180*np.pi
n1 = 1
n2 = np.linspace(1.3,1.7,100)
Theta_i,N2 = np.meshgrid(theta_i,n2)

Rp_up_1 = n1*(1-(n1/N2*np.sin(Theta_i))**2)**0.5
Rp_up_2 = N2*np.cos(Theta_i)
Rp_up = Rp_up_1 - Rp_up_2
Rp_down = Rp_up_1 + Rp_up_2
Rp = (Rp_up/Rp_down)**2

#print("Reflection rate(Rp): ",Rp)
plt.imshow(Rp,cmap="gray")
plt.show() 