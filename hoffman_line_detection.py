import numpy as np
import cv2


def canny_demo(image):
    t = 80
    canny_output = cv2.Canny(image, t, t*2)
    cv2.imwrite("Canny_output.png", canny_output)
    return canny_output

image_path = r"C:\Users\emircan\Desktop\openCV/"
sudoku = cv2.imread("sudoku.jpg")

cv2.imshow("Input", sudoku)
cv2.waitKey(1)

binary = canny_demo(sudoku)

cv2.imshow("Binary", binary)
cv2.waitKey(1)

lines = cv2.HoughLines(binary, 1, np.pi / 180, 150, None, 0, 0)
if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
        pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
        cv2.line(sudoku, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)
        
cv2.imshow("Detected", sudoku)
cv2.waitKey(1)  
        
cv2.imwrite("Line_Detected_Sudoku.png", sudoku)