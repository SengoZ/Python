# coding: utf-8
import cv2
import sys
import numpy as np

#Abrimos la imagen ruidosa en imgR...
imgR=cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE )
#  y la imagen original para comparación en imgO.
imgO=cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE )

#Comprobamos si la imagen se ha abierto correctamente.
if imgR is None or imgO is None:
     print ("ERROR: Imagen ",sys.argv[1]," o ",sys.argv[2]," no existe\n")
     exit(0)

#Creamos ventanas para mostrar las imágenes.
cv2.namedWindow("Original", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Ruidosa", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Filtrada", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Diferencia", cv2.WINDOW_AUTOSIZE)

_,img0=cv2.threshold(imgO, 128, 255, cv2.THRESH_BINARY)
#Mostramos la imagen original, binarizada, en pantalla.
cv2.imshow("Original", img0)

#Ajustar umbral.
umbral=128
#Umbralizamos la imagen ruidosa.
_,imgR=cv2.threshold(imgR, umbral, 255, cv2.THRESH_BINARY)
#Mostramos la imagen en pantalla.
cv2.imshow("Ruidosa", imgR);

#Operaciones morfológicas
...

#Mostramos la imagen en pantalla.
cv2.imshow("Filtrada", imgR)

#Ontenemos la diferencia
dif=imgR != img0
# Sumamos los píxeles diferentes
a=np.sum(dif[:])
print ("Diferencia: ",a)

#Mostramos la difrencia entre las dos
cv2.imshow("Diferencia", np.uint8(255*dif));

#Esperamos a que el usuario pulse una tecla.
cv2.waitKey(0)

cv2.destroyAllWindows
