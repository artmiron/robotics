#include <wiringPi.h>
#include <stdio.h>

int main(void)
{
        wiringPiSetupGpio();
        pinMode(21, OUTPUT);
	printf("The program has been started\n");

        for(;;)
        {
                digitalWrite(21, HIGH);
		printf("Diode ON\n");
                delay(500);
                digitalWrite(21, LOW);
		printf("Diode OFF\n");
                delay(500);
        }

        return 0;
}
