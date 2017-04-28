import RPi.GPIO as GPIO
import sys
import paho.mqtt.client as mqtt
import argparse

GPIO.setmode(GPIO.BCM)

pinDiode = 21
frequentzy_hertz = 5

#GPIO.setwarnings(False)
GPIO.setup(pinDiode, GPIO.OUT)
pwmDiode = GPIO.PWM(pinDiode, frequentzy_hertz)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("World")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    msgStr = str(msg.payload)
    print(msg.topic +": "+ msgStr)
    # if (msgStr in steringNumb):
    #     light_diode(int(msgStr))
    if  is_number(msgStr):
        percentValue = int(msgStr)
        if 0 <= percentValue <= 100:
            # light diode with int value 0-100
            light_diode(percentValue)

# light diode with value 0-100
def light_diode(percent):
    print("setting light to "+ str(percent) +" percent")
    pwmDiode.start(percent)


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

# while True:
#     inputValue = raw_input('Type in a percent value to light diode: ')
#
#     if inputValue == 'x':
#         break
#     elif is_number(inputValue):
#         percentValue = int(inputValue)
#         if 0 <= percentValue <= 100:
# #            print("Servo moved to %s position" % (degrees))
#             print("Servo will set PWM to: %s" % percentValue)
#         else:
#             print("Warning! The value needs to be between 0-100")
#     else:
#         print("Warning! Please type in int or 'x' value to quit")
#
#     # new line
#     print("")
#
# print("Program ended")

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('i', metavar='ip addr', help='IP address')
parser.add_argument('-p', metavar='port number', type=int,
                    default=1883, help='Port (default: 1883)')
parser.add_argument('-t', metavar='topic',
                    default='World', help='Topic name (default "World")')

args = parser.parse_args()
print(args.p, args.t, args.i)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#client.connect("iot.eclipse.org", 1883, 60)
client.connect("192.168.0.108", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
