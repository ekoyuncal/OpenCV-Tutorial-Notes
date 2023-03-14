import numpy as np
import cv2



image_path = r"C:\Users\emircan\Desktop\openCV\opencv401/"

source = cv2.imread("test_corners.jpg")

def sub_pixel(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, maxCorners=100, qualityLevel = 0.05, minDistance=10)
    
    for pt in corners:
        print(pt)
        b = np.random.randint(0, 256)
        g = np.random.randint(0, 256)
        r = np.random.randint(0, 256)
        x = np.int32(pt[0][0])
        y = np.int32(pt[0][1])
        cv2.circle(image, (x, y), 5, (int(b), int(g), int(r)), 2)
        
    winSize = (3, 3)
    zeroZone = (-1, -1)
    
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TermCriteria_COUNT, 40, 0.001)
    corners = cv2.cornerSubPix(gray, corners, winSize, zeroZone, criteria)
    
    for i in range(corners.shape[0]):
        print(" -- Refined Corner [", i, "] (", corners[i, 0, 0], ",", corners[i, 0, 1], ")")
    
    return image


copysource = np.copy(source)

copysource= sub_pixel(copysource)

h, w = source.shape[:2]

result = np.zeros([h, w *2, 3], dtype = source.dtype)
result[0:h, 0:w, :] = source
result[0:h, w:2*w, :] = copysource

cv2.imshow("Result", result)
cv2.waitKey(1)

cv2.imwrite("improved wsub_pixel_corners.jpg", result)


