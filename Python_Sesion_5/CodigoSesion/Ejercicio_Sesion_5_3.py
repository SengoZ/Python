# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt


#INICIO_APARTADO_3
#Ejemplo de normalización del histograma

img = cv2.imread('../Material/Clara.tif', cv2.IMREAD_GRAYSCALE)

if img is None: #Si está vacía es que no se ha leído
    print('Imagen no encontrada\n')
    exit(0)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img)

img2=(img-min_val)/(max_val-min_val)*255.0 #Normalización de la imagen

#Mostramos la dos imágenes juntas
res = np.hstack((img,np.uint8(img2)))

cv2.imshow("Corregida",res)

#Obtenemos y mostramos el histograma normalizado
hist2,bins2 = np.histogram(img2.flatten(),256,[0,256])
legend = ['Clara', 'Corregida']
plt.hist((img.flatten(),img2.flatten()),256,[0,256], color = ['g', 'r'])
plt.legend(legend)
plt.xlim([0,256])
plt.show()

cv2.destroyWindow('Corregida')

img5 = cv2.imread('../Material/Oscura.tif', cv2.IMREAD_GRAYSCALE)

if img is None: #Si está vacía es que no se ha leído
    print('Imagen no encontrada\n')
    exit(0)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img5)

img6=(img5-min_val)/(max_val-min_val)*255.0 #Normalización de la imagen

#Mostramos la dos imágenes juntas
res = np.hstack((img5,np.uint8(img6)))

cv2.imshow("Corregida_Oscuro",res)

#Obtenemos y mostramos el histograma normalizado
hist2,bins2 = np.histogram(img6.flatten(),256,[0,256])
legend = ['Oscura', 'Corregida_Oscuro']
plt.hist((img5.flatten(),img6.flatten()),256,[0,256], color = ['g', 'r'])
plt.legend(legend)
plt.xlim([0,256])
plt.show()

cv2.destroyWindow('Corregida_Oscuro')

img8 = cv2.imread('../Material/Bajo contraste.tif', cv2.IMREAD_GRAYSCALE)

if img8 is None: #Si está vacía es que no se ha leído
    print('Imagen no encontrada\n')
    exit(0)
    
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img8)

equ=cv2.equalizeHist(img8)

legend = ['Bajo contraste', 'Ecualizada']

#Mostramos la dos imágenes juntas
res = np.hstack((img8,np.uint8(equ)))

cv2.imshow("Ecualizada_Bajo",res)

#Obtenemos y mostramos el histograma original
hist,bins = np.histogram(img8.flatten(),256,[0,256])

hist,bins = np.histogram(equ.flatten(),256,[0,256])
plt.hist((img8.flatten(), equ.flatten()),256,[0,256], color = ['r', 'g'])
plt.legend(legend)
plt.xlim([0,256])
plt.show()

cv2.destroyWindow('Ecualizada_Bajo')

img3 = cv2.imread('../Material/Alto contraste.tif', cv2.IMREAD_GRAYSCALE)

if img3 is None: #Si está vacía es que no se ha leído
    print('Imagen no encontrada\n')
    exit(0)
    
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img3)

equ=cv2.equalizeHist(img3)

legend = ['Alto contraste', 'Ecualizada']

#Mostramos la dos imágenes juntas
res = np.hstack((img3,np.uint8(equ)))

cv2.imshow("Ecualizada_Alto",res)

#Obtenemos y mostramos el histograma original
hist,bins = np.histogram(img3.flatten(),256,[0,256])

hist,bins = np.histogram(equ.flatten(),256,[0,256])
plt.hist((img3.flatten(), equ.flatten()),256,[0,256], color = ['r', 'g'])
plt.legend(legend)
plt.xlim([0,256])
plt.show()

cv2.destroyWindow('Ecualizada_Alto')
cv2.destroyAllWindows()

#FIN_APARTADO_3