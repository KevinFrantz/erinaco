"""
	Enthaelt die Klasse fuer die Sensoren
	@author kf
	@since 2017-04-15
"""
from sensoren.boolsensor import Boolsensor as BOOLSENSOR 
class Vero(object):
	def __init__(self):
		self.pir=BOOLSENSOR(19);
		#self.dht;
		#self.camera;
		#self.ultraschallLinks;
		#self.ultraschallMitte;
		#self.ultraschallRechts;
		self.infarotLinks=BOOLSENSOR(12);
		self.infarotRechts=BOOLSENSOR(21);
		self.infarotMitteLinks=BOOLSENSOR(16);
		self.infarotMitteRechts=BOOLSENSOR(20);
	def printValues(self):
		print("PIR:              {0}".format(self.pir.getValue()));
		#print("Temperatur:       {0}".format(self.dht.getTemperatur()));
		#print("Luftfeuchtigkeit: {0}".format(self.dht.getLuftfeuchtigkeit()));
                #print("PIR:              {0}".format(self.ultraschallLinks.getValue()));
                #	self.ultraschallMitte.getValue();
                #	self.ultraschallRechts.getValue();
		print("Infarot Links:    {0}".format(self.infarotLinks.getValue()));
		print("Infarot Mitte-Links:   {0}".format(self.infarotMitteLinks.getValue()));
		print("Infarot Mitte-Rechts:   {0}".format(self.infarotMitteRechts.getValue()));
		print("Infarot Rechts:   {0}".format(self.infarotRechts.getValue()));
	def saveToDB(self): #Speichert die Werte in der Datenbank
		pass

