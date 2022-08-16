import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
# Motor #1
# PWM Pin 3
GPIO.setup(3, GPIO.OUT)
# Pin 11 and 12 allow us to control the direction of the Motor 1
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

# Motor #2
# PWM Pin 5
# Pin 13 and 15 allow us to control the direction of the Motor 1
GPIO.setup(5, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


def main():
    forward()
    forward()
 # Reset all the GPIO pins by setting them to LOW


def reset():
    # Cleaning up the GPIO pin for next user
    GPIO.cleanup()

# Both motors are rotating forward


def forward():
    # Motor # 1
    # Creating a PWM object
    myPWM = GPIO.PWM(3, 100)
    myPWM.start(50)

    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.LOW)

    # Motor # 2
    myPWM2 = GPIO.PWM(5, 100)
    myPWM2.start(50)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.HIGH)

    # Wait 5 seconds
    time.sleep(5)

    reset()


def right():
    # Motor # 1
    # Creating a PWM object
    myPWM = GPIO.PWM(3, 100)
    myPWM.start(50)

    # Pin 11 and 12 allow us to control the direction of the motor
    GPIO.output(12, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)

    # Motor # 2
    myPWM2 = GPIO.PWM(5, 100)
    myPWM2.start(50)

    GPIO.output(15, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)

    # Wait 2.5 seconds
    time.sleep(0.5)

    reset()


main()
