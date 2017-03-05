#include <wiringPi.h>
#include <stdio.h>

int main(void)
{
        wiringPiSetupGpio();
	int pinDiode = 18;
        pinMode(pinDiode, OUTPUT);
	printf("The program has been started\n");

        for(;;)
        {
                digitalWrite(pinDiode, HIGH);
		printf("Diode ON\n");
                delay(15);
                digitalWrite(pinDiode, LOW);
		printf("Diode OFF\n");
                delay(2000);
        }

        return 0;
}
