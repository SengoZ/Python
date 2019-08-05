# -*- coding: utf-8 -*-
import cv2

img1=cv2.imread('Pez.jpg')
if img1 is None: #Si está vacía es que no se ha leído
	print('Imagen no encontrada\n')
	exit(0)

img2=cv2.imread('flor.jpg')
if img2 is None: #Si está vacía es que no se ha leído
	print('Imagen no encontrada\n')
	exit(0)

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

suma=gray1+gray2 # Suma numpy

suma2=cv2.add(gray1,gray2) # Suma OpenCV

cv2.imshow("Suma Numpy", suma)
cv2.imshow("Suma OpenCV", suma2)

cv2.waitKey(0)
cv2.destroyAllWindows()
