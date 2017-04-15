from time import sleep
import getch
from core import Core as CORE
core=CORE();
def doIt(order):
	switcher = {
        	'w': lambda: core.forward(),
        	's': lambda: core.backward(),
        	'd': lambda: core.turnRight(),
		'a': lambda: core.turnLeft(),
		' ': lambda: core.stop(),
		'i': lambda: core.printValues(),
	}
	func = switcher.get(order, "Der gewuenschte Befehl steht nicht zur Verfuegung")
	return func();
print("Herzlich Willkommen im manuellen Controll-Interface!") 
try:
	while True:
		input=getch.getch();
		print("Erinaco>>{0}".format(input))
		doIt(input);
except KeyboardInterrupt:
	print("Verlasse Erinaco...")
