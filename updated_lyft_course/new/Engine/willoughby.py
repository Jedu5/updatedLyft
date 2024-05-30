class willoughbyEngine():
    def __init__(self, lastServiceMileage, currentMileage):
        self.lastServiceMileage = lastServiceMileage
        self.currentMileage = currentMileage

    def needs_service(self):
        if self.currentMileage - self.lastServiceMileage > 60000:
            return True
        else:
            return False