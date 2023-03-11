import numpy as np
import cv2

image_path = r"C:\Users\emircan\Desktop\openCV/"
walle = cv2.imread("wall-e.jpg")
eve = cv2.imread("eve.jpg")

#to test
eve2 = eve

hsv1 = cv2.cvtColor(walle, cv2.COLOR_BGR2HSV)
hsv2 = cv2.cvtColor(eve, cv2.COLOR_BGR2HSV)

hsv3 = cv2.cvtColor(eve2, cv2.COLOR_BGR2HSV)

#calcHist

#                #images  #calcChanels #Mask  #HistSize  #Ranges    
hist1 = cv2.calcHist([hsv1], [0, 1], None,  [60, 64], [0, 180, 0, 256])
hist2 = cv2.calcHist([hsv2], [0, 1], None,  [60, 64], [0, 180, 0, 256])
hist3 = cv2.calcHist([hsv3], [0, 1], None,  [60, 64], [0, 180, 0, 256])


#normalize
cv2.normalize(hist1, hist1, 0, 1.0, cv2.NORM_MINMAX)
cv2.normalize(hist2, hist2, 0, 1.0, cv2.NORM_MINMAX)

cv2.normalize(hist3, hist3, 0, 1.0, cv2.NORM_MINMAX)

#CompareHist

#HistComp_Correl
value = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

value2 =cv2.compareHist(hist2, hist3, cv2.HISTCMP_CORREL)

cv2.imshow("Eve", eve)
cv2.waitKey(1)

cv2.imshow("Wall-e",walle)
cv2.waitKey(1)


