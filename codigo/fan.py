from dc_motor import DCMotor

class Fan():
    def __init__ (self, input1_pin, input2_pin):
        self.motor = DCMotor(input1_pin, input2_pin)

    def stop(self):
        self.motor.rotate(0)

    def spin(self):
        self.motor.rotate(1)
