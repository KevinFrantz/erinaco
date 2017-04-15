import RPi.GPIO as GPIO
from motion import Motion as MOTION
"""
Diese Klasse stellt alle Core-Funktionen (Aktoren, Sensoren) fuer den Erinaco Roboter zur Verfuegung. 
@author kf
@since 2017-04-15
"""
class Core(MOTION):
	def __init__(self):
		GPIO.setmode(GPIO.BCM);
		MOTION.__init__(self);
	def __del__(self):
		GPIO.cleanup();
