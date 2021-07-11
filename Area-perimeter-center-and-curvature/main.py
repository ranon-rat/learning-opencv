import numpy as np
import cv2

img = cv2.imread('detect_blob.png',1)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Binary", thresh)
#Canny-edge-detection

_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img2 = img.copy()
index = -1
thickness = 4
color = (255, 0, 255)

objects=np.zeros([img.shape[0],img.shape[1],3], 'uint8')
for c in contours:
    cv2.drawContours(objects,[c],-1,color,-1)
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c,True)
    M = cv2.moments(c)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.circle(objects, (cx, cy), 4, (0, 0, 255), -1)
    cv2.putText(objects, "center", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    print("Area: {}, perimeter: {}".format(area,perimeter))
    cv2.imshow("Contour", objects)
    index += 1
    print("Index: {}".format(index))

    

cv2.waitKey(0)
cv2.destroyAllWindows()
