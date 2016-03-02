import cv2
import numpy as np
import sys
from HoughLines import HoughLines
from HoughCircles import HoughCircles

'''

img = cv2.imread('/home/nikhil/Documents/Python Projects/CIrcle and Line Detection/Landing Pad.PNG', 0)

houghCircleImage = HoughCircles(img)
houghLineImage = HoughLines(houghCircleImage)

cv2.imshow('Circles and Lines', houghLineImage)	

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	houghCircleImage = HoughCircles(gray)
	houghLineImage = HoughLines(houghCircleImage)

	cv2.imshow('Circles and Lines', houghLineImage)	

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.waitKey(0)
cv2.destroyAllWindows()

