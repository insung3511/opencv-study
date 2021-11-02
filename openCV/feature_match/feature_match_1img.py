import numpy as np
import cv2

org_img = cv2.imread('images/ORGmy_room.jpg')
fea_img = cv2.imread('images/PAGmy_room_box.jpg')
org_gray = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)
fea_gray = cv2.cvtColor(fea_img, cv2.COLOR_BGR2GRAY)

detector = cv2.xfeatures2d.SIFT_create()
kp1, desc1 = detector.detectAndCompute(org_gray, None)
kp2, desc2 = detector.detectAndCompute(fea_gray, None)

matcher = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
matches = matcher.match(desc1, desc2)
res = cv2.drawMatches(org_img, kp1, fea_img, kp2, matches, None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

cv2.imshow('BFMatcher + SIFT', res)
cv2.waitKey()
cv2.destroyAllWindows()