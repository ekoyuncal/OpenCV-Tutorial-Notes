import numpy as np
import cv2

image_path = r"C:\Users\emircan\Desktop\openCV\opencv 501/"

src = cv2.imread(image_path+"frame.png")

gray_src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

qrCoder = cv2.QRCodeDetector()

codeinfo, points, straight_qrcode = qrCoder.detectAndDecode(gray_src)

result = np.copy(src)
cv2.drawContours(result, [np.int32(points)], 0, (0, 0, 255), 2)
##parametreler sırayla çizilecek kaynak, kontor noktaları, kontoru gosteren parametre, renk bilgisi(rgb), thickess(kalınlık)

print("QR code info :\n%s" % codeinfo)