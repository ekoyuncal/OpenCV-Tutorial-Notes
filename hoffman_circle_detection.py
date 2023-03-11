import numpy as np
import cv2


image_path = r"C:\Users\emircan\Desktop\openCV/"
coins = cv2.imread("coins.jpg")

gray = cv2.cvtColor(coins, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (9,9), 2, 2)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1,
                            minDist = 10, param1 = 100, param2=100,
                            minRadius = 10, maxRadius = 180)
#param0, verilen gaussianBlured gray signal
#param1 = hoffmn method
#param2 = output size
#param3(minDist) = min distance from detected circle
#param4-5 = to adjust focus to color changing
#param6-7 = to adjust radius


for c in circles[0, :]:
    print(c)
    cx, cy, r = c
    cv2.circle(coins, (int(cx), int(cy)), 2, (0, 255, 0), 2, 8, 0)
    cv2.circle(coins, (int(cx), int(cy)), int(r), (0, 0, 255), 2, 8, 0)
    
cv2.imshow("Hough line demo", coins)
cv2.waitKey(1)    
    
cv2.imwrite("detected_coins.jpg", coins)