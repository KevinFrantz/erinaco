"""
Autopilot-Klasse schmeisst Exceptions und stoppt Erinaco bei Fehlern

@author kf
@since 	2017-04-15

Status-Codes 
0: Stopp
1: Forward
2: Backward
3: Left
4: Right
"""

#Bewegungs-Exeptions:
class MoveException(Exception):	
	pass
class RightMoveException(MoveException):
	pass
class LeftMoveException(MoveException):
	pass
class ForwardMoveException(MoveException):
	pass

#Hauptklasse
from core import Core as CORE
from threading import Thread as THREAD
from time import sleep 
class Autopilot(CORE,THREAD):
	def __init__(self):
		CORE.__init__(self);
		THREAD.__init__(self);
		self.moveStatus=0; 
		self.ultraschalminimum=10;
		self.threadRun=True;
		#self.start();
	def run(self):
		x=1
		while self.threadRun:
			self.statusTest();
			print("Autopilot-Test #{0}".format(x));			
			#sleep(0.2);
			x+=1		
	def statusTest(self):
		switcher = {
			1: lambda: self.testForward(),
			3: lambda: self.testLeft(),
			4: lambda: self.testRight(),
		}
		func = switcher.get(self.moveStatus, lambda:0)
		return func();		
	def testLeft(self):
		ultraschallLinks=self.ultraschallLinks.getValue();
		if(ultraschallLinks<=self.ultraschalminimum or self.infarotLinks.getValue()):
			self.stop();					
			raise LeftMoveException("Abstand Ultraschall-Links betraegt {0}cm und Infarot-Links hat Wert {1}".format(ultraschallLinks,self.infarotLinks.getValue()));
	def testRight(self):
		ultraschallRechts=self.ultraschallRechts.getValue();
		if(ultraschallRechts<=self.ultraschalminimum or self.infarotRechts.getValue()):
			self.stop();					
			raise RightMoveException("Abstand Ultraschall-Rechts betraegt {0}cm und Infarot-Rechts hat Wert {1}".format(ultraschallRechts,self.infarotRechts.getValue()));
	def testForward(self):
		ultraschallMitte=self.ultraschallMitte.getValue();
		if(ultraschallMitte<=self.ultraschalminimum 
			or self.ultraschallRechts.getValue()<=self.ultraschalminimum 
			or self.ultraschallLinks.getValue()<=self.ultraschalminimum 
			or self.infarotMitteLinks.getValue() 
			or self.infarotMitteRechts.getValue()):
			self.stop();					
			raise ForwardMoveException("Abstand Ultraschallmitte betraegt {0}cm. Infarot-Mitte-Links: {1}. Infarot-Mitte-Rechts:{2}".format(ultraschallMitte,self.infarotMitteLinks.getValue(),self.infarotMitteRechts.getValue()));	
	def turnLeft(self):
		self.statusTest();
		self.moveStatus=3;
		CORE.turnLeft(self);
	def turnRight(self):
		self.statusTest();
		self.moveStatus=4;	
		CORE.turnRight(self);
	def forward(self):
		self.statusTest();
		self.moveStatus=1;		
		CORE.forward(self);
	def backward(self):
		self.statusTest();
		self.moveStatus=2;
		CORE.backward(self);
	def stop(self):
		self.statusTest();
		self.moveStatus=0;
		CORE.stop(self);
	def __del__(self):
		self.threadRun=False;
