# coding: utf-8
import cv2
import sys
import numpy as np

def nada(x): #Necesitamos esta función aunque no haga nada
    pass

#Abrimos la imagen indicada en el primer argumento
try:
    img=cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED);
except:
    print("ERROR al abrir la imagen\n")
    sys.exit(1)

if img is None:
    print("ERROR: Imagen: ", sys.argv[1], " no existe\n")
    sys.exit(1)

#Creamos una imagen vacía de las mismas dimensiones que luego contendrá el resultado final
resultado=np.zeros(img.shape, np.uint8)

#Creamos la ventana
cv2.namedWindow('Imagen')

# Creamos las barras para cada color 
cv2.createTrackbar('R','Imagen',50,255,nada)
cv2.createTrackbar('G','Imagen',100,255,nada)
cv2.createTrackbar('B','Imagen',150,255,nada)

# Creamos un botón ON/OFF
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'Imagen',1,1,nada)

while(1):
    cv2.imshow('Imagen',resultado)#Mostramos la imagen

    k = cv2.waitKey(1) & 0xFF #Miramos la tecla pulsada. Si es Esc nos salimos
    if k == 27:
        break

    # Leemos las posiciones de los 4 trackbars
    r = cv2.getTrackbarPos('R','Imagen')
    g = cv2.getTrackbarPos('G','Imagen')
    b = cv2.getTrackbarPos('B','Imagen')
    s = cv2.getTrackbarPos(switch,'Imagen')
 
    #Modificamos cada componente según su peso. 
    # La operación de multiplicación ha de ser con float
    resultado[:,:,0]=img[:,:,0]*np.float32(b)/255.0
    resultado[:,:,1]=img[:,:,1]*np.float32(g)/255.0
    resultado[:,:,2]=img[:,:,2]*np.float32(r)/255.0
     
    #Si el switch es 0 el resultado será negro
    if s == 0:
        resultado[:] = 0

cv2.destroyAllWindows()
