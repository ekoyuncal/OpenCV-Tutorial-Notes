import numpy as np
import cv2

#Gürültü azaltmak ve nesne belirleme amacıyla
#pikselleri eşik değerine göre siyah ya da beyaz olarak günceller

image_path = r"C:\Users\emircan\Desktop\openCV/"
lena = cv2.imread("lena.jpg")

#Gri skalaya çevrilmiş resim üzerine uygulanabilir

gray_lena = cv2.cvtColor(lena, cv2.COLOR_BGR2GRAY)

ret, binary =cv2.threshold(gray_lena, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)


cv2.imshow("binary", binary)
cv2.waitKey(1)



