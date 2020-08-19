import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

gorilla = cv2.imread('gorilla.jpg',0)
def display_pic(img,cmap=None):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap)

display_pic(gorilla,cmap='gray')

hist_values = cv2.calcHist([gorilla],channels=[0],mask=None,histSize=[256],ranges=[0,256])
plt.plot(hist_values)

eq_gorilla = cv2.equalizeHist(gorilla)
display_pic(eq_gorilla,cmap='gray')

hist_values = cv2.calcHist([eq_gorilla],channels=[0],mask=None,histSize=[256],ranges=[0,256])
plt.plot(hist_values)

color_gorilla = cv2.imread('gorilla.jpg')
show_gorilla = cv2.cvtColor(color_gorilla,cv2.COLOR_BGR2RGB)
display_pic(show_gorilla)

hsv_gorilla = cv2.cvtColor(color_gorilla,cv2.COLOR_BGR2HSV)
#display_pic(hsv_gorilla)
hsv_gorilla[:,:,2] = cv2.equalizeHist(hsv_gorilla[:,:,2])
#display_pic(hsv_gorilla)
eq_color_gorilla = cv2.cvtColor(hsv_gorilla,cv2.COLOR_HSV2RGB)
display_pic(eq_color_gorilla)

