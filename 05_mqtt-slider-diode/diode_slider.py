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
    # print(msg.topic +": "+ msgStr)
    if  is_number(msgStr):
        percentValue = int(msgStr)
        if 0 <= percentValue <= 100:
            # light diode with int value 0-100
            light_diode(percentValue)

# light diode with value 0-100
def light_diode(percent):
    pwmDiode.start(percent)


def is_number(var):
    try:
        var = int(var)
        if var == int(var):
            return True
    except Exception:
        return False


############## Argument parser #################

parser = argparse.ArgumentParser(description='Light diode through MQTT.')
parser.add_argument('i', metavar='ip addr', help='IP address')
parser.add_argument('-p', metavar='port number', type=int,
                    default=1883, help='Port (default: 1883)')
parser.add_argument('-t', metavar='topic',
                    default='World', help='Topic name (default "World")')

args = parser.parse_args()

############# Execution section ###############

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#client.connect("192.168.0.108", 1883, 60)
client.connect(args.i, args.p, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
