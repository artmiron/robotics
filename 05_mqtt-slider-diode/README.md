# Steering diode light by MQTT/Websocket jQuery slider

﻿This is upgraded version of 04 project.
Added jQuery slider which steers diode light.

## Running

1. Run python program
* run diode_slider.py
* optionally to watch communication logs
```
> mosquitto_sub -h 192.168.0.108 -t "World" -v
```
2. Open html page with Websocket and connect to Mosquitto
3. Slide and enjoy changing diode light intensity
