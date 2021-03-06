import numpy as np
import cv2
import datetime
# use it if you wonna write video or ffmpeg 
# from skvideo.io import FFmpegWriter 

def Rodar(cam):

    cap = cv2.VideoCapture(cam)
    start = 1
    duration = 10
    fps = '30'

    outfile = 'heatmap.mp4'

    while True:
        try:
            _, f = cap.read()
            f = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
            f = cv2.GaussianBlur(f, (11, 11), 2, 2)
            cnt = 0
            res = 0.05*f
            res = res.astype(np.float64)
            break
        except:
            print('s')


    fgbg = cv2.createBackgroundSubtractorMOG2(history=1, varThreshold=100,
                                              detectShadows=True)


    #writer = FFmpegWriter(outfile, outputdict={'-r': fps})
    #writer = FFmpegWriter(outfile)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (13, 13))
    cnt = 0
    sec = 0
    #fotoRelatorio = cap.read();
    while True:
        #if sec == duration: break
        cnt += 1
        if cnt % int(fps) == 0:
            print(sec)
            sec += 1
        ret, frame = cap.read()
        if not ret: break
        fgmask = fgbg.apply(frame, None, 0.01)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #if cnt == 30: res
        gray = cv2.GaussianBlur(gray, (11, 11), 2, 2)
        gray = gray.astype(np.float64)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
        fgmask = fgmask.astype(np.float64)
        res += (40 * fgmask + gray) * 0.01
        res_show = res / res.max()
        res_show = np.floor(res_show * 255)
        res_show = res_show.astype(np.uint8)
        res_show = cv2.applyColorMap(res_show, cv2.COLORMAP_JET)
        #cv2.imshow('s', res_show)
        relatorio = datetime.datetime.now();
        data = "{:02d}-{:02d}-{:02d}".format(relatorio.day, relatorio.month, relatorio.replace(year=20).year)
        if relatorio.hour == 22 and relatorio.minute == 29 and relatorio.second == 1:
          cv2.imwrite("static/reports/report_"+data+".jpg", res_show)
        ret, jpeg = cv2.imencode('.jpg', res_show)
        send_frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + send_frame + b'\r\n\r\n')


#writer.close()
#cap.release()
#cv2.destroyAllWindows()