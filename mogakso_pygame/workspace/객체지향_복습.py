class rabbit:
    def __init__(self):
        self.name = input('이름 입력:')
        self.num = int(input('번호 입력:'))
        # num,name 두가지 필드를 입력받게 합니다. (num은 정수)

    def check(self):
        print('{}번 이름: {} ,출석체크!')
        #출석체크를 의미함
    

    def score(self,score):
        if score <= 40 :
            self.grade = 'c'
            print('학점은 c 입니다.')
        
        elif score > 40 and score < 80 :
            self.grade = 'b'
            print('학점은 b 입니다.')
        
        else :
            self.grade = 'a'
            print('학점은 a 입니다.')
        
        print("{}점 이고 학점은 {} 입니다.".format(self.score , self.grade))
        # 입력변수, 인수를 입력받아서 grade를 설정
        # 40점 이하면 c, 40점 초과 80점 미만 b , 80점 이상일 때 a -> grade



a = rabbit()
b = rabbit()
c = rabbit()

print("{}번 이름: {}".format(a.num, a.name))
print("{}번 이름: {}".format(b.num, b.name))
a.check()
b.check()
a.score(55)
b.score(88)