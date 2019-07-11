import imutils
import cv2

image = cv2.imread("./pictures/people.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

(B, G, R) = image[100, 100]
print("R={}, G={}, B={}".format(R,G,B))

blurred = cv2.GaussianBlur(image, (3, 3), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

cv2.imshow("opencv", image)
cv2.waitKey(0)