import BoafSensors, BoafPosition, BoafMovement, BoafPathfinding
import csv
from datetime import datetime
import RPi.GPIO as GPIO

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



#### Do Measurements ####

propeller.setSpeed(100)

while not pathfinder.Done():
    Update(0.1)

####/Do Measurements/####

propeller.stop()