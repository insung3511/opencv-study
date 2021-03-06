import imutils
import cv2

image = cv2.imread("./pictures/people.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

(B, G, R) = image[100, 100]
print("R={}, G={}, B={}".format(R,G,B))

#image[startY:endY, startX:endX]
roi = image[500:600, 500:600]
cv2.imshow("ROI", roi)

cv2.imshow("opencv", image)
cv2.waitKey(0)