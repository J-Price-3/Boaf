import BoafPosition
import time

positionReader = BoafPosition.PositionReader()
positionReader.Update(0.6)
positionReader.centre = (positionReader.latitude, positionReader.longitude)

positionHistory = open("positions.txt", "w")
positionHistory.close()
velocityHistory = open("velocities.txt", "w")
velocityHistory.close()

t = 0
while t < 60:
    positionReader.Update(0.1)
    positionHistory = open("positions.txt", "a")
    positionHistory.write(str(positionReader.GetPosition()) + "\n")
    positionReader.close()

    velocityHistory = open("velocities.txt", "a")
    velocityHistory.write(str(positionReader.GetVelocity()) + "\n")
    velocityHistory.close()
    
    time.sleep(0.1)
    t+=0.1