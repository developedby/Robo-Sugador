# mover.py - o movimentador do robo, cuida de andar pra frente, para tras e para os lados

from wheel import Wheel
import time
from threading import Timer

def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

class Mover():
    sign = lambda x: x and (1, -1)[x < 0]
    speed_adjust_frequency = 0.25

    def __init__ (self, input1_a_pin, input2_a_pin, pwm_a_pin, encoder_a_pin, num_a_holes, input1_b_pin, input2_b_pin, pwm_b_pin, encoder_b_pin, num_b_holes, speed_adjust_delta):
        self.left_wheel = Wheel(input1_a_pin, input2_a_pin, pwm_a_pin, encoder_a_pin, num_a_holes)
        self.right_wheel = Wheel(input1_b_pin, input2_b_pin, pwm_b_pin, encoder_b_pin, num_b_holes)
        self.left_wheel_sent_speed = 0  # velocidade enviada a roda, em % do pwm - Alefe
        self.right_wheel_sent_speed = 0
        self.left_wheel_required_speed = None # velocidade desejada, em graus por segundo
        self.right_wheel_required_speed = None
        self.speed_adjust_delta = speed_adjust_delta
        self.speed_adjust_timer = None
        self.move_duration_timer = None


    def adjustSpeed(self):
        if not self.left_wheel.encoder.angular_velocity or not self.right_wheel.encoder.angular_velocity:
            return

        if (sign(self.left_wheel_required_speed) * self.left_wheel.encoder.angular_velocity) > self.left_wheel_required_speed:
            self.left_wheel_sent_speed -= speed_adjuster_delta
        elif (sign(self.left_wheel_required_speed) * self.left_wheel.encoder.angular_velocity) < self.left_wheel_required_speed:
            self.left_wheel_sent_speed += speed_adjuster_delta

        if (sign(self.right_wheel_required_speed) * self.left_wheel.encoder.angular_velocity) > self.right_wheel_required_speed:
            self.right_wheel_sent_speed -= speed_adjuster_delta
        elif (sign(self.right_wheel_required_speed) * self.left_wheel.encoder.angular_velocity) < self.right_wheel_required_speed:
            self.right_wheel_sent_speed += speed_adjuster_delta

        self.left_wheel_sent_speed = clamp(self.left_wheel_sent_speed, -100, 100)
        self.left_wheel_sent_speed = clamp(self.left_wheel_sent_speed, -100, 100)
        self.left_wheel.spin(self.left_wheel_sent_speed)
        self.right_wheel.spin(self.right_wheel_sent_speed)

    def moveForward(self, duration, speed):
        self.left_wheel_required_speed = speed
        self.right_wheel_required_speed = speed

        stopTimers()
        setTimers(duration)

    def turn(self, duration, speed): # usando sentido positivo: antihorario
        self.left_wheel_required_speed = -speed
        self.right_wheel_required_speed = speed

        stopTimers()
        setTimers(duration)

    def stop(self):
        stopTimers()
        self.left_wheel.spin(0)
        self.right_wheel.spin(0)
        self.left_wheel_required_speed = 0
        self.right_wheel_required_speed = 0

    def stopTimers(self):
        if self.speed_adjust_timer:
            self.speed_adjust_timer.cancel()
        if self.move_duration_timer:
            self.move_duration_timer.cancel()

    # duration <= 0 -> Infinite duration
    def setTimers(self, duration):
        self.speed_adjust_timer = Timer(self.speed_adjust_frequency, self.adjustSpeed)
        self.speed_adjust_timer.start()

        if duration > 0:
            self.move_duration_timer = Timer(duration, self.stopTimers)
            self.move_duration_timer.start()
