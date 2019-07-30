
#Crear un proyecto de procesado de imágenes con OPENCV

import cv2  #Cargamos OpenCV

#INICIO APARTADO 3

#Leemos la imagen
imagen = cv2.imread('../Material/Pez.jpg', cv2.IMREAD_UNCHANGED)

#Creamos la ventana donde mostrar la imagen
cv2.namedWindow("Ejemplo 1", cv2.WINDOW_AUTOSIZE)

if imagen is None: #Si está vacia es que no se ha leido
    print('Imagen no encontrada\n')
else:
    #Inicio Ejercicio_1
    print('\n'+str(imagen.shape)+'\n')
    #Fin Ejercicio_1
    cv2.imshow('Ejemplo 1', imagen) #Mostramos la imagen

    #Inicio Ejercicio_2
    #Guardar Imagen en formato PNG
    status_imagen = cv2.imwrite('../Material/Pez.png', imagen)
    if status_imagen:
        print('Imagen guardada correctamente')
    else:
        print('La imagen no se ha podido guardar')
    #Fin Ejercicio_2
    
    #Inicio Ejercicio 3
    imagen_gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    status_imagen_gray = cv2.imwrite('../Material/Pez_Gray.png', imagen_gray)
    
    if status_imagen_gray:
        print('Imagen GRAY guardada correctamente')
    else:
        print('La imagen GRAY no se ha podido guardar')
    
    #Fin Ejercicio 3
#FIN APARTADO 3

#INICIO APARTADO 4

img = cv2.imread('../Material/Smile.png') #Leemos la imagen

if img is None: #Si está vacía es que no se ha leído
    print('Imagen no encontrada\n')
    exit(0)
#INICIO Ejercicio 4
status_ojo_izq = cv2.imwrite('../Material/Ojo_Izq.png', img[55:150, 95:160]) 
status_ojo_drch = cv2.imwrite('../Material/Ojo_Drch.png', img[55:150, 160:225]) 
status_boca = cv2.imwrite('../Material/Boca.png', img[150:255, 65:250]) 

if status_ojo_izq & status_ojo_drch & status_boca:
    print('\nExtracciones ROI completadas')
else:
    print('\nNo se han podido completar las extraciones')
#FIN Ejercicio 4

img[10:150, 20:160]=(0, 0, 255) #Ponemos la ROI en rojo

cv2.imshow('ROI', img)

#FIN APARTADO 4

#INICIO APARTADO 5

img2 = cv2.imread('../Material/Smile.png')

if img2 is None: #Si está vacía es que no se ha leído
    print('Imagen no encontrada\n')
    exit(0)
#INICIO Ejercicio 5
##img_aux = img2 #Ahora img_aux y img2 son iguales pero comparten la misma matriz y si modificamos una, también modificamos otra.
img_aux = img2.copy() #Ahora img_aux es una copia de la original y en ella podemos modificar lo que queramos
#FIN Ejercicio 5

img_aux[10:60, 50:80] = (0, 255, 0)

status_copia = cv2.imwrite('../Material/Copia.png', img2)
status_modificada = cv2.imwrite('../Material/Modificada.png', img_aux)
if status_copia & status_modificada:
    print('\nCopia y Modificada realizadas con exito')
else:
    print('\nError al realizar copia y modificada')
#FIN APARTADO 5


#Espera hasta presionar una tecla. Importante porque si no, no visualizamos la imagen.

cv2.waitKey(0)

#Liberamos la ventana creada

cv2.destroyAllWindows()
