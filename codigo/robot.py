# robot.py - Representa o robo como um todo. So criar e ele ja funciona

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

from vision import Vision
from mover import Mover
from sucker import Sucker
from communicator import Communicator
from intelligence import Intelligence

class Robot :
    def __init__ (self, echo_pin, trigger_pin, long_distance_cam_port, short_distance_cam_port,
                        input1_left_wheel_pin, input2_left_wheel_pin, pwm_left_wheel_pin, encoder_left_wheel_pin, num_encoder_left_wheel_holes,
                        input1_right_wheel_pin, input2_right_wheel_pin, pwm_right_wheel_pin, encoder_right_wheel_pin, num_encoder_right_wheel_holes, speed_adjust_delta,
                        infrared_pin, fan_input1_pin, fan_input2_pin, cover_pin, servo_min_angle, servo_max_angle, cover_closed_angle, cover_open_angle,
                        communicator_port):
        GPIO.setmode(GPIO.BOARD)
        self.vision = Vision(echo_pin, trigger_pin, long_distance_cam_port, short_distance_cam_port)
        self.mover = Mover(input1_left_wheel_pin, input2_left_wheel_pin, pwm_left_wheel_pin, encoder_left_wheel_pin, num_encoder_left_wheel_holes,
        input1_right_wheel_pin, input2_right_wheel_pin, pwm_right_wheel_pin, encoder_right_wheel_pin, num_encoder_right_wheel_holes, speed_adjust_delta)
        self.sucker = Sucker(infrared_pin, fan_input1_pin, fan_input2_pin, cover_pin, servo_min_angle, servo_max_angle, cover_closed_angle, cover_open_angle)
        self.communicator = Communicator(communicator_port)
        self.intelligence = Intelligence(self)
