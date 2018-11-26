# sucker.py - O sugador de bolinhas. Tem um ventilador e uma portinhola (tampa)

from fan import Fan
from cover import Cover
from infrared import Infrared

class Sucker:
    def __init__ (self, infrared_pin, fan_input1_pin, fan_input2_pin, cover_pin, cover_initial_angle, cover_min_angle, cover_max_angle, closed_angle , open_angle):
        self.cover = Cover(cover_pin, cover_initial_angle, cover_min_angle, cover_max_angle, closed_angle, open_angle)
        self.fan = Fan(fan_input1_pin, fan_input2_pin)
        self.infrared = Infrared(infrared_pin)
        self.state = "off"

    def suck(self):
        self.cover.close()
        self.fan.spin()

    def drop(self):
        self.cover.open()
        self.fan.stop()

    def close(self):
        self.cover.close()
        self.fan.stop()

    def deactivate(self):
        self.cover.open()
        self.fan.stop()
        self.cover.motor.detach()
        