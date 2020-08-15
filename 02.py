import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from PIL import Image
pic = Image.open("00-puppy.jpg")
type(pic)
pic_array=np.asarray(pic)
pic_array.shape
plt.imshow(pic_array)
pic_red=pic_array.copy()
pic_red.shape
plt.imshow(pic_red)
plt.imshow(pic_red[:,:,1],cmap='gray')
plt.imshow(pic_red[:,:,2],cmap='gray')
plt.imshow(pic_red[:,:,0],cmap='gray')
pic_red[:,:,0]=1
pic_red[:,:,2]=1
plt.imshow(pic_red)
