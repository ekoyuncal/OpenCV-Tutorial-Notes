
# Object Detection with Opencv Template Matching

import numpy as np
import cv2

image_path = r"C:\Users\emircan\Desktop\openCV\opencv401/"

src = cv2.imread("OpenCV_Logo.png")
template = cv2.imread("template.png")

def template_demo(src, template):
    th, tw = template.shape[:2]
    
    result = cv2.matchTemplate(src, template, method = cv2.TM_CCORR_NORMED)
    #cv2.imshow("result", result)
    #cv2.waitKey(1)
    
    t = 0.98
    loc = np.where(result > t)
    
    for pt in zip(*loc[::-1]):
        cv2.rectangle(src, pt, (pt[0] + tw, pt[1] + th), (255, 0, 0), 1, 8, 0)
        
    cv2.imshow("demo1", src)
    cv2.waitKey(1)
    
template_demo(src, template)