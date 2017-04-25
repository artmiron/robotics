import RPi.GPIO as GPIO
import sys
import paho.mqtt.client as mqtt

GPIO.setmode(GPIO.BCM)

pinDiode = 21
frequentzy_hertz = 5

#GPIO.setwarnings(False)
GPIO.setup(pinDiode, GPIO.OUT)
pwmDiode = GPIO.PWM(pinDiode, frequentzy_hertz)

steringNumb = ['0','1','2','3','4','5','6','7','8','9']

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
#    client.subscribe("$SYS/#")
    client.subscribe("World")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    msgStr = str(msg.payload)
    print(msg.topic +": "+ msgStr)
    if (msgStr in steringNumb):
        light_diode(int(msgStr))

def light_diode(freq):
    movement = 11*int(freq)
    print("setting light to "+ str(movement) +" percent")
    pwmDiode.start(movement)


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
