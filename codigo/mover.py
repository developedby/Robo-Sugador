from wheel import Wheel

class Mover():
    def __init__ (self, input1_a_pin, input2_a_pin, pwm_a_pin, encoder_a_pin, num_a_holes, input1_b_pin, input2_b_pin, pwm_b_pin, encoder_b_pin, num_b_holes):
        self.left_wheel = Wheel(input1_a_pin, input2_a_pin, pwm_a_pin, encoder_a_pin, num_a_holes)
        self.right_wheel = Wheel(input1_b_pin, input2_b_pin, pwm_b_pin, encoder_b_pin, num_b_holes)
        self.left_wheel_actual_speed = None
        self.right_wheel_actual_speed = None
        self.left_wheel_required_speed = None
        self.right_wheel_required_speed = None

    def adjustSpeed(self):
        pass
    def moveForward(self, speed):
        pass
    def turn(self, time, speed):
        pass
    def stop(self):
        self.left_wheel.walk(0)
        self.right_wheel.walk(0)
