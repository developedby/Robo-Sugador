import RPi.GPIO as GPIO

class ServoMotor:
    def __init__ (self, input_pin):
        self.input_pin = input_pin
        self.position = None
        GPIO.setup(self.input_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.input_pin, 50)#20ms de periodo
        self.pwm.start(7.5)#passar uma posicao inicial?

    def goToPosition (position):
        self.position = position;
        pulse = ((self.position/180 + 1)/20)*100
        self.pwm.ChangeDutyCycle(pulse)
