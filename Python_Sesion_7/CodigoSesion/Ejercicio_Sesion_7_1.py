import cv2
import numpy as np

#INICIO_APARTADO_2

#Leemos la imagen
img = cv2.imread('../Material/Morfologico.png',0) 
if img is None: #Si está vacía es que no se ha leído
    print('Imagen no encontrada\n')
    exit(0)

bordersize=10

#Creamos el kernel  usar, en este caso una matriz de 1 de 5x5
kernel = np.ones((5,5),np.uint8)

#INICIO_EJERCICIO_1

font = cv2.FONT_HERSHEY_SIMPLEX #Fuente de texto

#Realizamos la erosión
erosion_1=cv2.erode(img,kernel,iterations = 1)
cv2.putText(erosion_1,'Iteracion: 1',(25,25), font, 1,(127,127,127),1 ,cv2.LINE_AA)

erosion_2=cv2.erode(erosion_1,kernel,iterations = 1)
cv2.putText(erosion_2,'Iteracion: 2',(25,25), font, 1,(127,127,127),1 ,cv2.LINE_AA)

h_aux__1 = np.hstack((erosion_1,erosion_2))


erosion_3=cv2.erode(erosion_2,kernel,iterations = 1)
cv2.putText(erosion_3,'Iteracion: 3',(25,25), font, 1,(127,127,127),1 ,cv2.LINE_AA)

erosion_4=cv2.erode(erosion_3,kernel,iterations = 1)
cv2.putText(erosion_4,'Iteracion: 4',(25,25), font, 1,(127,127,127),1 ,cv2.LINE_AA)

h_aux__2 = np.hstack((erosion_3,erosion_4))
#erosion = .....#Añadir el código necesario

v_aux = np.vstack((h_aux__1, h_aux__2))

#Mostramos las imágenes
cv2.imshow("Original",img)
cv2.imshow("Erosion",v_aux)

#FIN_EJERCICIO_1

#INICIO_EJERCICIO_2

#Realizamos la erosión
dilate_1=cv2.dilate(img,kernel,iterations = 1)
cv2.putText(dilate_1,'Iteracion: 1',(25,25), font, 1,(127,127,127),1 ,cv2.LINE_AA)

dilate_2=cv2.dilate(img,kernel,iterations = 2)
cv2.putText(dilate_2,'Iteracion: 2',(25,25), font, 1,(127,127,127),1 ,cv2.LINE_AA)

h_aux__1 = np.hstack((dilate_1,dilate_2))


dilate_3=cv2.dilate(img,kernel,iterations = 3)
cv2.putText(dilate_3,'Iteracion: 3',(25,25), font, 1,(127,127,127),1 ,cv2.LINE_AA)

dilate_4=cv2.dilate(img,kernel,iterations = 4)
cv2.putText(dilate_4,'Iteracion: 4',(25,25), font, 1,(127,127,127),1 ,cv2.LINE_AA)

h_aux__2 = np.hstack((dilate_3,dilate_4))
#erosion = .....#Añadir el código necesario

v_aux = np.vstack((h_aux__1, h_aux__2))

#Mostramos las imágenes
cv2.imshow("Dilatacion",v_aux)

#FIN_EJERCICIO_2



cv2.waitKey(0)
cv2.destroyAllWindows()

#FIN_APARTADO_2