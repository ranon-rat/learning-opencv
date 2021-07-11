import numpy as np
import cv2
#original
img =cv2.imread("sudoku.png",0)
cv2.imshow("original",img)
#basic thresholding 
ret,thresh_basic=cv2.threshold(img,70,255,cv2.THRESH_BINARY)
cv2.imshow("basic",thresh_basic)
#adaptive thresholding
thresh_adaptive=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow("adaptive",thresh_adaptive)

cv2.waitKey(0)
cv2.destroyAllWindows()
