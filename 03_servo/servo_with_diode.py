import RPi.GPIO as GPIO
import time, sys


def is_number(var):
    try:
        var = int(var)
        if var == int(var):
            return True
    except Exception:
        return False


# convert degrees value (0-180) intu Duty Cycle compatybile with PWM
def convertToDutyCycle( param ):
    leftPos = 2.5 		# min duty cycle %
    rightPos = 11.3 	# max duty cycle %
	# other documetns say about values between 5 and 10 %

    servoRangeDegr = 180
    rangeDutyCycle = rightPos - leftPos

    dutyCycle = (param / float(servoRangeDegr)) * rangeDutyCycle + leftPos

    return dutyCycle;


GPIO.setmode(GPIO.BCM)

pinServo = 18
pinDiode = 21

#GPIO.setwarnings(False)
GPIO.setup(pinDiode, GPIO.OUT)
GPIO.setup(pinServo, GPIO.OUT)

frequentzy_hertz = 50
pwm = GPIO.PWM(pinServo, frequentzy_hertz)
pwmDiode = GPIO.PWM(pinDiode, frequentzy_hertz)

while True:
    inputValue = raw_input('Type in a number of degree to move servo: ')

    if inputValue == 'x':
        break
    elif is_number(inputValue):
        degrees = int(inputValue)
        if 0 <= degrees <= 180:
			dutyCycle = convertToDutyCycle( degrees )
			print("Servo will set PWM to: %s" % (dutyCycle))
			pwm.start(dutyCycle)
			# duty cycle for Diode convertion 0-100 %
			pwmDiode.start(degrees*10/18)
        else:
            print("Warning! The value needs to be between 0-180")
    else:
        print("Warning! Please type in int or 'x' value")

    # new line
    print("")

GPIO.cleanup()
print("Program ended")
