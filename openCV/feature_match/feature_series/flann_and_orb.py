from get_image import get_image
import numpy as np
import cv2

org_img, fea_img, org_gray, fea_gray = get_image()

detector = cv2.ORB_create()
kp1, desc1 = detector.detectAndCompute(org_gray, None)
kp2, desc2 = detector.detectAndCompute(fea_gray, None)

FLANN_INDEX_LSH = 6
index_params = dict(algorithm = FLANN_INDEX_LSH,
                    table_number = 6,
                    key_size = 12,
                    multi_probe_level = 1)
search_params = dict(checks=32)

matcher = cv2.FlannBasedMatcher(index_params, search_params)
matches = matcher.match(desc1, desc2)
res = cv2.drawMatches(org_img, kp1, fea_img, kp2, matches, None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

print("Predict: ",matches[0].distance)
cv2.imshow('FLANN + ORB', res)
cv2.waitKey()
cv2.destroyAllWindows()