#include <wiringPi.h>
#include <stdio.h>

int main(void) {

	wiringPiSetupGpio();
	pinMode(16, INPUT);
	pullUpDnControl(16, PUD_UP);

	for (;;) {
		if(digitalRead(16) == LOW) {
			printf("Smile! ;)\n");
			system("raspistill -o /home/pi/Desktop/projects/02_camera/photo.jpg");
			printf("Photo was made\n");
		} 
	}
	return 0;

}
