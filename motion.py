from aktoren.motor import Motor as MOTOR
from time import sleep;
"""
Diese Klasse stellt alle Motion-Funktionen fuer den Erinaco Roboter zur Verfuegung.
@author kf
@since 2017-04-15
"""
class Motion(object):
	def __init__(self):
		self.motorRight=MOTOR(23,18,1) #Initialisierung des linken Motors
		self.motorLeft=MOTOR(24,25,0) #Initialisierung des rechten Motors
		self.FULLTURNTIME=4.5; #Dauer welche fuer eine 360 Grad wendebenoetigt wird in Sekunden        
		self.SEKPERMETER=6.9;
	def turnLeft(self):
		self.motorRight.forward()
		self.motorLeft.backward()
	def turnRight(self):
		self.motorRight.backward()
		self.motorLeft.forward()
	def forward(self):
		self.motorRight.forward()
		self.motorLeft.forward()
	def backward(self):
		self.motorRight.backward()
		self.motorLeft.backward()
	def stop(self):
		self.motorRight.stop()
		self.motorLeft.stop()
	def runCm(self,cm):
		if cm<0:
			self.backward();
			cm=cm*-1;		
		else:
			self.forward();
		sleep((self.SEKPERMETER/100)*cm);
		self.stop();
	def turnDegree(self,degree):
		if degree<0:
			self.turnLeft();
			degree=degree*-1;		
		else:
			self.turnRight();
		sleep((self.FULLTURNTIME/360)*degree);
		self.stop();
