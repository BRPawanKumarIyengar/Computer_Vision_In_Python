#We will perform Colour based Tracking of an object

#We import CV2 to get all Computer Vision Modules 
import cv2 as Pawan_Camera_Capture

#We import Numpy module to prform mathematical calculations
import numpy as Pawan_Numpy_Module

#We import time module to get the sleep (wait function)
import time as Samay_in_Seconds

Sabse_Kam_Blue = Pawan_Numpy_Module.array([100,50,50])
Sabse_Zyada_Blue = Pawan_Numpy_Module.array([140,255,255])

Chitra = Pawan_Camera_Capture.VideoCapture(0)

if Chitra.isOpened():
	Jay = True
else:
	Jay=False
	
while Jay:
		Jay, Chaaya = Chitra.read()
		Vichitra_Chitra = Pawan_Camera_Capture.cvtColor(Chaaya,Pawan_Camera_Capture.COLOR_BGR2HSV)
		Parivartit_Chitra = Pawan_Camera_Capture.inRange(Vichitra_Chitra,Sabse_Kam_Blue,Sabse_Zyada_Blue)
		Punah_Parivartit_Chitra = Pawan_Camera_Capture.bitwise_and(Chaaya,Chaaya,mask = Parivartit_Chitra)
		Pawan_Camera_Capture.imshow("Original Image",Chaaya)
		Pawan_Camera_Capture.imshow("Modified Image",Parivartit_Chitra)
		Pawan_Camera_Capture.imshow("Re-Modified Image",Punah_Parivartit_Chitra)
		if Pawan_Camera_Capture.waitKey(1) == 27:
			break
		