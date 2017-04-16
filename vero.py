"""
	Enthaelt die Klasse fuer die Sensoren
	@author kf
	@since 2017-04-15
"""
from sensoren.boolsensor import Boolsensor as BOOLSENSOR 
from sensoren.ultraschall import Ultraschall as ULTRASCHALL
import time
#from sensoren.dht11 import Dht11 as DHT11
class Vero(object):
	def __init__(self):
		self.pir=BOOLSENSOR(19);
		#self.dht=DHT11(26);
		#self.camera;
		self.ultraschallLinks=ULTRASCHALL(5,17);
		self.ultraschallMitte=ULTRASCHALL(6,27);
		self.ultraschallRechts=ULTRASCHALL(13,22);
		self.infarotLinks=BOOLSENSOR(12);
		self.infarotRechts=BOOLSENSOR(21);
		self.infarotMitteLinks=BOOLSENSOR(16);
		self.infarotMitteRechts=BOOLSENSOR(20);
		self.timestampValue=0;
	def printValues(self): 		
		#self.dht.setValues();
		print("PIR:			{0}".format(self.pirValue));
		#print("Temperatur:		{0}".format(self.dht.getTemperatur()));
		#print("Luftfeuchtigkeit:	{0}".format(self.dht.getLuftfeuchtigkeit()));
		print("Ultraschall-Links:	{0}cm".format(self.ultraschallLinksValue));
		print("Ultraschall-Mitte:	{0}cm".format(self.ultraschallMitteValue));
		print("Ultraschall-Rechts:	{0}cm".format(self.ultraschallRechtsValue));
		print("Infarot Links:		{0}".format(self.infarotLinksValue));
		print("Infarot Mitte-Links:	{0}".format(self.infarotMitteLinksValue));
		print("Infarot Mitte-Rechts:	{0}".format(self.infarotMitteRechtsValue));
		print("Infarot Rechts:		{0}".format(self.infarotRechtsValue));
	def saveToDB(self): #Speichert die Werte in der Datenbank
		pass
	def setSensorValues(self):
		if(time.time() >= self.timestampValue+1): #Werte maximal jede Sekunde abspeichern
			self.pirValue			= self.pir.getValue();
			self.infarotMitteLinksValue  	= self.infarotMitteLinks.getValue();
			self.infarotMitteRechtsValue 	= self.infarotMitteRechts.getValue();
			self.infarotLinksValue  	= self.infarotLinks.getValue();
			self.infarotRechtsValue  	= self.infarotRechts.getValue();
			self.ultraschallLinksValue	= self.ultraschallLinks.getValue();
			self.ultraschallMitteValue	= self.ultraschallMitte.getValue();
			self.ultraschallRechtsValue	= self.ultraschallRechts.getValue();
			self.timestampValue		= time.time();
