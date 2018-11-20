# encoder.py - Encoder optico que conecta em um motor
# Informações sobre a licensa no arquivo LICENSE

import RPi.GPIO as GPIO
import time

class Encoder :
    #log = []

    def __init__ (self, read_pin, num_holes):
        self.read_pin = read_pin
        self.num_holes = num_holes
        self.angular_velocity = None #velocidade em graus/seg
        self.degree_per_hole = float(360/self.num_holes)
        self.last_time_checked = time.time()
        GPIO.setup(read_pin, GPIO.IN)
        GPIO.add_event_detect(read_pin, GPIO.FALLING, callback=self.updateSpeed)

    def updateSpeed (self, channel):
        current_time = time.time()
        measured_velocity = self.degree_per_hole/float(current_time - self.last_time_checked)
        if measured_velocity < 1000:
            self.angular_velocity = measured_velocity
#        print(self.angular_velocity)
        self.last_time_checked = current_time
        #self.log.append(self.angular_velocity)