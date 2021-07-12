import cv2
import numpy as np

cap=cv2.VideoCapture(0)
path="haarcascade_eye.xml"

eye_cascade=cv2.CascadeClassifier(path)
while True:
    _,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    eyes=eye_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in eyes:
        yc=(y+y+h)/2
        xc=(x+x+w)/2
        radius=w/2
        
        cv2.circle(img,(int(xc),int(yc)),int(radius),(0,0,255),2)

  

    cv2.imshow("Eyes",img)
    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()

