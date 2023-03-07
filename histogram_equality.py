import numpy as np
import cv2
import matplotlib.pyplot as plt

#To create contrast

def custom_hist(gray):
    h, w = gray.shape
    hist = np.zeros([256], dtype = np.int32)
    
    for row in range(h):
        for col in range(w):
            pv = gray[row, col]
            hist[pv] += 1
            
    
    y_pos = np.arange(0, 256, 1, dtype = np.int32)
    plt.bar(y_pos, hist, align = "center", color = "r", alpha = 0.5)
    plt.xticks(y_pos, y_pos)
    plt.ylabel("Freq")
    plt.title("Histogram")
    plt.show()
    
image_path = r"C:\Users\emircan\Desktop\openCV/"
source = cv2.imread("wall-e.jpg")
    
gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
cv2.imshow("Input Wall-E", gray)
cv2.waitKey(1)

custom_hist(gray)

dst = cv2.equalizeHist(gray)
cv2.imshow("Equalized Hist", dst)
cv2.waitKey(1)

custom_hist(dst)