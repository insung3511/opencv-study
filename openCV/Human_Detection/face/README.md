# Face Detection (by openCV)
개소리 없이 바로 코드 설명에 들어간다. 
``` python
import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

img = cv.imread("../../pictures/people.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

cv.imshow('img', img)
cv.waitKey(0)
cv.destoryAllWindows()
```
이게 코드이다. 위에서 부터 이 놈은 뭐하는 놈인지 설명을 하겠다. <br/> <br/> <br/>
Line 1 ~ 5
``` python
import numpy as np
import cv2 as cv


face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
```
라이브러리를 불러온다. 이때 불러오는 라이브러리는 <a href="https://numpy.org/"> NumPy </a> 와 <a href="https://opencv.org/"> OpenCV </a> 라이브러리를 불러온다. <br/> <br/>
이 둘은 최대한 짧게 설명하고 가자면 Numpy는 C언어로 구성된 Python 라이브러리로 고-오 성능의 계산을 위해서 만들어진 라이브러리 이다. openCV는 컴퓨터 비전을 목적으로 한 인텔에서 개발한 실시간 이미지 프로세싱에 이점을 둔 라이브러리 이다. 
<br/> <br/>

<a href="https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml"> haarcascade_frontalface_default.xml </a> 와 <a href="https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml">haarcascade_eye.xml </a>, 이 둘은 사람의 얼굴과 눈을 찾을 때 도와주는(?) 일종의 공부 데이터라고 생각하면 쉬울거 같다..  2001년에 마이클 존스(Michael Jones), 폴 비올라(Paul Viola) 개발자가 “Rapid Object Detection using a Boosted Cascade of Simple Features” 제안한 방식이다. 사실 나도 이건 잘 이해가 안된다... 정 궁금하다면 <a herf="https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html"> 이 문서 </a> 를 읽어보길 바란다. <br/>  <br/>  
Line 7~8
``` python
img = cv.imread("../../pictures/people.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
``` 
가장 먼저 openCV 라이브러리를 통하여 사진을 불러온다. cv.cvtColor는 opencv의 함수 중 하나로 색을 변경하는 함수이다. 쓰는 방법은 cvtColor(사진, 색) 이렇게 쓰면 된다. 색을 쓸때에는 COLOR_BGR2GRAY, COLOR_RGB2GRAY 등등 여러가지가 있으니 자세한 내용은 <a href="https://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html"> 이 문서 </a>를 확인하길 바란다. 

<br/>
Line 10~17

```python
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
```
