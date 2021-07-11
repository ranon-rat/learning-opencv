import cv2
import numpy as np

cap=cv2.VideoCapture(0)


while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(500,500),fx=0.5,fy=0.5)

    blur=cv2.blur(frame,(5,5))
    
    edges=cv2.Canny(blur,100,70)
    cv2.imshow('edges',edges)
    cv2.imshow('frame',frame)
    cv2.imshow('blur',blur)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

"""
img=cv2.imread("tomatoes.jpg",1)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
res,thresh=cv2.threshold(hsv[:,:,0],25,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Thresholded",thresh)
edges=cv2.Canny(img,100,70)
cv2.imshow("Canny-edge-detection",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()"""