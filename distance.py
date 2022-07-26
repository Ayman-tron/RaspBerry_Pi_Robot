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
        # The Ultrasonic Transmitter in the Sensor generates a 40 KHz Ultrasound. In order to send the 40 KHz Ultrasound, the TRIG Pin of the
        # Ultrasonic Sensor must be held HIGH for a minimum duration of 10µS. After this, the Ultrasonic Transmitter, will transmits a burst of 8-pulses
        # of ultrasound at 40 KHz. Immediately, the control circuit in the sensor will change the state of the ECHO pin to HIGH. This pins stays HIGH
        # until the ultrasound hits an object and returns to the Ultrasonic Receiver. (source: https://www.electronicshub.org/raspberry-pi-ultrasonic-sensor-interface-tutorial/)
        time.sleep(1E-6)
        GPIO.output(trigPin, 0)

        while GPIO.input(echoPin) == 0:
            pass
        # Gives us the system time (starting the stopwatch)
        echoStartTime = time.time()
        while GPIO.input(echoPin) == 1:
            pass
        # Stopping the stopwatch
        echoStopTime = time.time()
        pingTravelTime = echoStopTime - echoStartTime

        distance = 34300 * (pingTravelTime/2)
        # Rounding to two decimal point
        print(round(distance, 2), 'cm')

        # sensor requires a delay before sending and receiving the ping
        time.sleep(0.2)

except KeyboardInterrupt():
    GPIO.cleanup()
    print("Cleanup successful")
