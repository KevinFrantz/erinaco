#!/usr/bin/python3
import time
import RPi.GPIO as GPIO
class Ultraschall(object):
	def __init__(self,trigPin,echoPin):
		self.trigPin=trigPin
		self.echoPin=echoPin
		GPIO.setup(echoPin, GPIO.IN)
		GPIO.setup(trigPin, GPIO.OUT)
	def getValue(self):
    		GPIO.output(self.trigPin, True)
    		time.sleep(0.00001) # 10 Mikrosekunden
    		GPIO.output(self.trigPin, False)
    		while GPIO.input(self.echoPin) == 0:
        		pass
    		start = time.time()   
    		while GPIO.input(self.echoPin) == 1:
        		pass
    		ende = time.time()
    		return ((ende - start) * 34300) / 2
