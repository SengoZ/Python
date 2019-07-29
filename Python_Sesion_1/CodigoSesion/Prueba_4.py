import cv2
 
# Create a VideoCapture object
cap = cv2.VideoCapture(0)
 
 

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
 
#Definimos el nombre y tipo de extensión del archivo de video.
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
 
#El bucle se ejecutará cuando la camara sea abierta satisfactoriamente.
while(cap.isOpened()):
    ret, frame = cap.read()
 
    if ret == True: 
     
        out.write(frame)
 
        cv2.imshow('frame',frame)
 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

 
# Para ternimar tenemos que liberar los objetos de video tanto de lectura como de escritura.
cap.release()
out.release()
 
# Cerramos todas las ventanas
cv2.destroyAllWindows() 
