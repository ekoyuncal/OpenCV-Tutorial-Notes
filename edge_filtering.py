import numpy as np
import cv2

#Kenarları Koruyan Filtreleme

image_path = r"C:\Users\emircan\Desktop\openCV/"
tree = cv2.imread("tree.jpg")

h, w = tree.shape[:2]

dst = cv2.edgePreservingFilter(tree, sigma_s = 10, sigma_r = 0.9, flags = cv2.RECURS_FILTER)

result = np.zeros([h, w *2, 3], dtype = tree.dtype)
result[0:h, 0:w, :] = tree
result[0:h, w:2*w, :] = dst

result = cv2.resize(result, (w, h //2))
cv2.imshow("Result", result)
cv2.waitKey(1)