from dc_motor import DCMotor

class Fan(DCMotor):
    def __init__ (self, input1_pin, input2_pin):
        DCMotor.__init__(input1_pin, input2_pin)

    def stop(self):
        self.rotate(0)

    def spin(self):
        self.rotate(1)
