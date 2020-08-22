import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

img = cv2.imread('sammy_face.jpg')
plt.imshow(img)

edges = cv2.Canny(img,threshold1=127,threshold2=127)
plt.imshow(edges)

edges = cv2.Canny(img,threshold1=0,threshold2=255)
plt.imshow(edges)

med_val = np.median(img)
med_val

lower = int(max(0,0.7*med_val))
upper = int(min(255,1.3*med_val))
edges = cv2.Canny(img,threshold1=lower,threshold2=upper)
plt.imshow(edges)

blured_img = cv2.blur(img,ksize=(5,5))
edges = cv2.Canny(blured_img,threshold1=lower,threshold2=upper)
plt.imshow(edges)

blured_img = cv2.blur(img,ksize=(7,7))
edges = cv2.Canny(blured_img,threshold1=lower,threshold2=upper)
plt.imshow(edges)

blured_img = cv2.blur(img,ksize=(5,5))
edges = cv2.Canny(blured_img,threshold1=lower,threshold2=upper+50)
plt.imshow(edges)