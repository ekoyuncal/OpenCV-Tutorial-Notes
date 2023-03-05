
import cv2
import numpy as np

image_path = r"C:\Users\emircan\Desktop\openCV/"
source = cv2.imread("wall-e.jpg")


#X Flip
dst1 = cv2.flip(source, 0)
cv2.imshow("X-Flip", dst1)
cv2.waitKey(1)

cv2.imwrite(image_path + "x_wall-e.jpg", dst1)

#Y Flip
dst2 = cv2.flip(source, 1)
cv2.imshow("Y-Flip", dst2)
cv2.waitKey(1)

cv2.imwrite(image_path + "y_wall-e.jpg", dst2)


#XY Flip
dst3 = cv2.flip(source, -1)
cv2.imshow("XY-Flip", dst3)
cv2.waitKey(1)

cv2.imwrite(image_path + "xy_wall-e.jpg", dst3)