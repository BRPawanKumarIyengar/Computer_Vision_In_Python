# To understand Video Camera

#We import CV2 to get all Computer Vision Modules 
import cv2 as Pawan_Camera_Capture

#We import Numpy module to prform mathematical calculations
import numpy as Pawan_Numpy_Module

#We import time module to get the sleep (wait function)
import time as Samay_in_Seconds

#We now create a Function to capture the laptop camera 
def Pawan_Video_Camera():
	# Here the number zero denotes that we are using inbuilt laptop camera(Camera of choice); If more are connected then then get numbers like 1 , 2 ,3 ... so on.  
	Chitra = Pawan_Camera_Capture.VideoCapture(0)
	
	#We capture the resolution of the camera interms of Length and Width
	print('Width of Pic is: ' +str(Chitra.get(3)))
	print('Height of Pic is: ' +str(Chitra.get(4)))
	
	#We can set the resolution of the camera that is set
	ret = Chitra.set(3,64)
	ret = Chitra.set(4,48)
	
	#Et_Number is a Boolean vatriable that stores if image was successfully captured by Camera and Chaaya has all the RBG information for captured image
	Ret_Number,Chaaya = Chitra.read()
	
	#The loop plays the same image again and again and if statement ensures that the loop is broken if the user preses "Q" o the keyboard
	while True:
		Pawan_Camera_Capture.imshow('Pawan Ne Chitra Banaya',Chaaya)
		if Pawan_Camera_Capture.waitKey(0) & 0xFF==ord('q'):
			break
	
	#We reease the the camera via Chitra.release and use destroyAllWindows to terminate all running windows
	Chitra.release()
	Pawan_Camera_Capture.destroyAllWindows()
	
	#the pcture captured by the Camera is converted to an array of pixels with colours in RBG
	Pixel_Array = Pawan_Numpy_Module.array(Chaaya)
	
	#The function then returns the array of Pixels
	return Pixel_Array
	
yoyo = Pawan_Video_Camera()
#print (yoyo)