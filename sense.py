import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

trigPin = 16
echoPin = 18

# Sending signals to the trigger Pin and reading from the
# Echo pin
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

try:
    # Sending a ping and then see how long it takes to get the
    # echo back to get the relflection back from the Target
    # If the echo is small it should be a smaller number and if the
    # echo is large it will be further away.
    while True:
        GPIO.output(trigPin, GPIO.LOW)
        # Sleep for 2 micro seconds
        time.sleep(2E-6)
        GPIO.output(trigPin, GPIO.HIGH)
        time.sleep(10E-6)
        GPIO.output(trigPin, GPIO.LOW)
        while GPIO.input(echoPin) == 0:
            pass

        # Gives me the system time
        echoStartTime = time.time()
        while GPIO.input(echoPin) == 1:
            pass
        echoStopTime = time.time()
        pingTravelTime = echoStopTime - echoStartTime
        # Reporting the number in milli seconds
        print(int(pingTravelTime*1E6))
        time.sleep(.2)
except KeyboardInterrupt():
    GPIO.cleanup()
    print("Cleanup successful")
