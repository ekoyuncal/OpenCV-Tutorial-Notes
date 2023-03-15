import numpy as np
import cv2

image_path = r"C:\Users\emircan\Desktop\openCV\opencv401/"

#p1 = cv2.imread("pedestrian1.jpg")
p2 = cv2.imread("pedestrian2.jpg")

cv2.imshow("Pedestrians2", p2)
cv2.waitKey(1)

hog = cv2.HOGDescriptor()

hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

rects, weights = hog.detectMultiScale(p2, winStride=(4, 4),
                                      padding = (8, 8), scale=1.25)

for (x, y, w, h) in rects:
    cv2.rectangle(p2, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
cv2.imshow("Pedestrians", p2)
cv2.waitKey(1)

cv2.imwrite("detected_pedestrians.jpg", p2)
