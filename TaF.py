print("1000이하의 정수들 중에서 3과 5의 배수의 합을 구하는 프로그램입니다.")

TaF = 0
#변수 설정(Three and Five)

for n in range(1, 1000):
#1000이하의 정수의 범위를 설정한다.

    if n % 3 == 0 or n % 5 == 0:
#3과 5로 나눴을 때 나머지가 0인 정수들을 저장

        TaF += n
#3과 5의 배수 더하기를 시킴

print("답=", TaF)
#출력
