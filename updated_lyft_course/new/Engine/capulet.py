class capuletEngine():
    def __init__(self, lastServiceMileage, currentMileage):
        self.currentMileage, self.lastServiceMileage = 0, 0 
        self.lastServiceMileage = lastServiceMileage
        self.currentMileage = currentMileage
    
    def needs_service(self):
        if self.currentMileage - self.lastServiceMileage > 30000:
            return True
        else:
            return False
    