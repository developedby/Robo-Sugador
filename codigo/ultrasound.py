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
        self.edge = True
        GPIO.setup(trigger_pin, GPIO.OUT)
        GPIO.setup(echo_pin, GPIO.IN)
        GPIO.add_event_detect(echo_pin, GPIO.BOTH, callback=self.countEchoTime)
        self.start()

    def sendTrigger (self):
        GPIO.output(self.trigger_pin, GPIO.HIGH)
        GPIO.output(self.trigger_pin, GPIO.LOW)
        self.timer = Timer(0.1, self.sendTrigger)
        self.timer.start()

    def countEchoTime (self, channel):
        #print(self.distance)
        if self.edge == True:
            self.echo_time = time.time()
            self.edge = False
        else:
            self.echo_time = time.time() - self.echo_time
            #self.distance = self.echo_time * 170 # Velocidade do som (340) / 2 (tem que ir e voltar)
            self.distance = 100
            #print(self.distance)#nunca chega aqui
            self.edge = True

    def stop(self):
        self.timer.cancel()
        self.distance = None

    def start(self):
        self.timer = Timer(0.1, self.sendTrigger)
        self.timer.start()

'''
import gpiozero

class Ultrasound (gpiozero.DistanceSensor):
    def __init__ (self, echo_pin, trigger_pin):
        super().__init__(echo=echo_pin, trigger=trigger_pin, max_distance=1)
      

import RPi.GPIO as GPIO
import time
from threading import Timer

class Ultrasound ():

    def __init__ (self, echo_pin, trigger_pin):
        self.distance = None
        self.echo_pin = echo_pin
        self.trigger_pin = trigger_pin
        GPIO.setup(trigger_pin, GPIO.OUT)
        GPIO.setup(echo_pin, GPIO.IN)
        #self.timer = Timer(0.1, self.sendTrigger)
        #self.timer.start()

    def sendTrigger (self):
        # set Trigger to HIGH
        GPIO.output(self.trigger_pin, True)
     
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, False)
     
        StartTime = time.time()
        StopTime = time.time()
     
        # save StartTime
        while GPIO.input(self.echo_pin) == 0:
            StartTime = time.time()
     
        # save time of arrival
        while GPIO.input(self.echo_pin) == 1:
            StopTime = time.time()
     
        self.distance = (StopTime - StartTime) * 171.5
        #self.timer = Timer(0.1, self.sendTrigger)
        #self.timer.start()

''' 