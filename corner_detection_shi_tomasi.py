import numpy as np
import cv2

#Better than harris for more complex images

image_path = r"C:\Users\emircan\Desktop\openCV\opencv401/"

source = cv2.imread("3d_shapes.jpg")

def shi_tomasi(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, maxCorners=30, qualityLevel = 0.05, minDistance=30)
    
    for pt in corners:
        print(pt)
        b = np.random.randint(0, 256)
        g = np.random.randint(0, 256)
        r = np.random.randint(0, 256)
        x = np.int32(pt[0][0])
        y = np.int32(pt[0][1])
        cv2.circle(image, (x, y), 5, (int(b), int(g), int(r)), 2)
        
    return image

#up_width = 600
#up_height = 500
#up_points = (up_width, up_height)

#source = cv2.resize(source, up_points, interpolation= cv2.INTER_LINEAR)

copysource = np.copy(source)

copysource= shi_tomasi(copysource)

h, w = source.shape[:2]

result = np.zeros([h, w *2, 3], dtype = source.dtype)
result[0:h, 0:w, :] = source
result[0:h, w:2*w, :] = copysource

cv2.imshow("Result", result)
cv2.waitKey(1)

cv2.imwrite("3d_shapes_wcorners.jpg", result)

