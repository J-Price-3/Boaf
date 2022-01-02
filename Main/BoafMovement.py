import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(37, GPIO.OUT)
rudder = GPIO.PWM(37, 50)
rudderDuty = 2
rudder.start(0)
time.sleep(2)
while rudderDuty <= 12:
    rudder.ChangeDutyCycle(rudderDuty)
    time.sleep(1)
    rudderDuty += 1

time.sleep(1)

rudder.ChangeDutyCycle(2)
