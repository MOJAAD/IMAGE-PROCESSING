import numpy as np
import cv2

drowing=False
ix=-1
iy=-1


def drow_rectangle(event,x,y,flags,param):
    global ix,iy,drowing
    if event == cv2.EVENT_LBUTTONDOWN:
        drowing=True
        ix,iy=x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drowing == True :
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        if drowing == False:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        
    
img = np.zeros((512,512,3))
cv2.namedWindow(winname='MY_Drowing')
cv2.setMouseCallback('MY_Drowing',drow_rectangle)

while True :
    
    cv2.imshow('MY_Drowing',img)
    if cv2.waitKey(1) and 0xFF ==27 :
        break
        
cv2.destroyAllWindows()