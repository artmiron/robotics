This is test example with mqtt client on RaspberryPi 3.
Communication over mqtt trigers light on or light off diode.

Diode is connected to GPIO 21 (see example 01).

Running
1) Start program
> python mqtt.py

2) Connect to mqtt broker (browser with websocket or mosquitto client)
a) browser
eg. http://myrontech.pl/paho-mqtt.html
- server ip: rPi addr (192.168.0.108)
- port: 1884 (websocket) or 1883 (directly mqtt)
- topic: "World"
b) shell
or mosquitto client
- to listen
> mosquitto_sub -h 192.168.0.108 -t "World" -v
- to publish
> mosquitto_pub -h 192.168.0.108 -t "World" -m "Hello boyz"

3) Stering the diode light
- place number 0-9 to change diode light
