import cv2
import numpy as np
cap=cv2.VideoCapture(0)


while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(500,500),(0,0),fx=0.5,fy=0.5)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    ret,thresh=cv2.threshold(frame,thresh=150,maxval=255,type=cv2.THRESH_BINARY)
    cv2.imshow('Threshold',thresh)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
"""
height,width=bw.shape[0:2]
cv2.imshow("Original",bw)
binary=np.zeros([height,width,1],'uint8')
thres=85
for row in range(height):
    for col in range(width):
        if bw[row][col]>thres:
            binary[row][col]=255

cv2.imshow("Slow Binary",binary)
cv2.waitKey(0)
cv2.destroyAllWindows()"""