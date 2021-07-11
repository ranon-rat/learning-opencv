import cv2
import numpy as np
color=cv2.imread("butterfly.jpg")
height,width,channels=color.shape
cv2.imshow("image",color)
cv2.moveWindow("image",0,0)

#rgb
b,g,r=cv2.split(color)
rgb_split=np.empty([height,width*3,3],'uint8')
rgb_split[:,0:width]=cv2.merge([b,b,b])
rgb_split[:,width:width*2]=cv2.merge([g,g,g])
rgb_split[:,width*2:width*3]=cv2.merge([r,r,r])
cv2.imshow("channels",rgb_split)
cv2.moveWindow("channels",0,height)
#hsv
hsv=cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
hsv_split=np.concatenate((h,s,v),axis=1)
cv2.imshow("hsv",hsv_split)
cv2.waitKey(0)
cv2.destroyAllWindows()