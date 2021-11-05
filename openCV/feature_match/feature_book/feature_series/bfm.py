import numpy as np
import cv2

img1 = cv2.imread('./images/ORGwall_and_paper.jpg')
img2 = cv2.imread('./images/PAGwall_and_paper.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

detector = cv2.xfeatures2d.SIFT