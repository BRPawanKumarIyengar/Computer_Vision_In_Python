# To understand Video Camera

#We import CV2 to get all Computer Vision Modules 
import cv2 as Pawan_Camera_Capture

#We import Numpy module to prform mathematical calculations
import numpy as Pawan_Numpy_Module

#We import time module to get the sleep (wait function)
import time as Samay_in_Seconds

Chitra = Pawan_Camera_Capture.VideoCapture(0)
	
#We determine the output file name to save file in (.avi format) 
Video_File_Output1 = 'Pawan_Video_Output_Correct.avi'
Video_File_Output2 = 'Pawan_Video_Output_Inverted.avi'
	
#We set frame rate to 30 (please note that human eyes can detect frame rates below 24)
Set_Frame_Rate = 30
	
#We set Resolution to 640` and 480
Set_Resolution_Camera = (640,480)

Set_Codec = Pawan_Camera_Capture.VideoWriter_fourcc('W', 'M', 'V', '2')
	
#Now we create a combined output Variable
Pawan_Video_Save1 = Pawan_Camera_Capture.VideoWriter(Video_File_Output1,Set_Codec, Set_Frame_Rate,Set_Resolution_Camera)
Pawan_Video_Save2 = Pawan_Camera_Capture.VideoWriter(Video_File_Output2,Set_Codec, Set_Frame_Rate,Set_Resolution_Camera)
	
#The loop plays the same image again and again and if statement ensures that the loop is broken if the user preses "Q" o the keyboard
while(True):
	Jay, Chaaya = Chitra.read()
	Palti_Chaaya = Pawan_Camera_Capture.flip(Chaaya,90)
	#Shows image accurately but Text is inverted
	Pawan_Camera_Capture.imshow("Pawan's Live Video",Palti_Chaaya)
	#Shows inverted movements but text is easy to read
	Pawan_Camera_Capture.imshow("Good For Reading Text", Chaaya)
	Pawan_Video_Save1.write(Palti_Chaaya)
	Pawan_Video_Save2.write(Chaaya)
	#If we want Still Image Output we use waitkey(0) and for Video Output we use waitKey(1)
	if Pawan_Camera_Capture.waitKey(1) & 0xFF == ord('q'):
		break
	
#We reease the the camera via Chitra.release and use destroyAllWindows to terminate all running windows
Chitra.release()
Pawan_Video_Save1.release()
Pawan_Video_Save2.release()
Pawan_Camera_Capture.destroyAllWindows()
	
#the pcture captured by the Camera is converted to an array of pixels with colours in RBG
Pixel_Array = Pawan_Numpy_Module.array(Chaaya)