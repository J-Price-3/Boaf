from turtle import pos, position
import BoafSensors, BoafPosition, BoafMovement, BoafPathfinding
import csv
from datetime import datetime
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

phReader = BoafSensors.PhReader()
tdsReader = BoafSensors.TdsReader()
turbidityReader = BoafSensors.TurbidityReader()
obstacleDetector = BoafSensors.ObstacleDetector()

positionReader = BoafPosition.PositionReader()
positionReader.Update(0.6)
positionReader.centre = (positionReader.latitude, positionReader.longitude)

pathfinder = BoafPathfinding.Pathfinder(positionReader, obstacleDetector)

rudder = BoafMovement.Rudder()
propeller = BoafMovement.Propellor()

now = datetime.now()
file = open("results/"+now.strftime("%d-%m-%Y %H:%M:%S")+"/results.csv", "w")
writer = csv.writer(file)
writer.writerow(["X", "Y", "PH", "TDS", "TURBIDITY"])

#use increments of 0.1s
def Update(increment):
    
    phReader.Update(increment)
    tdsReader.Update(increment)
    turbidityReader.Update(increment)
    
    positionReader.Update(increment)

    BoafMovement.turny_boi(rudder, positionReader, pathfinder.currentNode)

    check = pathfinder.Update()
    if(check):
        writer.writerow([check[0], check[1], phReader.GetMovingAverage(), tdsReader.GetMovingAverage(), turbidityReader.GetMovingAverage()])


def Run():
    #### Do Measurements ####

    propeller.setSpeed(100)

    while not pathfinder.Done():
        Update(0.1)

    ####/Do Measurements/####
    propeller.stop()

def SystemCheck():
    print("motor running")
    propeller.setSpeed(100)
    time.sleep(1)
    propeller.setSpeed(0)
    print("motor stopped")
    input("enter to continue")
    rudder.setAngle(0)
    print("rudder to 0")
    time.sleep(3)
    print("rudder to 90")
    rudder.setAngle(90)
    time.sleep(3)
    print("rudder to -90")
    rudder.setAngle(-90)
    time.sleep(3)
    input("enter to continue")
    print("testing positon reader")
    t = 0
    while t < 100:
        positionReader.Update(0.1)
        time.sleep(0.1)
        t += 1
        if(t % 10 == 0):
            print("pos:" + str(positionReader.GetPosition()))
            print("vel:" + str(positionReader.GetVelocity()))
    input("enter to continue")
    print("testing sensors")
    t = 0
    while t < 100:
        phReader.Update(0.1)
        tdsReader.Update(0.1)
        turbidityReader.Update(0.1)
        time.sleep(0.1)
        t += 1
        if(t % 10 == 0):
            print("ph:" + str(phReader.GetMovingAverage()))
            print("tds:" + str(tdsReader.GetMovingAverage()))
            print("turb:" + str(turbidityReader.GetMovingAverage()))
    input("enter to continue")
    print("testing laser")
    t=0
    while t < 100:
        obstacleDetector.Update(0.1)
        time.sleep(0.1)
        t += 1
        if(t % 10 == 0):
            print("obstacle:" + str(obstacleDetector.valid))
    input("enter to continue")    

Run()