import cv2
import matplotlib.pyplot as plt
%matplotlib inline

pic1 = cv2.imread("dog_backpack.png")
pic1 = cv2.cvtColor(pic1,cv2.COLOR_BGR2RGB)
pic2 = cv2.imread("watermark_no_copy.png")
pic2 = cv2.cvtColor(pic2,cv2.COLOR_BGR2RGB)

plt.imshow(pic1)
plt.imshow(pic2)

pic1.shape
pic2.shape

pic1 = cv2.resize(pic1,(800,1400))
pic2 = cv2.resize(pic2,(800,1400))

plt.imshow(pic2)

blended = cv2.addWeighted(pic1,0.5,pic2,0.5,0)
plt.imshow(blended)

pic1 = cv2.imread("dog_backpack.png")
pic1 = cv2.cvtColor(pic1,cv2.COLOR_BGR2RGB)
pic2 = cv2.imread("watermark_no_copy.png")
pic2 = cv2.cvtColor(pic2,cv2.COLOR_BGR2RGB)

pic2 = cv2.resize(pic2,(600,600))

pic12 = pic1
x_offset = 0
y_offset = 0

x_end = x_offset + pic2.shape[1]
y_end = y_offset + pic2.shape[0]
pic12[x_offset:x_end,y_offset:y_end] = pic2
plt.imshow(pic12)