# -*- coding: utf-8 -*-
import cv2
import numpy as np

#INICIO_APARTADO_4
def ruido(tipo_ruido,imagen):
    if tipo_ruido == "gauss":
        row,col= imagen.shape
        mean = 0
        var = 20
        sigma = var**0.5
        gauss = np.random.normal(mean,sigma,(row,col))
        gauss = gauss.reshape(row,col)
        ruidosa = np.uint8(imagen + gauss)
        return ruidosa
    elif tipo_ruido == "sp":
        row,col = imagen.shape
        s_vs_p = 0.5
        
        #INICIO_EJERCICIO_3
        
        #amount = 0.1 #10% de los pixeles modificados, por defecto
        
        #INICIO_EJERCICIO_5
        
        #amount = 0.3 #30% de los pixeles modificados
        amount = 0.5 #50% de los pixeles modificados
        
        #FIN_EJERCICIO_5
        
        #FIN_EJERCICIO_3
        
        out = imagen
        # Sal
        num_salt = np.ceil(amount/2.0 * imagen.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt)) for i in imagen.shape]
        out[tuple(coords)] = 255
        # Pimienta
        num_pepper = np.ceil(amount/2.0* imagen.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in imagen.shape]
        out[tuple(coords)] = 0
        return out 

#PSNR: Proporción Máxima de Señal a Ruido, Los valores típicos que adopta este parámetro están entre 30 y 50 dB, siendo mayor cuanto mejor es la codificación.
def psnr(img1, img2):
    dif=(img1-img2)**2 #Obtenemos el error cuadrático entre las dos imágenes
    dif=np.float32(dif)/img1.size #Hacemos la media para toda la imagen

    if not dif.sum()==0:    
        psnr=10*np.log10(255.0*255.0/dif.sum()) #Obtenemos PSNR
        return psnr
    else:
        print("Imágenes iguales")
        return 10000

img = cv2.imread('../Material/Lenna.png',cv2.IMREAD_GRAYSCALE)
if img is None: #Si está vacía es que no se ha leído
    print('Imagen no encontrada\n')
    exit(0)

img2=img.copy()

img= ruido('sp', img)

#INICIO_EJERCICIO_1

#median = cv2.medianBlur(img,3) #Por defecto

#INICIO_EJERCICIO_2

#median = cv2.medianBlur(img,5) #Modificamos el filtro de mediana a 5x5, se utiliza para la reducción de ruido

#INICIO_EJERCICIO_3

#median = cv2.medianBlur(img,7) #Modificamos el filtro de mediana a 7x7, valor máximo de la matriz de filtro de mediana

#INICIO_EJERCICIO_4

#median = cv2.medianBlur(img,3) #Pixeles modificados al 30% y con un filtro de mediana de 3x3

#INICIO_EJERCICIO_5

#median = cv2.medianBlur(img,5) #Pixeles modificados al 30% y con un filtro de mediana de 5x5

#INICIO_EJERCICIO_6

#median = cv2.medianBlur(img,3) #Pixeles modificados al 50% y con un filtro de mediana de 3x3
median = cv2.medianBlur(img,5) #Pixeles modificados al 50% y con un filtro de mediana de 5x5

#FIN_EJERCICIO_6

#FIN_EJERCICIO_5

#FIN_EJERCICIO_4

#FIN_EJERCICIO_3

#FIN_EJERCICIO_2

#FIN_EJERCICIO_1


print(psnr(img2,median))

res = np.hstack((img,median))

#INICIO_EJERCICIO_1

font = cv2.FONT_HERSHEY_SIMPLEX #Fuente de texto

aux = 'PSNR: ' + str(psnr(img2,median)) + 'dB'

cv2.putText(res,str(aux),(250,500), font, 1,(0,0,0),3 ,cv2.LINE_AA)

#FIN_EJERCICIO_1

cv2.imshow("Corregida",res)

cv2.waitKey(0)
cv2.destroyAllWindows()
#FIN_APARTADO_4
