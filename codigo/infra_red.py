import RPi.GPIO as GPIO

class InfraRed():
    def __init__ (read_pin):
        self.read_pin = read_pin
        self.obstacle = False
        GPIO.setup(self.read_pin, GPIO.IN)
        GPIO.add_event_detect(echo_pin, GPIO.RISING, callback=self.setObstacle)

    def setObstacle():
        self.obstacle = True

    def thereIsObstacle():
        return self.obstacle
