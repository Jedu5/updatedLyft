from car_factory import carFactory
from Engine.engine import Engine
from Battery.battery import Battery
#car_1 = carFactory.createCalliope("01/01/2006",1000, 500)
#car_2 = carFactory.createPalindrome("01/01/2023", False)

class Car():
    class Engine():
        def __init__(self,engine):
            self.engine = engine
    class Battery():
        def __innit__(self, battery):
            self.battery = battery
    def needs_service():
        if Engine.needs_service == True or Battery.needs_service == True:
            return True
        else:
            return False

    

