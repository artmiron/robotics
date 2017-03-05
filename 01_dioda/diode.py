import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)

pinDiode = 21
frequentzy_hertz = 50

#GPIO.setwarnings(False)
GPIO.setup(pinDiode, GPIO.OUT)
pwmDiode = GPIO.PWM(pinDiode, frequentzy_hertz)

steringNumb = ['0','1','2','3','4','5','6','7','8','9']

print("Type in number [0..9] to light the diode")
print("'x' - exit program")

while 1:
	key = sys.stdin.read(1)

	if key in steringNumb:
		movement = 11*int(key)
		print("setting light to "+ str(movement) +" percent")
		pwmDiode.start(movement)

	if key == 'x':
		print("Exit")
		break;


GPIO.cleanup()
