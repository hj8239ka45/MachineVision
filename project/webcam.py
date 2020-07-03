# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:32:25 2020

@author: hj823
"""

import cv2
from threading import Thread
  
class Webcam:
    def __init__(self):
        self.flag = False
        self.video_capture = cv2.VideoCapture(0)
        self.current_frame = self.video_capture.read()[1]
          
    # create thread for capturing images
    def start(self):
        Thread(target=self._update_frame, args=()).start()
  
    def _update_frame(self):
        while(True):
            cv2.waitKey(33)
            self.current_frame = self.video_capture.read()[1]
            #self._catch_frame()
            if self.flag:
                break
            
    def _catch_frame(self):
        #rewrite frame, just save the .jpg data for pygame
        cv2.imwrite("now.jpg",self.current_frame)
        
    # get the current frame
    def get_current_frame(self):
        return self.current_frame
    
    def close(self):
        self.flag = True
        self.video_capture.release()