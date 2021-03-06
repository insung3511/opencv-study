import imutils
import cv2

image = cv2.imread("./pictures/people.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

(B, G, R) = image[100, 100]
print("R={}, G={}, B={}".format(R,G,B))

rotated = imutils.rotate_bound(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)

cv2.imshow("opencv", image)
cv2.waitKey(0)