# mover.py - o movimentador do robo, cuida de andar pra frente, para tras e para os lados

from wheel import Wheel
import time

class Mover():
    def __init__ (self, input1_a_pin, input2_a_pin, pwm_a_pin, encoder_a_pin, num_a_holes, input1_b_pin, input2_b_pin, pwm_b_pin, encoder_b_pin, num_b_holes):
        self.left_wheel = Wheel(input1_a_pin, input2_a_pin, pwm_a_pin, encoder_a_pin, num_a_holes)
        self.right_wheel = Wheel(input1_b_pin, input2_b_pin, pwm_b_pin, encoder_b_pin, num_b_holes)
        self.left_wheel_actual_speed = 50#velocidade inicial das rodas, em % do pwm - Alefe
        self.right_wheel_actual_speed = 50
        self.left_wheel_required_speed = None
        self.right_wheel_required_speed = None

    def adjustSpeed(self, speed_adjuster_delta):#o certo era verificar se esta na hora de verificar, ou seja, atualiza a velocidade sempre a cada 1s por ex.
        self.left_wheel.encoder.atualizaVelocidade()
        self.right_wheel.encoder.atualizaVelocidade()

        if self.left_wheel.encoder.angular_velocity > self.left_wheel_required_speed:
            self.left_wheel_actual_speed -= speed_adjuster_delta
            if self.left_wheel_actual_speed <= 0:
                self.left_wheel_actual_speed = 0
        elif self.left_wheel.encoder.angular_velocity < self.left_wheel_required_speed:
            self.left_wheel_actual_speed += speed_adjuster_delta
            if self.left_wheel_actual_speed >= 100:
                self.left_wheel_actual_speed = 100

        if self.right_wheel.encoder.angular_velocity > self.right_wheel_required_speed:
            self.right_wheel_actual_speed -= speed_adjuster_delta
            if self.right_wheel_actual_speed <= 0:
                self.right_wheel_actual_speed = 0
        elif self.right_wheel.encoder.angular_velocity < self.right_wheel_required_speed:
            self.right_wheel_actual_speed += speed_adjuster_delta
            if self.right_wheel_actual_speed >= 100:
                self.right_wheel_actual_speed = 100


    def moveForward(self, time, speed, speed_adjuster_delta):#essa velocidade eh angular? se nao for, tem que recalcular - Alefe
        self.left_wheel_required_speed = speed
        self.right_wheel_required_speed = speed
        aux_timer = time.time()
        while (time.time() - aux_timer) < time:
            self.left_wheel.spim(self.left_wheel_actual_speed)
            self.right_wheel.spim(self.right_wheel_actual_speed)#tinha que ser espelhado, mas melhor inverter isso no hardware
            adjustSpeed(speed_adjuster_delta)

    def turn(self, time, speed, speed_adjuster_delta):#usando sentido positivo: antihorario
        self.left_wheel_required_speed = speed#positivo porque encoder da a velocidade em modulo
        self.right_wheel_required_speed = speed
        aux_timer = time.time()
        while (time.time() - aux_timer) < time:
            self.left_wheel.spim(-self.left_wheel_actual_speed)
            self.right_wheel.spim(self.right_wheel_actual_speed)
            adjustSpeed(speed_adjuster_delta)

    def stop(self):
        self.left_wheel.spin(0)
        self.right_wheel.spin(0)
        self.left_wheel_required_speed = 0
        self.right_wheel_required_speed = 0
