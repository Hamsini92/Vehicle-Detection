# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 02:00:30 2017

@author: Hamsini Sankaran
"""

import cv2
filename = 'D:\\CV\\traffic1.avi'
cap = cv2.VideoCapture(filename)
reference_frame = None 
image_area = None
while True:
    ret,frame = cap.read()
    
    if ret is False:
        break 
    else:
        if reference_frame is None:
            reference_frame = frame 
            reference_frame = cv2.cvtColor(reference_frame,cv2.COLOR_BGR2GRAY)
            image_area = reference_frame.shape[0] * reference_frame.shape[1]
            continue
        
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        difference = cv2.absdiff(reference_frame,gray)
        blur = cv2.medianBlur(difference,31)
        
        
        f, threshold = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
        (_,contours,_) = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(frame,contours,-1,(0,0,255),2)
        for i in contours:
            contour_area = cv2.contourArea(i)
            if (contour_area > 0.001*image_area)and( contour_area <0.03 *image_area):
                
                (x,y,w,h)=cv2.boundingRect(i)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            
        cv2.imshow("frames",frame)
        if cv2.waitKey(1) == ord('q'):
            break
    