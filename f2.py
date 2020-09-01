print("본 프로그램은 이메일 비밀번호 안전성 평가 프로그램입니다.")

password = input("비밀번호를 입력하세요:")

if len(password) >= 9:
    print("Your password : Good")

elif len(password) >= 5 and len(password) < 9 :
    print("Your password : Normal")

elif len(password) < 5 :
    print("Your password: Bad")

else:
    print("비밀번호를 제대로 입력해 주십시오.")
