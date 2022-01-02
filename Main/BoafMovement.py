import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)

class Rudder:
    def __init__(self):
        self.rudder = GPIO.PWM(37, 50)
        self.duty = 7
        self.rudder.start()
        self.rudder.ChangeDutyCycle(self.duty)
    
    def setAngle(self, angle):
        self.duty = angle/18 + 7
    
    def update(self):
        self.rudder.ChangeDutyCycle(self.duty)

rudder = Rudder()

rudder.update()
time.sleep(5)
rudder.setAngle(90)
rudder.update()
time.sleep(5)
rudder.setAngle(-69)
time.sleep(5)

rudder.rudder.stop()
GPIO.cleanup()
