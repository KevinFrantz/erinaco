from time import sleep
#from core import Core as CORE
#core=CORE();
#core.backward()               

from aktoren.motor import Motor as MOTOR
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#motorLeft=MOTOR(23,18,1) #Initialisierung des linken Motors
motorRight=MOTOR(24,25,0) #Initialisierung des rechten Motors
motorRight.forward()
GPIO.cleanup();

sleep(5)
