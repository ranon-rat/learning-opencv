import cv2 
import numpy as np
import random
img=cv2.imread("fuzzy.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(3,3),0)
threshold=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,205,1)
cv2.imshow("threshold",threshold)
_,contours,hierarchy=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img2=img.copy()
index=-1
thickness=4
color=(255,0,255)

cv2.imshow("contours",img2)
print(type(contours))
a=[]

for i in contours:
    if cv2.contourArea(i)>500:
        print(cv2.contourArea(i))
        col=(random.randint(0,256),random.randint(0,256),random.randint(0,256))
        cv2.drawContours(img2,[i],-1,col,-1)
cv2.imshow("contours",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()