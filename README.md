# every_software
아주대학교 모각소_python 자료구조 및 알고리즘 및 pygame

## 1주차 
날짜: 1/12 ( 시간: 15:30 ~ 18:30 ) 
장소: 팔달관 317호
팀명 : 데이터란 무엇인가

##### 공부 내용: 자료구조와 함께 배우는 알고리즘 입문 계획 작성 및 pygame (유튜브 링크 :https://www.youtube.com/watch?v=Dkx8Pl6QKW0&t=4042s)를 참고하여 코드 작성 더불어 코드를 리뷰하여 pygame 모듈이 어떻게 돌아가는 지 큰 틀을 이해하였다. 

github 주소 : https://github.com/aosdbfc/every_software/blob/main/mogakso_pygame/workspace/mogakso_oneweek


## 2주차 
날짜: 1/28 ( 시간: 13:00 ~ 16:30 ) 
장소: 팔달관 317호
팀명 : 데이터란 무엇인가

##### 공부 내용: 자료구조와 함께 배우는 알고리즘 입문 1-3장 공부 리뷰 및 pygame (장애물 피하기 만들기)를 참고하여 코드 작성 더불어 코드를 리뷰하며 객체지향 개념에 대해서 이해하도록 하였다. 객체지향 개념 정리는 velog에 정리하였다. 


## 3주차 
날짜: 2/2 ( 시간: 13:40 ~ 17:20 ) 
장소: 팔달관 317호
팀명 : 데이터란 무엇인가

##### 공부 내용: 자료구조와 함께 배우는 알고리즘 입문 4-5장 공부 리뷰 및 pygame (슈팅 게임)를 참고하여 코드 작성 더불어 코드를 리뷰하며 객체지향 개념에 전 주차보다 더 자세히 알아보았다.
OOP는 이러한 객체 개념을 프로그램으로 표현
속성은 변수(variable), 행동은 함수(method)로 표현됨

- 축구 선수 정보를 Class로 구현하기
class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number
    def change_back_number(self, new_number):
    print("선수의 등번호를 변경합니다 : From %d to %d" %(self.back_number, new_number))
    self.back_number = new_number
   
   #### 객체 지향 언어의 특징 중 필요한 것들
   상속, 다형성, 가시성
   
   #### decorate
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
self.gotmarks = self.name + ' obtained ' + self.marks + ' marks'

@property
def gotmarks(self):
return self.name + ' obtained ' + self.marks + ' marks

#### decorate function
def generate_power(exponent):
    def wrapper(f):
        def inner(*args):
            result = f(*args)
            return exponent**result
        return inner
    return wrapper
    
@generate_power(2)
def raise_two(n):
    return n**2



## 4주차 
날짜: 2/9 ( 시간: 15:00 ~ 18:20 ) 
장소: 팔달관 317호
팀명 : 데이터란 무엇인가

##### 공부 내용:  건강검진 정보 데이터로 음주여부 분류하기 분류 모델 프로젝트를 진행하였다. 판다스, 넘파이, 사이킷런 라이브러리에서 진행하였다. 더불어 시각화를 위한 seaborn, matplotlib 라이브러리를 사용하였다. 데이터 불러오기 -> EDA -> 데이터 전처리 (결측치 채우기) -> 정규분표 형태로 변환 -> 학습, 예측 데이터셋 나누기 -> 머신러닝 알고리즘(여기선 랜덤포레스트 분류기 사용) 사용 -> 학습 후 예측 -> 정확도 측정 순으로 데이터 사이언스의 전반적인 과정을 공부하였다. 아직 머신러닝이 익숙하지 않고 여러 모듈에서 사용하는 것이 많아 공부해야 할 것이 많지만 하나씩 기본부터 진행하고 있다. 
