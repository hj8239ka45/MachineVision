#dataObject : itom ????
#d = dataObject.randN([16,16],'uint16')
#plot(d)

#import cv2
##1.?????????????python??????????\????\\???????python????\\??\??
## 
#img = cv2.imread("C:\\Users\\USER\\Desktop\\th.jpg")
#print("rgb in pixel",img.shape)
#img = cv2.resize(img, (200,300))
#print("rgb in pixel",img.shape)
#
#img[:][:][0] = 255
#img[:][:][1] = 0
#img[:][:][2] = 0
#
#print(img[1][1][0])
#print(img[1][1][1])
#print(img[1][1][2])
#cv2.imshow("image",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#
#img = dataObject()
#filter("loadAnyImage",img,'th.jpg')
#plot(img)
#
#



#import cv2
##1.?????????????python??????????\????\\???????python????\\??\??
## 
#img = cv2.imread("C:\\Users\\USER\\Desktop\\th.jpg")
#print("rgb in pixel",img.shape)
#img = cv2.resize(img, (200,300))
#print("rgb in pixel",img.shape)
#img[100:110][:] = [255,0,0]
#print(img[1][1])
#cv2.imshow("image",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#import cv2
#import numpy as np
#img1 = np.full((300,300,3),(255,0,0),np.uint8)
#img2 = np.zeros([300,300,3])
#img2[:,:,0] = 255
#cv2.imshow("img1",img1)
#cv2.imshow("img2",img2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# =============================================================================
# import cv2
# import numpy as np
# img = np.zeros([300,300,3])
# img[:][:] = [255,255,255]
# x = np.linspace(0,250,8000)
# for i in x:
#     j = 50*(np.sin(i*0.05)+3)
#     if i >299 or j>299:
#         break;
#     img[int(j),int(i)] = [0,0,255]
# #cv2.imwrite('test.jpg',img)
# #can be adjust the windows range by mouse
# cv2.namedWindow('img',cv2.WINDOW_NORMAL)
# cv2.imshow("img",img)
# key = cv2.waitKey(0)&0xff
# print(key)
# cv2.destroyAllWindows()
# 
# =============================================================================






import cv2
import numpy as np
img = cv2.imread("th.jpg")
p1 = (10,10)
p2 = (120,120)
#p3 = (240,120)
#LINE:point to point
# =============================================================================
# cv2.line(img,p1,p2,(255,0,0),5)
# =============================================================================
# =============================================================================
# cv2.line(img,p2,p3,(255,0,0),5)
# #RECT:left top point to right down point
# =============================================================================
# =============================================================================
# cv2.rectangle(img,p1,p2,(255,0,0),2)
# =============================================================================
#CIRCLE: center,radius,color,(>0:width,-1:covered)
cv2.circle(img,p2,20,(255,0,0),-1)
# center, long short,angle, angle->angle
# =============================================================================
# cv2.ellipse(img,p2,(10,30),30,0,270,(255,0,0),2)
# =============================================================================
cv2.imshow("img",img)

