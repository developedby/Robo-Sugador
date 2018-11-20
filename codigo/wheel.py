# wheel.py - Uma roda do robo. Anda pra frente ou pra tras com velocidade relativa à maxima

import RPi.GPIO as GPIO
from dc_motor import DCMotor
from encoder import Encoder

class Wheel (DCMotor):
    def __init__ (self, input1_pin, input2_pin, pwm_pin, encoder_pin, num_holes):
        super().__init__(input1_pin, input2_pin)
        self.pwm_pin = pwm_pin
        self.encoder = Encoder(encoder_pin, num_holes)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pwm_pin, 60)#60hz ta bom?
        self.pwm.start(0)#inicia parado

    # speed entre -100 e 100
    def spin(self, speed):
        self.rotate(speed) # Da a direção
        self.pwm.ChangeDutyCycle(abs(speed)) # Da a velocidade (modulo)
