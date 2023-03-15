import numpy as np
import cv2

image_path = r"C:\Users\emircan\Desktop\openCV\opencv401/"

lena = cv2.imread("lena.jpg")

sharpen = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype = np.float32)
                      #kaynak      #uygulanan maske   #istenen 2d array
sharpen_image = cv2.filter2D(lena, cv2.CV_32F, sharpen)

sharpen_image = cv2.convertScaleAbs(sharpen_image)

cv2.imshow("Sharped_Lena", sharpen_image)
cv2.waitKey(1)

cv2.imread("sharped_lena.jpg", sharpen_image)