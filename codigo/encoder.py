# encoder.py - Encoder optico que conecta em um motor
# Informações sobre a licensa no arquivo LICENSE

import RPi.GPIO as GPIO
from threading import Timer

class Encoder :
    #log = []

    def __init__ (self, read_pin, num_holes, speed_update_frequency):
        self.read_pin = read_pin
        self.num_holes = num_holes
        self.angular_velocity = 0 #velocidade em voltas/seg
        self.counter = 0
        self.speed_update_frequency = speed_update_frequency
        GPIO.setup(read_pin, GPIO.IN)
        GPIO.add_event_detect(read_pin, GPIO.FALLING, callback=self.contRoles)
        self.timer = Timer(self.speed_update_frequency, self.updateSpeed)
        self.timer.start()
    
    def contRoles(self, channel):
        self.counter = self.counter+1;

    def updateSpeed (self):
        self.angular_velocity = self.counter/float(self.num_holes*self.speed_update_frequency)
        self.counter = 0;
        self.timer = Timer(self.speed_update_frequency, self.updateSpeed)
        self.timer.start()