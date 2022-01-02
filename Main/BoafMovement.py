import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)

class Rudder:
    def __init__(self):
        self.rudder = GPIO.PWM(33, 50)
        self.duty = 0
        self.setAngle(0)
        self.rudder.start(0)
        self.update()
    
    def setAngle(self, angle):
        self.duty = angle/20 + 7.5
    
    def update(self):
        self.rudder.ChangeDutyCycle(self.duty)

    def endRudder(self):
        self.rudder.stop()
        GPIO.cleanup()

rudder = Rudder()