from dc_motor import DCMotor

class Fan():
    def __init__ (inp1_pin, inp2_pin):
        self.motor = DCMotor(inp1_pin, inp2_pin)

    def stop():
        self.motor.rotate(0)

    def spin():
        self.motor.rotate(1)
