import cv2,time

cap = cv2.VideoCapture("hand_move.mp4")

if cap.isOpened() == False :
    print('file not found or codec error')
    
while cap.isOpened():
    
    ret,frame = cap.read()
    if ret == True :
        time.sleep(1/10)
        cv2.imshow('frame',frame)
        if cv2.waitKey(10) and 0xFF == ord('q') :
            break
            
    else:
        break
        
cap.release()
cv2.destroyAllWindows()