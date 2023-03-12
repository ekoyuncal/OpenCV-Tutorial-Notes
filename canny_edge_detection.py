import numpy as np
import cv2

image_path = r"C:\Users\emircan\Desktop\openCV/"
src = cv2.imread("guy.jpg")

edge = cv2.Canny(src, 100, 50)

cv2.imshow("AI Guy", edge)
cv2.waitKey(1)
