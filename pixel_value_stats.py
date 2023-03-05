import numpy as np
import cv2

image_path = r"C:\Users\emircan\Desktop\openCV/"

source = cv2.imread("OpenCV_Logo.png", cv2.IMREAD_GRAYSCALE)

min_value, max_value, min_loc, max_loc = cv2.minMaxLoc(source)

print(f" min value {min_value}, max value {max_value}")


#mean ve standart spma

means, stddev = cv2.meanStdDev(source)

print(f"Mean: {means}, stddev: {stddev}")


source[np.where(source < means)] = 0
source[np.where(source > means)] = 255
# resim piksellerini 0 ve 1 gibi binary hale çevirdik ara renk hiç kalmadı

cv2.imshow("Binary", source)
cv2.waitKey(1)

cv2.imwrite(image_path + "binary_openCV.jpg", source)