from robot import Robot
import os
import math

class Intelligence:
    mode_function_dict = {'sleep': sleepMode, 'jaguar':jaguarMode, 'manual':manualMode, 'patrol':patrolMode, 'home':homeMode, 'shutdown':shutdownMode}
    manual_mode_speed = 180 #ou seja, 30 voltas por minuto
    manual_mode_duration = 0 # 0 significa que vai ficar executando o comando ate mandar parar ou trocar de comando
    min_obstacle_distance = 0.5 # Nao chega mais perto de obstaculos que essa distancia (tem que setar pra distancia max que a camera de perto enxerga)
    chased_distant_ball = None
    move_duration = 0.8
    turn_speed = 90
    forward_speed = 135
    def __init__ (self, robot):
        self.robot = robot
        self.current_state = 'sleep'
        self.current_substate = 'stopped'
        self.current_manual_command = None
        self.mainLoop()

    def mainLoop(self):
        while 1:
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
                suckCloseBall(close_balls)
            elif self.robot.vision.obstacleDistance() < self.min_obstacle_distance:
                self.current_substate = 'obstacle'
            else:
                distant_balls = self.robot.vision.findDistantBalls()
                if len(distant_balls) > 0:
                    chaseDistantBall(distant_balls)
                else:
                    self.current_substate = 'stopped'
        elif self.current_substate = 'obstacle':
            self.avoidObstacle() #TODO
        pass

    def distance(coord1, coord2):
        return math.hypot(coord2[0]-coord1[0], coord2[1]-coord1[1])

    def suckCloseBall(self, close_balls):
        self.robot.sucker.suck()
        if close_balls[0][0] < (0.25+(0.15*close_balls[0][1]/self.robot.vision.short_distance_cam.resolution['height']))*self.robot.vision.short_distance_cam.resolution['width']:
            self.robot.mover.turn(self.move_duration, self.turn_speed)
        elif close_balls[0][0] > (0.75-(0.15*close_balls[0][1]/self.robot.vision.short_distance_cam.resolution['height']))*self.robot.vision.short_distance_cam.resolution['width']:
            self.robot.mover.turn(self.move_duration, -self.turn_speed)
        else:
            self.robot.mover.moveForward(self.move_duration, self.forward_speed)

    def chaseDistantBall(self, distant_balls):
        if not chased_distant_ball:
            max_radius = -1
            for c in distant_balls:
                if c[2] > max_radius:
                    max_radius = c[2]
                    chased_distant_ball = c
        else:
            min_dist = math.inf
            for c in distant_balls:
                if distance(c, chased_distant_ball) < min_dist:
                    min_dist = distance(c, chased_distant_ball)
                    circle = c
                chased_distant_ball = circle

        if chased_distant_ball[0] < 0.4*self.robot.vision.long_distance_cam.resolution['width']:
            self.robot.mover.turn(self.move_duration, self.turn_speed)
        elif chased_distant_ball[0] > 0.6*self.robot.vision.long_distance_cam.resolution['width']:
            self.robot.mover.turn(self.move_duration, -self.turn_speed)
        else:
            self.robot.mover.moveForward(self.move_duration, self.forward_speed)

    def shutdownMode(self):
        self.robot.sucker.close()
        self.robot.mover.stop()
        os.system('systemctl poweroff')

    def executeCurrentState(self):
        mode_function_dict[current_state]()

    def manualMode(self):
        if current_manual_command == 'forward':
            self.robot.mover.moveForward(manual_mode_duration, manual_mode_speed)
        elif current_manual_command == 'backward':
            self.robot.mover.moveForward(manual_mode_duration, -manual_mode_speed)
        elif current_manual_command == 'stop':
            self.robot.mover.stop()
        elif current_manual_command == 'left':
            self.robot.mover.turn(manual_mode_duration, manual_mode_speed)
        elif current_manual_command == 'right':
            self.robot.mover.turn(manual_mode_duration, -manual_mode_speed)
        elif current_manual_command == 'fan': #tem que fazer um ultimo comando manual pra saber qd eh para ligar ou desligar ventilador
            self.robot.sucker.suck()
        elif current_manual_command == 'cover': #idem
            self.robot.cover.open():
