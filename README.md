# openCV - Study 
openCV를 깊이 다뤄 본적이 없는거 같아서 openCV를 다시 공부 하는 겸, 이렇게 만들어보았다. 디렉토리 설명은 아래에.

# Directory
<pre>
.
├── README.md
└── openCV
    ├── Basic\ of\ Basic
    │   ├── opencv_blur.py
    │   ├── opencv_circleDraw.py
    │   ├── opencv_cropimage.py
    │   ├── opencv_drawLine.py
    │   ├── opencv_openImage.py
    │   ├── opencv_putText.py
    │   ├── opencv_rectangle.py
    │   ├── opencv_resizingImage.py
    │   ├── opencv_rotate.py
    │   └── opencv_rotatedSize.py
    ├── Basic\ of\ Middle
    │   ├── opencv_changeBlack.py
    │   ├── opencv_edgeDetection.py
    │   ├── opencv_objContuer.py
    │   └── opencv_threasholding.py
    ├── Human_Detection
    │   ├── Ho
    │   │   └── people.jpg
    │   ├── cascadeHuman.py
    │   ├── counter.txt
    │   ├── face
    │   │   └── README.md
    │   ├── face.py
    │   ├── haarcascade_eye.xml
    │   ├── haarcascade_frontalface_default.xml
    │   ├── haarcascade_fullbody.xml
    │   ├── hogcascade_pedestrians.xml
    │   ├── human_detection
    │   │   ├── gtg.png
    │   │   ├── me.jpg
    │   │   ├── standing_person.jpg
    │   │   ├── street.jpg
    │   │   ├── threePerson.jpg
    │   │   └── walking_person.jpg
    │   ├── human_pic.py
    │   ├── human_video.py
    │   ├── main.py
    │   ├── main_test.py
    │   ├── result.jpg
    │   ├── subway.mp4
    │   └── time.txt
    ├── feature_match
    │   ├── feature_book
    │   │   ├── exam_feature_match.py
    │   │   ├── feature_match.py
    │   │   ├── feature_series
    │   │   │   ├── bfm.py
    │   │   │   └── images
    │   │   │       ├── ORGgraffiti.jpg
    │   │   │       ├── ORGmy_room.jpg
    │   │   │       ├── ORGwall_and_paper.jpg
    │   │   │       ├── PAGcarhartt_patch.jpg
    │   │   │       ├── PAGmy_room_big.jpg
    │   │   │       ├── PAGmy_room_box.jpg
    │   │   │       ├── PAGwall_and_paper.jpg
    │   │   │       ├── box.png
    │   │   │       └── box_in_scene.png
    │   │   ├── images
    │   │   └── test_images
    │   │       ├── ORGgraffiti.jpg
    │   │       ├── ORGmy_room.jpg
    │   │       ├── ORGwall_and_paper.jpg
    │   │       ├── PAGcarhartt_patch.jpg
    │   │       ├── PAGmy_room_big.jpg
    │   │       ├── PAGmy_room_box.jpg
    │   │       ├── PAGwall_and_paper.jpg
    │   │       ├── box.png
    │   │       └── box_in_scene.png
    │   ├── feature_series
    │   │   ├── README.md
    │   │   ├── __pycache__
    │   │   │   └── get_image.cpython-39.pyc
    │   │   ├── bfm_and_sift.py
    │   │   ├── flann_and_orb.py
    │   │   ├── flann_and_sift.py
    │   │   ├── flann_and_surf.py
    │   │   └── get_image.py
    │   └── images
    │       ├── ORGgraffiti.jpg
    │       ├── ORGmy_room.jpg
    │       ├── ORGwall_and_paper.jpg
    │       ├── PAGcarhartt_patch.jpg
    │       ├── PAGmy_room_big.jpg
    │       ├── PAGmy_room_box.jpg
    │       └── PAGwall_and_paper.jpg
    └── pictures
        ├── boradcast.jpg
        ├── clothes.jpg
        └── rgb.png

17 directories, 75 files
</pre>
Last Updated: Nov.7.2021

# Basic of Basic
<pre>
├── opencv_blur.py
├── opencv_circleDraw.py
├── opencv_cropimage.py
├── opencv_drawLine.py
├── opencv_openImage.py
├── opencv_putText.py
├── opencv_rectangle.py
├── opencv_resizingImage.py
├── opencv_rotate.py
└── opencv_rotatedSize.py
</pre>
가장 기초적인 openCV 사진 처리 기술과 문법을 공부한 파일들이다. 대부분의 자료들과 공부한 내용들은 pyimagesearch 코드를 활용 하였다. pyimagesearch의 특징은 파라먼트를 활용하여 다른 사진을 분석할때에는 코드를 수정하지 않고 명령문에서 선택을 할수 있게 한다.

각 코드마다의 설명은 파일의 이름만 봐도 무엇을 말하는지 알거 라고 생각이 되기 때문에 따로 긴 말은 그리 하지 않겠다.

# Basic of Middle
<pre>
├── opencv_changeBlack.py
├── opencv_edgeDetection.py
├── opencv_objContuer.py
└── opencv_threasholding.py
</pre>
가장 기초적인 문법을 다 했다면 edge만 마스킹 하기 등 좀 더 멋진 짓들을 할수가 있다. 이 또한 pyimagesearch에서 갖고 온 자료들이다. ~~opencv 모르는거나 필요한거는 pyimagesearch로 가자.. 없는게 없다.~~ 

객체 인식 등에서 가장 많이 쓰이는 함수들로 사실상 기본적으로 알아 둬야 하는 함수들이 대다수이다.

# Human_Detection
<pre>
├── Ho
│   └── threePerson.jpg
├── counter.txt
├── face
│   └── README.md
├── face.py
├── haarcascade_eye.xml
├── haarcascade_frontalface_default.xml
├── haarcascade_fullbody.xml
├── human_detection
│   ├── gtg.png
│   ├── me.jpg
│   ├── standing_person.jpg
│   ├── street.jpg
│   └── walking_person.jpg
├── human_pic.py
├── human_video.py
├── main.py
├── main_test.py
├── result.jpg
├── subway.mp4
└── time.txt
</pre>
해커톤을 준비하면서 공부한 자료들이다.. 음 조만간 새로 저장소 만들어서 거기에 넣을 거긴 한데 일단 귀찮아서 같이 뒀다.

face.py 는 얼굴인식, human_pic.py 는 사진에서 사람 찾기, human_video.py 는 영상에서 사람 찾기, main.py와 main_test.py는 해커톤에서 쓸 코드.

human_detection 디렉토리 안에 있는 사진들은 사람 인식을 하기 위해서 모은 귀-중한 자료들이다. ~~아무튼 그렇다.~~ subway.mp4는 사람 코드 갖고 오다가 같이 딸려온거 같은데 이것은 정-말로 진짜 귀-중한 자료이다. 

Ps. 참고로 사실 해커톤에서는 Hog를 활용하여 Human Detection을 진행하진 못했다. 그 이유는 굉장히 낮은 인식율로 인해서 그러는데 그거에 대한 자세한 내용은 <a href="https://github.com/insung3511/human-detection">여기에</a> 작성해두었다.

# feature_match
최근에 3D Reconsturction에 관심이 생겨서 이것저것 해보고 있는데 feature match을 먼저 해야하는거 같아서 시작하게 되었다.
```.
├── feature_book
│   ├── exam_feature_match.py
│   ├── feature_match.py
│   ├── feature_series
│   │   ├── bfm.py
│   │   └── images
│   │       ├── ORGgraffiti.jpg
│   │       ├── ORGmy_room.jpg
│   │       ├── ORGwall_and_paper.jpg
│   │       ├── PAGcarhartt_patch.jpg
│   │       ├── PAGmy_room_big.jpg
│   │       ├── PAGmy_room_box.jpg
│   │       ├── PAGwall_and_paper.jpg
│   │       ├── box.png
│   │       └── box_in_scene.png
│   ├── images
│   └── test_images
│       ├── ORGgraffiti.jpg
│       ├── ORGmy_room.jpg
│       ├── ORGwall_and_paper.jpg
│       ├── PAGcarhartt_patch.jpg
│       ├── PAGmy_room_big.jpg
│       ├── PAGmy_room_box.jpg
│       ├── PAGwall_and_paper.jpg
│       ├── box.png
│       └── box_in_scene.png
├── feature_series
│   ├── README.md
│   ├── __pycache__
│   │   └── get_image.cpython-39.pyc
│   ├── bfm_and_sift.py
│   ├── flann_and_orb.py
│   ├── flann_and_sift.py
│   ├── flann_and_surf.py
│   └── get_image.py
└── images
    ├── ORGgraffiti.jpg
    ├── ORGmy_room.jpg
    ├── ORGwall_and_paper.jpg
    ├── PAGcarhartt_patch.jpg
    ├── PAGmy_room_big.jpg
    ├── PAGmy_room_box.jpg
    └── PAGwall_and_paper.jpg

8 directories, 35 files
```
BFM을 시작으로 SURF, ORB, SIFT 등 여러 Feature Matching에 대해서 공부를 하고 있다. 이에 대한 내용 또한 [나의 블로그](http://insung3511.github.io) 에 적어가면서 지속적으로 정리할 예정이다. **많관부~**

# 이게 왜 안되는데 이것아. 
참 나만 그런건지 모르겠다. openCV 정말 좋은 라이브러리 이다. 정말로. 무거운 만큼, 설치하는데 힘든 만큼 쓸일은 많다. 그런데 개발 환경에 따른 차이가 존재 하는 것 같다. 허ㅓ어ㅓㅓㅇ..ㅇㄹ
~~안된다면 에러문을 모두 복사하지 말고 에러에 마지막 줄만 복사해서 구글 검색을 해보자. 이 말이 이해가 안된다면 좀 알아서 찾아봐라. ~~
문제가 있는 경우에는 Issue에 내용을 적으면 그 내용을 토대로 도와주겠다. 어떤 도움이든 괜찮으니 언제든지 어떤 Issue던지 환영이다 :)

## P.S.
개인적으로는 이 저장소의 코드를 참고하면서 <a href="https://github.com/insung3511/human-detection"> human-detection </a> 저장소도 한번 들러 보는 것을 추천한다. 사람 인식에만 열정을 쏟아부어 공부한 흔적들이 고이 담겨 있다. 한번 꼭 봐주시길.. ~~Plz~~