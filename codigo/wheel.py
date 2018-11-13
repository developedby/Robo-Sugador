import RPi.GPIO as GPIO
import DCMotor
import Encoder

class Wheel (DCMotor):
    def __init__ (inp1_pin, inp2_pin, pwm_pin, encoder_pin, holes_number):
        self.pwm_pin = pwm_pin
        super().__init__(inp1_pin, inp2_pin)
        self.encoder = Encoder(encoder_pin, holes_number)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pwm_pin, 60)#60hz ta bom?
        self.pwm.start(0)#inicia parado

    def walk(speed):
         if(speed => 0):
            rotate(1)
        else:
            rotate(-1)
        pulse = (speed/250)*100#tem que ver a resolucao do motor, 250 é um valor aleatorio
        self.pwm.ChangeDutyCycle(pulse)
        #tem que fazer a funcao que le a velocidade real e manda para  o movimentador
