#import numpy as np
import cv2 as cv

img = cv.imread('asdf.PNG')
face = cv.CascadeClassifier('haarcascade_fullbody.xml')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = face.detectMultiScale(gray, 1.1, 4)

f = open('counter.txt', 'w')

for (x, y, w, h) in faces:
	cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)
	print('I found : ',faces, ' faces.')
	f.write('true')

cv.imshow('img', img)
cv.waitKey(0)