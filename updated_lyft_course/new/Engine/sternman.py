class sternmanEngine():
    def __init__(self, warningLightOn):
        self.warningLightOn = warningLightOn
    
    def needs_service(self):
        if self.warningLightOn == True:
            return True
        else:
            return False