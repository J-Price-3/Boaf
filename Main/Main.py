import BoafSensors, BoafPosition, BoafMovement, BoafPathfinding
import csv
from datetime import datetime

phReader = BoafSensors.PhReader()
tdsReader = BoafSensors.TdsReader()
turbidityReader = BoafSensors.TurbidityReader()
#depthReader = BoafSensors.DepthReader()

positionReader = BoafPosition.PositionReader()

pathfinder = BoafPathfinding.Pathfinder(positionReader, depthReader)

rudder =BoafMovement.Rudder()

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

while not pathfinder.Done():
    Update(0.1)

####/Do Measurements/####



#### Return To Shore ####

#do something

####/Return To Shore/####
