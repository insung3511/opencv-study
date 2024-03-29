'''import numpy as np
import cv2

org_img = cv2.imread('../images/ORGwall_and_paper.jpg')
fea_img = cv2.imread('../images/PAGwall_and_paper.jpg')
org_gray = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)
fea_gray = cv2.cvtColor(fea_img, cv2.COLOR_BGR2GRAY)

detector = cv2.xfeatures2d.SURF_create()
kp1, desc1 = detector.detectAndCompute(org_gray, None)
kp2, desc2 = detector.detectAndCompute(fea_gray, None)

FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

matcher = cv2.FlannBasedMatcher(index_params, search_params)
matches = matcher.match(desc1, desc2)
res = cv2.drawMatches(org_img, kp1, fea_img, kp2, matches, None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

print("Predict: ",matches[0].distance)
cv2.imshow('FLANN + SURF', res)
cv2.waitKey()
cv2.destroyAllWindows()'''