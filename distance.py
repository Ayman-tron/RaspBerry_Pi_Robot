from turtle import distance
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

trigPin = 23
echoPin = 24

GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

try:
    for i in range(20):
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
        # Reporting the number in milli seconds
        distance = 34300 * (pingTravelTime/2)
        # Rounding to one decimal point
        print(round(distance, 1), ' Inches')
        average = distance + average
        # sensor required a delay before sending and receiving the ping
        time.sleep(0.2)
    print("The average is: ", average)
except KeyboardInterrupt():
    GPIO.cleanup()
    print("Cleanup successful")
