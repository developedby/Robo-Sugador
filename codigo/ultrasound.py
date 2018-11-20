# ultrasound.py - Ultrassom que diz distancia até obstaculos
# Informações sobre a licensa no arquivo LICENSE

import RPi.GPIO as GPIO
import time
from threading import Timer

class Ultrasound ():

    def __init__ (self, echo_pin, trigger_pin):
        self.distance = None
        self.echo_pin = echo_pin
        self.trigger_pin = trigger_pin
        #GPIO.setmode(GPIO.BCM)
        GPIO.setup(trigger_pin, GPIO.OUT)
        GPIO.setup(echo_pin, GPIO.IN)
        GPIO.add_event_detect(echo_pin, GPIO.BOTH, callback=self.countEchoTime)
        self.timer = Timer(0.1, self.sendTrigger)
        self.timer.start()
        self.edge = 'rising'

    def sendTrigger (self):
        GPIO.output(self.trigger_pin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, GPIO.LOW)
        self.timer = Timer(0.1, self.sendTrigger)
        self.timer.start()

    def countEchoTime (self, channel):
        #print(self.distance)
        if self.edge == 'rising':
            self.echo_time = time.time()
            self.edge = 'falling'
        else:
            self.echo_time = time.time() - self.echo_time
            self.distance = self.echo_time * 170 # Velocidade do som (340) / 2 (tem que ir e voltar)
            print(self.distance)#nunca chega aqui
            self.edge = 'rising'

    def stop(self):
        self.timer.cancel()
        self.distance = None

    def start(self):
        self.timer.start()
