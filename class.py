print("본 프로그램은 승용차와 트럭의 상속 프로그램입니다.")

class Car(object):
    def __init__(self,name,color,speed,seat,carrying_capacity):
        self.name=name
        self.color=color
        self.speed=speed
        self.seat=seat
        self.carrying_capacity=carrying_capacity


    def change_speed(self, value):
        print("속도를 변경합니다:From %d to %d" % (self.speed,value))
        self.speed=value

Sedan = Car("승용차","파랑색","120","4자리","300")
print("차의 종류:", Sedan.name)
print("색상:", Sedan.color)
print("좌석수:",Sedan.seat)
print("속도:",Sedan.speed)
print("속도를 변경합니다:From 120 to 150")
print("속도:","150")

Truck = Car("트럭","초록색","110","4자리","900")
print("차의 종류:", Truck.name)
print("색상:", Truck.color)
print("적재량(kg):",Truck.carrying_capacity)
print("속도:",Truck.speed)
print("속도를 변경합니다:From 110 to 130")
print("속도:","130")
