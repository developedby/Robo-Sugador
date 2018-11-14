# cover.py - Tampa que abre e fecha o caminho da bolinha para o recipiente de armazenamento
#          - Tem que estar fechada para ter poder de sucção suficiente
#          - Tem que medir os angulos para criar sem estragar nada

from servo_motor import ServoMotor

class Cover():
    def __init__ (self, input_pin, min_angle, max_angle,  closed_angle ,  open_angle):
        self.motor = ServoMotor(input_pin, min_angle, max_angle)

    #TODO: Medir o angulo certo
    def open(self):
        self.motor.goToPosition(self.motor.max_angle)

    def close(self):
        self.motor.goToPosition(self.motor.min_angle)
