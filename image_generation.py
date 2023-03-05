
import cv2
import numpy as np

image_path = r"C:\Users\emircan\Desktop\openCV"
resim = cv2.imread("wall-e.jpg")

cv2.namedWindow("Wall-E Renkli", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Wall-E Renkli", resim)
cv2.waitKey(1)

m1 = np.copy(resim)
m2 = resim


resim[100:200, 200:300, :] = 0
cv2.imshow("m2", m2)
cv2.waitKey(1)

m3 = np.zeros(resim.shape, resim.dtype)
cv2.imshow("m3", m3)
cv2.waitKey(1)



#Draw Rectangle


# Start coordinate, here (5, 5)
# represents the top left corner of rectangle
start_point = (5, 5)

# Ending coordinate, here (220, 220)
# represents the bottom right corner of rectangle
end_point = (1020, 1250)

color = (141, 190, 134)

#Line thickness
thickness = 3


dikdortgenli = cv2.rectangle(m3, start_point, end_point, color, thickness)
cv2.imshow("Dikdortgen", dikdortgenli)


