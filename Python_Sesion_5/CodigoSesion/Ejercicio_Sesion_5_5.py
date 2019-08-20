# -*- coding: utf-8 -*-
import cv2

#INICIO_EJERCICIO_3

import numpy as np

#FIN_EJERCICIO_3

#INICIO_APARTADO_5

#INICIO_EJERCICIO_3

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

img=cv2.imread("../Material/Lenna.png")

if img is None: #Si está vacía es que no se ha leído
    print('Imagen no encontrada\n')
    exit(0)
    
#FIN_EJERCICIO_3


#INICIO_EJERCICIO_1

#res = cv2.resize(img,(int(width/2), int(height/2)), interpolation = cv2.INTER_LANCZOS4)
res = cv2.resize(img, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_LANCZOS4) #Redimensionamos la altura y la anchura de la imagen a la mitad

cv2.imshow("Redimensionado a la mitad",res)
cv2.waitKey(0)
cv2.destroyWindow("Redimensionado a la mitad")

#FIN_EJERCICIO_1


#INICIO_EJERCICIO_2

img2 = res.copy()

height, width = img2.shape[:2]

res = cv2.resize(img2,(int(width*2), int(height*2)), interpolation = cv2.INTER_LANCZOS4) #Redimensionamos la altura y la anchura de la imagen a la forma original

cv2.imshow("Redimensionado original",res)
cv2.waitKey(0)
cv2.destroyWindow("Redimensionado original")

#FIN_EJERCICIO_2

#INCIO_EJERCICIO_3

font = cv2.FONT_HERSHEY_SIMPLEX #Fuente de texto

img_aux = np.hstack((img,res))

aux = 'PSNR: ' + str(psnr(img,res)) + 'dB'

cv2.putText(img_aux,str(aux),(250,500), font, 1,(0,0,0),3 ,cv2.LINE_AA)

cv2.imshow("PSNR",img_aux)
cv2.waitKey(0)
cv2.destroyWindow("PSNR")

#FIN_EJERCICIO_3

#INCIO_EJERCICIO_4

res = cv2.resize(img, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)

img2 = res.copy()

height, width = img2.shape[:2]

res = cv2.resize(img2,(int(width*2), int(height*2)), interpolation = cv2.INTER_CUBIC)

font = cv2.FONT_HERSHEY_SIMPLEX #Fuente de texto

img_aux = np.hstack((img,res))

aux = 'PSNR: ' + str(psnr(img,res)) + 'dB'

cv2.putText(img_aux,str(aux),(250,500), font, 1,(0,0,0),3 ,cv2.LINE_AA)

cv2.imshow("PSNR_2",img_aux)
cv2.waitKey(0)
cv2.destroyWindow("PSNR_2")


#FIN_EJERCICIO_4

#INCIO_EJERCICIO_5

res = cv2.resize(img, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_AREA)

img2 = res.copy()

height, width = img2.shape[:2]

res = cv2.resize(img2,(int(width*2), int(height*2)), interpolation = cv2.INTER_AREA)

font = cv2.FONT_HERSHEY_SIMPLEX #Fuente de texto

img_aux = np.hstack((img,res))

aux = 'PSNR: ' + str(psnr(img,res)) + 'dB'

cv2.putText(img_aux,str(aux),(250,500), font, 1,(0,0,0),3 ,cv2.LINE_AA)

cv2.imshow("PSNR_3",img_aux)
cv2.waitKey(0)
cv2.destroyWindow("PSNR_3")


#FIN_EJERCICIO_5

#INCIO_EJERCICIO_6

res = cv2.resize(img, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_LINEAR)

img2 = res.copy()

height, width = img2.shape[:2]

res = cv2.resize(img2,(int(width*2), int(height*2)), interpolation = cv2.INTER_LINEAR)

font = cv2.FONT_HERSHEY_SIMPLEX #Fuente de texto

img_aux = np.hstack((img,res))

aux = 'PSNR: ' + str(psnr(img,res)) + 'dB'

cv2.putText(img_aux,str(aux),(250,500), font, 1,(0,0,0),3 ,cv2.LINE_AA)

cv2.imshow("PSNR_3",img_aux)
cv2.waitKey(0)
cv2.destroyWindow("PSNR_3")


#FIN_EJERCICIO_6

#O si queremos un tamaño determinado. Cuidado con la relación de aspecto

#res = cv2.resize(img,(640, 480), interpolation = cv2.INTER_AREA)

#cv2.imshow("Resultado3",res)
#cv2.waitKey(0)

#cv2.destroyAllWindows()

#FIN_APARTADO_5