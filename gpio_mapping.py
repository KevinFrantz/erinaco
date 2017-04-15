import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM);

def pinIt(pin,art,value,name):
	print("Pin {0:2}; Art {1:3};  Value: {2}; Name: {3}; ".format(pin,art,value,name));
def checkInput(pin,name):
	GPIO.setup(pin, GPIO.IN);
	pinIt(pin,"IN",GPIO.input(pin),name);
def output(pin,name):
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 0)
	pinIt(pin,'OUT','0',name);
print('--- Allgemeine Sensoren ---')
checkInput(19,"PIR")
checkInput(26,"DHT11")
print('--- Linetrackingsensoren (Erster Sensor-Fahrtrichtung-Rechts) ---');
checkInput(21,"IR-LT-1")
checkInput(20,"IR-LT-2")
checkInput(16,"IR-LT-3")
checkInput(12,"IR-LT-4")
print('--- Ultraschall-Abstanssensoren (Erster Sensor-Fahrtrichtung-Rechts) ---');
output(13,"UA-1-TRIGGER")
checkInput(22,"UA-1-ECHO")
output(6,"UA-2-TRIGGER")
checkInput(27,"UA-2-IN")
output(5,"UA-3-TRIGGER")
checkInput(17,"UA-3-IN")
print('--- Motorenbelegung ---');
output(23,"A-1A") #Grau
output(18,"A-1B") #Weiss
output(25,"B-1A") #Blau
output(24,"B-1B") #Lila
GPIO.cleanup();

