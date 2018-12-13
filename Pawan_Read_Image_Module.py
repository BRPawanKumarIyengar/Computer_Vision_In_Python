import os as Pawan_Operating_System_Module
from PIL import Image as ChitraKala
import numpy as Pawan_Numpy_Module
import cv2 as Pawan_Camera_Capture
import pickle as Achaar

Mukh = Pawan_Camera_Capture.CascadeClassifier("Cascade\\haarcascade_frontalface_alt2.xml")


def Pawan_Read_Images(Image_Path):
	Ankh_Ganit = 0
	Y_Label = []
	X_Train = []
	Chitra_Sankhya = None
	Chitra_Suchana ={}
	
	recognizer = Pawan_Camera_Capture.face.LBPHFaceRecognizer_create()
	
	for root, dirs, files in Pawan_Operating_System_Module.walk(Image_Path):
		for file in files:
			if file.endswith("PNG") or file.endswith("jpg"):
				path = Pawan_Operating_System_Module.path.join(root, file)
				Pawan_label = Pawan_Operating_System_Module.path.basename(Pawan_Operating_System_Module.path.dirname(path)).replace(" ","-").lower()
				if not Pawan_label in Chitra_Suchana:
					Chitra_Suchana[Pawan_label] = Ankh_Ganit
					Ankh_Ganit = Ankh_Ganit + 1
				Chitra_Sankhya = Chitra_Suchana[Pawan_label]
				Chitra = ChitraKala.open(path).convert("L")
				Chitra_Pankti = Pawan_Numpy_Module.array(Chitra, 'uint8')
				Bhavyata = (550, 550)
				final_image = Chitra.resize(Bhavyata, ChitraKala.ANTIALIAS)
				Mukh_Chaaya = Mukh.detectMultiScale(Chitra_Pankti, scaleFactor = 1.5,minNeighbors = 5)
				
				
				for (x, y, w, h) in Mukh_Chaaya:
					Mukh_Kendrit = Chitra_Pankti[y:(y+h), x:(x+w)]
					Y_Label.append(Chitra_Sankhya)
					X_Train.append(Mukh_Kendrit)
	with open("face-labels.pickle", 'wb') as Chitra_Maaya:
		 Achaar.dump(Chitra_Suchana, Chitra_Maaya)

	recognizer.train(X_Train, Pawan_Numpy_Module.array(Y_Label))
	recognizer.save("face-trainner.yml")
	return Chitra_Suchana
					
					
Toto = Pawan_Read_Images('C:\\Users\\brpaw\\Desktop\\Ho\\Mukh__Chitra')
print(Toto)

