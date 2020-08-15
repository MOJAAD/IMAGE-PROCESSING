import cv2

img = cv2.imread('E:/University-working/openCV python/Udemy - Python for Computer Vision with OpenCV and Deep Learning 2019-9/Computer-Vision-with-Python/DATA/00-puppy.jpg')

while True :
    
    cv2.imshow('puppy',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
        