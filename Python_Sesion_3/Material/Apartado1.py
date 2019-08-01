# -*- coding: utf-8 -*-
'''
Created on 5 de sept. de 2015

@author: hilario
'''
import cv2
import sys

cap = cv2.VideoCapture(sys.argv[1])
fps = cap.get(cv2.CAP_PROP_FPS)
time=int(1000/fps)
print("La variable time =",time)

ret, frame = cap.read()

font = cv2.FONT_HERSHEY_SIMPLEX

while(cap.isOpened() and ret):
    cv2.imshow("frame",frame)
    if cv2.waitKey(time) & 0xFF == ord('q'):
        break
    ret, frame = cap.read()
    
cap.release()
cv2.destroyAllWindows()
