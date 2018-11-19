# Teste1 - Versao que vai ser usada no final, Hough transform


import cv2
import numpy as np
import time

def no():
    pass

cam = cv2.VideoCapture()
cam.open(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
cam.set(cv2.CAP_PROP_BUFFERSIZE, 1)
# cam.set(cv2.CAP_PROP_FRAME_COUNT, 1)

cv2.namedWindow('sliders')
cv2.createTrackbar('param1','sliders',50,100,no)
cv2.createTrackbar('param2','sliders',50,100,no)
cv2.createTrackbar('blur window','sliders',5,10,no)
cv2.createTrackbar('blur p1','sliders',100,200,no)
cv2.createTrackbar('blur p2','sliders',100,200,no)


while 1:
    ret, img = cam.read()
    if img is None:
        print("nao conseguiu ler imagem")
        continue
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Ruim, muito xiado, muitos falsos positivos
    # img = cv2.GaussianBlur(img,
    #                       (2*cv2.getTrackbarPos('blur window','sliders')+1,
    #                        2*cv2.getTrackbarPos('blur window','sliders')+1),
    #                        cv2.getTrackbarPos('blur p1','sliders'))

    img = cv2.medianBlur(img, (2*cv2.getTrackbarPos('blur window','sliders')+1))

    # Ruim, lento e não filtra o suficiente
    # img = cv2.bilateralFilter(img,
    #                        cv2.getTrackbarPos('blur window','sliders')+1,
    #                        cv2.getTrackbarPos('blur p1','sliders'),
    #                        cv2.getTrackbarPos('blur p2','sliders'))

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 90,
                  param1=cv2.getTrackbarPos('param1','sliders'),
                  param2=cv2.getTrackbarPos('param2','sliders'),
                  minRadius=5,
                  maxRadius=150)
    print(circles)
    if not (circles is None):
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
            cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
    cv2.imshow('circles', img)
    # time.sleep(.1)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
