class Cover():
    def __init__ (inp_pin):
        self.motor = ServoMotor(inp_pin)

    def open():
        self.motor.goToPosition(180)#ideal que seja no estremo que dai a trava do motor ajuda

    def close():
        self.motor.goToPosition(120)#sei la que angulo, tem que testar
