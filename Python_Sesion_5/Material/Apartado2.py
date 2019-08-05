# -*- coding: utf-8 -*-
import cv2

mano=cv2.imread("Radiografia.jpeg")
if mano is None: #Si está vacía es que no se ha leído
	print('Imagen no encontrada\n')
	exit(0)

ilum=cv2.imread("EscalaGris.png")
if ilum is None: #Si está vacía es que no se ha leído
	print('Imagen no encontrada\n')
	exit(0)

mult=cv2.multiply(...,...,None,...)#Sustituya los puntos por los parámetros adecuados

cv2.imshow("Mano", mano)
cv2.imshow("Corregida", mult)


cv2.waitKey(0)
cv2.destroyAllWindows()
