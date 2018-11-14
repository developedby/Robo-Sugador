# cover.py - Tampa que abre e fecha o caminho da bolinha para o recipiente de armazenamento
#          - Tem que estar fechada para ter poder de sucção suficiente

from servo_motor import ServoMotor

class Cover():
    def __init__ (self, input_pin, min_angle=-90, max_angle=90):
        self.motor = ServoMotor(input_pin, min_angle, max_angle)

    def open(self):
        self.motor.goToPosition(self.motor.max_angle)

    def close(self):
        self.motor.goToPosition(self.motor.min_angle)
