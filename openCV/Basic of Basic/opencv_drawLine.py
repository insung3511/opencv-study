import imutils
from cv2 import cv2

image = cv.imread("./pictures/people.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

(B, G, R) = image[100, 100]
print("R={}, G={}, B={}".format(R,G,B))

output = image.copy()
cv.line(output, (60, 20),         (900, 1200), (0, 0, 255), 5)
#           start(X,   Y),      END(  X,    Y), (B, G,   R), STORKE)
cv.imshow("Line", output)
cv.waitKey(0)

cv.imshow("opencv", image)
cv.waitKey(0)