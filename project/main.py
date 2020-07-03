# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 10:46:57 2020
    Reference:
        Basic OBJ file viewer. needs objloader from:
            http://www.pygame.org/wiki/OBJFileLoader
        AR based on QR Code
            https://www.geeksforgeeks.org/project-idea-augmented-reality-qr-code-scanner/
        solvepnp:三維位姿估算
            mode:    https://www.itread01.com/content/1548328537.html
                     https://blog.csdn.net/cocoaqin/article/details/77485436
            camera:  https://blog.csdn.net/jay463261929/article/details/53818611
        opengl for X64
                https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl
        AR:
            https://bitesofcode.wordpress.com/2017/09/12/augmented-reality-with-python-and-opencv-part-1/
            http://www.pygame.org/wiki/OBJFileLoader
            https://rdmilligan.wordpress.com/2015/10/15/augmented-reality-using-opencv-opengl-and-blender/
        openGL light:
            https://www.itread01.com/content/1549815668.html
        OGJ material:
            https://clara.io/libraryff
            https://free3d.com/3d-models/obj
@author: hj823
"""
import sys, pygame, os
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
import cv2
import numpy as np
# IMPORT OBJECT LOADER
from objloader import *
from QR_gesture import *
from webcam import Webcam
from draw_obj import draw_obj
import time as t

pygame.init()  # 初始化pygame
SIZE = width, height = 640,480  # 設定視窗大小
display = pygame.display.set_mode(SIZE, OPENGL | DOUBLEBUF | OPENGLBLIT)  # 顯示視窗

'''
    GL光源 :
        編號   : GL_LIGHT0
        位置   : GL_POSITION
        散射   : GL_DIFFUSE
        環境光 : GL_AMBIENT
        反射光 : GL_SPECULAR
'''
glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 50, 50, 0.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.6, 0.6, 0.6, 1.0))  # 白光(弱)
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))  # 白光
glLightfv(GL_LIGHT0, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0)) # 白光
glEnable(GL_LIGHT0)     # 光源致能



if __name__=="__main__":
    hx = SIZE[0]/2
    hy = SIZE[1]/2
    #srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)
    
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH) # most obj files expect to be smooth-shaded
    
    obj_name = None
    
    clock = pygame.time.Clock()
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90.0, width/float(height), 1, 100.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_MODELVIEW)
    
    '''
        obj姿態定義
        _o以及(tx,ty) : 為可手動定義部分
    '''
    rx_o, ry_o, rz_o = (0,0,0)
    rx, ry, rz = (rx_o, ry_o, rz_o)
    tx, ty = (-25,0)
    zpos = 0
    zpos_o = 4
    rotate = move = False
    
    '''
        畫線、區域初始
    '''
    drawline = False
    drawContours = False
    # initialise webcam and start thread
    webcam = Webcam()
    webcam.start()
    while True:
        clock.tick(30)
        frame = webcam.get_current_frame()

        for e in pygame.event.get():
            if e.type == QUIT or pygame.key.get_pressed()[pygame.K_q]:
                pygame.quit()
                cv2.destroyAllWindows()
                webcam.close()
                sys.exit()
                break
            elif e.type == KEYDOWN and e.key == K_ESCAPE:
                sys.exit()
            elif pygame.key.get_pressed()[pygame.K_l]:
                drawline = not drawline             # drawline
            elif pygame.key.get_pressed()[pygame.K_k]:
                drawContours = not drawContours     # drawcontour
            elif pygame.key.get_pressed()[pygame.K_c]:
                glEnable(GL_LIGHTING)               # 點亮
            elif pygame.key.get_pressed()[pygame.K_d]:
                glDisable(GL_LIGHTING)              # 關閉
            elif e.type == MOUSEBUTTONDOWN:
                if e.button == 4: zpos_o = max(1, zpos_o-1)
                elif e.button == 5: zpos_o += 1
                elif e.button == 1: rotate = True
                elif e.button == 3: move = True
            elif e.type == MOUSEBUTTONUP:
                if e.button == 1: rotate = False
                elif e.button == 3: move = False
            elif e.type == MOUSEMOTION:
                i, j = e.rel
                if rotate:
                    rx_o += i
                    ry_o += j
                if move:
                    tx += i
                    ty -= j
        try:
            imgpts = None
            try:
                (name, rvets, imgpts, dist, size) = qr_gesture(frame, drawContours, drawline)
            except:
                (name, rvets, imgpts, dist, size) = qr_gesture(frame)

            if obj_name != name:
                obj_name = name
                print(name)
                dir_obj = os.getcwd()+"/obj_rar/" + obj_name + "/" + obj_name + ".obj"
                print(dir_obj)
                tic = t.clock()
                # LOAD OBJECT AFTER PYGAME INIT
                obj = OBJ(dir_obj, swapyz=True)
                toc = t.clock()
                #print("delta T (s)",toc-tic)
            color = [(255,0,0),(0,255,0),(0,0,255)]
            if imgpts:
                center = tuple(imgpts[0][0,0])#取中心
                for i in range(3):
                    p1 = tuple(imgpts[0][i+1,0])
                    #cv2.line(frame,p1,center,color[i],2)
                    
            ry = ry_o + rvets[0]*180.0/np.pi
            rx = rx_o + rvets[1]*-180.0/np.pi
            zpos = dist/40 + zpos_o     #由距離做為輔助調整
        except:
            size = None
            center = None
            print("no data")
        
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
    
        # RENDER OBJECT in pygame
        
        #print("tx,ty=(%d,%d)"%(tx,ty))
        #print(tx,ty)
        print(zpos)
        glTranslate(tx/20., ty/20., - zpos)
        #glRotate(rz, 0, 0, 1)
        glRotate(ry, 1, 0, 0)
        glRotate(rx, 0, 1, 0)
        if obj_name is not None:
            glCallList(obj.gl_list)
        # Draw OBJ in camera
        draw_obj(frame, width, height, size, center)

        pygame.display.flip()
        
        
        
        
        