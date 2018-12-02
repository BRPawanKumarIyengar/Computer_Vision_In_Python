#Get RGB values of Pixels in am image
from PIL import Image as Chitra
import numpy as Pawan_Numpy_Module

def Pawan_get_RGB_Values(image_path):
	Chaaya = Chitra.open(image_path, 'r')
	width, height = Chaaya.size
	pixel_values = list(Chaaya.getdata())
	if Chaaya.mode == 'RGB':
		channels = 3
	elif Chaaya.mode == 'L':
		channels = 1
	else:
		print("Unknown mode: %s" % Chaaya.mode)
		return None
		
	Ctr = len(pixel_values)
	Num_Ctr = 0
	No_Black_or_White_Array =[]
	
	while Num_Ctr < (Ctr -1):
		if pixel_values[Num_Ctr] == (255,255,255):
			pixel_values.remove((255,255,255))
			Ctr = Ctr - 1
		elif pixel_values[Num_Ctr] == (0,0,0):
			pixel_values.remove((0,0,0))
			Ctr = Ctr - 1
		else:
			No_Black_or_White_Array.append(pixel_values[Num_Ctr])
		Num_Ctr = Num_Ctr + 1
		
	return No_Black_or_White_Array	
	
Toto = Pawan_get_RGB_Values('C:/Users/brpaw/Desktop/Ho/Pawan_Colour.png')
print(Toto)
	
	
