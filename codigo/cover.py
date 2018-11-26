# cover.py - Tampa que abre e fecha o caminho da bolinha para o recipiente de armazenamento
#          - Tem que estar fechada para ter poder de sucção suficiente
#          - Tem que medir os angulos para criar sem estragar nada

from servo_motor import ServoMotor

class Cover():
    def __init__ (self, input_pin, initial_angle, min_angle, max_angle, closed_angle, open_angle):
        self.motor = ServoMotor(input_pin, initial_angle, min_angle, max_angle)
        self.closed_angle = closed_angle
        self.open_angle = open_angle
        self.is_open = None

    def open(self):
        if not self.is_open:
            self.motor.angle = self.open_angle
            self.is_open = True
            #print('open cover')

    def close(self):
        if self.is_open:
            self.motor.angle = self.closed_angle
            self.is_open = False
            #print('close cover')
