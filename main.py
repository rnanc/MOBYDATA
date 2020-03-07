import cv2
import numpy as np
from time import sleep

largura_min=80 #Largura minima do retangulo
altura_min=80 #Altura minima do retangulo

offset=2 #Erro permitido entre pixel  

pos_linha=230 #Posição da linha de contagem 

delay= 60 #FPS do vídeo

detec = []
pessoas= 0

	
def pega_centro(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx,cy
cap = cv2.VideoCapture('supermarket.mp4')
cap.set(3,1280)

cap.set(4,1024)
human_cascade = cv2.CascadeClassifier( cv2.data.haarcascades + 'haarcascade_upperbody.xml')
subtracao = cv2.bgsegm.createBackgroundSubtractorMOG()
# FULLSCREEN
# cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
while True:
    ret , frame1 = cap.read()
    # tempo = float(1/delay)
    # sleep(tempo) 
    grey = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey,(3,3),5)
    img_sub = subtracao.apply(blur)
    dilat = cv2.dilate(img_sub,np.ones((5,5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx (dilat, cv2. MORPH_CLOSE , kernel)
    # dilatada = cv2.morphologyEx (dilatada, cv2. MORPH_CLOSE , kernel)
    # dilatada = cv2.morphologyEx (dilatada, cv2. MORPH_CLOSE , kernel)
    # dilatada = cv2.morphologyEx (dilatada, cv2. MORPH_CLOSE , kernel)
    # dilatada = cv2.morphologyEx (dilatada, cv2. MORPH_CLOSE , kernel)
    
    human = human_cascade.detectMultiScale(grey, 1.1, 4)
    contorno,h = cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for(x,y,w,h) in human:
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,0,225),3)
        centro = pega_centro(x, y, w, h)
        detec.append(centro)
        cv2.circle(frame1, centro, 4, (0, 225,0), -1)
        # for(i,c) in enumerate(contorno):
        #     (x,y,w,h) = cv2.boundingRect(c)
        #     validar_contorno = (w >= largura_min) and (h >= altura_min)
        #     if not validar_contorno:
        #         continue
        for (x,y) in detec:
            if y<(pos_linha+offset) and y>(pos_linha-offset):
                pessoas+=1
                cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (0,127,255), 3)  
                detec.remove((x,y))
                print("Pessoas detectados até o momento: "+str(pessoas))  
    cv2.line(frame1, (25, pos_linha), (1000, pos_linha), (255,127,0), 3) 
    # for(i,c) in enumerate(contorno):
    #     (x,y,w,h) = cv2.boundingRect(c)
    #     validar_contorno = (w >= largura_min) and (h >= altura_min)
    #     if not validar_contorno:
    #         continue

    #     cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)        
         

    #     for (x,y) in detec:
    #         if y<(pos_linha+offset) and y>(pos_linha-offset):
    #             pessoas+=1
    #             cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (0,127,255), 3)  
    #             detec.remove((x,y))
    #             print("Pessoas detectados até o momento: "+str(pessoas))        
       
    cv2.putText(frame1, "Pessoas: "+str(pessoas), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
    cv2.imshow("Video Original" , frame1)
    cv2.imshow("Detectar",dilatada)

    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()
cap.release()