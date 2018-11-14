# wheel.py - Uma roda do robo. Anda pra frente ou pra rtas com velocidade relativa à maxima

import RPi.GPIO as GPIO
from dc_motor import DCMotor
from encoder import Encoder

class Wheel (DCMotor):
    def __init__ (self, input1_pin, input2_pin, pwm_pin, encoder_pin, num_holes):
        self.pwm_pin = pwm_pin
        super(self, Wheel).__init__(input1_pin, input2_pin)
        self.encoder = Encoder(encoder_pin, num_holes)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pwm_pin, 60)#60hz ta bom?
        self.pwm.start(0)#inicia parado

    # speed entre -1 e 1
    def spin(self, speed):
        self.rotate(speed) # Da a direção
        self.pwm.ChangeDutyCycle(abs(speed)) # Da a velocidade (modulo)
