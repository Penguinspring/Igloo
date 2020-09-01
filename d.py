class Car:
    ##init생략##
    def turn_on(self):
        print("부르릉")

class Bus(Car):
    def __init__(self, sheets):
        super(Bus, self).__init__()
        self.sheets=sheet
    def turn_on(self):
        print("뿌앙")

school_bus=Bus(42)
school_bus.turn_on()
