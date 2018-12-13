import cv2 as Pawan_Camera_Capture
import numpy as Pawan_Numpy_Module
import time as Samay_in_Seconds
import matplotlib.pyplot as Pawan_Plot
import pickle as Achaar

def Pawan_Face_Recognition():
	Mukh = Pawan_Camera_Capture.CascadeClassifier("Cascade\\haarcascade_frontalface_alt2.xml")
	recognizer = Pawan_Camera_Capture.face.LBPHFaceRecognizer_create()
	recognizer.read("face-trainner.yml")
	
	Pawan_label_Names = {"person_name":1}
	with open("face-labels.pickle", 'rb') as Chitra_Maaya:
		Pawan_label_Names_Aagami = Achaar.load(Chitra_Maaya)
		#Pawan_label_Names = {values:keys for keys,values in Pawan_label_Names_Aagami.items()}
		Pawan_label_Names = {v:k for k,v in Pawan_label_Names_Aagami.items()}
		
	Chitra = Pawan_Camera_Capture.VideoCapture(0)
	
	while True:
		Jay, Chaaya = Chitra.read()
		Rang_Heen_Chitra = Pawan_Camera_Capture.cvtColor(Chaaya, Pawan_Camera_Capture.COLOR_BGR2GRAY)
		Mukh_Chaaya = Mukh.detectMultiScale(Rang_Heen_Chitra, scaleFactor = 1.5,minNeighbors = 5)

		for (x, y, w, h) in Mukh_Chaaya:
			print("JO")
			Mukh_Kendrit = Chaaya[y:(y+h), x:(x+w)]
			Mukh_Kendrit_Rangheen = Rang_Heen_Chitra[y:(y+h), x:(x+w)]
			Ankh, Vishwas = recognizer.predict(Mukh_Kendrit_Rangheen)
			print(Ankh, Vishwas)
			Antim_Chitra = "my_image.png"
			Box_Ka_Rang = (0,255,0)
			Likhai = Pawan_Camera_Capture.FONT_HERSHEY_SIMPLEX
			Stroke = 2
			Naam = Pawan_label_Names[Ankh]
			Choudai = x + w
			Lambai = y + h
			Pawan_Camera_Capture.putText(Chaaya, Naam, (x,y), Likhai, 1, Box_Ka_Rang, Stroke, Pawan_Camera_Capture.LINE_AA)
			Pawan_Camera_Capture.rectangle(Chaaya, (x,y),(Choudai, Lambai), Box_Ka_Rang,Stroke)
			Pawan_Camera_Capture.imwrite(Antim_Chitra, Chaaya)	
		Pawan_Camera_Capture.imshow("Pawan_Face_Recognition",Chaaya)
		if Pawan_Camera_Capture.waitKey(1) == 27:
			break
		
	Chitra.release()
	Pawan_Camera_Capture.destroyAllWindows()
	
	return Vishwas
	
Toto = Pawan_Face_Recognition()
print(Toto)