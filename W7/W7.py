import matplotlib.pyplot as plt
import cv2
import numpy as np
import random
'''
#cv2 -> bgr
#matplotlib -> rgb
#flags
#cv2.cvtColor(input_image,flag)
img = cv2.imread("C:\\Users\\USER\\Desktop\\th.jpg",0)#grey
img2 = cv2.imread("C:\\Users\\USER\\Desktop\\th.jpg",1)#colorful
img3 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
cv2.imshow("image1",img)
cv2.imshow("image2",img2)
cv2.imshow("image3",img3)
plt.imshow(img3)
plt.show()
'''

'''
galaxy = dataObject()
#only itom object
filter("loadAnyImage",galaxy,'th.jpg')
Galaxy = dataObject()
# CV_BGR2GRAY = 6
filter("cvCvtColor",galaxy, Galaxy, 6) 
'''

'''
img = cv2.imread("th.jpg",1)
b,g,r = cv2.split(img)
cv2.imshow('B',b)
cv2.imshow('G',g)
cv2.imshow('R',r)
GAlaxy = cv2.merge([b,g,r])
cv2.imshow('galaxy',GAlaxy)
'''

'''
#add: image overlap
b = np.zeros([300,300,3],dtype='uint8')
g = np.zeros([300,300,3],dtype='uint8')
r = np.zeros([300,300,3],dtype='uint8')

b[100:200,50:250] = [255,0,0]
g[75:125,100:150] = [0,255,0]
r[150:225,125:200] = [0,0,255]

br = cv2.add(b,r)
bgr = cv2.add(br,g)
cv2.imshow('x',bgr)
'''

'''
img = np.zeros([300,300,3],dtype='uint8')
img1 = np.zeros([300,300,3],dtype='uint8')
img2 = np.zeros([300,300,3],dtype='uint8')

r = 70
p1 = (100,100)
p2 = (150,150)
p3 = (200,100)

cv2.circle(img,p1,r,(255,0,0),-1)
cv2.circle(img1,p2,r,(0,255,0),-1)
cv2.circle(img2,p3,r,(0,0,255),-1)

ab = cv2.addWeighted(img,0.85,img1,0.85,0)
abc = cv2.addWeighted(ab,0.85,img2,0.85,0)
cv2.imshow('three',abc)
'''

'''
#warpaffine only gray
img = cv2.imread("th.jpg",0)
rows,cols = img.shape
M = np.float32([[1.5,0,100],[0,1.5,50]])
dst = cv2.warpAffine(img,M,(cols+300,rows+150))
cv2.imshow('imgl',dst)

res = cv2.resize(img,(cols*2,rows*2))
cv2.imshow('res',res)
#center,angle,scaling
M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('imgr',dst)
'''

'''
img = cv2.imread("th.jpg",0)
rows,cols = img.shape
BB = np.zeros([rows,cols,3],dtype='uint8')
GG = np.zeros([rows,cols,3],dtype='uint8')
RR = np.zeros([rows,cols,3],dtype='uint8')

img = cv2.imread("th.jpg",1)
b,g,r = cv2.split(img)
M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
B = cv2.warpAffine(b,M,(cols,rows))
G = cv2.warpAffine(g,M,(cols,rows))
R = cv2.warpAffine(r,M,(cols,rows))
BB[:,:,0] = B
GG[:,:,1] = G
RR[:,:,2] = R
br = cv2.add(BB,RR)
bgr = cv2.add(br,GG)
cv2.imshow('x',bgr)
dst = cv2.merge([B,G,R])
cv2.imshow('x2',dst)
img = cv2.imread("th.jpg",1)
M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
s = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('s',s)
'''
'''
#transform
img = cv2.imread('th.jpg',0)
h,w = img.shape
s = np.array([[0,0],[w-1,0],[0,h-1],[w-1,h-1]],np.float32)
d = np.array([[0,0],[w-1,0],[w/3,h/3*2],[w/3*2,h/3*2]],np.float32)
p = cv2.getPerspectiveTransform(s,d)
r = cv2.warpPerspective(img,p,(w,h))
cv2.imshow('img',img)
cv2.imshow('r',r)
'''

'''
#noise
img = cv2.imread("th.jpg",1)
cv2.imshow('image1',img)
shape = img.shape
numNoise = 2000
for i in range(numNoise):
    i = random.randint(0,shape[0]-1)
    j = random.randint(0,shape[1]-1)
    if(len(shape)==2):
        img.itemset((i,j),255)
    else:
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        img.itemset((i,j,0),b)
        img.itemset((i,j,1),g)
        img.itemset((i,j,2),r)
cv2.imshow('image2',img)
'''

#filter2D
img = cv2.imread("th.jpg",1)
cv2.imshow('image',img)
kernel = np.ones((10,10),np.float32)/100
dst = cv2.filter2D(img,-1,kernel)
cv2.imshow('image1',img)

