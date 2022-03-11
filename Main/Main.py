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

pathfinder = BoafPathfinding.Pathfinder(positionReader, obstacleDetector)

rudder = BoafMovement.Rudder()
propeller = BoafMovement.Propellor()

#### Initialise ####


#create writing files#
now = datetime.now()
phFile = open("PH"+now.strftime("%d/%m/%Y %H:%M:%S")+".csv", "w")
phWriter = csv.writer(phFile)

tdsFile = open("TDS"+now.strftime("%d/%m/%Y %H:%M:%S")+".csv", "w")
tdsWriter = csv.writer(tdsFile)

turbidityFile = open("Turbidity"+now.strftime("%d/%m/%Y %H:%M:%S")+".csv", "w")
turbidityWriter = csv.writer(turbidityFile)
#/create writing files/#

done = False

#### /Initialise/ ####

#use increments of 0.1s
def Update(increment):
    
    phReader.Update(increment)
    tdsReader.Update(increment)
    turbidityReader.Update(increment)
    
    positionReader.Update(increment)

    BoafMovement.turny_boi(rudder, positionReader, pathfinder.currentNode)

    pathfinder.Update()


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
    while t < 10:
        positionReader.Update(0.1)
        time.sleep(0.1)
        t += 0.1
        if(t % 1 == 0):
            print("pos:" + positionReader.GetPosition())
            print("vel:" + positionReader.GetVelocity())
    input("enter to continue")
    print("testing sensors")
    t = 0
    while t < 10:
        phReader.Update(0.1)
        tdsReader.Update(0.1)
        turbidityReader.Update(0.1)
        time.sleep(0.1)
        t += 0.1
        if(t % 1 == 0):
            print("ph:" + phReader.GetMovingAverage())
            print("tds:" + tdsReader.GetMovingAverage()())
            print("turb:" + turbidityReader.GetMovingAverage()())
    input("enter to continue")
    print("testing laser")
    while t < 10:
        obstacleDetector.Update(0.1)
        time.sleep(0.1)
        t += 0.1
        if(t % 1 == 0):
            print("obstacle:" + obstacleDetector.valid)
    input("enter to continue")    

