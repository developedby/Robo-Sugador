# servo_motor.py - Servo motor que recebe angulos

# Usando RPi.GPIO
''' 
import RPi.GPIO as GPIO

class ServoMotor:
    def __init__ (self, input_pin, min_angle=-90, max_angle=90):
        self.input_pin = input_pins
        self.angle = None
        self.min_angle = min_angle
        self.max_angle = max_angle
        GPIO.setup(self.input_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.input_pin, 50)#20ms de periodo
        self.pwm.start(7.5)#passar uma posicao inicial?

    def goToAngle (angle):
        self.angle = angle
        pulse = ((self.angle/180 + 1)/20)*100
        self.pwm.ChangeDutyCycle(pulse)
'''   
     
# Usando gpiozero

import gpiozero

class ServoMotor (self, gpiozero.AngularServo):
    def __init__ (self, input_pin, min_angle=-90, max_angle=90):
        super(self, ServoMotor).__init__(input_pin, min_angle, max_angle)
        self.angle = max_angle  # Fecha o servo no comeco
        
    def goToAngle (self, angle):
        self.angle = angle
