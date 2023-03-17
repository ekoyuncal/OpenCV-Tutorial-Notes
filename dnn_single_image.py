import numpy as np
import cv2

#DNN SSD MODELİ İLE TEK SINIFLI GÖRÜNTÜ SINIFLANDIRMA

image_path = r"C:\Users\emircan\Desktop\openCV\opencv 501/"

model_bin = "MobileNetSSD_deploy.caffemodel"
config_text = "MobileNetSSD_deploy.prototxt"

objName = ["background", "aeroplane", "cow", "bird", "boat", "bottle", "bus", "car",
           "cat", "sheep", "sofa", "train", "dog", "horse"]

net = cv2.dnn.readNetFromCaffe(config_text, model_bin)

image = cv2.imread("akita.jpg")
h = image.shape[0]
w = image.shape[1]

layerNames = net.getLayerNames()
lastLayerId = net.getLayerId(layerNames[-1])
lastLayer = net.getLayer(lastLayerId)

blobImage = cv2.dnn.blobFromImage(image, 0.007843, (300, 300), (127.5, 127.5, 127.5), True, crop = False)
net.setInput(blobImage)
cvOut = net.forward()

for detection in cvOut[0, 0, :, :]:
    score = float(detection[2])
    objIndex = int(detection[1])
    if score > 0.5:
        left = detection[3]*w
        top = detection[4]*h
        right = detection[5]*w
        bottom = detection[6]*h
        
        cv2.rectangle(image, (int(left), int(top)), (int(right), int(bottom)), (255, 0, 0), thickness = 2)
        cv2.putText(image, "Score:%.2f, %s" %(score, objName[objIndex]), 
                    (int(left) -10, int(top) -5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, 8)
        
cv2.imshow("Mobilenet-ssd-demo", image)
cv2.imwrite("detected_dog.jpg", image)
cv2.waitKey(1)