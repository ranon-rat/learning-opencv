import cv2 
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    frame=frame.resize((500,500),(0,0),fx=0.5,fy=0.5)
    kernel=np.ones((5,5),np.uint8)
    dilate=cv2.dilate(frame,kernel,iterations=5)
    cv2.imshow('frame',dilate)
    erode=cv2.erode(frame,kernel,iterations=5)
    cv2.imshow('erode',erode)
  
    #hsv
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    h,s,v=cv2.split(hsv)
    hsv_split=np.concatenate((h,s,v),axis=1)
    cv2.imshow('hsv',hsv_split)
    #ycrcb
    ycrcb=cv2.cvtColor(frame,cv2.COLOR_BGR2YCR_CB)
    y,cr,cb=cv2.split(ycrcb)
    ycrcb_split=np.concatenate((y,cr,cb),axis=1)
    cv2.imshow('ycrcb',ycrcb_split)
    #blur
    blur=cv2.blur(frame,(55,5))
    cv2.imshow('blur',blur)
    

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
