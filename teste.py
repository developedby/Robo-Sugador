import cv2
import numpy as np


cam = cv2.VideoCapture()
cam.open(1)

while 1:
    ret, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                  param1=30,
                  param2=15,
                  minRadius=0,
                  maxRadius=0)

    print(circles)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('circles', img)

    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
