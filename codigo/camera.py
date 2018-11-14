# camera.py - Tira fotos com uma camera usb
# Informações sobre a licensa no arquivo LICENSE

import cv2

class Camera:
    def __init__ (self, port, resolution):
            self.capture = cv2.VideoCapture(port)
            if not self.capture.isOpened():
                print("Warning - camera " + port + " not opened correctly")
            self.capture.set(cv2.CV_CAP_PROP_FRAME_WIDTH, resolution['width'])
            self.capture.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, resolution['height'])

    def image (self):
        retval, image = self.capture.read()
        return image