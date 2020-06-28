import cv2
import numpy as np
from time import sleep
import datetime
def Rodar(cam=0, largura=None, altura=None, tamanho_font_letra=None, offset=None, ponto_y_init = None, ponto_y_final=None, ponto_x_init=None, ponto_x_final=None, sentido_detectar=None, cor_letra=None, posicao_letra_x = None, posicao_letra_y = None):
    cap = cv2.VideoCapture(cam)
    largura_min = largura or 65  # Largura minima do retangulo
    altura_min = altura or 200  # Altura minima do retangulo
    offset = offset or 2  # Erro permitido entre pixel
    sentido_detectar = sentido_detectar or "h"
    ponto_y_init = ponto_y_init or 2
    ponto_y_final = ponto_y_final or 450
    ponto_x_init = ponto_x_init or 300
    ponto_x_final = ponto_x_final or 300
    cor_letra = cor_letra or (0, 0, 0)
    tamanho_font_letra = tamanho_font_letra or 1
    posicao_letra_x = posicao_letra_x or 20
    posicao_letra_y = posicao_letra_y or 30
    delay = 60  # FPS do vídeo
    detec = []
    pessoas = 0

    def pega_centro(x, y, w, h):
        x1 = int(w / 2)
        y1 = int(h / 2)
        cx = x + x1
        cy = y + y1
        return cx, cy

    #fshape = frame.shape
    #fheight = fshape[0]
    #fwidth = fshape[1]
    #fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    #video_editado = cv2.VideoWriter("videos/output.mp4", -1, 20.0, (fwidth, fheight))

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

        cv2.line(frame1, (ponto_x_init, ponto_y_init), (ponto_x_final, ponto_y_final), (255, 127, 0), 3)
        cv2.line(dilatada, (ponto_x_init, ponto_y_init), (ponto_x_final, ponto_y_final), (255, 127, 0), 3)

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
                if sentido_detectar=="h":
                    if x < (ponto_x_init + offset) and x > (ponto_x_final - offset):
                        pessoas += 1
                        cv2.line(frame1, (ponto_x_init, ponto_y_init), (ponto_x_final, ponto_y_final), (255, 127, 0), 3)
                        detec.remove((x, y))
                        print("Pessoas detectados até o momento: " + str(pessoas))
                        ret, frame1 = cap.read()
                        break
                if sentido_detectar == "v":
                    if y < (ponto_y_init + offset) and y > (ponto_y_final - offset):
                        pessoas += 1
                        cv2.line(frame1, (ponto_x_init, ponto_y_init), (ponto_x_final, ponto_y_final), (255, 127, 0), 3)
                        detec.remove((x, y))
                        print("Pessoas detectados até o momento: " + str(pessoas))
                        ret, frame1 = cap.read()
                        break
        cv2.putText(frame1, "Pessoas entraram: " + str(pessoas), (posicao_letra_x, posicao_letra_y) , cv2.FONT_HERSHEY_SIMPLEX, tamanho_font_letra, cor_letra, 3)
        #cv2.imshow("Video Original", frame1)
        #video_editado.write(frame1)
        #cv2.imshow("Detectar", dilatada)
        relatorio = datetime.datetime.now();
        data = "{:02d}-{:02d}-{:02d}".format(relatorio.day, relatorio.month, relatorio.replace(year=20).year)
        if relatorio.hour == 22 and relatorio.minute == 34 and relatorio.second == 1:
          cv2.imwrite("static/reports/report_"+data+".jpg", frame1)
        ret, jpeg = cv2.imencode('.jpg', frame1)
        send_frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + send_frame + b'\r\n\r\n')
