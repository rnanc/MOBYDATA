import numpy as np
import cv2
import copy
from time import sleep
# from progress.bar import Bar


def Rodar(cam):
    capture = cv2.VideoCapture(cam)
    background_subtractor = cv2.bgsegm.createBackgroundSubtractorMOG()
    #length = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

    # bar = Bar('Processing Frames', max=length)

    first_iteration_indicator = 1
    while True:
        sleep(1/60)
        ret, frame = capture.read()

        # If first frame
        if first_iteration_indicator == 1:

            first_frame = copy.deepcopy(frame)
            height, width = frame.shape[:2]
            accum_image = np.zeros((height, width), np.uint8)
            first_iteration_indicator = 0
        else:

            filter = background_subtractor.apply(frame)  # remove the background

            threshold = 2
            maxValue = 2
            ret, th1 = cv2.threshold(filter, threshold, maxValue, cv2.THRESH_BINARY)

            # add to the accumulated image
            accum_image = cv2.add(accum_image, th1)

            color_image_video = cv2.applyColorMap(accum_image, cv2.COLORMAP_SUMMER)

            video_frame = cv2.addWeighted(frame, 0.7, color_image_video, 0.7, 0)
            color_image = cv2.applyColorMap(accum_image, cv2.COLORMAP_HOT)
            result_overlay = cv2.addWeighted(frame, 0.7, color_image, 0.7, 0)

            #cv2.imshow("Video Original" , result_overlay)
            ret, jpeg = cv2.imencode('.jpg', result_overlay)
            send_frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + send_frame + b'\r\n\r\n')
        # bar.next()

    # bar.finish()



    # save the final heatmap
    # cv2.imwrite('diff-overlay.jpg', result_overlay)

    # cleanup
    #capture.release()
    #cv2.destroyAllWindows()
