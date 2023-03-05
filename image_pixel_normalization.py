
import numpy as np
import cv2

image_path = r"C:\Users\emircan\Desktop\openCV/"



source = cv2.imread("OpenCV_Logo.png")

print(source.shape)

source_gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray", source_gray)
cv2.waitKey(1)


print(source_gray.shape)

source_gray = np.float32(source_gray)


#Normalize min_max
print(source_gray)


min_value, max_value, min_loc, max_loc = cv2.minMaxLoc(source_gray)

print(f" min value {min_value}, max value {max_value}")


#mean ve standart spma
means, stddev = cv2.meanStdDev(source_gray)

print(f"Mean: {means}, stddev: {stddev}")

#minmax
dst = np.zeros(source_gray.shape, dtype = np.float32)

cv2.normalize(source_gray, dst=dst, alpha = 0, beta = 1.0, norm_type=cv2.NORM_MINMAX)
print(dst)


cv2.imshow("NORM_MINMAX", np.uint8(dst*255))
cv2.waitKey(1)

means, stddev = cv2.meanStdDev(dst)
print(f"Mean: {means}, stddev: {stddev}")

#Resmin özellikleri ve kendisi aynı yenisi 0 ile 1 ile olusturudu
"""
print(np.uint8(dst*255))
means, stddev = cv2.meanStdDev(source_gray)
print(f"Mean: {means}, stddev: {stddev}")
"""

#NORM_INF
dst = np.zeros(source_gray.shape, dtype = np.float32)
cv2.normalize(source_gray, dst=dst, alpha = 1.0, beta = 0, norm_type=cv2.NORM_INF)
print(dst)
cv2.imshow("NORM_INF", np.uint8(dst*255))
cv2.waitKey(1)

#NORM_L1
dst = np.zeros(source_gray.shape, dtype = np.float32)
cv2.normalize(source_gray, dst=dst, alpha = 1.0, beta = 0, norm_type=cv2.NORM_L1)
print(dst)
cv2.imshow("NORM_L1", np.uint8(dst*10000000))
cv2.waitKey(1)

#NORM_L2
dst = np.zeros(source_gray.shape, dtype = np.float32)
cv2.normalize(source_gray, dst=dst, alpha = 1.0, beta = 0, norm_type=cv2.NORM_L2)
print(dst)
cv2.imshow("NORM_L2", np.uint8(dst*10000))
cv2.waitKey(1)
