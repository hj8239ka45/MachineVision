# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 20:59:54 2020
    https://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html?highlight=solvepnp
@author: hj823
"""


import pyzbar.pyzbar as zbar
from PIL import Image,ImageColor
import cv2 
import numpy as np
import math

def qr_gesture(im, drawContours=False, drawLine=False):
    # Read Image
    
    size = im.shape
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY, dstCn=0) 
    pil = Image.fromarray(gray) 
    width, height = pil.size 
    raw = pil.tobytes()
    
    Imgpts = []
    #find qr code
    image = zbar.decode(im)
    for symbol in image: 
        #print ('decoded', symbol.type, 'symbol', '"%s"' % symbol.data)
        topLeftCorners, bottomLeftCorners, bottomRightCorners, topRightCorners = [item for item in symbol.polygon] 
        contour = np.array([topLeftCorners, bottomLeftCorners, bottomRightCorners, topRightCorners])
        # draw ground floor
        if drawContours:
            im = cv2.drawContours(im, [contour],-1,(255,255,255),-3)
        if drawLine:
            cv2.line(im, topLeftCorners, topRightCorners, (255,0,255),2) 
            cv2.line(im, topLeftCorners, bottomLeftCorners, (255,0,255),2) 
            cv2.line(im, topRightCorners, bottomRightCorners, (255,0,255),2) 
            cv2.line(im, bottomLeftCorners, bottomRightCorners, (255,0,255),2)
        #2D image points. If you change the image, you need to change vector
        #print(symbol)
        #2xN UV
        image_points = np.array([ 
                            (int((topRightCorners[0]+bottomLeftCorners[0])/2), int((topRightCorners[1]+bottomLeftCorners[1])/2)),     # Nose 
                            topLeftCorners,     # Left eye left corner 
                            topRightCorners,     # Right eye right corne 
                            bottomLeftCorners,     # Left Mouth corner 
                            bottomRightCorners      # Right mouth corner 
                        ], dtype="double") 
        # 3D model points.
        #3xN XYZ
        model_points = np.array([
                            (0.0, 0.0, 0.0),             # Nose
                            (-10.0, -10.0, 0.0),     # Left eye left corner
                            (10.0, -10.0, 0.0),      # Right eye right corne
                            (-10.0, 10.0, 0.0),    # Left Mouth corner
                            (10.0, 10.0, 0.0)      # Right mouth corner
                        ])
        #ITERATIVE 適合點在同一平面上的情況
        
        # Camera internals
        focal_length = size[1]
        center = (size[1]/2, size[0]/2)
        mtx = np.array(
                         [[focal_length, 0, center[0]],
                         [0, focal_length, center[1]],
                         [0, 0, 1]], dtype = "double"
                         )
        
        dist = np.zeros((4,1)) # Assuming no lens distortion
        (success, rvecs, tvecs) = cv2.solvePnP(model_points, image_points, mtx, dist, flags=cv2.SOLVEPNP_ITERATIVE)

        
        axis = np.float32([[0,0,0],[5,0,0], [0,5,0], [0,0,-5]]).reshape(-1,3)
        (imgpts, jacobian) = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)
        Imgpts.append(imgpts)
        dist = (tvecs[0, 0]**2+tvecs[1, 0]**2+tvecs[2, 0]**2)**0.5
        size = (dx,dy) = (symbol.rect[2],symbol.rect[3])
        name = (symbol.data).decode()
        
    return (name, rvecs, Imgpts, dist, size)

if __name__=="__main__":
    # initialise webcam and start thread
    cap = cv2.VideoCapture(0) 
    while True:
        A = None
        ret, im = cap.read()
        # get image from webcam
        
        # Read Image 
        #im = cv2.imread("sahilkhosla.jpg"); 
        size = im.shape
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY, dstCn=0) 
        pil = Image.fromarray(gray) 
        width, height = pil.size 
        raw = pil.tobytes()
        try:
            (name, rvecs, Imgpts, dist, size) = qr_gesture(im, True, True)
        except:
            Imgpts = None            

        color = [(255,0,0),(0,255,0),(0,0,255)]
        if Imgpts:
            p2 = tuple(Imgpts[0][0,0])#取中心
            for i in range(3):
                p1 = tuple(Imgpts[0][i+1,0])
                cv2.line(im,p1,p2,color[i],2)
        cv2.imshow("Output", im)
        
        # Wait for the magic key
        if cv2.waitKey(30) & 0xFF == ord('q'): 
            break
    cv2.destroyAllWindows()

