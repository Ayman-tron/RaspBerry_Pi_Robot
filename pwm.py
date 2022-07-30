import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Motor #1
GPIO.setup(3, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

# Motor #2
# PWM Pin 5
GPIO.setup(37, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

# Motor # 1
# Creating a PWM object
myPWM = GPIO.PWM(3, 100)
myPWM.ChangeDutyCycle(100)
# Pin 11 and 12 allow us to control the direction of the motor
GPIO.output(12, GPIO.LOW)
GPIO.output(11, GPIO.HIGH)

# Motor # 2
myPWM = GPIO.PWM(37, 100)
myPWM.ChangeDutyCycle(100)
GPIO.output(15, GPIO.HIGH)
GPIO.output(13, GPIO.LOW)

# Wait 2.5 seconds
time.sleep(2.5)

# Reset all the GPIO pins by setting them to LOW
GPIO.output(11, GPIO.LOW)
GPIO.output(12, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.LOW)

# Cleaning up the GPIO pin for next user
GPIO.cleanup()
