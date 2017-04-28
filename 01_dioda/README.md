# Diode lighting

This is simple test with lighting Diode connected to RaspberryPi 3.

Diode is connected do GPIO 21

## Elements used:
* diode (green ;) )
* resistor 100 Ohm
* aditional and optional (Pyta stykowa 830, tasma z adapterem)

## Running

1. After any change first You need to compile your C file, eg.:
```
> gcc -o diode dioda.c -l wiringPi
```
output file is diode
2. After compiling you can run the program
```
> sudo ./diode
```
