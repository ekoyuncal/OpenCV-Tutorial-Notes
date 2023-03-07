import numpy as np
import cv2

#HSV Hue Saturation Value

image_path = r"C:\Users\emircan\Desktop\openCV/"
source = cv2.imread("OpenCV_Logo.png")
cv2.namedWindow("RGB", cv2.WINDOW_AUTOSIZE)
cv2.imshow("RGB", source)
cv2.waitKey(1)


#RGB TO HSV

hsv = cv2.cvtColor(source, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
cv2.waitKey(1)