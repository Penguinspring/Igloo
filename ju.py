print("본 프로그램은 스택을 이용한 주차장 관리 프로그램입니다.")

p=["주","차","장","공","간"]
#p는 parking lot의 줄임말, 자동차 5개가 보관 가능한 주차장 설정
print(p)

p.pop()
p.pop()
p.pop()
#리스트의 3자리를 빼야되는데 교체하는 법을 몰라서
#pop로 뺀 후에 push하기로 결정
#실제로는 리스트의 5자리 모두 빈 공간임

p.append("자동차A")
print (p)
p.append("자동차B")
print (p)
p.append("자동차C")
print (p)

#주차장의 빈 자리에 자동차 A,B,C가 차례로 들어감

p.pop()
print (p)
p.pop()
print (p)
p.pop()
#스택을 이용해 자동차C부터 차례로 나감

p=["주","차","장","공","간"]
print (p)
#다시 처음 주차장 5자리의 빈공간으로 됨
