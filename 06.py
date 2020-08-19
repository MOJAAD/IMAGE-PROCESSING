import cv2
import matplotlib.pyplot as plt
%matplotlib inline

pic = cv2.imread("00-puppy.jpg")
plt.imshow(pic)

pic = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
plt.imshow(pic)

pic = cv2.cvtColor(pic,cv2.COLOR_BGR2HSV)
plt.imshow(pic)

pic = cv2.cvtColor(pic,cv2.COLOR_BGR2HLS)
plt.imshow(pic)