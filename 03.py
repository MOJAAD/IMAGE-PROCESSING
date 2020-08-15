import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import cv2

blank_img=np.zeros(shape=(512,512,3),dtype=np.int16)
plt.imshow(blank_img)

cv2.rectangle(blank_img,pt1=(384,0),pt2=(510,150),color=(85,125,0),thickness=5)
plt.imshow(blank_img)

cv2.rectangle(blank_img,pt1=(200,200),pt2=(300,300),color=(0,0,255),thickness=5)
plt.imshow(blank_img)

cv2.circle(img=blank_img,center=(100,100),radius=50,thickness=-1,color=(255,0,0))
plt.imshow(blank_img)

cv2.circle(img=blank_img,center=(400,400),radius=50,thickness=5,color=(255,0,0))
plt.imshow(blank_img)

cv2.line(blank_img,pt1=(0,512),pt2=(512,0),color=(105,105,105),thickness=5)
plt.imshow(blank_img)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img,text='Hello',org=(10,500),fontFace=font,fontScale=4,color=(255,255,255),thickness=5,lineType=cv2.LINE_AA)
plt.imshow(blank_img)

blank_img=np.zeros(shape=(512,512,3),dtype=np.int16)
plt.imshow(blank_img)

vertices=np.array([ [100,300] , [200,200] , [400,300] , [200,400] ],dtype=np.int32)
pts=vertices.reshape((-1,1,2))
pts

cv2.polylines(blank_img,[pts],thickness=5,color=(255,0,0),isClosed=True)
plt.imshow(blank_img)