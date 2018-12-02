# The code detects a single color based on upper and lower RGB count from a variety of colors
import cv2 as Pawan_Camera_Capture
import numpy as Pawan_Numpy_Module
import time as Samay_in_Seconds

Chitra = Pawan_Camera_Capture.imread('Pawan_Colour.PNG')

fontFace = Pawan_Camera_Capture.FONT_HERSHEY_TRIPLEX
fontScale = 1
fontColor = (0, 255, 255)

Lower_Red = Pawan_Numpy_Module.array([178,0,179])
Upper_Red = Pawan_Numpy_Module.array([255,255,255])
Parivartit_Chitra = Pawan_Camera_Capture.cvtColor(Chitra,Pawan_Camera_Capture.COLOR_BGR2HSV)
Pawan_Red_Filter = Pawan_Camera_Capture.inRange(Parivartit_Chitra, Lower_Red, Upper_Red)

Pawan_Camera_Capture.imshow('As seeen in Camera', Chitra)
Pawan_Camera_Capture.imshow('Only See Red', Pawan_Red_Filter)

while True:
	Pawan_Camera_Capture.imshow('As seeen in Camera', Chitra)
	Pawan_Camera_Capture.imshow('Only See King', Parivartit_Chitra)
	if Pawan_Camera_Capture.waitKey(10) & 0xFF==ord('q'):
		break
		
Pawan_Camera_Capture.destroyAllWindows()