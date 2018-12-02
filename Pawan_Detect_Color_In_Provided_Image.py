# The code detects a single color based on upper and lower RGB count from a variety of colors
import cv2 as Pawan_Camera_Capture
import numpy as Pawan_Numpy_Module


cap = Pawan_Camera_Capture.VideoCapture(0)

while(1):

    # Take each frame
    ret, Chitra = cap.read()

    # Convert BGR to HSV
    hsv = Pawan_Camera_Capture.cvtColor(Chitra, Pawan_Camera_Capture.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = Pawan_Numpy_Module.array([110,50,50])
    upper_blue = Pawan_Numpy_Module.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = Pawan_Camera_Capture.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = Pawan_Camera_Capture.bitwise_and(Chitra,Chitra, mask= mask)

    Pawan_Camera_Capture.imshow('Original Chitra',Chitra)
    Pawan_Camera_Capture.imshow('First Level Filter',mask)
    Pawan_Camera_Capture.imshow('Second Level Filter',res)
    k = Pawan_Camera_Capture.waitKey(0) & 0xFF("q")
    if k == 27:
        break

Pawan_Camera_Capture.destroyAllWindows()