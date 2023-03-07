import numpy as np
import cv2

image_path = r"C:\Users\emircan\Desktop\openCV/"
source = cv2.imread("wall-e_small.jpg")

height, weight = source.shape[:2]

image = source.copy()

roi = image[100:240, 400:500, :]

cv2.imshow("ROI", roi)
cv2.waitKey(1)

image[0:140, 0:100, :] = roi
cv2.imshow("Image", image)
cv2.waitKey(1)