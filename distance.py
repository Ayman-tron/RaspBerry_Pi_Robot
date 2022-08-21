import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

trigPin = 16
echoPin = 18

GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

try:
    while True:
        GPIO.output(trigPin, 1)
        # Sleep for 2 micro seconds
        time.sleep(1E-6)
        GPIO.output(trigPin, 0)
        while GPIO.input(echoPin) == 0:
            pass
        # Gives me the system time
        echoStartTime = time.time()
        while GPIO.input(echoPin) == 1:
            pass
        echoStopTime = time.time()
        pingTravelTime = echoStopTime - echoStartTime
        # Reporting the number in milli seconds
        distance = 34300 * (pingTravelTime/2)
        # Rounding to one decimal point
        print(round(distance, 2), 'cm')

        # sensor required a delay before sending and receiving the ping
        time.sleep(0.2)

except KeyboardInterrupt():
    GPIO.cleanup()
    print("Cleanup successful")
