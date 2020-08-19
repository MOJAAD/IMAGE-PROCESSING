import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

def load_img():
    blank_img = np.zeros((600,600))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blank_img,'ABCDE',org=(50,300),fontFace=font,fontScale=5,color=(255,255,255),thickness=20)
    return blank_img

def display_pic(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
    
img = load_img()
display_pic(img)

kernel = np.ones((5,5),dtype=np.uint8)
result = cv2.erode(img,kernel,iterations=3)
display_pic(result)

white_noise = np.random.randint(0,2,(600,600))
#display_pic(white_noise)

img.max()
white_noise = white_noise * 255
#display_pic(white_noise)

noise_img = white_noise + img
display_pic(noise_img)

opening = cv2.morphologyEx(noise_img,cv2.MORPH_OPEN,kernel)
display_pic(opening)

black_noise = np.random.randint(0,2,(600,600))
black_noise = black_noise * -255
black_noise_img = black_noise + img
display_pic(black_noise_img)

black_noise_img[black_noise_img==-255] = 0
display_pic(black_noise_img)

closing = cv2.morphologyEx(black_noise_img,cv2.MORPH_CLOSE,kernel)
display_pic(closing)

gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
display_pic(gradient)

