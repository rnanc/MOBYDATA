import cv2
import numpy as np
from time import sleep

largura_min = 65 # Largura minima do retangulo
altura_min = 200  # Altura minima do retangulo

offset = 2 # Erro permitido entre pixel

pos_linha = 300  # Posição da linha de contagem

delay = 60  # FPS do vídeo

detec = []
pessoas = 0


def pega_centro(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


cap = cv2.VideoCapture('videos/CESUPA.mp4')
i, frame = cap.read()
fshape = frame.shape
fheight = fshape[0]
fwidth = fshape[1]
#fourcc = cv2.VideoWriter_fourcc(*'MJPG')
video_editado = cv2.VideoWriter("videos/output.mp4", -1, 20.0, (fwidth,fheight))

subtracao = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret, frame1 = cap.read()
    tempo = float(1 / delay)
    sleep(tempo)
    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    img_sub = subtracao.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((15, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20, 1))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)

    img, contorno, h = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.line(frame1, (pos_linha, 2), (pos_linha, 450), (255, 127, 0), 3)
    cv2.line(dilatada, (pos_linha, 2), (pos_linha, 450), (255, 127, 0), 3)
    for (i, c) in enumerate(contorno):
        (x, y, w, h) = cv2.boundingRect(c)
        validar_contorno = (w >= largura_min) and (h >= altura_min)
        if not validar_contorno:
            continue

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        centro = pega_centro(x, y, w, h)
        if(centro not in detec):
            detec.append(centro)
        cv2.circle(frame1, centro, 3, (0, 0, 255), -1)

        for (x, y) in detec:
            if x < (pos_linha + offset) and x > (pos_linha - offset):
                pessoas += 1
                cv2.line(frame1, (pos_linha, 2), (pos_linha, 450), (255, 127, 0), 3)
                detec.remove((x, y))
                print("Pessoas detectados até o momento: " + str(pessoas))
                ret, frame1 = cap.read()
                break

    cv2.putText(frame1, "Pessoas entraram: " + str(pessoas), (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    cv2.imshow("Video Original", frame1)
    video_editado.write(frame1)
    cv2.imshow("Detectar", dilatada)

    if cv2.waitKey(1) == 27:
        break
cap.release()
video_editado.release()
cv2.destroyAllWindows()
