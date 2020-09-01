
x = int(input("첫번째 숫자 : "))
y = int(input("두번째 숫자 : "))

def sum_calculator(x,y):
    return(x+y)

def subtraction_calculator(x,y):
    return(x-y)

def multiplication_calculator(x,y):
    return(x*y)

def division_calculator(x,y):
    return(x//y,x%y)


print("합","=",x+y)
print("차","=",x-y)
print("곱","=",x*y)
print("몫과 나머지","=",x//y,"and",x%y)
