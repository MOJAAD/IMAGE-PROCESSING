import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

def load_pic():
    img = cv2.imread("bricks.jpg").astype(np.float32)/255
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img

def display_pic(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img)
    
i = load_pic()
display_pic(i)

gamma = 1/4
result = np.power(i,gamma)
display_pic(result)

img = load_pic()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'bricks',org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)
display_pic(img)

kernel = np.ones(shape=(5,5),dtype=np.float32)/25
dst = cv2.filter2D(img , -1 , kernel)
display_pic(dst)

img = load_pic()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'bricks',org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)
print('reset')

blurred = cv2.blur(img,ksize=(10,10))
display_pic(blurred)

img = load_pic()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'bricks',org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)
print('reset')

blurred_img = cv2.GaussianBlur(img,(5,5),10)
display_pic(blurred_img)

img = load_pic()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'bricks',org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)
print('reset')

median_result = cv2.medianBlur(img,5)
display_pic(median_result)

img = cv2.imread('sammy.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
display_pic(img)

noise_img = cv2.imread('noise.jpg')
display_pic(noise_img)

median = cv2.medianBlur(noise_img,5)
display_pic(median)

img = load_pic()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'bricks',org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)
blur = cv2.bilateralFilter(img,9,75,75)
display_pic(blur)

