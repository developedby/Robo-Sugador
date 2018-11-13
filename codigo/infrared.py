import RPi.GPIO as GPIO

class Infrared():
    def __init__ (read_pin):
        self.read_pin = read_pin
        GPIO.setup(self.read_pin, GPIO.IN)
        self.obstacle = GPIO.input(self.read_pin)
        GPIO.add_event_detect(read_pin, GPIO.RISING, callback=self.setObstacle)
        GPIO.add_event_detect(read_pin, GPIO.FALLING, callback=self.clearObstacle)

    def setObstacle (self):
        self.obstacle = True
  
    def clearObstacle (self):
        self.obstacle = False

    def thereIsObstacle (self):
        return self.obstacle
