import RPi.GPIO as GPIO

class DCMotor():
    def __init__ (self, input1_pin, input2_pin):
        self.input1_pin = input1_pin
        self.input2_pin = input2_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.input1_pin, GPIO.OUT)
        GPIO.setup(self.input2_pin, GPIO.OUT)

    def rotate(self, direction):
        if direction > 0:
            GPIO.output(self.input1_pin, GPIO.HIGH)
            GPIO.output(self.input2_pin, GPIO.LOW)#se tiver trocado, inverte os fios
        elif direction < 0:
            GPIO.output(self.input1_pin, GPIO.LOW)
            GPIO.output(self.input2_pin, GPIO.HIGH)
        else:
            GPIO.output(self.input1_pin, GPIO.LOW)
            GPIO.output(self.input2_pin, GPIO.LOW)
