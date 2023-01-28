# 객체지향 프로그래밍
# 파이썬 헬스장 
# 파이썬 사용해서 운영과 관리
# 회원이 등록 이름, 나이 , 몸무게, 체지방률

# 헬스장의 회원을 등록하는 양식
# 변수들을 쫙 미리 세팅해놓고 값을 받으면

# GYM_INFO -> 클래스 
# name, age, weight -> 변수 설정 가능
# a,b,c,d,e -> 객체, 인스턴스

class Gym_Info :  # 클래스 생성 기본형 class 클래스 이름 
    def __init__(self): # initiate 시작하다
        self.name = input("이름을 입력 해주세요.")
        self.age = int(input("나이를 입력 해주세요."))
        self.weight = int(input("몸무게를 입력해주세요."))
        
    def hello(self):
        print("반갑습니다. {}님 수집된 나이는 {}, 몸무게는 {} 입니다."
        .format(self.name,self.age,self.weight))

class Gym_InfoV2(Gym_Info):  # 상속 받기 
    def __init__(self):
        super().__init__()  # 위에 클래스를 받기 위해 super 사용


print("프로그램 시작")

c = Gym_InfoV2()
d = Gym_InfoV2()
