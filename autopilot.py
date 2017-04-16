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
from time import sleep 
class Autopilot(CORE):
	def __init__(self):
		CORE.__init__(self);
		self.moveStatus=0; 
		self.ultraschalminimum=10;
	def statusTest(self):
		switcher = {
			1: lambda: self.testForward(),
			3: lambda: self.testLeft(),
			4: lambda: self.testRight(),
		}
		func = switcher.get(self.moveStatus, lambda:"Error")
		return func();		
	def testLeft(self):
		if(self.ultraschallLinksValue<=self.ultraschalminimum or self.infarotLinks.getValue()):
			self.stop();					
			raise LeftMoveException("Abstand Ultraschall-Links betraegt {0}cm und Infarot-Links hat Wert {1}"
				.format(
					self.ultraschallLinksValue,
					self.infarotLinksValue
				)
			);
	def testRight(self):
		if(self.infarotMitteRechtsValue<=self.ultraschalminimum or self.infarotRechtsValue):
			self.stop();					
			raise RightMoveException("Abstand Ultraschall-Rechts betraegt {0}cm und Infarot-Rechts hat Wert {1}".
				format(
					self.infarotMitteRechtsValue,
					self.infarotRechtsValue
				)
			);
	def testForward(self):
		if(self.ultraschallMitteValue<=self.ultraschalminimum 
			or self.ultraschallRechtsValue<=self.ultraschalminimum 
			or self.ultraschallLinksValue<=self.ultraschalminimum 
			or self.infarotMitteLinksValue 
			or self.infarotMitteRechtsValue):
			self.stop();					
			raise ForwardMoveException("Abstand Ultraschallmitte betraegt {0}cm. Infarot-Mitte-Links: {1}. Infarot-Mitte-Rechts:{2}".
				format(
					self.ultraschallMitteValue,
					self.infarotMitteLinksValue,
					self.infarotMitteRechtsValue)
			);	
	def turnLeft(self):
		self.moveStatus=3;
		self.statusTest();
		CORE.turnLeft(self);
	def turnRight(self):
		self.moveStatus=4;
		self.statusTest();	
		CORE.turnRight(self);
	def forward(self):
		
		self.moveStatus=1;
		self.statusTest();		
		CORE.forward(self);
	def backward(self):
		self.moveStatus=2;		
		self.statusTest();
		CORE.backward(self);
	def stop(self):		
		self.moveStatus=0;
		self.statusTest();
		CORE.stop(self);
