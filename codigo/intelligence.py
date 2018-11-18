from robot import Robot
import os

class Intelligence:
    mode_function_dict = {'sleep': sleepMode, 'jaguar':jaguarMode, 'manual':manualMode, 'patrol':patrolMode, 'home':homeMode, 'shutdown':shutdownMode}
    manual_mode_speed = 180 #ou seja, 30 voltas por minuto
    manual_mode_duration = 0 # 0 significa que vai ficar executando o comando ate mandar parar ou trocar de comando
    min_obstacle_distance = 0.5 # Nao chega mais perto de obstaculos que essa distancia (tem que setar pra distancia max que a camera de perto enxerga) 
    def __init__ (self, robot):
        self.robot = robot
        self.current_state = 'sleep'
        self.current_substate = 'stopped'
        self.current_manual_command = None
        self.mainLoop()

    def mainLoop(self):
        if thereIsNewCommand():
            self.processNewCommand()
            self.robot.mover.stop()
            self.robot.sucker.close()
        executeCurrentState()

    def thereIsNewCommand(self):
        if self.robot.communicator.last_command == None:
            return False
        else:
            return True

    def processNewCommand(self):
            split_msg =  self.robot.communicator.last_command.split(msg, ':')
            if split_msg[0] == 'mode':
                self.current_state = split_msg[1]
                self.current_manual_command = None
            elif split_msg[0] == 'manual' and self.current_state == 'manual':
                self.current_manual_command = spilt_msg[1]
            self.robot.communicator.last_command = None

    def sleepMode(self):
        self.robot.sucker.close()
        self.robot.mover.stop()
        self.vision.close()

    def homeMode(self):
        pass

    def patrolMode(self):
        pass

    def jaguarMode(self): #TODO - logica menos simplista
        if self.current_substate = 'stopped':
            balls = self.robot.vision.findDistantBalls()
            if len(balls) > 0:
                self.current_substate = 'chasing'

        elif self.current_substate = 'chasing':
            close_balls = self.robot.vision.findCloseBalls()
            if len(close_balls > 0):
                suckCloseBall(close_balls) #TODO
            elif self.robot.vision.obstacleDistance() < self.min_obstacle_distance: 
                self.current_substate = 'obstacle'
            else:
                distant_balls = self.robot.vision.findDistantBalls()
                if len(distant_balls) > 0:
                    chaseDistantBall(distant_balls) #TODO
                else:
                    self.current_substate = 'stopped'

        pass

    def shutdownMode(self):
        self.robot.sucker.close()
        self.robot.mover.stop()
        os.system('systemctl poweroff')

    def executeCurrentState(self):
        mode_function_dict[current_state]()

    def manualMode(self):
        if current_manual_command == 'forward':
            robot.mover.moveForward(manual_mode_duration, manual_mode_speed)
        elif current_manual_command == 'backward':
            robot.mover.moveForward(manual_mode_duration, -manual_mode_speed)
        elif current_manual_command == 'stop':
            robot.mover.stop()
        elif current_manual_command == 'left':
            robot.mover.turn(manual_mode_duration, manual_mode_speed)
        elif current_manual_command == 'right':
            robot.mover.turn(manual_mode_duration, -manual_mode_speed)
        elif current_manual_command == 'fan': #tem que fazer um ultimo comando manual pra saber qd eh para ligar ou desligar ventilador
            robot.sucker.suck()
        elif current_manual_command == 'cover': #idem
            robot.cover.open():
