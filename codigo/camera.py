# camera.py - Tira fotos com uma camera usb
# Informações sobre a licensa no arquivo LICENSE

import cv2

class Camera:
    def __init__ (port, resolution):
            self.capture = cv2.VideoCapture(port)
            if not self.capture.isOpened():
                print("Warning - camera " + port + " not opened correctly")
            self.capture.set(CV_CAP_PROP_FRAME_WIDTH, resolution['width'])
            self.capture.set(CV_CAP_PROP_FRAME_HEIGHT, resolution['height'])

    def image ():
        retval, image = self.capture.read()
        return image