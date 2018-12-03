# Teste4 - Teste da raquete

import cv2
import time

def no(self):
    pass

cam = cv2.VideoCapture()
cam.open(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# cam.set(cv2.CAP_PROP_FRAME_COUNT, 1)

cv2.namedWindow('sliders')
cv2.createTrackbar('h_min','sliders',0,255,no)
cv2.createTrackbar('h_max','sliders',0,255,no)
cv2.createTrackbar('s_min','sliders',0,255,no)
cv2.createTrackbar('s_max','sliders',0,255,no)
cv2.createTrackbar('v_min','sliders',0,255,no)
cv2.createTrackbar('v_max','sliders',0,255,no)

while 1:
    ret, img = cam.read()
    img = cv2.GaussianBlur(img, (9, 9), 0)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 150 200 50 255 100 255
    img2 = cv2.inRange(img2, (cv2.getTrackbarPos('h_min','sliders'), cv2.getTrackbarPos('s_min','sliders'), cv2.getTrackbarPos('v_min','sliders')),
                            (cv2.getTrackbarPos('h_max','sliders'), cv2.getTrackbarPos('s_max','sliders'), cv2.getTrackbarPos('v_max','sliders')))
    img2 = cv2.erode(img2, (5,5))
    img2 = cv2.dilate(img2, (5,5))
    contours = cv2.findContours(img2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[1]

    center = None
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        if M["m00"] and M["m00"]:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            cv2.circle(img, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(img, center, 5, (0, 0, 255), -1)


    cv2.imshow('circles', img2)

    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
