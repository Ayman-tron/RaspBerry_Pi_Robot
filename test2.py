import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


# Motor #2
# PWM Pin 5
GPIO.setup(5, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

# Motor # 2
myPWM = GPIO.PWM(5, 100)
myPWM.ChangeDutyCycle(50)
GPIO.output(15, GPIO.HIGH)
GPIO.output(13, GPIO.LOW)

# Wait 2.5 seconds
time.sleep(2.5)

# Reset all the GPIO pins by setting them to LOW
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.LOW)

# Cleaning up the GPIO pin for next user
GPIO.cleanup()
