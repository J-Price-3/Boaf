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
file = open("results/"+now.strftime("%d-%m-%Y %H:%M:%S")+".csv", "w")
writer = csv.writer(file)
writer.writerow(["X", "Y", "PH", "TDS", "TURBIDITY"])
file.close()
#use increments of 0.1s
def Update(increment):
    
    phReader.Update(increment)
    tdsReader.Update(increment)
    turbidityReader.Update(increment)
    
    positionReader.Update(increment)

    BoafMovement.turny_boi(rudder, positionReader, pathfinder.currentNode)

    check = pathfinder.Update()
    if(check):
        file = open("results/"+now.strftime("%d-%m-%Y %H:%M:%S")+".csv", "w")
        writer.writerow([check[0], check[1], phReader.GetMovingAverage(), tdsReader.GetMovingAverage(), turbidityReader.GetMovingAverage()])
        file.close()


def Run():
    #### Do Measurements ####
    t = 0
    propeller.setSpeed(100)
    
    while not pathfinder.Done() and t <= 30:
        Update(0.1)
        t+=0.1

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
    rudder.update()
    print("rudder to 0")
    time.sleep(3)
    print("rudder to 90")
    rudder.setAngle(90)
    rudder.update()
    time.sleep(3)
    print("rudder to -90")
    rudder.setAngle(-90)
    rudder.update()
    time.sleep(3)

SystemCheck()
time.sleep(100)
Run()