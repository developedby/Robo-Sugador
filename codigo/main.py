# main.py - Codigo do robo que suga bolinhas
# Informações sobre a licensa no arquivo LICENSE

from robot import Robot

ultrasound_echo_pin = 4
ultrasound_trigger_pin = 27
long_distance_cam_port = 0
short_distance_cam_port = 1
left_wheel_input1_pin = 23
left_wheel_input2_pin = 24
left_wheel_pwm_pin = 18
left_wheel_encoder_pin = 6
left_wheel_encoder_num_holes = 20
right_wheel_input1_pin = 25
right_wheel_input2_pin = 8
right_wheel_pwm_pin = 13
right_wheel_encoder_pin = 5
right_wheel_encoder_num_holes = 20
speed_adjust_delta = 5
infrared_pin = 22
fan_input1_pin = 10
fan_input2_pin = 9
cover_pin = 12
servo_min_angle = 0
servo_max_angle = 180
cover_closed_angle = 150 #chute nos angulos de abertura e fechamento
cover_open_angle = 180
communicator_port = 49777

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
                    servo_min_angle,
                    servo_max_angle,
                    cover_closed_angle,
                    cover_open_angle,
                    # Communicator
                    communicator_port)
the_robot.intelligence.mainLoop()
