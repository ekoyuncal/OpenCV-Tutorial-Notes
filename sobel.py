import numpy as np
import cv2

image_path = r"C:\Users\emircan\Desktop\openCV/"
tree = cv2.imread("tree.jpg")

#Sobel Operator
#Türevlere dayali kenar algılama yöntemi

h, w = tree.shape[:2]

x_grad = cv2.Sobel(tree, cv2.CV_32F, 1, 0)
y_grad = cv2.Sobel(tree, cv2.CV_32F, 0, 1)

x_grad = cv2.convertScaleAbs(x_grad)
y_grad = cv2.convertScaleAbs(y_grad)

cv2.imshow("X_grad", x_grad)
cv2.waitKey(1)

cv2.imshow("Y_grad", y_grad)
cv2.waitKey(1)


dst = cv2.add(x_grad, y_grad, dtype = cv2.CV_16S)
dst = cv2.convertScaleAbs(dst)

cv2.imshow("Gradient", dst)
cv2.waitKey(1)
