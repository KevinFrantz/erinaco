"""
Klasse fuer Sensoren welche nur zwei Zustaende besitzen koennen
@author kf
@since 2017-04-15

"""
import RPi.GPIO as GPIO
class Boolsensor(object):
	def __init__(self,pin):
		self.pin=pin;
		GPIO.setup(self.pin, GPIO.IN)	
	def getValue(self):
		return GPIO.input(self.pin)
