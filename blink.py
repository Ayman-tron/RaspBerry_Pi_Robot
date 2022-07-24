import RPi.GPIO as GPIO
import time
# Using the Raspberry Pi's Board Pin
GPIO.setmode(GPIO.BOARD)
# Setting GPIO Pin 11 on the Raspberry Pi as the Output
GPIO.setup(11, GPIO.OUT)

continue_processing = True

while continue_processing:

    x = int(input("Please enter the number of time you wamt the LED to blink "))

    for i in range(x):
        GPIO.output(11, True)
        time.sleep(0.3)
        GPIO.output(11, False)
        time.sleep(0.3)
    y = int(input("Do you wish to continue, Enter 1 to continue or 0  to exit "))
    if y == 1:
        continue_processing = True
    else:
        continue_processing = False
# To clean up the port used
GPIO.cleanup()
