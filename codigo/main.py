# main.py - Codigo do robo que suga bolinhas
# Informações sobre a licensa no arquivo LICENSE

from robot import Robot

echo_pin = 4
trigger_pin = 27
long_distance_cam_port = 0
short_distance_cam_port = 1
input1_left_wheel_pin = 23
input2_left_wheel_pin = 24
pwm_left_wheel_pin = 18
encoder_left_wheel_pin = 6
num_encoder_left_wheel_holes = 20
input1_right_wheel_pin = 25
input2_right_wheel_pin = 8
pwm_right_wheel_pin = 13
encoder_right_wheel_pin = 5
num_encoder_right_wheel_holes = 20
speed_adjust_delta = 5
infrared_pin = 22
fan_input1_pin = 10
fan_input2_pin = 9
cover_pin = 12
servo_min_angle = 0
servo_max_angle = 180
cover_closed_angle = 150 #chute nos angulos de abertura e fechamento
cover_open_angle = 180
communicator_port = 2

the_robot = Robot(  echo_pin, trigger_pin, long_distance_cam_port, short_distance_cam_port,
                    input1_left_wheel_pin, input2_left_wheel_pin, pwm_left_wheel_pin, encoder_left_wheel_pin, num_encoder_left_wheel_holes,
                    input1_right_wheel_pin, input2_right_wheel_pin, pwm_right_wheel_pin, encoder_right_wheel_pin, num_encoder_right_wheel_holes, speed_adjust_delta,
                    infrared_pin, fan_input1_pin, fan_input2_pin, cover_pin, servo_min_angle, servo_max_angle, cover_closed_angle, cover_open_angle,
                    communicator_port)
the_robot.intelligence.mainLoop()
