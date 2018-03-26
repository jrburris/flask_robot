# This is a init script that runs on boot to insure the motors / GPIO pins
# are in a safe state

import RPi.GPIO as GPIO


# set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
# Motors
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

# Set all motors to stop
GPIO.output(7, False)
GPIO.output(11, False)
GPIO.output(13, False)
GPIO.output(15, False)
