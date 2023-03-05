
import cv2
import numpy as np

image_path = r"C:\Users\emircan\Desktop\openCV/"

capture= cv2.VideoCapture(image_path + "animation.mp4")

capture_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
capture_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
capture_count = capture.get(cv2.CAP_PROP_FRAME_COUNT)
capture_fps = capture.get(cv2.CAP_PROP_FPS)

print(capture_height, capture_width, capture_count, capture_fps)


#Avi şeklinde kaydet
write_out = cv2.VideoWriter(image_path + "animation_save.avi",
                            cv2.VideoWriter_fourcc('D', 'I', 'V', 'X'), 15,
                            (np.int(capture_width), np.int(capture_height)), True)

while True:
    
    #Kameradan görüntü alma
    ret, frame = capture.read()
    
    #Görüntünün gelip gelmediğinin kontrolü
    if ret is True:
        #Görüntüyü ekrana ver
        cv2.imshow("Animasyon Videosu", frame)
        write_out.write(frame)
        
        #50 sn sonra çık
        c = cv2.waitKey(50)
        if c == 27:
            break
    else:
        break
    
capture.release()
write_out.release()




