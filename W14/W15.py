# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:13:09 2020

@author: hj823
"""



import cv2
import numpy as np

mtx = np.array([[293., 0, 286.],[0, 297., 247],[0, 0, 1]])
# =============================================================================
# mtx = np.array([[3300, 0, 250],
#                 [0, 7250, 316],
#                 [0, 0, 1]], dtype = "double")
# =============================================================================
dist = np.array([[0.03, -0.02, 0.01, -0.01, 0.00]])

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER ,30, 0.001)
objp = np.zeros((6*7,3),np.float32) #[42x3]
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2) #[42x3]的前兩行
axis = np.float32([[3,0,0],[0,3,0],[0,0,3]])

color = [(255,0,0),(0,255,0),(0,0,255)]

winSize = (11,11)
zeroZone = (-1,-1)
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray,(7,6),None)
    if not ret:
        continue
    corners2 = cv2.cornerSubPix(gray, corners, winSize, zeroZone, criteria)
    #draw and display
    ret, rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners2, mtx, dist)
    imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)
    p2 = tuple(corners2[0][0])
    for i in range(3):
        p1 = tuple(imgpts[i][0])
        cv2.line(frame,p1,p2,color[i],2)
    d = (tvecs[0, 0]**2+tvecs[1, 0]**2+tvecs[2, 0]**2)**0.5
    cv2.putText(frame, "distance = %.3f"%(d), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("projected",frame)
    cv2.circle(frame,p2,5,(0,0,0),-1)
    print(d)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()


# =============================================================================
# import cv2
# import numpy as np
# #視2角點間距離為1
# 
# objp = np.zeros((6*7,3),np.float32) #[42x3]
# objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2) #[42x3]的前兩行
# axis = np.float32([[3,0,0],[0,3,0],[0,0,3]])
# img = cv2.imread("chess10.jpg")
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret, corners = cv2.findChessboardCorners(gray,(7,6),None)
# 
# mtx = np.array([[293.,0,286.],[0,297.,247],[0,0,1]])
# dist = np.array([[0.03,-0.02,0.01,-0.01,0.00]])
# 
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,30,0.001)
# winSize = (11,11)
# zeroZone = (-1,-1)
# 
# corners2 = cv2.cornerSubPix(gray, corners, winSize, zeroZone, criteria)
# ret, rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners2, mtx, dist)
# imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)
# 
# p2 = tuple(corners2[0][0])
# color = [(255,0,0),(0,255,0),(0,0,255)]
# for i in range(3):
#     p1 = tuple(imgpts[i][0])
#     cv2.line(img,p1,p2,color[i],2)
# cv2.circle(img,p2,5,(0,0,0),-1)
# cv2.imshow("projected",img)
# 
# #距離鏡頭20.8格
# dist = 0
# for i in range(3):
#     dist = dist + (tvecs[i])**2
# dist = dist**0.5
# print(dist)
# =============================================================================

# =============================================================================
# objp = np.zeros((6*7,3),np.float32) #[42x3]
# #T 轉置 reshape 至兩行
# objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2) #[42x3]的前兩行
# #世界座標三格軸
# axis = np.float32([[3,0,0],[0,3,0],[0,0,3]])
# 
# #存取角點座標 以及 影像角點位置
# objpoints = [] #3d
# imgpoints = [] #2d
# 
# winSize = (11,11)
# zeroZone = (-1,-1)
# 
# #疊代終止條件 30次 精度至0.001
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,30,0.001)
# 
# imgs = glob.glob("tmp/chess*.jpg")
# for frame in imgs:
#     img = cv2.imread(frame)
#     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     ret,corners = cv2.findChessboardCorners(gray,(7,6))
#     if ret == True:
#         #UV 像素點
#         corners2 = cv2.cornerSubPix(gray, corners, winSize, zeroZone, criteria)
#         objpoints.append(objp)
#         imgpoints.append(corners2)
#         
#         #draw and display
#         img = cv2.drawChessboardCorners(img, (7,6), corners2, ret)
#         cv2.imshow("img",img)
#         cv2.waitKey(1)
# # matrix
# #distortion  ->  undistortion
# #rotation_vector
# #transfer_vector
# # 鏡頭內參數
# ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints,imgpoints,gray.shape,None,None)
# 
# 
# 
# 
# cap = cv2.VideoCapture(0)
# i = 0
# while True:
#     rev, frame = cap.read()
#     cv2.imshow("frame",frame)
#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         print("quit")
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
#             # 此照片之轉移向量
#             ret, rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners2, mtx, dist)
# 
#             # 將世界座標投影至畫面
#             imgpts, _ = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)
# 
#             #draw and display
#             img = cv2.drawChessboardCorners(img, (7,6), corners2, ret)
#             
#             cv2.imshow("img",img)
#             cv2.waitKey(100)
#             
# cap.release()
# cv2.waitKey()
# cv2.destroyAllWindows()
# =============================================================================

