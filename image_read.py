import cv2 as cv

resim = cv.imread("wall-e.jpg")


#namedwindow
cv.namedWindow("Wall-E test", cv.WINDOW_AUTOSIZE)

#imshow
cv.imshow("Wall-E test", resim)
cv.waitKey(1)

cv.destroyAllWindows()
