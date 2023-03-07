import cv2
import numpy as np

image_path = r"C:\Users\emircan\Desktop\openCV/"
source = cv2.imread("wall-e.jpg")

rows = source.shape[0]
cols = source.shape[1]

#Shifting

#Changing axis
M = np.float32([[1, 0, 300], [0, 1, 90]])

#with Affine Transform

shifted = cv2.warpAffine(source, M, (cols, rows))

cv2.imshow("Original One", source)
cv2.waitKey(1)

cv2.imshow("Shifted", shifted)
cv2.waitKey(1)


#Rotation

M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)

dst = cv2.warpAffine(source, M, (cols, rows))

cv2.imshow("Img", dst)
cv2.waitKey(1)

#Scaling
#if you want to make it smaller you need to use values less than one.
resized = cv2.resize(source, None, fx = 0.4, fy = 0.4, interpolation = cv2.INTER_CUBIC)
cv2.imshow("img", resized)
cv2.waitKey(1)

cv2.imwrite(image_path + "wall-e_small.jpg", resized)