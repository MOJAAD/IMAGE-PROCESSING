import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

dark_horse = cv2.imread('horse.jpg')
show_horse = cv2.cvtColor(dark_horse,cv2.COLOR_BGR2RGB)

rainbow = cv2.imread('rainbow.jpg')
show_rainbow = cv2.cvtColor(rainbow,cv2.COLOR_BGR2RGB)

blue_bricks = cv2.imread('bricks.jpg')
show_bricks = cv2.cvtColor(blue_bricks,cv2.COLOR_BGR2RGB)

plt.imshow(show_bricks)

hist_values = cv2.calcHist([blue_bricks],channels=[0],mask=None,histSize=[256],ranges=[0,256])
hist_values.shape
plt.plot(hist_values)

hist_values = cv2.calcHist([dark_horse],channels=[0],mask=None,histSize=[256],ranges=[0,256])
plt.plot(hist_values)

img = blue_bricks
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color=col)
    plt.xlim([0,256])
    
plt.title('Histogram For Blue Brrcks')

img = dark_horse
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color=col)
    plt.xlim([0,50])
    plt.ylim([0,200000])
    
plt.title('Histogram For Dark Horse')

img = rainbow
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color=col)
    plt.xlim([0,256])
    
plt.title('Histogram For Rainbow')

img = rainbow
rec = np.zeros(img.shape[:2])
rec[300:400,100:400]=255
plt.imshow(rec,cmap='gray')

mask_img = cv2.bitwise_and(img,img,mask=rec)
show_mask_img = cv2.bitwise_and(show_rainbow,show_rainbow,mask=rec)
plt.imshow(show_mask_img)

hist_show_mask = cv2.calcHist([rainbow],channels=[2],mask=mask,histSize=[256],ranges=[0,256])
hist_show_red = cv2.calcHist([rainbow],channels=[2],mask=None,histSize=[256],ranges=[0,256])
plt.plot(hist_show_mask)
plt.title('RED HOSTOGRAM FOR MASKED RAINBOW')

plt.plot(hist_show_red)
plt.title('RED HOSTOGRAM FOR NORMAL RAINBOW')