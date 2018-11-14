# robot.py - Representa o robo como um todo. So criar e ele ja funciona

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

from vision import Vision
from mover import Mover
from sucker import Sucker
from communicator import Communicator # tem que mudar o nome pq da conflito -Nicolas
from intelligence import Intelligence



class Robot :
    def __init__ (self):
        GPIO.setmode(GPIO.BOARD)
        self.vision = Vision()
        self.mover = Mover()
        self.sucker = Sucker()
        self.communicator = Communicator()
        self.intelligence = Intelligence(self)
