import cv2

#INICIO SESION 3

#INICIO_APARTADO_1

cap = cv2.VideoCapture('../Material/video.avi') #distintos   formatos,  como  MPEG4, MJPG o XVID.

fps = cap.get(cv2.CAP_PROP_FPS) #leemos la velocidad de los fotogramas por segundo
time = int(1000/fps)  #tiempo necesario para cada fotograma

print("La variable time = ", time)

ret, frame = cap.read()

#frame --> fotograma actual
#retval --> si la lectura ha sido correcta

#INICIO_EJECICIO_2

#Ancho y alto del video
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
 
#Definimos el nombre y tipo de extensión del archivo de video.
out = cv2.VideoWriter('../Material/videopy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))

#FIN_EJERCICIO_2

font = cv2.FONT_HERSHEY_SIMPLEX #Fuente de texto

while(cap.isOpened() and ret):
    #INICIO_EJECICIO_1
    
    cv2.putText(frame,'Andres',(300,500), font, 1,(0,0,255),3 ,cv2.LINE_AA) #FRAME, TEXT, Punto en la imagen, fuente, tamaño, color, grosor, estilo
    
    #FIN_EJERCICIO_1
    
    cv2.imshow("frame", frame)
    
    #INICIO_EJECICIO_2
    
    out.write(frame)
    
    #FIN_EJECICIO_2
    
    if(cv2.waitKey(time) & 0xFF == ord('q')):
        break;
    
    ret, frame = cap.read()

#INICIO_EJECICIO_2

#out.release()

#FIN_EJECICIO_2

#cap.release()

#FIN_APARTADO_1

#INCIO_APARTADO_2

cap2 = cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
 
#Definimos el nombre y tipo de extensión del archivo de video.
out2 = cv2.VideoWriter('../Material/autoi.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
 
#El bucle se ejecutará cuando la camara sea abierta satisfactoriamente.
while(cap2.isOpened()):
    ret2, frame2 = cap2.read()
 
    if ret2 == True: 
     
        out2.write(frame2)
 
        cv2.imshow('frame 2',frame2)
 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap2.release()
out2.release()

#FIN_APARTADO_2

out.release()
cap.release()

cv2.destroyAllWindows()
#FIN SESION 3

