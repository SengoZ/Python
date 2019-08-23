import cv2
import sys

#Leemos la imagen
imagen = cv2.imread(sys.argv[1])
if imagen is None: #Si está vacía es que no se ha leído
	print('Imagen no encontrada\n')
	exit(0)

#La convertimos para asegurarnos que es en escala de grises
gris=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

#La umbralizamos y obtenemos la máscara y el umbral usado
ret,mask=cv2.threshold(gris, 128, 255, cv2.THRESH_BINARY)

print ("Umbral utilizado: ",ret)

#Mostramos el resultado    
cv2.namedWindow( "Imagen", cv2.WINDOW_AUTOSIZE )
cv2.imshow("Imagen", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
