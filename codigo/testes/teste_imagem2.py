# Teste 2 - Tenta fazer adaptiveThreshold para melhorar a informacao para o HoughCircles

import cv2
import numpy as np
import time

def no():
    pass

def channel_processing(channel):
    channel = cv2.adaptiveThreshold(channel,
      255,
      cv2.ADAPTIVE_THRESH_MEAN_C,
      cv2.THRESH_BINARY,
      2*cv2.getTrackbarPos('adaptive thresh block','sliders')+3,
      cv2.getTrackbarPos('adaptive const','sliders'))
    #mop up the dirt
    channel = cv2.erode(channel, (3,3))
    channel = cv2.dilate(channel, (3,3))
    return channel

def inter_centre_distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def colliding_circles(circles):
    for index1, circle1 in enumerate(circles):
        for circle2 in circles[index1+1:]:
            x1, y1, Radius1 = circle1[0]
            x2, y2, Radius2 = circle2[0]
            #collision or containment:
            if inter_centre_distance(x1,y1,x2,y2) < Radius1 + Radius2:
                return True

def find_circles(processed):
    # try:
    storage = cv2.HoughCircles(processed, cv2.HOUGH_GRADIENT, 1, 100,
                  param1=cv2.getTrackbarPos('param1','sliders'),
                  param2=cv2.getTrackbarPos('param2','sliders'),
                  minRadius=2,
                  maxRadius=100)
    # except:
    #     LOW += 1
    #     print ('try')
    #     find_circles(processed, storage, LOW)
    # circles = np.asarray(storage)
    # print ('number of circles:', len(circles))
    # if colliding_circles(circles):
    #     LOW += 1
    #     storage = find_circles(processed, storage, LOW)
    # print ('c', LOW)
    return storage

def draw_circles(storage, orig):
    # circles = np.asarray(storage)
    # print(len(circles), 'circles found')
    # for circle in circles:
    #     Radius, x, y = int(circle[0][2]), int(circle[0][0]), int(circle[0][1])
    #     cv2.Circle(output, (x, y), 1, cv2.RGB(0, 255, 0), -1, 8, 0)
    #     cv2.Circle(output, (x, y), Radius, cv2.RGB(255, 0, 0), 3, 8, 0)
    if not (storage is None):
        storage = np.uint16(np.around(storage))
        for i in storage[0,:]:
            cv2.circle(orig,(i[0],i[1]),i[2],(0,255,0),2)
            cv2.circle(orig,(i[0],i[1]),2,(0,0,255),3)
    return orig


cam = cv2.VideoCapture()
cam.open(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)
# cam.set(cv2.CAP_PROP_FRAME_COUNT, 1)


cv2.namedWindow('sliders')
cv2.createTrackbar('param1','sliders',100,100,no)
cv2.createTrackbar('param2','sliders',100,100,no)
cv2.createTrackbar('blur window','sliders',3,20,no)
cv2.createTrackbar('blur deviation','sliders',0,10,no)
cv2.createTrackbar('canny1','sliders',30,200,no)
cv2.createTrackbar('canny2','sliders',100,200,no)
cv2.createTrackbar('canny aperture','sliders',0,2,no)
cv2.createTrackbar('adaptive thresh block','sliders',25,200,no)
cv2.createTrackbar('adaptive const','sliders',7,20,no)

while 1:
    ret, orig = cam.read()

    #split image into RGB components
    rrr, ggg, bbb = cv2.split(orig)
    #process each component
    rrr = channel_processing(rrr)
    ggg = channel_processing(ggg)
    bbb = channel_processing(bbb)
    #combine images using logical 'And' to avoid saturation
    processed = cv2.add(rrr, ggg)
    processed = cv2.add(processed, bbb)
    #cv2.ShowImage('before canny', processed)
    # cv.SaveImage('case3_processed.jpg',processed)
    #use canny, as HoughCircles seems to prefer ring like circles to filled ones.
    processed = cv2.Canny(processed,
                          cv2.getTrackbarPos('canny1','sliders'),
                          cv2.getTrackbarPos('canny2','sliders'),
                          apertureSize=2*cv2.getTrackbarPos('canny aperture','sliders')+3)
    #smooth to reduce noise a bit more
    # cv.Smooth(processed, cv2.GAUSSIAN, 7, 7)
    processed = cv2.GaussianBlur(processed, (7, 7), 0)
    # cv2.ShowImage('processed', processed)
    #find circles, with parameter search
    storage = find_circles(processed)
    output = draw_circles(storage, orig)

    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # # img = cv2.GaussianBlur(img,
    # #                       (2*cv2.getTrackbarPos('blur window','sliders')+1,
    # #                        2*cv2.getTrackbarPos('blur window','sliders')+1),
    # #                        cv2.getTrackbarPos('blur deviation','sliders'))
    # img = cv2.medianBlur(img, (2*cv2.getTrackbarPos('blur window','sliders')+1))
    # circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 100,
    #               param1=cv2.getTrackbarPos('param1','sliders'),
    #               param2=cv2.getTrackbarPos('param2','sliders'),
    #               minRadius=2,
    #               maxRadius=100)
    # print(circles)
    # if not (circles is None):
    #     circles = np.uint16(np.around(circles))
    #     for i in circles[0,:]:
    #         cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    #         cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
    cv2.imshow('circles', output)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
