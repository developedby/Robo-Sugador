from dc_motor import DCMotor

class Fan(DCMotor):
    def __init__ (self, input1_pin, input2_pin):
        super().__init__(input1_pin, input2_pin)
        self.stop()

    def stop(self):
        self.rotate(0)
        self.is_on = False

    def spin(self):
        self.rotate(1)
        self.is_on = True