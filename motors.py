import threading
import RPi.GPIO as GPIO
import os  # added so we can shut down OK
import time  # import time module
import curses

motor_direction = 'Stop'


class run_motors():
    """ A class to control the motors """

    def __init__(self):
        # set GPIO numbering mode and define output pins
        GPIO.setmode(GPIO.BOARD)
        # Motors
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)
        # Lights

        GPIO.setup(29, GPIO.OUT)
        # Create a lock to syncronize access to hardware from multiple threads.
        self._lock = threading.Lock()

    def read_direction(self):
        """ read the global variable motor_direction """
        global motor_direction
        with self._lock:
            return motor_direction

    def forward(self):
        """ Move both motors forward """
        global motor_direction
        with self._lock:
            GPIO.output(7, True)
            GPIO.output(11, False)
            GPIO.output(13, True)
            GPIO.output(15, False)
            # time.sleep(sec)
            motor_direction = 'Forward'
            return motor_direction

    def reverse(self):
        """ Move both motors backwards """
        global motor_direction
        with self._lock:
            GPIO.output(7, False)
            GPIO.output(11, True)
            GPIO.output(13, False)
            GPIO.output(15, True)
            # time.sleep(sec)
            motor_direction = 'Reverse'
            return motor_direction

    def spin_right(self):
        """ Rotate to the right """
        global motor_direction
        with self._lock:
            GPIO.output(7, False)
            GPIO.output(11, True)
            GPIO.output(13, True)
            GPIO.output(15, False)
            # time.sleep(sec)
            motor_direction = 'Spin Right'
            return motor_direction

    def spin_left(self):
        """ Rotate to the left """
        global motor_direction
        with self._lock:
            GPIO.output(7, True)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, True)
            # time.sleep(sec)
            motor_direction = 'Spin Left'
            return motor_direction

    def stop(self):
        global motor_direction
        with self._lock:
            GPIO.output(7, False)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, False)
            motor_direction = 'Stop'
            return motor_direction
