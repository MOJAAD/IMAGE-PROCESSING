import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

img = cv2.imread('internal_external.png',0)
plt.imshow(img,cmap='gray')

img.shape

image,contours= cv2.findContours(img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

# external_contours.shape
external_contours = np.zeros(image.shape)

for i in range(len(contours)):
    if contours[0][i][3]==-1 :
        cv2.drawContours(external_contours,contours,i,255,-1)
plt.imshow(external_contours,cmap='gray')

internal_contours = np.zeros(image.shape)

for i in range(len(contours)):
    if contours[0][i][3] != -1 :
        cv2.drawContours(internal_contours,contours,i,255,-1)
plt.imshow(internal_contours,cmap='gray')

external_contours = np.zeros(image.shape)

for i in range(len(contours)):
    if contours[0][i][3] == 0 :
        cv2.drawContours(external_contours,contours,i,255,-1)
plt.imshow(external_contours,cmap='gray')