import gpiozero
import time

TRIG = 23
ECHO = 24

trigger = gpiozero.OutputDevice(TRIG)
echo = gpiozero.DigitalInputDevice(ECHO)

try:
    while True:
        trigger.on()
        # The Ultrasonic Transmitter in the Sensor generates a 40 KHz Ultrasound.
        # In order to send the 40 KHz Ultrasound, the TRIG Pin of the Ultrasonic Sensor must be held HIGH for a minimum duration of 10µS.
        # After this, the Ultrasonic Transmitter, will transmits a burst of 8-pulses of ultrasound at 40 KHz. Immediately, the control circuit in
        # the sensor will change the state of the ECHO pin to HIGH. This pins stays HIGH until the ultrasound hits an object
        # and returns to the Ultrasonic Receiver.
        time.sleep(0.00001)
        trigger.off()

        while echo.is_active == False:
            pulse_start = time.time()

        while echo.is_active == True:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = 34300 * (pulse_duration/2)

        round_distance = round(distance, 2)

        print(round_distance)
        time.sleep(.2)


except KeyboardInterrupt():
    GPIO.cleanup()
    print("Cleanup successful")
