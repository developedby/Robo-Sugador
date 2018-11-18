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
    def __init__ (self,
                    # Vision
                  ultrasound_echo_pin,
                  ultrasound_trigger_pin,
                  long_distance_cam_port,
                  short_distance_cam_port,
                    # Mover
                  left_wheel_input1_pin,
                  left_wheel_input2_pin,
                  left_wheel_pwm_pin,
                  left_wheel_encoder_pin,
                  left_wheel_encoder_num_holes,
                  right_wheel_input1_pin,
                  right_wheel_input2_pin,
                  right_wheel_pwm_pin,
                  right_wheel_encoder_pin,
                  right_wheel_encoder_num_holes,
                  speed_adjust_delta,
                    # Sucker
                  infrared_pin,
                  fan_input1_pin,
                  fan_input2_pin,
                  cover_pin,
                  servo_min_angle,
                  servo_max_angle,
                  cover_closed_angle,
                  cover_open_angle,
                    # Communicator
                  communicator_port):
                  
        GPIO.setmode(GPIO.BOARD)
        self.vision = Vision(ultrasound_echo_pin,
                             ultrasound_trigger_pin,
                             long_distance_cam_port,
                             short_distance_cam_port)
        self.mover = Mover(left_wheel_input1_pin,
                           left_wheel_input2_pin,
                           left_wheel_pwm_pin,
                           left_wheel_encoder_pin,
                           left_wheel_encoder_num_holes,
                           right_wheel_input1_pin,
                           right_wheel_input2_pin,
                           right_wheel_pwm_pin,
                           right_wheel_encoder_pin,
                           right_wheel_encoder_num_holes,
                           speed_adjust_delta)
        self.sucker = Sucker(infrared_pin,
                             fan_input1_pin,
                             fan_input2_pin,
                             cover_pin,
                             servo_min_angle,
                             servo_max_angle,
                             cover_closed_angle,
                             cover_open_angle)
        self.communicator = Communicator(communicator_port)
        self.intelligence = Intelligence(self)
