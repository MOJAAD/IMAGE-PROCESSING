import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

flat_chess = cv2.imread('E://University-working/openCV python/Udemy - Python for Computer Vision with OpenCV and Deep Learning 2019-9/Computer-Vision-with-Python/DATA/flat_chessboard.png')
flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2RGB)
plt.imshow(flat_chess)

gray_flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_flat_chess,cmap='gray')

real_chess = cv2.imread('E://University-working/openCV python/Udemy - Python for Computer Vision with OpenCV and Deep Learning 2019-9/Computer-Vision-with-Python/DATA/real_chessboard.jpg')
real_chess = cv2.cvtColor(real_chess,cv2.COLOR_BGR2RGB)
plt.imshow(real_chess)

gray = np.float32(gray_flat_chess)
dst = cv2.cornerHarris(gray,blockSize=2,ksize=3,k=0.04)
dst = cv2.dilate(dst,None)
flat_chess[dst>0.01*dst.max()] = [255,0,0] #RGB
plt.imshow(flat_chess)

gray = np.float32(gray_real_chess)
dst = cv2.cornerHarris(gray,blockSize=2,ksize=3,k=0.04)
dst = cv2.dilate(dst,None)
real_chess[dst>0.01*dst.max()] = [255,0,0] #RGB
plt.imshow(real_chess)

flat_chess = cv2.imread('E://University-working/openCV python/Udemy - Python for Computer Vision with OpenCV and Deep Learning 2019-9/Computer-Vision-with-Python/DATA/flat_chessboard.png')
real_chess = cv2.imread('E://University-working/openCV python/Udemy - Python for Computer Vision with OpenCV and Deep Learning 2019-9/Computer-Vision-with-Python/DATA/real_chessboard.jpg')

flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2RGB)
real_chess = cv2.cvtColor(real_chess,cv2.COLOR_BGR2RGB)

gray_flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2GRAY)
gray_real_chess = cv2.cvtColor(real_chess,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray_flat_chess,64,0.01,10)
corners = np.int0(corners)
for i in corners :
    x,y= i.ravel()
    cv2.circle(flat_chess,(x,y),3,(255,0,0),-1)
    
plt.imshow(flat_chess)

corners = cv2.goodFeaturesToTrack(gray_real_chess,100,0.01,10)
corners = np.int0(corners)
for i in corners :
    x,y= i.ravel()
    cv2.circle(real_chess,(x,y),3,(255,0,0),-1)
    
plt.imshow(real_chess)