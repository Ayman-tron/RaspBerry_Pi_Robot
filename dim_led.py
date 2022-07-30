import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)

# Creating a PWM object, first argument is pin number and second argument is frequency.
myPWM = GPIO.PWM(37, 100)
# Setting up a 50% duty cyle below
# myPWM.start(50)
# myPWM.stop(50)

# Better to use the ChangeDutyCycle function as per below instead of using the two functions above
myPWM.ChangeDutyCycle(75)


# Difference b/n Duty Cycle and Frequency
#  The duty cycle describes the amount of time the signal is in a high (on) state as a percentage of the total time of it takes to
# complete one cycle. The frequency determines how fast the PWM completes a cycle (i.e. 1000 Hz would be 1000 cycles per second), and
# therefore how fast it switches between high and low states.
myPWM.ChangeFrequency(200)

GPIO.cleanup()
