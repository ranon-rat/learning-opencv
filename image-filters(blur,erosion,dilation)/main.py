import cv2
import numpy as np

image =cv2.imread("thresh.jpg")
cv2.imshow("Original",image)
#blur
blug=cv2.GaussianBlur(image,(5,55),0)
cv2.imshow("Blur",blug)
#erode and dilation
kernel=np.ones((5,5),np.uint8)
erosion=cv2.erode(image,kernel,iterations=1)
cv2.imshow("Erosion",erosion)
dilation=cv2.dilate(image,kernel,iterations=1)
cv2.imshow("Dilation",dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()