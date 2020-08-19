import cv2
import matplotlib.pyplot as plt
%matplotlib inline

img = cv2.imread('rainbow.jpg',0)
plt.imshow(img,cmap='gray')

img.max()
ret , thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
plt.imshow(thresh,cmap='gray')

ret , thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
plt.imshow(thresh,cmap='gray')

ret , thresh = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
plt.imshow(thresh,cmap='gray')

ret , thresh = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
plt.imshow(thresh,cmap='gray')

ret , thresh = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
plt.imshow(thresh,cmap='gray')

img = cv2.imread('crossword.jpg',0)
plt.imshow(img,cmap='gray')

def show_pic(img):
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
    
show_pic(img)

ret , th1 = cv2.threshold(img,170,255,cv2.THRESH_BINARY)
show_pic(th1)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,8)
show_pic(th2)

blended = cv2.addWeighted(th1,0.6,th2,0.4,0)
show_pic(blended)

