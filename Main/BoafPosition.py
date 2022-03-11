import math


class PositionReader():
    def __init__(self):
        self.latitude = 0
        self.lastLat = 0
        self.longitude = 0
        self.centre = (0, 0)#lat long
        self.velocities = [(0, 0), (0, 0), (0, 0), (0, 0)]#4 item array for moving average (deltalat, deltalong)
        self.timeSince = 0
    
    def SetLatitude(self):
        file = open("GPSDATA.txt", "r")
        ret = file.readlines()
        file.close()
        try:
            self.lastLat = self.latitude
            self.latitude = float((ret[0])[0:10])
            ns = 1
            try:
                if((ret[2])[0] == "N"):
                    ns = 1
                else:
                    ns = -1
                self.latitude = ns * self.latitude
                self.velocities.pop(0)
                self.velocities.append((111320 * (self.latitude - self.lastLat) / self.timeSince, 0))
            except:
                return False
            return True
        except:
            return False
    
    def SetLongitude(self):
        file = open("GPSDATA.txt", "r")
        ret = file.readlines()
        file.close()
        try:
            lastLong = self.longitude
            self.longitude = float((ret[1])[0:10])
            ew = 1
            try:
                if((ret[3])[0] == "E"):
                    ew = 1
                else:
                    ew = -1
                self.longitude = ew * self.longitude
                self.velocities[len(self.velocities) - 1][1] = 111320 * (math.cos(self.latitude * math.pi / 180) * self.longitude - math.cos(self.lastLat * math.pi / 180) * lastLong) / self.timeSince
            except:
                return False
            return True
        except:
            return False

    #(N/S, E/W) (m/s)
    def GetVelocity(self):
        sum = [0, 0]
        for v in self.velocities:
            sum[0] += v[0]
            sum[1] += v[1]
        sum[0] /= 4
        sum[1] /= 4
        return sum

    #(N/S, E/W) (m) (relative to centre)
    def GetPosition(self):
        return (111320 * (self.latitude - self.centre[0]), 111320 * (self.longitude * math.cos(self.latitude * math.pi / 180) - self.centre[1]* math.cos(self.centre[0] * math.pi / 180)))

    #distance (m)
    def GetDistance(self, position):
        currentPosition = self.GetPosition()
        return math.sqrt(math.pow(currentPosition[0] - position[0], 2) + math.pow(currentPosition[1] - position[1], 2))
    
    def Update(self, deltaT):
        self.timeSince += deltaT
        if(self.timeSince >= 0.5):
            if(self.SetLatitude()):
                if(self.SetLongitude()):
                    self.timeSince = 0
    



