# servo_motor.py - Servo motor que recebe angulos
'''
# Usando RPi.GPIO

import RPi.GPIO as GPIO

class ServoMotor():
    def __init__ (self, input_pin, initial_angle=90, min_angle=0, max_angle=180):
        self.input_pin = input_pin
        self.angle = None
        self.min_angle = min_angle
        self.max_angle = max_angle
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.input_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.input_pin, 25)#20ms de periodo
        self.pwm.start(7.5)#passar uma posicao inicial?

    def goToAngle (self, angle):
        self.angle = angle
        pulse = ((self.angle/180 + 1)/20)*100
        self.pwm.ChangeDutyCycle(pulse)
'''   
 
# Usando gpiozero

import gpiozero

class ServoMotor (gpiozero.AngularServo):
    def __init__ (self, input_pin, initial_angle=90, min_angle=0, max_angle=180):
        super().__init__(input_pin, initial_angle=initial_angle, min_angle=min_angle, max_angle=max_angle, min_pulse_width=0.5/1000, max_pulse_width=2.25/1000)
        
