import cv2
import numpy as np

#Leemos la imagen
img = cv2.imread('Morfologico.png',0) 
if img is None: #Si está vacía es que no se ha leído
	print('Imagen no encontrada\n')
	exit(0)

#Creamos el kernel  usar, en este caso una matriz de 1 de 5x5
kernel = np.ones((5,5),np.uint8)
#Realizamos la erosión
erosion=cv2.erode(img,kernel,iterations = 1)
#erosion = .....#Añadir el código necesario

#Mostramos las imágenes
cv2.imshow("Imagen",img)
cv2.imshow("Erosion",erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
