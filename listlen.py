print("본 프로그램은 단어들의 길이의 합을 표현하는 프로그램입니다.")
print("리스트는 과일,동물,악기가 있습니다. 세가지 중 하나를 골라주세요.")

def list_selection(list):
    if list == '과일' : print(list_fruit),print(len(a[0]),len(a[1]),len(a[2])),print(len(a[0])+len(a[1])+len(a[2]),"자리")
    elif list == '동물' : print(list_animal),print(len(b[0]),len(b[1]),len(b[2])),print(len(b[0])+len(b[1])+len(b[2]),"자리")
    elif list == '악기' : print(list_instrument),print(len(c[0]),len(c[1]),len(c[2])),print(len(c[0])+len(c[1])+len(c[2]),"자리")
    else : print("리스트가 존재하지 않습니다. 옳은 리스트를 골라주세요.")


list_fruit=['apple','banana','tomato']
list_animal=['bear','elephant','monkey']
list_instrument=['guitar','piano','harmonica']
a=list_fruit
b=list_animal
c=list_instrument


list_selection(input("원하시는 리스트를 선택해주세요: "))
