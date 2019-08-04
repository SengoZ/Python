# coding: utf-8
import cv2
import numpy as np
import sys


#INICIO_APARTADO_1

#INICIO_EJERCICIO_2
visualizar = 1
#FIN_EJERCICIO_2

def nothing(x):
    pass

#INICIO_EJERCICIO_2
def colorR(value):
    global r
    
    r = value
    
    if visualizar == 1:
        img[:,:,2]=cap[:,:,2]*np.float32(r)/255.0
    
def colorB(value):
    global b
    
    b = value
    
    if visualizar == 1:
        
        img[:,:,0]=cap[:,:,0]*np.float32(b)/255.0
    
def colorG(value):
    global g
    
    g = value
    
    if visualizar == 1:
        img[:,:,1]=cap[:,:,1]*np.float32(g)/255.0

def cambio(value):
    global visualizar
    
    if value == 0:
        #El valor del switch es 0 por tanto ponemos la imagen en negro
        visualizar = 0
        img[:] = 0
    else:
        if visualizar == 0:
            #Restaurar la imagen después de cambiar el valor de switch
            img[:,:,0]=cap[:,:,0]*np.float32(b)/255.0
            img[:,:,1]=cap[:,:,1]*np.float32(g)/255.0
            img[:,:,2]=cap[:,:,2]*np.float32(r)/255.0
        
        visualizar = 1
#FIN_EJERCICIO_2
 
path = '../Material/Pez.png'

#Abrimos la imagen indicada en el primer argumento
try:
    cap=cv2.imread(path, cv2.IMREAD_UNCHANGED);
except:
    print("ERROR al abrir la imagen\n")
    sys.exit(1)

if cap is None:
    print("ERROR: Imagen: ", path, " no existe\n")
    sys.exit(1)

# Create a black image, a window
img = np.zeros(cap.shape, np.uint8)

cv2.namedWindow('image')

#INICIO_EJERCICIO_2
# create trackbars for color change
##cv2.createTrackbar('R','image',50,255,nothing)
##cv2.createTrackbar('G','image',100,255,nothing)
##cv2.createTrackbar('B','image',150,255,nothing)

cv2.createTrackbar('R','image',50,255,colorR)
cv2.createTrackbar('G','image',100,255,colorG)
cv2.createTrackbar('B','image',150,255,colorB)

#Asignamos valores para la primera iteración
colorR(50)
colorG(100)
colorB(150)
#FIN_EJERCICIO_2

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'

#INICIO_EJERCICIO_2
##cv2.createTrackbar(switch, 'image',1,1,nothing)
cv2.createTrackbar(switch, 'image',1,1,cambio)

#Imcovamos al metodo cambio para poder visualizar la imagen
cambio(cv2.getTrackbarPos(switch,'Imagen'))
#FIN_EJERCICIO_2

while(1):
    
    cv2.imshow('image',img)
    
    k = cv2.waitKey(1) & 0xFF
    
    if k == 27:
        break
    
    #INICIO_EJERCICIO_2
    # Leemos las posiciones de los 4 trackbars
    ##r = cv2.getTrackbarPos('R','Imagen')
    ##g = cv2.getTrackbarPos('G','Imagen')
    ##b = cv2.getTrackbarPos('B','Imagen')
    ##s = cv2.getTrackbarPos(switch,'Imagen')
 
    #Modificamos cada componente según su peso. 
    # La operación de multiplicación ha de ser con float
    ##img[:,:,0]=cap[:,:,0]*np.float32(b)/255.0
    ##img[:,:,1]=cap[:,:,1]*np.float32(g)/255.0
    ##img[:,:,2]=cap[:,:,2]*np.float32(r)/255.0
     
    #Si el switch es 0 el resultado será negro
    ##if s == 0:
        ##img[:] = 0
    #FIN_EJERCICIO_2

cv2.destroyAllWindows()