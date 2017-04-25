﻿This is test example with mqtt client on RaspberryPi 3.
Communication over mqtt trigers light on or light off diode.

Diode is connected to GPIO 21 (see example 01).

Running
1) run program
> python mqtt.py
2) open mqtt client (browser with websocket or mosquitto client)
eg. http://myrontech.pl/paho-mqtt.html
- server ip: rPi addr (192.168.0.108)
- port: 1884 (websocket) or 1883 (directly mqtt)
- topic: "World"
3) commands
- place number 1-9 to change diode light
