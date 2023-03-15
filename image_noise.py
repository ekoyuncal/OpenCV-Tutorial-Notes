import numpy as np
import cv2

def add_salt_pepper_noise(image):
    h, w = image.shape[:2]
    nums = 10000
    rows = np.random.randint(0, h, nums, dtype=np.int)
    cols = np.random.randint(0, w, nums, dtype=np.int)
    
    for i in range(nums):
        if i % 2 == 1:
            image[rows[i], cols[i]] = (255, 255, 255)
        
        else:
            image[rows[i], cols[i]] = (0, 0, 0)
            
    return image

image_path = r"C:\Users\emircan\Desktop\openCV\opencv401/"

lena = cv2.imread("lena.jpg")

copylena = np.copy(lena)

lena_noise = add_salt_pepper_noise(copylena)

h, w = lena.shape[:2]

result = np.zeros([h, w *2, 3], dtype = lena.dtype)
result[0:h, 0:w, :] = lena
result[0:h, w:2*w, :] = copylena

cv2.imshow("Lenas", result)
cv2.waitKey(1)

cv2.imwrite("Lenas_pure_and_wnoise.jpg", result)







