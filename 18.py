import cv2

def draw_rectsngle(event,x,y,flag,param):
    global pt1,pt2,topleft_clicked,botright_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        if topleft_clicked == True and botright_clicked == True :
            pt1 = (0,0)
            pt2 = (0,0)
            topleft_clicked = False
            botright_clicked = False
        if topleft_clicked == False:
            pt1=(x,y)
            topleft_clicked = True
        elif botright_clicked == False:
            pt2=(x,y)
            botright_clicked = True

pt1 = (0,0)
pt2 = (0,0)
topleft_clicked = False
botright_clicked = False

cap = cv2.VideoCapture(0)
cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_rectsngle)

while True:
    
    ret,frame = cap.read()
    
    if topleft_clicked:
        cv2.circle(frame,pt1,5,(0,0,255),-1)
    if topleft_clicked and botright_clicked :
        cv2.rectangle(frame,pt1,pt2,(0,0,255),3)
    
    cv2.imshow('Test',frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q') :
        break
        
cap.release()
cv2.destroyAllWindows()