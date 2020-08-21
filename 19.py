import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

full = cv2.imread('sammy.jpg')
full = cv2.cvtColor(full,cv2.COLOR_BGR2RGB)
plt.imshow(full)

face = cv2.imread('sammy_face.jpg')
face = cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
plt.imshow(face)

face.shape
full.shape

sum([1,2,3])
myfunc = eval('sum')
myfunc([1,2,3])

# All the 6 methods for comparison in a list
# Note how we are using strings, later on we'll use the eval() function to convert to function
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for m in methods : 
    
    full_copy = full.copy()
    
    method = eval(m)
    res = cv2.matchTemplate(full_copy,face,method)
    
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
    
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc #(x,y)
    else:
        top_left = max_loc
        
    height , width , channels = face.shape
    bottom_right = [top_left[0]+width,top_left[1]+height]
    
    cv2.rectangle(full_copy,(top_left[0],top_left[1]),(bottom_right[0],bottom_right[1]),(255,0,0),10)
    #plot image
    plt.subplot(121) # 1 row , 2 colomn , in colomn 1
    plt.imshow(res)
    plt.title('HEATMAP OF TEMPLATE MATCHING')
    plt.subplot(122)
    plt.imshow(full_copy)
    plt.title('DETECTION OF TEMPLATE')
    
    plt.suptitle(m)
    plt.show()
    
    print('\n\n')
    
# my_method = eval('cv2.TM_CCOEFF')
# full_copy = full.copy()
# res = cv2.matchTemplate(full_copy,face,my_method)
# plt.imshow(res)