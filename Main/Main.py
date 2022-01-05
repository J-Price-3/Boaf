import BoafSensors, BoafPosition, BoafMovement, BoafPathfinding
import csv
from datetime import datetime

phReader = BoafSensors.phReader()
tdsReader = BoafSensors.tdsReader()
turbidityReader = BoafSensors.turbidityReader()

positionReader = BoafPosition.PositionReader()




#### Initialise ####

#set centre of lake
#positionReader.centre = get lake reference coords


#create writing files#
now = datetime.now()
phFile = open("PH"+now.strftime("%d/%m/%Y %H:%M:%S")+".csv", "w")
phWriter = csv.writer(phFile)

tdsFile = open("TDS"+now.strftime("%d/%m/%Y %H:%M:%S")+".csv", "w")
tdsWriter = csv.writer(tdsFile)

turbidityFile = open("Turbidity"+now.strftime("%d/%m/%Y %H:%M:%S")+".csv", "w")
turbidityWriter = csv.writer(turbidityFile)
#/create writing files/#

#set start node
#nextNode = pathfinder.getnextnode or something

done = False

#### /Initialise/ ####

#use increments of 0.1s
def Update(increment):
    
    phReader.Update(increment)
    tdsReader.Update(increment)
    turbidityReader.Update(increment)
    
    positionReader.Update(increment)


    #check if at next node and then read and store data and set next node
#    if(positionReader.GetDistance(nextNode) < 10):
#        phWriter.writerow([str(nextNode[0]), str(nextNode[1]), str(phReader.GetMovingAverage())])
#        tdsWriter.writerow([str(nextNode[0]), str(nextNode[1]), str(tdsReader.GetMovingAverage())])
#        turbidityWriter.writerow([str(nextNode[0]), str(nextNode[1]), str(turbidityReader.GetMovingAverage())])
#
#        nextNode = pathfinder.GetNextNode()
#        if(nextNode == None):
#            done = True
#            return None
    

    #set rudder direction




#### Do Measurements ####

while not done:
    Update(0.1)

####/Do Measurements/####



#### Return To Shore ####

#do something

####/Return To Shore/####
