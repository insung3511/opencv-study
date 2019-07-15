import imutils
import cv2

image = cv2.imread("./pictures/people.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

(B, G, R) = image[100, 100]
print("R={}, G={}, B={}".format(R,G,B))

#center = (w // 2, h // 2)
#M = cv2.getRotationMatrix2D(center, -30, 0.5)
#rotated = cv2.warpAffine(image, M, (w, h))
#cv2.imshow("OpenCV Rotation", rotated)
#cv2.waitKey(0)

# 👆위에 내용을 함수 활용하기
rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)

cv2.imshow("opencv", image)
cv2.waitKey(0)