import numpy as np
import cv2


def canny_demo(image):
    t = 80
    canny_output = cv2.Canny(image, t, t*2)
    return canny_output

image_path = r"C:\Users\emircan\Desktop\openCV/"
sudoku = cv2.imread("sudoku.jpg")

binary = canny_demo(sudoku)
cv2.imshow("binary", binary)
cv2.waitKey(1)

linesP = cv2.HoughLinesP(binary, 1, np.pi / 180, 55, None, 50, 10)

if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv2.line(sudoku, (l[0], l[1]), (l[2], l[3]), (255, 0, 0), 1, cv2.LINE_AA)
        
cv2.imshow("ProbHoughman", sudoku)
cv2.waitKey(1)