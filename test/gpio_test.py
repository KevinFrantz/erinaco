import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM);
pin=0;
while pin<=40:
	GPIO.setup(pin, GPIO.IN);
	print("Pin {0}; Value {1};".format(pin,GPIO.input(pin)));
	pin += 1;
GPIO.cleanup();

