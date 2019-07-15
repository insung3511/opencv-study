import imutils
import cv2

image = cv2.imread("./pictures/people.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

(B, G, R) = image[100, 100]
print("R={}, G={}, B={}".format(R,G,B))

output = image.copy()
cv2.rectangle(output, (961, 63),    (1126, 239), (255,  0,    0), 2)
#                   pt1(pX, pY), pt2(pX,    pY), (B,    G,    R), STORKE)  
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

cv2.imshow("opencv", image)
cv2.waitKey(0)