import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Motor #1
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

# Motor #2
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.output(12, GPIO.HIGH)
GPIO.output(11, GPIO.LOW)

time.sleep(5)

# Stopping all motors
GPIO.output(11, GPIO.LOW)
GPIO.output(12, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.LOW)
