import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import cv2

def drow_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN : 
        cv2.circle(img,(x,y),100,(0,255,255),-1)
    elif event == cv2.EVENT_RBUTTONDOWN : 
        cv2.circle(img,(x,y),100,(255,255,0),-1)
        
cv2.namedWindow(winname='My_Drowing')
cv2.setMouseCallback('My_Drowing',drow_circle)

img = np.zeros((512,512,3),np.int8)

while True :
    
    cv2.imshow('My_Drowing',img)
    if cv2.waitKey(20) and 0xFF ==27 :
        break
        
cv2.destroyAllWindows()