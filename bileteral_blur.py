import numpy as np
import cv2

#Görüntüde gürültü azaltma ve görüntü yumuşatma için
#filtreleme teknikleri

image_path = r"C:\Users\emircan\Desktop\openCV/"
tree = cv2.imread("tree.jpg")

cv2.namedWindow("Input Tree", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Input Tree", tree)
cv2.waitKey(1)
                   
h, w = tree.shape[:2]
                            #sigma color   #sigma space
dst = cv2.bilateralFilter(tree, 0, 100, 20)
#                       pixel diameter
result = np.zeros([h, w *2, 3], dtype = tree.dtype)
result[0:h, 0:w, :] = tree
result[0:h, w:2*w, :] = dst

#cv2.imshow("Result", result)
#cv2.waitKey(1)

resized = cv2.resize(result,None, fx = 0.6, fy=0.6, interpolation = cv2.INTER_AREA)

cv2.imshow("Result", resized)
cv2.waitKey(1)


