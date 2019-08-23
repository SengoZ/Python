# coding: utf-8
import numpy as np
import sys
import cv2

#Función para atender a los eventos del ratón
def EventoRaton(evento, x, y, flags,datos):
     '''
     Aquí vamos a utilizar el color que hemos extraido y el umbral pasado, para segmentar
     con la función inRange(). Para ello debemos fijar un umbral inferior de color
     y un umbral superior. Entre ellos estarán los colores que queremos.
     '''	
     if evento == cv2.EVENT_LBUTTONDOWN:
          #Leemos el color en el punto marcado. En este caso en HSV
          color=hsv[y,x]
          #Buscamos los colores alrededor del marcado según los umbrales
          low=np.float32(color)-Umbral 
          high=np.float32(color)+Umbral
          #Los que son negativos los ponemos a 0
          low[low<0]=0 
          #Los que son mayores que 255 los ponemos a 255
          high[high>255]=255
          if high[0]>180:#Pero la componente H sólo puede llegar a 180
              high[0]=180

          print "Color seleccionado:",color
          print "Color low:",low,"Color high:",high 

          #Obtenemos la máscara
          mask=cv2.inRange(hsv,low,high)
          img2=img.copy()#Copiamos la imagen para no perderla
          #Pintamos de verde los colores que queremos segmentar
          img2[mask==255]=(0,255,0)
          #Mostramos el resultado
          cv2.imshow("Imagen", img2)

#Iniciamos aquí el programa

if len(sys.argv) < 5:
    print "\nUso: python Apartado3hsv.py Imagen UmbralH UmbralS UmbralV\n"
    exit()

# Cargar la imagen
img = cv2.imread(sys.argv[1])
#Convertimos a HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# Leemos los umbrales para segmentar
UmbralH=int(sys.argv[2])
UmbralS=int(sys.argv[3])
UmbralV=int(sys.argv[4])
#Y los juntamos en un array para manejarlos mejor
Umbral=[UmbralH, UmbralS, UmbralV]

#Definimos 
low=np.array([0,0,0])
high=np.array([0,0,0])


if img is None:
	print "ERROR: Imagen "+ sys.argv[1]+" no existe\n"
        exit(0)

#Creamos una ventana donde mostrar la imagen.
cv2.namedWindow("Imagen", cv2.CV_WINDOW_AUTOSIZE)
#Mostramos la imagen en pantalla.
cv2.imshow("Imagen", img)
#Creamos el Callback para el ratón
cv2.setMouseCallback("Imagen", EventoRaton)

c=0
#Creamos un bucle infinito, que sólo finalizará al pulsar Esc.
while not c==27:
	#Esperamos a que el usuario pulse una tecla.
	c=cv2.waitKey(0) & 0xFF


cv2.destroyAllWindows()

