import RPi.GPIO as GPIO
from time import sleep
class Motor(object):
	def __init__(self,directionPin,speedPin,directionForward):	
		self.directionPin=directionPin	#BCM-Pin
		self.speedPin=speedPin	#BCM-Pin
		self.directionForward=directionForward; 	#Enthaelt einen BOOL 
		self.speed=0;
		GPIO.setup(self.directionPin, GPIO.OUT)
		GPIO.setup(self.speedPin, GPIO.OUT)
		GPIO.output(self.speedPin, 0)
		GPIO.output(self.directionPin, 0)
	def forward(self):
		self.stop()
		GPIO.output(self.directionPin,self.directionForward)
		GPIO.output(self.speedPin,(not self.directionForward))
	def backward(self):
		self.stop()
		GPIO.output(self.directionPin,(not self.directionForward))
		GPIO.output(self.speedPin,self.directionForward)
	def changeSpeed(self,speed):
		self.speed=speed
	def stop(self):
		GPIO.output(self.speedPin, 0)
		GPIO.output(self.directionPin, 0)
		sleep(0.02)
		

