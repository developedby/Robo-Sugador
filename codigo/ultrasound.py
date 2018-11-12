# ultrasound.py - Ultrassom que diz distancia até obstaculos
# Informações sobre a licensa no arquivo LICENSE

import RPi.GPIO as GPIO
import time 

class Ultrasound ():
	distance = None

    def __init__ (self, echo_pin, trigger_pin, max_distance):
        self.echo_pin = echo_pin
        self.trigger_pin = trigger_pin

        GPIO.setup(trigger_pin, GPIO.OUT)
        GPIO.setup(echo_pin, GPIO.IN)
        GPIO.add_event_detect(echo_pin, GPIO.RISING, callback=self.startCountingEchoTime)
        GPIO.add_event_detect(echo_pin, GPIO.FALLING, callback=self.stopCountingEchoTime)
    def startCountingEchoTime (self):
        self.echo_time = time.time()
    def stopCountingEchoTime (self):
        self.echo_time = time.time() - self.echo_time
        self.distance = self.echo_time * 170 			# Velocidade do som (340) / 2 (tem que ir e voltar)