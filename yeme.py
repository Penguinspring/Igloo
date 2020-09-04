def destination(s): #목적지 함수
   if s == '부산':
       a=50000
    elif s == '대구':
        a=30000
    else : print("목적지를 제대로 입력하십시오.")
    return a
def train(c): #열차의 종류 함수
    if c == 'ktx':
        b= 25000
    elif c == '무궁화':
        b= 15000
    else : print("열차를 제대로 입력하십시오.")
    return b
def seat(k): #입석,좌석 함수
    if k == '입석':
        z= 1000
    elif k == '좌석':
        z= 3000
    else : print("입석과 좌석 중 하나를 제대로 입력하십시오.")
    return z
def resting_room(r):
    if r == '1' :
        m = 30000
    elif r == '2' :
        m = 0
    else : print("식사를 하실거면 1, 그렇지 않으면 2를 눌러주세요.")
    return m
def price(a,b,z,m): #총 금액을 구하는 함수
    pay=a+b+z+m
    return pay
print("본 프로그램은 기차표 예매 프로그램입니다.")
print("목적지는 부산(50,000원)과 대구(30,000원)\n열차는 ktx(25,000원)와 무궁화(15,000원)\n그리고 입석(1,000원)과 좌석(3,000원)이 있습니다.")
print("식사의 경우 식사를 하실거면 1, 그렇지 않으면 2를 눌러주세요.")
s=input("가고 싶은 목적지를 입력하세요 :")
c=input("열차의 종류를 선택해 주십시오 :")
k=input("입석과 좌석 중 하나를을 고르시오:")
r=input("식사의 여부를 말씀 해 주세요:")
a=destination(s)
b=train(c)
z=seat(k)
m=resting_room(r)
print("총 금액은",price(a,b,z,m),"원입니다.")
