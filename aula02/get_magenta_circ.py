import cv2
import numpy as np
from matplotlib import pyplot as plt
import time
import math


#Questao 1

H=14
D=15
h=621
f=D/H*h

# Questao 2
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged

while(True):
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blur = cv2.GaussianBlur(hsv,(5,5),0)
    # define range of blue color in HSV
    lower_blue = np.array([80,50,50])
    upper_blue = np.array([150,255,255])

    lower_pink = np.array([150, 50, 50])
    upper_pink = np.array([180, 255, 255])

    # Threshold the HSV image to get only blue colors
    pink_mask = cv2.inRange(blur, lower_pink, upper_pink)
    blue_mask = cv2.inRange(blur, lower_blue, upper_blue)

    ## final mask and masked
    mask = cv2.bitwise_or(blue_mask, pink_mask)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    segmentado_circ = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,np.ones((4, 4)))
    contornos, arvore = cv2.findContours(segmentado_circ.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    # cv2.drawContours(res, contornos, -1, [0, 0, 255], 3);
    try:
        maior = None
        segunda_maior = None
        maior_area = 1
        segunda_maior_area = 1
        for c in contornos:
            area = cv2.contourArea(c)
            if area > maior_area:
                maior_area = area
                maior = c
            elif area > segunda_maior_area:
                segunda_maior_area = area
                segunda_maior = c

        M = cv2.moments(maior)
        cX1 = int(M["m10"] / M["m00"])
        cY1 = int(M["m01"] / M["m00"])

        M2 = cv2.moments(segunda_maior)
        cX2 = int(M2["m10"] / M2["m00"])
        cY2 = int(M2["m01"] / M2["m00"])

        dist = math.sqrt((cX1-cX2)**2 + (cY1-cY2)**2) * 2 

        dist_cam = str ((H * f) / dist)
        angle = np.degrees([ math.atan( abs(cY1 - cY2) / abs(cX1 - cX2) ) ])
        cv2.putText(res , dist_cam , (0 , 50) , cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 255, 255), 5, cv2.LINE_AA)
        cv2.putText(res , str(angle[0]) , (0 , 150) , cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 255, 255), 5, cv2.LINE_AA)


        cv2.line(res,(cX1,cY1),(cX2,cY2),(255,0,0),5)
        # cv2.drawContours(res, [maior, segunda_maior], -1, [0, 255, 255], 5)

        (x,y),radius = cv2.minEnclosingCircle(maior)
        center = (int(x),int(y))
        radius = int(radius)
        cv2.circle(res,center,radius,(0,255,0),2)

        (x,y),radius = cv2.minEnclosingCircle(segunda_maior)
        center = (int(x),int(y))
        radius = int(radius)
        cv2.circle(res,center,radius,(0,255,0),2)

    except (ZeroDivisionError):
        print('no two contours found')

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#  When everything done, release the capture
cap.release()
cv2.destroyAllWindows()