import Adafruit_DHT
class Dht11(object):
	def __init__(self,pin):
		self.pin = pin;
	def setValues(self):
		self.humidity, self.temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, self.pin)
	def getLuftfeuchtigkeit(self):
		return self.humidity;
	def getTemperatur(self):
		return self.temperature;		
	
