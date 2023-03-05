
import cv2
import numpy as np

capture = cv2.VideoCapture(0)
#0 girildiğinde bilgisayarda bulunan dahili kamera kullanılır

capture_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
capture_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
capture_count = capture.get(cv2.CAP_PROP_FRAME_COUNT)
capture_fps = capture.get(cv2.CAP_PROP_FPS)
print(capture_height, capture_width, capture_count, capture_fps)

def process_video(image, opt = 1):
    dst = None
    if opt == 0:
        dst = cv2.bitwise_not(image)
    elif opt == 1:
        dst = cv2.GaussianBlur(image, (0, 0), 15)
    elif opt == 2:
        dst = cv2.Canny(image, 100, 200)
    return dst


index = 0

while True:
    
    #Kameradan görüntü alma
    ret, frame = capture.read()
    
    #Görüntünün gelip gelmediğinin kontrolü
    if ret is True:
        #Görüntüyü ekrana ver
        cv2.imshow("Video Girdisi", frame)
        c = cv2.waitKey(50)        
        #50 sn sonra çık

        if c == 49:
            index = c -49
        result = process_video(frame, index)
        cv2.imshow("Result", result)
        
        #ESC
        if c == 27: 
            break
        
    else:
        break
    
cv2.waitKey(1)
    

        

    