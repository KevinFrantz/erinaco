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
	core=AUTOPILOT()
	#core.start();
	while True:	
		try:	
			core.forward();
		except ForwardMoveException:
			if randint(0,1):			
				core.backward();
			else:
				if randint(0,1):
					core.turnLeft();				
				else:
					core.turnRight();
		except LeftMoveException:
			core.turnLeft();
		except RightMoveException:
			core.turnRight();
		sleep(0.5);
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
	}
	func = switcher.get(order, lambda: print("Der gewuenschte Befehl steht nicht zur Verfuegung"))
	return func();
print("Herzlich Willkommen im manuellen Controll-Interface!\n") 
try:	
	while True:
		input=getch.getch();
		print("Erinaco>>{0}".format(input))
		doIt(input);
except MoveException:
	print("Move Exception...")
except KeyboardInterrupt:
	print("Verlasse Erinaco...")
	core.__del__();
