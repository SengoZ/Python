# coding: utf-8
import cv2
import numpy as np

#INICIO_APARTADO_4

#Abrimos la imagen ruidosa en imgR...
imgR=cv2.imread('../Material/elipse2.png', cv2.IMREAD_GRAYSCALE )
#  y la imagen original para comparación en imgO.
imgO=cv2.imread('../Material/elipse.png', cv2.IMREAD_GRAYSCALE )

#Comprobamos si la imagen se ha abierto correctamente.
if imgR is None or imgO is None:
    print ("ERROR: Imagen ",'../Material/elipse2.png'," o ",'../Material/elipse.png'," no existe\n")
    exit(0)

#Creamos ventanas para mostrar las imágenes.
cv2.namedWindow("Original", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Ruidosa", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Filtrada", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Diferencia", cv2.WINDOW_AUTOSIZE)

_,img0=cv2.threshold(imgO, 128, 255, cv2.THRESH_BINARY)
#Mostramos la imagen original, binarizada, en pantalla.
#cv2.imshow("Original", img0)

#Ajustar umbral.
umbral=128
#Umbralizamos la imagen ruidosa.
_,imgR=cv2.threshold(imgR, umbral, 255, cv2.THRESH_BINARY)
#Mostramos la imagen en pantalla.
#cv2.imshow("Ruidosa", imgR);

font = cv2.FONT_HERSHEY_SIMPLEX #Fuente de texto

cv2.putText(img0,'Original',(25,25), font, 0.5,(255,255,255),1 ,cv2.LINE_AA)
cv2.putText(imgR,'Ruidosa',(25,25), font, 0.5,(255,255,255),1 ,cv2.LINE_AA)

h_aux_1 = np.hstack((img0, imgR))

#kernel
kernel = np.ones((3,3),np.uint8)

#FORMA MANUAL DE REALIZAR LA APERTURA Y CIERRE

#imgR=cv2.erode(imgR,kernel,iterations = 1)

#imgR=cv2.dilate(imgR,kernel,iterations = 2)

#imgR=cv2.erode(imgR,kernel,iterations = 1)

#METODOS DE APERTURA Y CIERRE  MISMO RESULTADO QUE LAS LINEAS DE ARRIBA (DIFERENCIA 464)

imgR = cv2.morphologyEx(imgR, cv2.MORPH_OPEN, kernel)

imgR = cv2.morphologyEx(imgR, cv2.MORPH_CLOSE, kernel)

#Mostramos la imagen en pantalla.
#cv2.imshow("Filtrada", imgR)

#Ontenemos la diferencia
dif=imgR != img0
# Sumamos los píxeles diferentes
a=np.sum(dif[:])
print ("Diferencia: ",a)

cv2.putText(imgR,'Filtrada',(25,25), font, 0.5,(255,255,255),1 ,cv2.LINE_AA)
#cv2.putText(np.uint8(255*dif),'Diferencia',(25,25), font, 0.5,(255,255,255),1 ,cv2.LINE_AA)

h_aux_2 = np.hstack((imgR, np.uint8(255*dif)))

#Mostramos la difrencia entre las dos

v_aux = np.vstack((h_aux_1, h_aux_2))
cv2.imshow("Operaciones morfologicas", v_aux);

#Esperamos a que el usuario pulse una tecla.
cv2.waitKey(0)

cv2.destroyAllWindows

#FIN_APARTADO_4