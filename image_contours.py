import numpy as np
import cv2


#Image Contours ( Görüntü Konturları )

image_path = r"C:\Users\emircan\Desktop\openCV/"
lena = cv2.imread("lena.jpg")
                  
def threshold_demo(image):
    dst = cv2.GaussianBlur(image, (3, 3), 0) #Gürültü azaltma
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)#Gri yapma
    
    #Binarye cevirme
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
    
    cv2.imshow("binary", binary)
    return binary

def canny_demo(image):
    t = 100
    canny_output = cv2.Canny(image, t, t*2)
    cv2.imshow("Canny_output", canny_output)
    return canny_output


binary = threshold_demo(lena)
canny = canny_demo(lena)

contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)

for c in range(len(contours)):
    cv2.drawContours(lena, contours, c, (0, 0, 255), 1, 8)
    

cv2.imshow("Contours Demo", lena)
cv2.waitKey(1)

