from datetime import datetime
from datetime import date

class carFactory():

    class createCalliope():
        def __init__(self, lastServiceDate, currentMileage, lastServiceMileage):
            self.currentDate = date.today()
            self.lastServiceDate = datetime.strptime(lastServiceDate, '%d/%m/%Y')
            self.lastServiceDate = self.lastServiceDate.date()
            self.currentMileage = currentMileage
            self.lastServiceMileage = lastServiceMileage

    class createGlissade():
        def __init__(self, lastServiceDate, currentMileage, lastServiceMileage):
            self.currentDate = date.today()
            self.lastServiceDate = datetime.strptime(lastServiceDate, '%d/%m/%Y')
            self.lastServiceDate = self.lastServiceDate.date()
            self.currentMileage = currentMileage
            self.lastServiceMileage = lastServiceMileage
    class createPalindrome():
        def __init__(self, lastServiceDate, warningLightOn):
            self.currentDate = date.today()
            self.lastServiceDate = datetime.strptime(lastServiceDate, '%d/%m/%Y')
            self.lastServiceDate = self.lastServiceDate.date()
            self.warningLightOn = False
            self.warningLightOn = warningLightOn
    class createRorschach():
        def __init__(self, lastServiceDate, currentMileage, lastServiceMileage):
            self.currentDate = date.today()
            self.lastServiceDate = datetime.strptime(lastServiceDate, '%d/%m/%Y')
            self.lastServiceDate = self.lastServiceDate.date()
            self.currentMileage = currentMileage
            self.lastServiceMileage = lastServiceMileage
    class createThovex():
        def __init__(self, lastServiceDate, currentMileage, lastServiceMileage):
            self.currentDate = date.today()
            self.lastServiceDate = datetime.strptime(lastServiceDate, '%d/%m/%Y')
            self.lastServiceDate = self.lastServiceDate.date()
            self.currentMileage = currentMileage
            self.lastServiceMileage = lastServiceMileage