"""
	Enthaelt die Klasse fuer die Sensoren
	@author kf
	@since 2017-04-15
"""
from sensoren.boolsensor import Boolsensor as BOOLSENSOR 
from sensoren.ultraschall import Ultraschall as ULTRASCHALL
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
	def printValues(self):
		#self.dht.setValues();
		print("PIR:			{0}".format(self.pir.getValue()));
		#print("Temperatur:		{0}".format(self.dht.getTemperatur()));
		#print("Luftfeuchtigkeit:	{0}".format(self.dht.getLuftfeuchtigkeit()));
		print("Ultraschall-Links:	{0}cm".format(self.ultraschallLinks.getValue()));
		print("Ultraschall-Mitte:	{0}cm".format(self.ultraschallMitte.getValue()));
		print("Ultraschall-Rechts:	{0}cm".format(self.ultraschallRechts.getValue()));
		print("Infarot Links:		{0}".format(self.infarotLinks.getValue()));
		print("Infarot Mitte-Links:	{0}".format(self.infarotMitteLinks.getValue()));
		print("Infarot Mitte-Rechts:	{0}".format(self.infarotMitteRechts.getValue()));
		print("Infarot Rechts:		{0}".format(self.infarotRechts.getValue()));
	def saveToDB(self): #Speichert die Werte in der Datenbank
		pass

