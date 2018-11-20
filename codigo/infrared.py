import RPi.GPIO as GPIO

class Infrared():
    def __init__ (self, read_pin):
        self.read_pin = read_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.read_pin, GPIO.IN)
        self.obstacle = not(bool(GPIO.input(self.read_pin)))
        GPIO.add_event_detect(read_pin, GPIO.BOTH, callback=self.obstacleEvent)

    def obstacleEvent (self, channel):
        self.obstacle = not self.obstacle
        #print(self.obstacle)


