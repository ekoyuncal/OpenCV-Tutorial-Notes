
import cv2 

image_path = r"C:\Users\emircan\Desktop\openCV/"
resim = cv2.imread("wall-e.jpg")

cv2.namedWindow("Wall-E Renkli", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Wall-E Renkli", resim)
cv2.waitKey(1)



#cvtColor

gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
cv2.imshow("Wall-E Gri", gray)
cv2.waitKey(1)

#image write
#imwrite

status = cv2.imwrite(image_path + "wall-e_gray.jpg", gray)

print("Image written to file-system : ",status)

#Nedense masaüstüne kaydediyor

#direk gray okuyabiliriz

resim_gray = cv2.imread("wall-e.jpg", cv2.IMREAD_GRAYSCALE)
cv2.namedWindow("Gri Okunmus", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Gri Okunmus",resim_gray)
cv2.waitKey(1)