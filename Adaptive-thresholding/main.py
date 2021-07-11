import numpy as np
import cv2
#original
img =cv2.imread("sudoku.png",0)
cv2.imshow("original",img)
#basic thresholding 
ret,thresh_basic=cv2.threshold(img,70,255,cv2.THRESH_BINARY)
cv2.imshow("basic",thresh_basic)
#adaptive thresholding
thresh_adaptive=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,2)

_,contours,hierarchy=cv2.findContours(thresh_adaptive,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img2=img.copy()
cv2.drawContours(img2,contours,-1,(0,255,0),3)
cv2.imshow("adaptive",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
