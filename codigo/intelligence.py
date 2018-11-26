from os import system
import math
import threading
from time import sleep

class Intelligence:
    
    manual_mode_speed = 2
    min_obstacle_distance = 0.5 # Nao chega mais perto de obstaculos que essa distancia (tem que setar pra distancia max que a camera de perto enxerga)
    turn_speed = 2
    forward_speed = 2
    def __init__ (self, robot):
        self.robot = robot
        self.current_state = 'sleep'
        self.current_substate = 'idle'
        self.current_manual_command = None
        self.chased_distant_ball = None
        self.mode_function_dict = {'sleep': self.sleepMode, 'jaguar':self.jaguarMode, 'manual':self.manualMode, 'patrol':self.patrolMode, 'home':self.homeMode, 'shutdown':self.shutdownMode}

    def mainLoop(self):
        while True:
            #print(threading.current_thread())
            if self.thereIsNewCommand():
                self.processNewCommand()
            self.executeCurrentState()

    def thereIsNewCommand(self):
        if self.robot.communicator.last_command == None:
            return False
        else:
            return True

    def processNewCommand(self):
        if self.robot.communicator.last_command:
            split_msg =  self.robot.communicator.last_command.split(':')
            if split_msg[0] == 'mode':
                self.current_state = split_msg[1]
                self.current_manual_command = None
            elif split_msg[0] == 'manual' and self.current_state == 'manual':
                self.current_manual_command = split_msg[1]
        self.robot.communicator.last_command = None
        self.current_substate = 'idle'
        self.chased_distant_ball = None
        #print('modo:', self.current_state, 'manual:', self.current_manual_command)

    def sleepMode(self):
        if self.current_substate == 'idle':
            self.robot.sucker.deactivate()
            self.robot.mover.stop()
            self.robot.vision.close()
            self.current_substate = 'sleeping'
        elif self.current_substate == 'sleeping':
            sleep(1)

    def homeMode(self):
        racket = self.robot.vision.findRacket(self.robot.vision.long_distance_cam.image())
        if self.current_substate == 'idle':
            if racket is not None:
                if self.robot.vision.obstacleDistance():
                    if self.robot.vision.obstacleDistance() < self.min_obstacle_distance:
                        self.robot.mover.stop()
                        self.robot.sucker.close()
                    else:
                        self.current_substate = 'chasing'
            else:
                if self.robot.vision.obstacleDistance():
                    if self.robot.vision.obstacleDistance() < self.min_obstacle_distance:
                        self.current_substate = 'obstacle'
        elif self.current_substate == 'chasing':
            if racket is not None:
                self.chaseRacket(racket)
            else:
                self.current_substate = 'idle'
        elif self.current_substate == 'obstacle':
            if self.robot.vision.obstacleDistance():
                if self.robot.vision.obstacleDistance() < self.min_obstacle_distance:
                    self.current_substate = 'obstacle'
                    self.avoidObstacle()
                else:
                    self.current_substate = 'idle'

    def chaseRacket(self, racket):
        if racket[0] < 0.4*self.robot.vision.long_distance_cam.resolution['width']:
            self.robot.mover.turn(self.turn_speed)
        elif racket[0] > 0.6*self.robot.vision.long_distance_cam.resolution['width']:
            self.robot.mover.turn(-self.turn_speed)
        else:
            self.robot.mover.moveForward(self.forward_speed)

    def dropBall(self):
            self.robot.sucker.drop()
            self.robot.mover.stop()
            sleep(2)
            self.robot.sucker.close()

    def patrolMode(self):
        if self.robot.sucker.infrared.obstacle:
            self.dropBall()
    
        if self.current_substate == 'idle':
            if self.robot.vision.obstacleDistance():
                if self.robot.vision.obstacleDistance() < self.min_obstacle_distance:
                    self.current_substate = 'obstacle'
            self.robot.mover.moveForward(self.forward_speed)
            self.robot.sucker.close()
            balls = self.robot.vision.findDistantBalls()
            if balls is not None:
                self.current_substate = 'chasing'
        elif self.current_substate == 'chasing':
            self.chaseBall()
        elif self.current_substate == 'obstacle':
            self.avoidObstacle()

    def jaguarMode(self):
        if self.robot.sucker.infrared.obstacle:
            self.dropBall()
    
        if self.current_substate == 'idle':
            self.robot.mover.stop()
            self.robot.sucker.close()
            if self.robot.vision.obstacleDistance():
                if self.robot.vision.obstacleDistance() < self.min_obstacle_distance:
                    self.current_substate = 'obstacle'
            balls = self.robot.vision.findDistantBalls()
            if balls is not None:
                self.current_substate = 'chasing'
        elif self.current_substate == 'chasing':
            self.chaseBall()
        elif self.current_substate == 'obstacle':
            self.avoidObstacle()

    def chaseBall(self):
        close_balls = self.robot.vision.findCloseBalls()
        if close_balls is not None:
            self.suckCloseBall(close_balls)
        elif self.robot.vision.obstacleDistance() < self.min_obstacle_distance:
            self.current_substate = 'obstacle'
        else:
            distant_balls = self.robot.vision.findDistantBalls()
            if distant_balls is not None:
                self.chaseDistantBall(distant_balls)
            else:
                self.current_substate = 'idle'

    def avoidObstacle(self):
        while self.robot.vision.obstacleDistance() < self.min_obstacle_distance:
            self.robot.mover.turn(self.turn_speed)

    def distance(coord1, coord2):
        return math.hypot(coord2[0]-coord1[0], coord2[1]-coord1[1])

    def suckCloseBall(self, close_balls):
        self.robot.sucker.suck()
        if close_balls[0][0][0] < (0.25+(0.15*close_balls[0][0][1]/self.robot.vision.short_distance_cam.resolution['height']))*self.robot.vision.short_distance_cam.resolution['width']:
            self.robot.mover.turn(self.turn_speed)
        elif close_balls[0][0][0] > (0.75-(0.15*close_balls[0][0][1]/self.robot.vision.short_distance_cam.resolution['height']))*self.robot.vision.short_distance_cam.resolution['width']:
            self.robot.mover.turn(-self.turn_speed)
        else:
            self.robot.mover.moveForward(self.forward_speed)

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
        if chased_distant_ball:
            if chased_distant_ball[0] < 0.4*self.robot.vision.long_distance_cam.resolution['width']:
                self.robot.mover.turn(self.turn_speed)
            elif chased_distant_ball[0] > 0.6*self.robot.vision.long_distance_cam.resolution['width']:
                self.robot.mover.turn(-self.turn_speed)
            else:
                self.robot.mover.moveForward(self.forward_speed)

    def shutdownMode(self):
        self.robot.sucker.close()
        self.robot.mover.stop()
        system('systemctl poweroff')

    def executeCurrentState(self):
        self.mode_function_dict[self.current_state]()

    def manualMode(self):
        if self.current_manual_command != None:
            #print(self.current_manual_command)
            pass
        if self.current_manual_command == 'forward':
            self.robot.mover.moveForward(self.manual_mode_speed)
        elif self.current_manual_command == 'backward':
            self.robot.mover.moveForward(-self.manual_mode_speed)
        elif self.current_manual_command == 'stop':
            self.robot.mover.stop()
        elif self.current_manual_command == 'left':
            self.robot.mover.turn(self.manual_mode_speed)
        elif self.current_manual_command == 'right':
            self.robot.mover.turn(-self.manual_mode_speed)
        elif self.current_manual_command == 'fan': 
            if self.robot.sucker.fan.is_on:
                self.robot.sucker.fan.stop()
            else:
                self.robot.sucker.fan.spin()
        elif self.current_manual_command == 'cover':
            if self.robot.sucker.cover.is_open:
                self.robot.sucker.cover.close()
            else:
                self.robot.sucker.cover.open()
        self.current_manual_command = None

from robot import Robot