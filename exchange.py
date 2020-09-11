print("본 프로그램은 입력한 금액에 대해 최적의 수량을 갖도록 교환하는 프로그램입니다.")
print("금액을 입력하세요.")

money=int(input())


m50000=money//50000
print("5만원",m50000)
money=money%50000

m10000=money//10000
print("1만원",m10000)
money=money%10000

m5000=money//5000
print("5천원",m5000)
money=money%5000

m1000=money//1000
print("1천원",m1000)
money=money%1000

m500=money//500
print("5백원",m500)
money=money%500

m100=money//100
print("1백원",m100)
money=money%100

m50=money//50
print("5십원",m50)
money=money%50

m10=money//10
print("1십원",m10)
money=money%10
