from robot import Robot

class Intelligence:
    state  = set(('sleeping', 'jaguar', 'manual', 'patroling', 'going_after_ball', 'going_after_racket' 'turning_off'))
    def __init__ (self, Robot):
        self.actual_state = None
        commandProcess(Robot)

    def commandProcess(Robot):
        msg = Robot.communicator.decodeMessage
        if msg:
            actual_state = msg
            executeActualState(Robot)

    def sleeping(Robot):
        pass

    def goAfterBall(Robot):
        pass

    def goAfterRacket(Robot):
        pass

    def patroling(Robot):
        pass

    def jaguar(Robot):
        pass

    def goingToHome(Robot):
        pass

    def executeActualState(Robot):
        pass
