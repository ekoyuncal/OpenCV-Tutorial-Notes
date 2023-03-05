import cv2
import numpy as np

image_path = r"C:\Users\emircan\Desktop\openCV/"

img1 = cv2.imread("wall-e.jpg")
img2 = cv2.imread("wall-e_gray.jpg")
#cv2.namedWindow("OpenCV Renkli", cv2.WINDOW_AUTOSIZE)


cv2.imshow("renkli", img1)
cv2.waitKey(1)

cv2.imshow("gri", img2)
cv2.waitKey(1)

horizontal = np.hstack((img2, img1))
cv2.imshow("renkli ve gri", horizontal)
cv2.waitKey(1)

cv2.imwrite(image_path + "wall-e_2.jpg", horizontal)