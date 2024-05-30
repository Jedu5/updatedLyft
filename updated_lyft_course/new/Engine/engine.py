from capulet import capuletEngine
from willoughby import willoughbyEngine
from sternman import sternmanEngine

class Engine():
    def needs_service(self):
        if sternmanEngine.needs_service == True or capuletEngine.needs_service == True or willoughbyEngine.needs_service == True:
            return True
        else:
            return False