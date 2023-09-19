import cv2,numpy as np,sys,re
def houghCircles(img):
	A=img;A=cv2.medianBlur(A,5);D=cv2.cvtColor(A,cv2.COLOR_GRAY2BGR)
	if re.compile('3*').match(cv2.__version__):B=cv2.HoughCircles(A,cv2.HOUGH_GRADIENT,1,20,param1=70,param2=50,minRadius=0,maxRadius=0)
	else:B=cv2.HoughCircles(A,cv2.cv.CV_HOUGH_GRADIENT,1,20,param1=70,param2=50,minRadius=0,maxRadius=0)
	if B!=None:
		B=np.uint16(np.around(B))
		for C in B[0,:]:cv2.circle(D,(C[0],C[1]),C[2],(0,255,0),2);cv2.circle(D,(C[0],C[1]),2,(0,0,255),3)
	return D
def eulerToCoordinateTransform(line):
	for(C,D)in line:A=np.cos(D);B=np.sin(D);E=A*C;F=B*C;G=int(E+1000*-B);H=int(F+1000*A);I=int(E-1000*-B);J=int(F-1000*A)
	return[(G,H),(I,J)]
def getIntersection(line_1,line_2):
	E=eulerToCoordinateTransform(line_1);F=eulerToCoordinateTransform(line_2);A=np.array(E[0]);G=np.array(E[1]);B=np.array(F[0]);H=np.array(F[1]);C=(A[1]-G[1])/(A[0]-G[0]);I=A[1]-C*A[0];D=(B[1]-H[1])/(B[0]-H[0]);K=B[1]-D*B[0]
	if abs(C-D)<sys.float_info.epsilon:return False
	J=(K-I)/(C-D);L=C*J+I;return J,L
def houghLines(img):
	B=img;H=cv2.cvtColor(B,cv2.COLOR_BGR2GRAY);I=cv2.Canny(H,50,150,apertureSize=3);A=cv2.HoughLines(I,1.75,np.pi/180,150)
	if A!=None:
		for D in A:
			for(J,K)in D:E=eulerToCoordinateTransform(D);cv2.line(B,E[0],E[1],(0,0,255),2)
		for C in range(len(A)):
			for F in range(C+1,len(A)):
				if getIntersection(A[C],A[F]):G=getIntersection(A[C],A[F]);cv2.circle(B,(G[0],G[1]),2,(0,255,0),3)
	return B
if __name__=='__main__':
	cap=cv2.VideoCapture(0)
	if not cap.isOpened():print('Exiting with state 1...');exit(1)
	while True:
		ret,frame=cap.read()
		if not ret:break
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);houghCircleImage=houghCircles(gray);houghLineImage=houghLines(houghCircleImage);cv2.imshow('Circles and Lines',houghLineImage)
		if cv2.waitKey(1)&255==ord('q'):break
	cv2.waitKey(0);cv2.destroyAllWindows()
