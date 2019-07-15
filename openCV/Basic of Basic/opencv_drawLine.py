import imutils
import cv2

image = cv2.imread("./pictures/people.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

(B, G, R) = image[100, 100]
print("R={}, G={}, B={}".format(R,G,B))

output = image.copy()
cv2.line(output, (60, 20),         (900, 1200), (0, 0, 255), 5)
#           start(X,   Y),      END(  X,    Y), (B, G,   R), STORKE)
cv2.imshow("Line", output)
cv2.waitKey(0)

cv2.imshow("opencv", image)
cv2.waitKey(0)