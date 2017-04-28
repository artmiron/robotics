import sys
import argparse

def is_number(var):
    try:
        var = int(var)
        if var == int(var):
            return True
    except Exception:
        return False


# convert degrees value (0-180) intu Duty Cycle compatybile with PWM
def convertToDutyCycle( param ):
    leftPos = 5
    rightPos = 10

    servoRangeDegr = 180
    rangeDutyCycle = rightPos - leftPos

    dutyCycle = (param / float(servoRangeDegr)) * rangeDutyCycle + leftPos

    return dutyCycle;



parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('i', metavar='ip addr', help='IP address')
parser.add_argument('-p', metavar='port number', type=int,
                    default=1883, help='Port (default: 1883)')
parser.add_argument('-t', metavar='topic',
                    default='World', help='Topic name (default "World")')

args = parser.parse_args()
print(args.p, args.t, args.i)

while True:
    inputValue = raw_input('Type in a number of degree to move servo: ')

    if inputValue == 'x':
        break
    elif is_number(inputValue):
        degrees = int(inputValue)
        if 0 <= degrees <= 180:
#            print("Servo moved to %s position" % (degrees))
            print("Servo will set PWM to: %s" % (convertToDutyCycle( degrees )))
        else:
            print("Warning! The value needs to be between 0-180")
    else:
        print("Warning! Please type in int or 'x' value")

    # new line
    print("")

print("Program ended")
