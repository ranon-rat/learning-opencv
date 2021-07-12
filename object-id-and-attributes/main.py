import cv2
import numpy as np
import random
cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    threshold = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1)
    
    _, contours, hierarchy = cv2.findContours(
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for i in contours:
        if cv2.contourArea(i) > 200:
            print(cv2.contourArea(i))
            col = (random.randint(0, 256), random.randint(
                0, 256), random.randint(0, 256))
            cv2.drawContours(img, [i], -1, col, -1)

    cv2.imshow("contours", cv2.dilate(img, None, iterations=2))

    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()
