# main.py - Codigo do robo que suga bolinhas
# Informações sobre a licensa no arquivo LICENSE

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.setmode(GPIO.BCM)

from robot import Robot

ultrasound_echo_pin = 4
ultrasound_trigger_pin = 27
long_distance_cam_port = 0
short_distance_cam_port = 1
left_wheel_input1_pin = 25
left_wheel_input2_pin = 8
left_wheel_pwm_pin = 13
left_wheel_encoder_pin = 6
left_wheel_encoder_num_holes = 20
right_wheel_input1_pin = 23
right_wheel_input2_pin = 24
right_wheel_pwm_pin = 18
right_wheel_encoder_pin = 5
right_wheel_encoder_num_holes = 20
speed_adjust_delta = 1
infrared_pin = 22
fan_input1_pin = 10
fan_input2_pin = 9
cover_pin = 12
servo_min_angle = 0
servo_max_angle = 180
cover_closed_angle = 15 # Medida mais ou menos certa
cover_open_angle = 0
servo_initial_angle = (cover_closed_angle + cover_open_angle)/2


the_robot = Robot(  # Vision
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
                    servo_initial_angle,
                    servo_min_angle,
                    servo_max_angle,
                    cover_closed_angle,
                    cover_open_angle)
the_robot.intelligence.mainLoop()
