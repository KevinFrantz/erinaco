import RPi.GPIO as GPIO
import time

SENSOR_PIN = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

try:
	while True:
		if GPIO.input(SENSOR_PIN):
			print('Es gab eine Bewegung!')
		else:
			print('Es gab KEINE Bewegung!')
		time.sleep(1)
except KeyboardInterrupt:
	print("Beende...")
GPIO.cleanup()

