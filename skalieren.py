from core import Core as CORE
import getch
import time
core=CORE()
core.setSensorValues()
core.printValues()
def trackTime():
	
	startTime=time.time();
	whileStatus=0
	while True:
		if core.infarotMitteRechts.getValue():
			if whileStatus==1:				
				print("Die ausfuehrzeit betraegt {0} Sekunden.".format(time.time()-startTime));				
				break;
		else:
			whileStatus=1;
print("Auswaehlen: Sekunden pro Meter(m) oder Sekunden pro turn...");
if(getch.getch()=='m'):
	core.forward();
	trackTime();
	core.stop();
else:
	core.turnRight();
	trackTime();
	core.stop();
			

