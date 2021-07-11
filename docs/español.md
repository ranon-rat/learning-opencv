# aprendiendo opencv
# waitKey
## cuerpo
```py
cv2.waitKey(mode)
```
## acerca de esta funcion
el mode desconozco lo que hace pero esta funcion basicamente sirve para obtener la key ,normalmente se usa para evitar que se cierren las ventanas , de esta manera

```py
import numpy
import cv2
img =cv2.imread("opencv-logo.png")
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
cv2.imshow("Image",img)

cv2.waitKey(0)
```
# destroyAllWindows
## cuerpo 
```py
cv2.destroyAllWindows()
```
## acerca de esta funcion
esta funcion lo unico que hace es cerrar todas las ventanas donde se este mostrando alguna imagen
# imread
## cuerpo
```py
cv2.imread(dist,color:int)
```
## acerca de esta funcion
Esta funcion lo que hace es abrir una imagen con el modo configurado (default es todo color(1)).
En el caso de que queramos tener una imagen gris pues se pude hacer lo siguiente

```py
img=cv2.imread("opencv-logo.png",0)
```
# imshow
## cuerpo
```py
cv2.imshow("name",src)
```
## acerca de esta funcion
a esta funcion lo que hace es pasarle el nombre y el array de numpy(en opencv las imagenes son basicamente arrays) , y despues mostrarla en una ventana

# namedWindow
## cuerpo
```py
cv2.namedWindow(name,method)
```
## acerca de esta funcion
Esta funcion lo que hace es configurar la ventana donde se van a mostrar las imagenes de opencv.
# setMouseCallback
## cuerpo 
```py
cv2.setMouseCallback("name",callback)
```
## acerca de esta funcion
para lo que sirve esta funcion basicamente es para detectar algun tipo de evento relacionado con el mouse como dice su nombre , es bastante sencillo de usarlo y solo se necesita tener una funcion con un body algo parecido a este
```py
def click(event,x,y,flags,param):
```
# threshold
## cuerpo
```py
cv2.threshold(source, thresholdValue, maxVal, thresholdingTechnique)
```
## acerca de esta funcion

es basicamente una funcion la cual lo unico que hace es repasar toda una imagen y checar si el valor del pixel que se a ingresado es menor a el valor del threshold , en el caso de que asi sea se va a pasar a la imagen y en el caso de que no pues no va a aparecer.

Y esta es mas o menos la forma en la que funciona:

```py
bw=cv2.imread("detect_blob",0)
height,width=bw.shape[0:2]
binary=np.zeros([height,width,1],'uint8')
thres=85
for row in range(height):
    for col in range(width):
        if frame[row][col]>thres:
            binary[row][col]=255
cv2.imshow('Binary',binary)
```



y la otra forma de hacerlo y la forma mas optima es la siguiente

```py
import numpy as np
import cv2
#original
img =cv2.imread("sudoku.png",0)
cv2.imshow("original",img)
#basic thresholding
ret,thresh_basic=cv2.threshold(img,70,255,cv2.THRESH_BINARY)
cv2.imshow("basic",thresh_basic)

cv2.waitKey(0)
cv2.destroyAllWindows()
```
nos tendria que dar una salida mas o menos asi 
![img](https://media.discordapp.net/attachments/820472030474272769/863602157743243264/Screen_Shot_2021-07-10_at_21.06.26.png?width=904&height=943)
# cvtColor
## cuerpo
```py
cv2.cvtColor(src, code[, dst[, dstCn]])
```
## acerca de esta funcion
Esta funcion te retorna un array con los colores convertidos

```py
import cv2
import numpy as np

img=cv2.imread("tomatoes.jpg",1)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
res,thresh=cv2.threshold(hsv[:,:,0],25,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Thresholded",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

lo que va a hacer aqui es pasarlo de RGB a HSV, en muchos casos es necesario usarlo debido a que si estas usando un threshold por ejemplo quisieras que te de algo asi
![img](https://media.discordapp.net/attachments/820472030474272769/863594676312342538/Screen_Shot_2021-07-10_at_20.36.35.png)


# adaptiveThreshold
## cuerpo 
```py
cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst])
```
## acerca de esta funcion
La funcion anterior de `cv2.threshold` no es tan buena en todos los casos ya que esta solo usa una variable global y esto no es tan bueno debido a que normalmente en una imagen hay una gran cantidad de variedad de condiciones de luz , y para eso viene esta funcion.

Lo que basicamente hace es repazar una y adaptarce a las condiciones de luz con un algoritmo desarrollado por opencv  el cual es bastante cool, 
la manera en la que uno puede usarlo seria mas o menos asi:

```py
import numpy as np

import cv2



img =cv2.imread("sudoku.png",0)



#adaptive thresholding

thresh_adaptive=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,2)

cv2.imshow("adaptive",thresh_adaptive)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

ademas de eso aqui pueden ver las diferencias que hay entre los metodos que tiene threshold 
[![img](https://docs.opencv.org/4.5.2/ada_threshold.jpg)](https://docs.opencv.org/4.5.2/d7/d4d/tutorial_py_thresholding.html)
