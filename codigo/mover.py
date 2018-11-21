# mover.py - o movimentador do robo, cuida de andar pra frente, para tras e para os lados

from wheel import Wheel
import time
from threading import Timer


def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

class Mover():
    #sign = lambda x: x and (1, -1)[x < 0]
    speed_adjust_frequency = 0.05

    def __init__ (self, input1_a_pin, input2_a_pin, pwm_a_pin, encoder_a_pin, num_a_holes, input1_b_pin, input2_b_pin, pwm_b_pin, encoder_b_pin, num_b_holes, speed_adjust_delta):
        self.left_wheel = Wheel(input1_a_pin, input2_a_pin, pwm_a_pin, encoder_a_pin, num_a_holes)
        self.right_wheel = Wheel(input1_b_pin, input2_b_pin, pwm_b_pin, encoder_b_pin, num_b_holes)
        self.left_wheel_sent_speed = None               # velocidade enviada a roda, em % do pwm
        self.right_wheel_sent_speed = None
        self.left_wheel_required_speed = None           # velocidade desejada, em graus por segundo
        self.right_wheel_required_speed = None
        self.speed_adjust_delta = speed_adjust_delta    # quanto a velocidade enviada varia a cada ajuste
        self.speed_adjust_timer = None
        self.moving = False


    def adjustSpeed(self):
        if (self.sign(self.left_wheel_required_speed) * self.left_wheel.encoder.angular_velocity) > self.left_wheel_required_speed:
            self.left_wheel_sent_speed -= self.speed_adjust_delta
        elif (self.sign(self.left_wheel_required_speed) * self.left_wheel.encoder.angular_velocity) < self.left_wheel_required_speed:
            self.left_wheel_sent_speed += self.speed_adjust_delta

        if (self.sign(self.right_wheel_required_speed) * self.right_wheel.encoder.angular_velocity) > self.right_wheel_required_speed:
            self.right_wheel_sent_speed -= self.speed_adjust_delta
        elif (self.sign(self.right_wheel_required_speed) * self.right_wheel.encoder.angular_velocity) < self.right_wheel_required_speed:
            self.right_wheel_sent_speed += self.speed_adjust_delta

        self.left_wheel_sent_speed = clamp(self.left_wheel_sent_speed, -99, 99)
        self.right_wheel_sent_speed = clamp(self.right_wheel_sent_speed, -99, 99)
        self.left_wheel.spin(self.left_wheel_sent_speed)
        self.right_wheel.spin(self.right_wheel_sent_speed)
        
        print("Vel desejada roda direita:", self.right_wheel_required_speed)
        print("Vel lida na roda direita:", self.sign(self.right_wheel_required_speed) * self.right_wheel.encoder.angular_velocity)
        print("Escrevendo roda direita:", self.right_wheel_sent_speed)
        
        print("Vel desejada roda esquerda:", self.left_wheel_required_speed)
        print("Vel lida na roda esquerda:", self.sign(self.left_wheel_required_speed) * self.left_wheel.encoder.angular_velocity)
        print("Escrevendo roda esquerda:", self.left_wheel_sent_speed)
        
        self.setTimer()

    def moveForward(self, speed):
        self.left_wheel_required_speed = speed
        self.right_wheel_required_speed = speed
        self.left_wheel_sent_speed = self.sign(speed)*50
        self.right_wheel_sent_speed = self.sign(speed)*50
        self.left_wheel.spin(self.left_wheel_sent_speed)
        self.right_wheel.spin(self.right_wheel_sent_speed)


        if not self.speed_adjust_timer or not self.speed_adjust_timer.is_alive():
            self.setTimer()

    def turn(self, speed): # usando sentido positivo: antihorario
        self.left_wheel_required_speed = -speed
        self.right_wheel_required_speed = speed
        self.left_wheel_sent_speed = -self.sign(speed)*50
        self.right_wheel_sent_speed = self.sign(speed)*5
                

        if not self.speed_adjust_timer or not self.speed_adjust_timer.is_alive():
            self.setTimer()

    def stop(self):
        self.stopTimer()
        self.left_wheel.spin(0)
        self.right_wheel.spin(0)
        self.left_wheel_sent_speed = 0
        self.right_wheel_sent_speed = 0
        self.left_wheel_required_speed = 0
        self.right_wheel_required_speed = 0

    def stopTimer(self):
        if self.speed_adjust_timer:
            self.speed_adjust_timer.cancel()
            self.speed_adjust_timer = None

    def setTimer(self):
        self.speed_adjust_timer = Timer(self.speed_adjust_frequency, self.adjustSpeed)
        self.speed_adjust_timer.start()
        #print('ativando timer das rodas com tempo', self.speed_adjust_frequency)

            
    def sign(self, x):
        if x == 0:
            return 0
        elif x > 0:
            return 1
        else:
            return -1