import RPi.GPIO as GPIO
class Motor(object):
	def __init__(self,directionPin,speedPin,directionForward):	
		self.directionPin=directionPin	#BCM-Pin
		self.speedPin=speedPin	#BCM-Pin
		self.directionForward=directionForward; 	#Enthaelt einen BOOL 
		self.changeSpeed(0)
		GPIO.setup(self.directionPin, GPIO.OUT)
		GPIO.setup(self.speedPin, GPIO.OUT)
		self.stop()
	def forward(self):
		GPIO.output(self.directionPin,self.directionForward)
		GPIO.output(self.speedPin,1)
	def backward(self):
		GPIO.output(self.directionPin,(not self.directionForward))
		GPIO.output(self.speedPin,1)
	def changeSpeed(self,speed):
		self.speed=speed
	def stop(self):
		GPIO.output(self.speedPin, 0)

