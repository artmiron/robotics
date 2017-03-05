import RPi.GPIO as GPIO
import time, sys

GPIO.setmode(GPIO.BCM)

pinServo = 18
pinDiode = 21

#GPIO.setwarnings(False)
GPIO.setup(pinDiode, GPIO.OUT)
GPIO.setup(pinServo, GPIO.OUT)

frequentzy_hertz = 50
pwm = GPIO.PWM(pinServo, frequentzy_hertz)
pwmDiode = GPIO.PWM(pinDiode, frequentzy_hertz)

left_pos = 0.4
right_pos = 2.5
s_left_pos = 0.9
s_right_pos = 2
mid_pos = (right_pos - left_pos) / 2 + left_pos
positionList = [left_pos, mid_pos, right_pos, mid_pos]
ms_per_cycle = 1000 / frequentzy_hertz #20ms

'''for i in range(3):
	for position in positionList:
		duty_cycle_percentage = position * 100 / ms_per_cycle
		print("Position: "+ str(position))
		print("Duty cycle: "+ str(duty_cycle_percentage) +"\n")
		pwm.start(duty_cycle_percentage)
		time.sleep(5)

pwm.stop()
'''

steringChars = ['r','l','e','k','x']
steringNumb = ['1','2','3','4','5','6','7','8','9','10']

print("Usage:")
print("'r' - rotate right, 'l' - rotate left,")
print("'e' - small right, 'k' - small left")
print("[1..10] - rotate by number*10 range percentege")
print("'x' - exit program")
while 1:
	key = sys.stdin.read(1)

	if key in steringNumb:
		movement = 10*int(key)
		print("moving servo "+ str(movement))
		pwmDiode.start(movement)
		# pwm.start(movement)

	if key == 'r':
		GPIO.output(pinDiode,1)
		duty_cycle_percentage = right_pos * 100 / ms_per_cycle
		print("The R button was pressed - "+ str(duty_cycle_percentage))
		pwm.start(duty_cycle_percentage)

	if key == 'l':
		GPIO.output(pinDiode,0)
		duty_cycle_percentage = left_pos * 100 / ms_per_cycle
		print("The L button was pressed - "+ str(duty_cycle_percentage))
		pwm.start(duty_cycle_percentage)

	if key == 'e':
		duty_cycle_percentage = s_right_pos * 100 / ms_per_cycle
		print("The R button was pressed - "+ str(duty_cycle_percentage))
		pwm.start(duty_cycle_percentage)

	if key == 'k':
		duty_cycle_percentage = s_left_pos * 100 / ms_per_cycle
		print("The L button was pressed - "+ str(duty_cycle_percentage))
		pwm.start(duty_cycle_percentage)


	if key == 'x':
		print("Exit")
		break;


GPIO.cleanup()
