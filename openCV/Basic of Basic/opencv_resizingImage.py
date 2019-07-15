import imutils
import cv2

image = cv2.imread("./pictures/people.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

(B, G, R) = image[100, 100]
print("R={}, G={}, B={}".format(R,G,B))

#resized = cv2.resize(image, (200, 200))
#cv2.imshow("Fixed Resized", resized)

#r = 500.0 / w
#dim = (500, int(h * r))
#resized = cv2.resize(image, dim)
#cv2.imshow("Resized Picture", resized)
#cv2.waitKey(0)

# 👆위에 내용을 함수 활용하기
resized = imutils.resize(image, width=300)
cv2.imshow("Resize", resized)
cv2.waitKey(0)

cv2.imshow("opencv", image)
cv2.waitKey(0)