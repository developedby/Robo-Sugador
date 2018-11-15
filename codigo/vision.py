# vision.py - Usa processamento de imagem para achar objetos e obstáculos

from camera import Camera
from ultrasound import Ultrasound

import cv2
import numpy as np

class Vision():
    def __init__(self, echo_pin, trigger_pin, long_distance_port, short_distance_port):
        self.long_distance_cam = Camera(port=self.long_distance_port, resolution=(1920,1080))
        self.short_distance_cam = Camera(port=self.short_distance_port, resolution=(1280,720))
        self.ultrasound = Ultrasound(echo_pin, trigger_pin)
        self.long_distance_port = long_distance_port
        self.short_distance_port = short_distance_port

    def findDistantBalls(self):
        return self.findBalls(long_distance_cam.image())

    def findCloseBalls(self):
        return self.findBalls(short_distance_cam.image())

    def findBalls(self, image):
        image = cv2.GaussianBlur(image,5)

        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                                    param1=50,param2=30,minRadius=0,maxRadius=0)

    def findRacket(self):
        pass

    def getObstacleDistance():
        self.Ultrasound.sendTrigger()
        return self.ultrasound.distance
