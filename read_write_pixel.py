import cv2
import numpy as np


resim = cv2.imread("OpenCV_Logo.png")
cv2.namedWindow("OpenCV Renkli", cv2.WINDOW_AUTOSIZE)
cv2.imshow("OpenCV Renkli", resim)
cv2.waitKey(1)

x, y, z = resim.shape
print(f"x, y, z -> {x} {y} {z}")


for row in range(x):
    for col in range(y):
        b, g, r = resim[row, col]
        if(b == 255 and g == 255 and r == 255 ):
            b = 0
            g = 0
            r = 0
        elif(b == 0 and g == 0 and r == 0 ):
            b = 255
            g = 255
            r = 255
            
        resim[row, col] = [b, g, r]

cv2.imshow("Siyah OpenCV", resim)
cv2.waitKey(1)