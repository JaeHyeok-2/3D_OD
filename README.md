# Simulation 
![](Result.gif)


# `CV Function 정리`
## BackgroundSubtractorMOG2 클래스 생성 함수 

###  ```cv2.BackgroundSubstractMOG2(history=None, varThreshold=None, detectShadows=None) ->dst ```
- history : 히스토리의 길이. 기본값은 500으로, 과거 몇 개의 프레임을 배경으로 이용한 것인지에 대한 Argument

- varTheshold : 픽셀과 모델 사이의 마할라노비스 거리(Mahalanobis distance) 제곱에 대한 임계값. 해당 픽셀이 
배경모델에 의해 잘 표현되는지를 판단. Default Value =16

- detectShadows : 그림자 여부 검출. 기본값은 True 



## 전면 객체 마스크 생성 함수 - cv2.BackgroundSubtractor
### ```cv2.BackgroundSubtractor.apply(image, fgmask=None, learningRate=None) -> fgmask```

* image : (입력) 다음 Video Frame
* fgmask : (출력) 전경 마스크 영상. 8-bit Binary Video
* learningRate : 배경 모델 학습 속도 지정(0~1 사이의 실수) Default = -1 
    - 0 : 배경 모델을 갱신하지 않음
    - 1 : 매 프레임마다 배경모델을 새로 만듦
    - -1 : 자동으로 결정



### ```math.hypot(x, y)```
* x, y 간의 Euclidean Distance를 계산하는 파이썬 math module Function 
* tracker.py 내에서 같은 Object인지를 구분하기 위한 거리함수로 쓰임

