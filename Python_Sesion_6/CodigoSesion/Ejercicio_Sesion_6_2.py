import cv2
import numpy as np

#INICIO_APARTADO_2

#INICIO_EJERCICIO_2

cap = cv2.VideoCapture('../Material/movil.avi') #distintos   formatos,  como  MPEG4, MJPG o XVID.

fps = cap.get(cv2.CAP_PROP_FPS) #leemos la velocidad de los fotogramas por segundo
time = int(1000/fps)  #tiempo necesario para cada fotograma

print("La variable time = ", time)

ret, frame = cap.read()

##Leemos la imagen
#imagen = cv2.imread('../Material/Fotograma.png')
#if imagen is None: #Si está vacía es que no se ha leído
    #print('Imagen no encontrada\n')
    #exit(0)

#FIN_EJERCICIO_2

#INICIO_EJERCICIO_2

#Ancho y alto del video
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

#Definimos el nombre y tipo de extensión del archivo de video.
out = cv2.VideoWriter('../Enunciado/Resultado_Apartado_2/THRESH_TOZERO_INV.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width*2,frame_height))

##La convertimos para asegurarnos que es en escala de grises
#gris=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)



#FIN_EJERCICIO_2

##La umbralizamos y obtenemos la máscara y el umbral usado
#ret,mask=cv2.threshold(gris, 128, 255, cv2.THRESH_BINARY)
#mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

#print ("Umbral utilizado: ",ret)

#INICIO_EJERCICIO_2

#img_aux = np.hstack((imagen,mask_bgr))

#Mostramos el resultado    
cv2.namedWindow( "Imagen")
#cv2.imshow("Imagen", img_aux)

#cv2.waitKey(0)

#FIN_EJERCICIO_2

#INICIO_EJERCICIO_2

font = cv2.FONT_HERSHEY_SIMPLEX #Fuente de texto

while(cap.isOpened() and ret):
    
    aux = 'Original'
    original = frame.copy()
    cv2.putText(original,str(aux),(25,25), font, 0.5,(127,127,127),1 ,cv2.LINE_AA)
    
    image_conversion = frame.copy()
    gris=cv2.cvtColor(image_conversion, cv2.COLOR_BGR2GRAY)
    
    #La umbralizamos y obtenemos la máscara y el umbral usado
    ret,mask=cv2.threshold(gris, 170, 255, cv2.THRESH_TOZERO_INV)
    mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    
    aux_gray = 'threshold-->cv2.THRESH_TOZERO_INV'
    cv2.putText(mask_bgr,str(aux_gray),(25,25), font, 0.5,(127,127,127),1 ,cv2.LINE_AA)

    img_aux = np.hstack((original,mask_bgr))
    cv2.imshow("Imagen", img_aux)
    
    out.write(img_aux)
    
    if(cv2.waitKey(time) & 0xFF == ord('q')):
        break;
    
    ret, frame = cap.read()

#FIN_EJERCICIO_2

cv2.destroyAllWindows()


#FIN_APARTADO_2