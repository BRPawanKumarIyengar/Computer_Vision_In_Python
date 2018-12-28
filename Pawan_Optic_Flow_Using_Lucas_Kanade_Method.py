import cv2 as Pawan_Camera_Chitrature
import numpy as Pawan_Numpy_Module
import time as Samay_in_Seconds
import matplotlib.pyplot as Pawan_Plot
import pickle as Achaar
 
Chitra = Pawan_Camera_Chitrature.VideoCapture(0)
 
# Create old Chaaya
_, Chaaya = Chitra.read()
old_gray = Pawan_Camera_Chitrature.cvtColor(Chaaya, Pawan_Camera_Chitrature.COLOR_BGR2GRAY)
 
# Lucas kanade params
lk_params = dict(winSize = (15, 15),
                 maxLevel = 4,
                 criteria = (Pawan_Camera_Chitrature.TERM_CRITERIA_EPS | Pawan_Camera_Chitrature.TERM_CRITERIA_COUNT, 10, 0.03))
 
# Mouse function
def select_point(event, x, y, flags, params):
    global point, point_selected, Purva_Bindu
    if event == Pawan_Camera_Chitrature.EVENT_LBUTTONDOWN:
        point = (x, y)
        point_selected = True
        Purva_Bindu = Pawan_Numpy_Module.array([[x, y]], dtype=Pawan_Numpy_Module.float32)
 
Pawan_Camera_Chitrature.namedWindow("Pawan_Object_Track")
Pawan_Camera_Chitrature.setMouseCallback("Pawan_Object_Track", select_point)
 
point_selected = False
point = ()
Purva_Bindu = Pawan_Numpy_Module.array([[]])
while True:
    _, Chaaya = Chitra.read()
    gray_Chaaya = Pawan_Camera_Chitrature.cvtColor(Chaaya, Pawan_Camera_Chitrature.COLOR_BGR2GRAY)
 
    if point_selected is True:
        Pawan_Camera_Chitrature.circle(Chaaya, point, 5, (0, 0, 255), 2)
 
        new_points, status, error = Pawan_Camera_Chitrature.calcOpticalFlowPyrLK(old_gray, gray_Chaaya, Purva_Bindu, None, **lk_params)
        old_gray = gray_Chaaya.copy()
        Purva_Bindu = new_points
 
        x, y = new_points.ravel()
        Pawan_Camera_Chitrature.circle(Chaaya, (x, y), 5, (0, 255, 0), -1)
 
 
 
    Pawan_Camera_Chitrature.imshow("Pawan_Object_Track", Chaaya)
 
    if Pawan_Camera_Chitrature.waitKey(1) == 27:
        break
 
Chitra.release()
Pawan_Camera_Chitrature.destroyAllWindows()
