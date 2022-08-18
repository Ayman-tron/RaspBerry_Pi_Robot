import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

trigPin = 23
echoPin = 24

GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

try:
    while True:
        GPIO.output(trigPin, 0)
        # Sleep for 2 micro seconds
        time.sleep(2E-6)
        GPIO.output(trigPin, 1)
        time.sleep(10E-6)
        GPIO.output(trigPin, 0)
        while GPIO.input(echoPin) == 0:
            pass
        # Gives me the system time
        echoStartTime = time.time()
        while GPIO.input(echoPin) == 1:
            pass
        echoStopTime = time.time()
        pingTravelTime = echoStopTime - echoStartTime
        speed_of_sound = 16/pingTravelTime*(3600)/(12*5280)
        print('Speed', speed_of_sound)

except KeyboardInterrupt():
    GPIO.cleanup()
    print("Cleanup successful")
