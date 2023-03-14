import numpy as np
import cv2

image_path = r"C:\Users\emircan\Desktop\openCV\opencv401/"

board = cv2.imread("chessboard.jpg")

def harris(image):
    blockSize = 2#köşe tespiti için düşünülen komşuluk boyutu
    apertureSize = 3 #diyafram parametresi
    k = 0.04 #serbestlik parametresi
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dst = cv2.cornerHarris(gray, blockSize, apertureSize, k)
    dst_norm = np.empty(dst.shape, dtype = np.float32)
    cv2.normalize(dst, dst_norm, alpha=0, beta=255, norm_type = cv2.NORM_MINMAX)
    
    for i in range(dst_norm.shape[0]):
        for j in range(dst_norm.shape[1]):
            if int(dst_norm[i, j]) > 120:
                cv2.circle(image, (j, i), 2, (0, 0, 255), 2)
                
    return image


up_width = 600
up_height = 500
up_points = (up_width, up_height)

board = cv2.resize(board, up_points, interpolation= cv2.INTER_LINEAR)

copyboard = np.copy(board)

copyboard = harris(copyboard)

h, w = board.shape[:2]

result = np.zeros([h, w *2, 3], dtype = board.dtype)
result[0:h, 0:w, :] = board
result[0:h, w:2*w, :] = copyboard

cv2.imshow("Result", result)
cv2.waitKey(1)

cv2.imwrite("board_wcorners.jpg", result)



