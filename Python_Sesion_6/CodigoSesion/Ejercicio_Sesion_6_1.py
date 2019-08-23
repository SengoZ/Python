import cv2

#INICIO_APARTADO_1

#INICIO_EJERCICIO_1

#import numpy as np
#import sys
#from matplotlib import pyplot as plt

#FIN_EJERCICIO_1

#INICIO_EJERCICIO_1

lower = 50
upper = 200

def unbralBajo(value):
    global lower
    lower = value
    actualizar() 

    
def umbralAlto(value):
    global upper
    upper = value
    actualizar()


def actualizar():
    global img_bordes, bordes, aux
    aux = "Umbral bajo: "+ str(lower)+ "\nUmbral alto: "+ str(upper)
    img_bordes = img.copy()
    bordes = cv2.Canny(img, lower, upper)
        
    img_bordes[bordes==255]=(0,255,0)

#FIN_EJERCICIO_1

img = cv2.imread('../Material/Senal.jpg')

if img is None: #Si está vacía es que no se ha leído
    
    print('Imagen no encontrada\n')
    exit(0)

#INICIO_EJERCICIO_1

#bordes = cv2.Canny(img,50,200,apertureSize = 3)# Canny(imagen,Umbral_bajo, Umbral_alto, grado de suavizado)
bordes = cv2.Canny(img,lower,upper,apertureSize = 3)# Canny(imagen,Umbral_bajo, Umbral_alto, grado de suavizado)


cv2.imshow('Original',img)


img_bordes = img.copy()

cv2.namedWindow('Bordes')
font = cv2.FONT_HERSHEY_SIMPLEX #Fuente de texto

# add lower and upper threshold slidebars to "Bordes"
cv2.createTrackbar('Umbral bajo', 'Bordes', 50, 255, unbralBajo)
cv2.createTrackbar('Umbral alto', 'Bordes', 100, 255, umbralAlto)

actualizar()

#cv2.waitKey(0)

# Infinite loop until we hit the escape key on keyboard
while(1):

    # display images
    y0, dy = 25, 25
    for i, line in enumerate(aux.split('\n')):
        y = y0 + i*dy
        cv2.putText(img_bordes,line,(100,y), font, 0.5,(0,0,0),1 ,cv2.LINE_AA)
    cv2.imshow('Bordes', img_bordes)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:   # hit escape to quit
        break

cv2.destroyAllWindows()

#FIN_EJERCICIO_1


#FIN_APARTADO_1

