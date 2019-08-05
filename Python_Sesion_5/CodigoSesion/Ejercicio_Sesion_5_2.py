# -*- coding: utf-8 -*-
import cv2

mano = cv2.imread("../Material/Radiografia.jpeg")

if mano is None: #Si está vacía es que no se ha leído
    print('Imagen no encontrada\n')
    exit(0)
    
iluminacion = cv2.imread('../Material/EscalaGris.png')

if iluminacion is None: #Si está vacia es que no se ha leído
    print('Imagen no encontrada\n')
    exit(0)

mult=cv2.multiply(mano,iluminacion,None,1/255)

#Python: cv2.multiply(src1, src2[, dst[, scale[, dtype]]])
    #src1 – first input array.
    #src2 – second input array of the same size and the same type as src1.
    #dst – output array of the same size and type as src1. --> si sustituimos None por iluminación podemos aplicar la multiplicidad sobre la imagen iluminacion
    #scale – optional scale factor.


cv2.imshow("Mano", mano)
cv2.imshow("Iluminación", iluminacion)
cv2.imshow("Corregida", mult)

cv2.waitKey(0)
cv2.destroyAllWindows()