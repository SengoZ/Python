
#Crear un proyecto de procesado de imágenes con OPENCV

import cv2  #Cargamos OpenCV

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
    status = cv2.imwrite('../Material/Pez.png', imagen)
    if status:
        print('Imagen guardada correctamente')
    else:
        print('La imagen no se ha podido guardar')
    #Fin Ejercicio_2

#Espera hasta presionar una tecla. Importante porque si no, no visualizamos la imagen.

cv2.waitKey(0)

#Liberamos la ventana creada

cv2.destroyAllWindows()
