import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

def display_pic(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
    
img = cv2.imread('sudoku.jpg',0)
display_pic(img)

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
display_pic(sobelx)

sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
display_pic(sobely)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
display_pic(laplacian)

blended = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
display_pic(blended)

ret , th1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
display_pic(th1)

kernel = np.ones((5,5),dtype=np.uint8)
gradient = cv2.morphologyEx(blended,cv2.MORPH_GRADIENT,kernel)
display_pic(gradient)

