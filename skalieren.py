from core import Core as CORE
import getch
import time
core=CORE()
core.setSensorValues()
core.printValues()
print("Zum fortfahren beliebige Taste druecken...");
getch.getch();
core.turnRight();
startTime=time.time();
whileStatus=0
while True:
	if core.infarotMitteRechts.getValue():
		if whileStatus==1:
			runTime=time.time()-startTime;			
			core.stop();
			break;
	else:
		whileStatus=1;	
print("Die ausfuehrzeit betraegt {0} Sekunden.".format(runTime));
			

