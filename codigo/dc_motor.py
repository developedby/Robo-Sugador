import RPi.GPIO as GPIO

class DCMotor():
    def __init__ (inp1_pin, inp2_pin):
        self.input1_pin = inp1_pin
        self.input2_pin = inp2_pin
        GPIO.setup(self.input1_pin, GPIO.OUT)
        GPIO.setup(self.input2_pin, GPIO.OUT)

    def rotate(direction):
        if(direction ==  1):
            GPIO.output(self.input1_pin, GPIO.LOW)
            GPIO.output(self.input2_pin, GPIO.HIGH)#se tiver trocado, inverte os fios
        else if (direction == -1):
            GPIO.output(self.input1_pin, GPIO.HIGH)
            GPIO.output(self.input2_pin, GPIO.LOW)
        else
            GPIO.output(self.input1_pin, GPIO.LOW)
            GPIO.output(self.input2_pin, GPIO.LOW)
