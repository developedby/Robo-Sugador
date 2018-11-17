# encoder.py - Encoder optico que conecta em um motor
# Informações sobre a licensa no arquivo LICENSE

import RPi.GPIO as GPIO
import time

class Encoder :
    def __init__ (self, read_pin, num_holes):
        self.read_pin = read_pin
        self.num_holes = num_holes
        self.angular_velocity = None #velocidade em graus/seg
        self.degree_per_hole = 360/self.num_holes
        self.last_time_checked = time.time()
        GPIO.setup(read_pin, GPIO.IN)
        GPIO.add_event_detect(read_pin, GPIO.RISING, callback=self.atualizaVelocidade)

    def atualizaVelocidade (self):
        current_time = time.time()
        self.angular_velocity = self.degree_per_hole/(current_time - self.last_time_checked)
        self.last_time_checked = current_time
