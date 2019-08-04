import cv2
import numpy as np
import sys

#INICIO_APARTADO_1

#INICIO_EJERCICIO_1
ix,iy = -1,-1
borde = 1
#FIN_EJERCICIO_1

def draw_circle(evento,x,y,flags,datos):
    #evento --> Tipo de evento: click, dbl click, mouse over, ...
    #'x, y' --> Coordenadas del punto del ratón
    # flags --> Teclas modificadoras (Ctrl, Alt, May, ...)
    # datos --> Opcional 
    global color
    
    #INICIO_EJERCICIO_1
    global ix, iy
    #FIN_EJERCICIO_1

    if evento == cv2.EVENT_MOUSEMOVE:
        '''
        Este evento se genera cada vez que el ratón se mueve por encima de la
        ventana. Se pueden generar varios eventos similares por segundo.
        Por ese motivo, si el evento no es necesario, es conveniente salir
        inmediatamente de la función para no bloquear la aplicación.
        '''
        pass
    elif evento == cv2.EVENT_RBUTTONDOWN:
        
        print("Doble click botón izquierdo\n")
        cv2.circle(img, (x,y), 3, color, -1)
        
    elif evento == cv2.EVENT_LBUTTONDOWN:
        
        print("Pulsar botón izquierdo\n")
        
        #INICIO_EJERCICIO_1
        ix, iy = x, y
        #FIN_EJERCICIO_1
        
    elif evento == cv2.EVENT_LBUTTONUP:
        
        print("Soltar botón izquierdo\n")
        
        #INICIO_EJERCICIO_1
        cv2.rectangle(img, (ix, iy), (x, y), color, borde)
        #FIN_EJERCICIO_1
        
    else:
        
        print("Otro evento\n")
    
            
color = (0,0,255)
path = '../Material/Pez.png'

#Abrimos la imagen indicada en el primer argumento
try:
    cap = cv2.imread(path, cv2.IMREAD_UNCHANGED)
except:
    print("ERROR al abrir la imagen\n")
    sys.exit(1)

if cap is None:
    print("ERROR: Imagen: ", path, " no existe\n")
    sys.exit(1)

cap = cv2.imread('../Material/Pez.png', cv2.IMREAD_UNCHANGED)

rows, cols, channel = cap.shape

img = np.zeros((rows,cols,channel), np.uint8)

img = cap.copy()

'''
Asociamos la función de manejo de eventos a esta ventana.
Pasamos la imagen como argumento a la función. Tener en cuenta
la conversión a puntero void para poder realizar el paso. Observar
en la vallback como se deshace la conversión.

'''
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
#'imagen' --> ventana: Nombre de la ventana de OpenCV
#draw_cicle --> funcion: Nombre de la función que atiende el evento
#datos --> Opcional


while(1): #Bucle infinito, pulsar Esc para salir
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF #Leemos la tecla pulsada
    
    #Cambiamos el color en función de la tecla pulsada
    if k == ord('v'):
        
        color=(0,255,0) #Verde
        
    elif k == ord('a'):
        
        color=(255,0,0) #Azul
        
    elif k == ord('r'):
        
        color=(0,0,255) #Rojo
        
    #INICIO_EJERCICIO_1   
    elif k == 43: #Tecla pulsada +
        
        borde += 1
        
    elif k == 45: #Tecla pulsada -
        
        if borde > 1:
            
            borde -= 1
    #FIN_EJERCICIO_1
            
    elif k == 27:
        break

#Liberamos la ventana creada
cv2.destroyAllWindows()

#FIN_APARTADO_1