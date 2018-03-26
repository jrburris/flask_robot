import time
import motors


motors = motors.run_motors()

# current light status
status = motors.read_direction()
print('Motor status is: {}'.format(status))

print('Testing Motors (Ctrl-C to stop)...')
while True:

    motors.forward()
    print('Motor status is: {}'.format(motors.read_direction()))
    time.sleep(2)

    motors.reverse()
    print('Motor status is: {}'.format(motors.read_direction()))
    time.sleep(2)

    motors.spin_left()
    print('Motor status is: {}'.format(motors.read_direction()))
    time.sleep(2)

    motors.spin_right()
    print('Motor status is: {}'.format(motors.read_direction()))
    time.sleep(2)

    motors.stop()
    print('Motor status is: {}'.format(motors.read_direction()))
    time.sleep(4)
