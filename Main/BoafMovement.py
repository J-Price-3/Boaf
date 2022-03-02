import RPi.GPIO as GPIO
import time, math

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

def dot(v1,v2):
    theta=math.acos((v1[0]*v2[0]+v1[1]*v2[1])/math.sqrt((v1[0]**2+v1[1]**2)*(v2[0]**2+v2[1]**2)))
    return theta

def turny_boi(rudder, posReader, nextNode):#vectors are of form x,y       current and target are the velocity vector and then the velocity that it must become
    target = [nextNode[0] - posReader.GetPosition()[0], nextNode[0] - posReader.GetPosition()[0]]

    pleft=[-posReader.GetVelocity()[1],posReader.GetVelocity()[0]]#perpendicular vectors left and right
    pright=[posReader.GetVelocity()[1],-posReader.GetVelocity()[0]]

    left=dot(pleft,target)
    right=dot(pright,target)

    if left<right and (right-left) > 0.08:
        rudder.setAngle(-70)

    if right>left and (left-right) > 0.08:
        rudder.setAngle(70)
