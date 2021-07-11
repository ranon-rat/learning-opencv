import cv2
import numpy as np

img=cv2.imread("tomatoes.jpg",1)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
res,thresh=cv2.threshold(hsv[:,:,0],25,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Thresholded",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()