# robot.py - Representa o robo como um todo. So criar e ele ja funciona

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

from vision import Vision
from mover import Mover
from sucker import Sucker
from communicator import Communicator
from intelligence import Intelligence

class Robot :
    def __init__ (self):
        GPIO.setmode(GPIO.BOARD)
        self.vision = Vision(4, 27, 0, 1)
        self.mover = Mover(23, 24, 18, 6, 20, 25, 8, 13, 5, 20)
        self.sucker = Sucker(22,  10,  9,  12,  0, 180, 150,  180)#chute nos angulos de abertura e fechamento
        self.communicator = Communicator(2)
        self.intelligence = Intelligence(self)
