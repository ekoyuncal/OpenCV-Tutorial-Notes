
import cv2 
import numpy as np

image_path = r"C:\Users\emircan\Desktop\openCV/"
source = cv2.imread("work.jpg")

#Örnek eşik
sample_th = 127

gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)

for i in range(5):
    
    ret, binary = cv2.threshold(gray, sample_th, 255, i)
    #sonda verilen threshold tipi her seferinde degisir 1,2,3...
    cv2.imshow("Binary_" + str(i), binary)

cv2.waitKey(1)
