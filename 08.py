import cv2
import matplotlib.pyplot as plt
%matplotlib inline

pic1 = cv2.imread("dog_backpack.png")
pic1 = cv2.cvtColor(pic1,cv2.COLOR_BGR2RGB)
pic2 = cv2.imread("watermark_no_copy.png")
pic2 = cv2.cvtColor(pic2,cv2.COLOR_BGR2RGB)
pic2 = cv2.resize(pic2,(600,600))
pic1.shape

x_offset=934-600
y_offset=1401-600
rows,cols,chan=pic2.shape
roi = pic1[y_offset:1401,x_offset:934]
pic2gray = cv2.cvtColor(pic2,cv2.COLOR_RGB2GRAY)
plt.imshow(pic2gray,cmap='gray')

pic2_mask = cv2.bitwise_not(pic2gray)
plt.imshow(pic2_mask,cmap='gray')

import numpy as np
pic2.shape

white_background = np.full(pic2.shape,255,dtype=np.uint8)
white_background.shape

bk = cv2.bitwise_or(white_background,white_background,mask=pic2_mask)
bk.shape
plt.imshow(bk)

fg = cv2.bitwise_or(pic2,pic2,mask=pic2_mask)
plt.imshow(fg)
final_roi = cv2.bitwise_or(roi,fg)
plt.imshow(final_roi)
large_pic1 = pic1
large_pic1[y_offset:y_offset+600,x_offset:x_offset+600] = final_roi
plt.imshow(large_pic1)