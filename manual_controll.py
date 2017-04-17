from time import sleep
import getch
from core import Core as CORE
from autopilot import Autopilot as AUTOPILOT
from autopilot import MoveException,RightMoveException,LeftMoveException,ForwardMoveException
from random import randint
core=CORE();
#Enthaelt die Hilfe
def help():
	print("MOTION:")
	print("Forward:  w");
	print("Backward: s");
	print("Left:     a");
	print("Right:    d");
	print("Stop:     Space\n")
	print("GENERAL:")
	print("Help:	 h\n");
	print("MODE:")
	print("Automatisch:     q")
	print("Halbautomatisch: w")
	print("Manuell:         e")
def autopilot():
	try:
		autopilot=AUTOPILOT()
		while True:						
			try:			
				try:	
					autopilot.setSensorValues();
					autopilot.printValues();
					print("Richtung: {0}".format(autopilot.moveStatus));			
					if autopilot.moveStatus!=1:			
						autopilot.forward();
					else:
						autopilot.statusTest();
				except ForwardMoveException:				
					if randint(0,1):			
						autopilot.backward();
					else:
						if randint(0,1):
							autopilot.turnLeft();				
						else:
							autopilot.turnRight();
				except LeftMoveException:
					core.turnLeft();
				except RightMoveException:
					core.turnRight();
			except MoveException:
				autopilot.stop();
			sleep(0.5);
	except KeyboardInterrupt:
		print("Verlasse Autopilot...")
def doIt(order):
	switcher = {
        	'w': lambda: core.forward(),
        	's': lambda: core.backward(),
        	'd': lambda: core.turnRight(),
		'a': lambda: core.turnLeft(),
		' ': lambda: core.stop(),
		'i': lambda: core.printValues(),
		'h': lambda: help(),
		'q': lambda: autopilot(),
		'x': lambda: core.turnDegree(int(input("Grad:"))),
		'w': lambda: core.runCm(int(input("cm:"))),
	}
	func = switcher.get(order, lambda: print("Der gewuenschte Befehl steht nicht zur Verfuegung"))
	return func();
print("Herzlich Willkommen im manuellen Controll-Interface!\n") 
try:	
	while True:
		core.setSensorValues()
		modus=getch.getch();
		print("Erinaco>>{0}".format(modus))		
		doIt(modus);
except KeyboardInterrupt:
	print("Verlasse Erinaco...")
	core.__del__();
