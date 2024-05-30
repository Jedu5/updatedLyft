from nubbin import Nubbin
from spindler import Spindler

class Battery():
    def needs_service(self):
        if Nubbin.needs_service == True or Spindler.needs_service == True:
            return True
        else:
            return False