# -*- coding: utf-8 -*-
import cv2
import numpy as np

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
        amount = 0.1
        out = imagen
        # Sal
        num_salt = np.ceil(amount/2.0 * imagen.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt)) for i in imagen.shape]
        out[coords] = 255
        # Pimienta
        num_pepper = np.ceil(amount/2.0* imagen.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in imagen.shape]
        out[coords] = 0
        return out 

def psnr(img1, img2):
    dif=(img1-img2)**2 #Obtenemos el error cuadrático entre las dos imágenes
    dif=np.float32(dif)/img1.size #Hacemos la media para toda la imagen

    if not dif.sum()==0:    
        psnr=10*np.log10(255.0*255.0/dif.sum()) #Obtenemos PSNR
        return psnr
    else:
        print("Imágenes iguales")
        return 10000

img = cv2.imread('Lenna.png',cv2.IMREAD_GRAYSCALE)
if img is None: #Si está vacía es que no se ha leído
	print('Imagen no encontrada\n')
	exit(0)

img2=img.copy()

img= ruido('sp', img)
 
median = cv2.medianBlur(img,3)

print(psnr(img2,median))

res = np.hstack((img,median))
cv2.imshow("Corregida",res)

cv2.waitKey(0)
cv2.destroyAllWindows()
