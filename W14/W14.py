# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:19:32 2020
    物件方位姿態偵測
    objpoints XYZ
    imgpoints UV
@author: hj823
"""
import cv2
import numpy as np
import os
# =============================================================================
# cap = cv2.VideoCapture(0)
# i = 0
# while True:
#     rev, frame = cap.read()
#     cv2.imshow("frame",frame)
#     
#     if cv2.waitKey(3) & 0xFF == ord('q'):
#         break
#     if cv2.waitKey(30) & 0xFF == ord('o'):
#         dir_name = os.getcwd()
#         direct = dir_name+"\\tmp\\chess%d.jpg"%i
#         print(direct)
#         rev = cv2.imwrite(direct,frame)
#         print(rev)
#         i = i+1
# cap.release()
# =============================================================================

# 找角點
# =============================================================================
# img = cv2.imread("tmp/chess0.jpg")
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,corners = cv2.findChessboardCorners(gray,(7,6))
# print(corners)
# tmp_p = np.zeros((1,2))
# for i in range(len(corners)):
#     p = (int(corners[i,0][0]), int(corners[i,0][1]))
#     cv2.circle(img, p, 4, (0,0,255), -1)
#     if i>0:
#         cv2.line(img, p, tmp_p, (255,0,0), 2)
#     tmp_p = p
# 
# cv2.imshow("img",img)
# cv2.waitKey()
# cv2.destroyAllWindows()
# =============================================================================


#精密角點
# =============================================================================
# import cv2
# import numpy as np
# import os
# 
# img = cv2.imread("tmp/chess0.jpg")
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,corners = cv2.findChessboardCorners(gray,(7,6))
# 
# winSize = (11,11)
# zeroZone = (-1,-1)
# criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,30,0.001)
# corners = cv2.cornerSubPix(gray, corners, winSize, zeroZone, criteria)
# print(corners)
# tmp_p = np.zeros((1,2))
# 
# for i in range(len(corners)):
#     p = (int(corners[i,0][0]), int(corners[i,0][1]))
#     p = (int(corners[i,0][0]), int(corners[i,0][1]))
#     cv2.circle(img, p, 4, (0,0,255), -1)
#     if i>0:
#         cv2.line(img, p, tmp_p, (255,0,0), 2)
#     tmp_p = p
# 
# cv2.imshow("img",img)
# cv2.waitKey()
# cv2.destroyAllWindows()
# =============================================================================








# =============================================================================
# #視2角點間距離為1
# import cv2
# import numpy as np
# import os
# import glob #方便找圖片->找相似檔案
# 
# objp = np.zeros((6*7,3),np.float32) #[42x3]
# #T 轉置 reshape 至兩行
# objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2) #[42x3]的前兩行
# 
# #存取角點座標 以及 影像角點位置
# objpoints = [] #3d
# imgpoints = [] #2d
# 
# winSize = (11,11)
# zeroZone = (-1,-1)
# criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,30,0.001)
# 
# imgs = glob.glob("tmp/chess*.jpg")
# for frame in imgs:
#     img = cv2.imread(frame)
#     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     ret,corners = cv2.findChessboardCorners(gray,(7,6))
#     if ret == True:
#         corners2 = cv2.cornerSubPix(gray, corners, winSize, zeroZone, criteria)
#         objpoints.append(objp)
#         imgpoints.append(corners2)
#         
#         #draw and display
#         img = cv2.drawChessboardCorners(img, (7,6), corners2, ret)
#         cv2.imshow("img",img)
#         cv2.waitKey(100)
#         
#     size = img.shape
#     focal_length = size[1]
#     center = (size[1]/2, size[0]/2)
#     camera_matrix = np.array(
#                      [[focal_length, 0, center[0]],
#                      [0, focal_length, center[1]],
#                      [0, 0, 1]], dtype = "double"
#                      )
# 
# dist_coeffs = np.zeros((4,1)) # Assuming no lens distortion
# objpoint = np.zeros((20,42,3))
# objpoint[:,:,:3] = np.array(objpoints).reshape(20,42,3)
# 
# imgpoint = np.zeros((20,42,3))
# imgpoint[:,:,:2] = np.array(imgpoints).reshape(20,42,2)
# (success, rotation_vector, translation_vector) = cv2.solvePnP(np.array(objpoints),imgpoint, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)
# 
# 
# cv2.waitKey()
# cv2.destroyAllWindows()
# =============================================================================


#視2角點間距離為1
import cv2
import numpy as np
import os
import glob #方便找圖片->找相似檔案

objp = np.zeros((6*7,3),np.float32) #[42x3]
#T 轉置 reshape 至兩行
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2) #[42x3]的前兩行

#存取角點座標 以及 影像角點位置
objpoints = [] #3d
imgpoints = [] #2d

winSize = (11,11)
zeroZone = (-1,-1)
criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,30,0.001)

imgs = glob.glob("tmp/chess*.jpg")
for frame in imgs:
    img = cv2.imread(frame)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,corners = cv2.findChessboardCorners(gray,(7,6))
    if ret == True:
        corners2 = cv2.cornerSubPix(gray, corners, winSize, zeroZone, criteria)
        objpoints.append(objp)
        imgpoints.append(corners2)
        
        #draw and display
        img = cv2.drawChessboardCorners(img, (7,6), corners2, ret)
        cv2.imshow("img",img)
        cv2.waitKey(1)
#matrix
#distortion  ->  undistortion
#rotation_vector
#transfer_vector
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints,imgpoints,gray.shape,None,None)
print(mtx)
print(dist)
print("first rotation pitch yaw row",rvecs[0])
print("first transfer x y z",tvecs[0])
cv2.waitKey()
cv2.destroyAllWindows()







# =============================================================================
#     cv2.findChessboardCorners(image, patternSize)
#     cv2.cornerSubPix(image, corners, winSize, zeroZone, criteria)
#     cv2.drawChessboardCorners(image, patternSize, corners, patternWasFound)
# =============================================================================









# =============================================================================
# #視2角點間距離為1
# import cv2
# import numpy as np
# import os
# import glob #方便找圖片->找相似檔案
# 
# objp = np.zeros((6*7,3),np.float32) #[42x3]
# #T 轉置 reshape 至兩行
# objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2) #[42x3]的前兩行
# 
# #存取角點座標 以及 影像角點位置
# objpoints = [] #3d
# imgpoints = [] #2d
# 
# winSize = (11,11)
# zeroZone = (-1,-1)
# criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,30,0.001)
# 
# 
# 
# cap = cv2.VideoCapture(0)
# i = 0
# while True:
#     rev, frame = cap.read()
#     cv2.imshow("frame",frame)
#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         break
#     if cv2.waitKey(20) & 0xFF == ord('o'):
#         print("pressed o")
#         #dir_name = os.getcwd()
#         #direct = dir_name+"\\tmp\\chess%d.jpg"%i
#         #rev = cv2.imwrite(direct,frame)
#         #print(rev)
#         #i = i+1
#         img = frame
#         gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#         ret,corners = cv2.findChessboardCorners(gray,(7,6))
#         if ret == True:
#             corners2 = cv2.cornerSubPix(gray, corners, winSize, zeroZone, criteria)
#             objpoints.append(objp)
#             imgpoints.append(corners2)
#             
#             #draw and display
#             img = cv2.drawChessboardCorners(img, (7,6), corners2, ret)
#             cv2.imshow("img",img)
#             cv2.waitKey(100)
# cap.release()
# =============================================================================

