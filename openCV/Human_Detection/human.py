import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt

path = "./human_detection/walking_person.jpg"

think_1 = cv.imread('./' + path)
grayThink_1 = cv.cvtColor(think_1, cv.COLOR_BGR2HSV)

think_2 = cv.imread('./' + path)
grayThink_2 = cv.cvtColor(think_2, cv.COLOR_BGR2HSV)

think_3 = cv.imread('./' + path)
grayThink_3 = cv.cvtColor(think_3, cv.COLOR_BGR2HSV)

body_cascade = cv.CascadeClassifier('haarcascade_fullbody.xml')

#Think_1
body = body_cascade.detectMultiScale(grayThink_1, 1.01, 10, minSize=(30, 30))
for (x, y, w, h) in body:
    cv.rectangle(think_1, (x, y), (x+w, y+h), (0, 0, 255), 3)

plt.subplot(1, 3, 1)
plt.imshow(think_1, cmap='gray')

#Think_2
body = body_cascade.detectMultiScale(grayThink_2,1.01, 2, 0, minSize=(70, 70))
for (x,y,w,h) in body :        
    cv.rectangle(think_2,(x,y),(x+w,y+h),(0,0,255),3)

plt.subplot(1, 3, 2)
plt.imshow(think_2, cmap='gray')


body = body_cascade.detectMultiScale(grayThink_3,1.01, 2, 0, minSize=(70, 70))
for (x,y,w,h) in body :        
    cv.rectangle(think_2,(x,y),(x+w,y+h),(0,0,255),3)

plt.subplot(1, 3, 3)
plt.imshow(think_2, cmap='gray')

plt.show()