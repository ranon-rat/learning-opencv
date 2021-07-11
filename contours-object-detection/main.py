import cv2 
import numpy as np
cap = cv2.VideoCapture(0)




while True:
    _,frame=cap.read()
    frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    blur=cv2.blur(frame,(5,5))
    gray=cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
    thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
    _,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    frame2=frame.copy()
    index=-1
    thickness=4
    color=(255,0,255)
    cv2.drawContours(frame2,contours,index,color,thickness)
    cv2.imshow("Contours",frame2)
    cv2.imshow("Thresh",thresh)
    cv2.imshow("Gray",gray)
    cv2.imshow("Dilate",blur)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
