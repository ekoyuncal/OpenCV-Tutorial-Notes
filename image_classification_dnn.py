import numpy as np
import cv2


#IMAGE CLASSIFICATION WITH GOOGLENET MODEL

image_path = r"C:\Users\emircan\Desktop\openCV\opencv 501/"

bin_model = "bvlc_googlenet.caffemodel"
protxt = "bvlc_googlenet.prototxt"

with open(image_path+"classification_classes_ILSVRC2012.txt", "rt") as f:
    classes = f.read().split('\n')
    
net = cv2.dnn.readNetFromCaffe(protxt, bin_model)

image2 = cv2.imread("akita.jpg")
image1 = cv2.imread("guinea_pig.jpg")

blob = cv2.dnn.blobFromImage(image1, 1.0, (224, 224), (104, 117, 123), False, crop = False)
# parametreler sırasıyla-> kaynak resim, ölçeklendirme, girdi boyutu, piksel değerlerinden çıkarılacak olan ortalama değer,
# false argumanı, bgr mı rgb mi olacak onu belirler, bgr değil rgb olsun isterseniz true demelisiniz, görüntünün yeniden boyutlanması


result = np.copy(image1)

net.setInput(blob)
out = net.forward()

out = out.flatten()

classId = np.argmax(out)
confidence = out[classId]

t, _ = net.getPerfProfile()
label = "cost time : %.2f ms" %(t * 1000.0 / cv2.getTickFrequency())
cv2.putText(result, label, (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

label = "%s: %.4f" % (classes[classId] if classes else "Class #%d" % classId, confidence)
cv2.putText(result, label, (0, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


show_img = np.hstack((image1, result))
cv2.namedWindow("demo", cv2.WINDOW_NORMAL)
cv2.imshow("demo", show_img)
cv2.waitKey(1)

cv2.imwrite("Classified_guinea_pig.jpg", show_img)