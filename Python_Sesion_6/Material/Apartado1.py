import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt

img = cv2.imread(sys.argv[1])
if img is None: #Si está vacía es que no se ha leído
	print('Imagen no encontrada\n')
	exit(0)

bordes = cv2.Canny(img,50,200,apertureSize = 3)# Canny(imagen,Umbral_bajo, Umbral_alto, grado de suavizado)

cv2.imshow('Original',img)

img[bordes==255]=(0,255,0)
cv2.imshow('Bordes',img)

cv2.waitKey(0)

