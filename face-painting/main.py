import cv2
import numpy as np
from random import randint
import time
cap = cv2.VideoCapture(0)
path = "haarcascade_frontalface_default.xml"
eye_path = "haarcascade_eye.xml"
face_cascade = cv2.CascadeClassifier(path)
eye_cascade = cv2.CascadeClassifier(eye_path)


def get_contours(frame: np.ndarray, x: int, y: int, w: int, h: int) -> np.ndarray:
    """
    Get contours of the image
    """

    resize_frame = frame[y:y+h, x:x+w]
    resize_frame = cv2.GaussianBlur(resize_frame, (5,5), 1)

    gray = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2GRAY)

    threshold = cv2.adaptiveThreshold(
        gray,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 105, 1)
    
    contours, _ = cv2.findContours(
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in contours:
        area = cv2.contourArea(i)
        if area > 50:

            cv2.drawContours(resize_frame, [i], 0, (randint(
                0, 255), randint(0, 255), randint(0, 255)), -1)

    return resize_frame


while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces: tuple[int, int, int] = face_cascade.detectMultiScale(gray, 1.3, 5)
    eyes: tuple[int, int, int] = eye_cascade.detectMultiScale(gray, 1.3, 5)
    before = frame.copy()
    #asd
    gray=cv2.GaussianBlur(gray,(5,5),3)
    threshold = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in contours:
       
        cv2.drawContours(frame, [i], 0, (randint(0, 255), randint(0, 255), randint(0, 255)), -1)
    
    dilate=cv2.dilate(frame,None,iterations=5)

    for a in [faces, eyes]:
        for (x, y, w, h) in a:
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            frame[y:y+h, x:x+w] = get_contours(before, x, y, w, h)
    #frame=cv2.dilate(frame,None,iterations=5)
    cv2.imshow("idk",np.concatenate((frame,dilate),axis=0))
   
   
  
    if cv2.waitKey(1) == 27:
        break


cap.release()
cv2.destroyAllWindows()
