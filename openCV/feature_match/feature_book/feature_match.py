import numpy as np
import cv2

lowe_ration = 0.98

org_img = cv2.imread('test_images/ORGwall_and_paper.jpg')
fea_img = cv2.imread('test_images/PAGwall_and_paper.jpg')
org_gray = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)
fea_gray = cv2.cvtColor(fea_img, cv2.COLOR_BGR2GRAY)

detector = cv2.xfeatures2d.SIFT_create()
kp1, desc1 = detector.detectAndCompute(org_gray, None)
kp2, desc2 = detector.detectAndCompute(fea_gray, None)

# matcher == bf
#matcher = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
matcher = cv2.BFMatcher()
matches = matcher.match(desc1, desc2, k=2)

# find some good ratio test
good = []

for m, n in matches:
    if m.distance < lowe_ration * n.distance:
        good.append([m])

msg1 = 'lowe_ration %.2f' % (lowe_ration)
msg2 = 'there are %d good matches' % (len(good))

# res is mean result
res = cv2.drawMatches(org_img, kp1, fea_img, kp2, matches, None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(res, msg1, (10, 250), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(res, msg2, (10, 270), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

#print("Predictor : ", )
cv2.imshow('BFMatcher + SIFT', res)
cv2.waitKey()
cv2.destroyAllWindows()