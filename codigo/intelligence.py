from robot import Robot
import os

class Intelligence:
    mode_function_dict = {'sleep': sleepMode, 'jaguar':jaguarMode, 'manual':manualMode, 'patrol':patrolMode, 'home':homeMode, 'shutdown':shutdownMode}

    def __init__ (self, robot):
        self.robot = robot
        self.current_state = None
        self.current_manual_command = None
        processCommand(Robot)

    def processCommand(self):
        msg = robot.communicator.last_command
        if msg is None:
            return

        split_msg =  msg.split(msg, ':')
        if split_msg[0] == 'mode':
            self.current_state = split_msg[1]
            self.current_manual_command = None
        elif split_msg[0] == 'manual':
            if current_state != 'manual':
                return
            self.current_manual_command = spilt_msg[1]

        self.robot.communicator.last_command = None
        executeCurrentState()


    def sleepMode(self):
        self.robot.sucker.close()
        self.robot.mover.stop()
        self.vision.close()

    def homeMode(self):
        pass

    def patrolMode(self):
        pass

    def jaguarMode(self):
        pass

    def shutdownMode(self):
        self.robot.sucker.close()
        self.robot.mover.stop()
        os.system('systemctl poweroff')

    def executeCurrentState(self):
        mode_function_dict[current_state]()
