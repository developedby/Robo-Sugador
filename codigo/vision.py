# vision.py - Usa processamento de imagem para achar objetos e obstáculos

from camera import Camera
from ultrasound import Ultrasound

import cv2
import numpy as np

class Vision():
    def __init__(self, echo_pin, trigger_pin, max_detectable_distance, long_distance_port, short_distance_port):
        self.long_distance_cam = Camera(port=long_distance_port, resolution={'width':1280, 'height':720})
        self.short_distance_cam = Camera(port=short_distance_port, resolution={'width':854, 'height':480})
        self.ultrasound = Ultrasound(echo_pin, trigger_pin, max_detectable_distance)
        self.long_distance_port = long_distance_port
        self.short_distance_port = short_distance_port

    def findDistantBalls(self):
        print('circulos distantes:')
        return self.findBalls(self.long_distance_cam.image(),  9, 90, 45, 45, 2, 140)
    def findCloseBalls(self):
        print('circulos proximos:')
        return self.findBalls(self.short_distance_cam.image(), 9, 90, 50, 45, 2, 140)

    def findBalls(self, image, blur, min_dist, hough1, hough2, min_radius, max_radius):
        img = image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.medianBlur(img, blur)
        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,
                      1, #dp - proporcao maluca
                      minDist=min_dist,
                      param1=hough1,
                      param2=hough2,
                      minRadius=min_radius,
                      maxRadius=max_radius)
        # Da [[[0. 0. 0.]]] quando encontra algo que parece um circulo mas nao e o suficiente para ser identificado
        if circles is not None:
            if np.zeros(shape=(1,1,3)) in circles:
                circles = None
        print(circles)
        return circles

    def findRacket(self, image, min_radius):
        img = image
        img = cv2.GaussianBlur(img, (9, 9), 0)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        img = cv2.inRange(img, (1, 0, 0),(8, 255, 255))
        img = cv2.erode(img, (5,5))
        img = cv2.dilate(img, (5,5))

        contours = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[1]

        center = None
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            if radius >= min_radius:
                M = cv2.moments(c)
                if M["m00"] and M["m00"]:
                    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            else:
                center = None
        print('raquete: ', center)
        return center

    def obstacleDistance(self):
        return self.ultrasound.distance

    def close(self):
        self.long_distance_cam.close()
        self.short_distance_cam.close()
