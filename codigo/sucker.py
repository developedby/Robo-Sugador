# sucker.py - O sugador de bolinhas. Tem um ventilador e uma portinhola (tampa)

from fan import Fan
from cover import Cover
from infrared import Infrared
from threading import Thread
import os

class Sucker:
    suck_period = 3
    def __init__ (self, infrared_pin, fan_input1_pin, fan_input2_pin, cover_pin, cover_initial_angle, cover_min_angle, cover_max_angle, closed_angle , open_angle):
        self.cover = Cover(cover_pin, cover_initial_angle, cover_min_angle, cover_max_angle, closed_angle, open_angle)
        self.fan = Fan(fan_input1_pin, fan_input2_pin)
        self.infrared = Infrared(infrared_pin)
        self.state = "off"
        self.timer = None

    def suck(self):
        self.cover.close()
        self.fan.spin()
        if not self.timer or not self.time.is_active():
            try:
                self.timer = Timer(self.suck_period, self.stopSucking)
            except:
                os.system('systemctl reboot')

    def stopSucking(self):
        self.fam.spin()

    def drop(self):
        self.cover.open()
        self.fan.stop()
        if self.timer and self.timer.is_active():
            self.timer.cancel()

    def close(self):
        self.cover.close()
        self.fan.stop()
        if self.timer and self.timer.is_active():
            self.timer.cancel()

    def deactivate(self):
        self.cover.open()
        self.fan.stop()
        if self.timer and self.timer.is_active():
            self.timer.cancel()
        self.cover.motor.detach()
        