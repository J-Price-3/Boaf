import BoafSensors, BoafPosition, BoafMovement, BoafPathfinding

phReader = BoafSensors.phReader()
tdsReader = BoafSensors.tdsReader()
turbidityReader = BoafSensors.turbidityReader()

positionReader = BoafPosition.PositionReader()

#use increments of 0.1s
def update(increment):
    
    phReader.update(increment)
    tdsReader.update(increment)
    turbidityReader.update(increment)
    
    positionReader.Update(increment)


    #check if at next node and then read and store data and set next node
    #set rudder direction