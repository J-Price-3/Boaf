import math


class PositionReader():
    def __init__(self):
        self.latitude = 0
        self.lastLat = 0
        self.longitude = 0
        self.centre = (0, 0)#lat long
        self.positions = [[0,0],[0,0],[0,0],[0,0]]
        self.velocities = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]#8 item array for moving average (deltalat, deltalong)
        self.timeSince = 0
    
    def SetLatitude(self):
        file = open("GPSDATA.txt", "r")
        ret = file.readlines()
        file.close()
        try:
            self.lastLat = self.latitude
            self.latitude = float(float((ret[0])[0:2]) + float((ret[0])[2:10]) / 60)
            ns = 1
            try:
                if((ret[2])[0] == "N"):
                    ns = 1
                else:
                    ns = -1
                self.latitude = ns * self.latitude
                self.velocities.pop(0)
                self.velocities.append([111320 * (self.latitude - self.lastLat) / self.timeSince, 0])
                return True
            except:
                return False
        except:
            return False
    
    def SetLongitude(self):
        file = open("GPS/GPSDATA.txt", "r")
        ret = file.readlines()
        file.close()
        try:
            lastLong = self.longitude
            self.longitude = float(float((ret[1])[1:3]) + float((ret[0])[3:11]) / 60)
            ew = 1
            try:
                if((ret[3])[0] == "E"):
                    ew = 1
                else:
                    ew = -1
                self.longitude = ew * self.longitude
                self.velocities[len(self.velocities) - 1][1] = 111320 * (math.sin(self.latitude * math.pi / 180) * self.longitude - math.sin(self.lastLat * math.pi / 180) * lastLong) / self.timeSince
                return True
            except:
                return False
        except:
            return False

    #(N/S, E/W) (m/s)
    def GetVelocity(self):
        sum = [0, 0]
        for v in self.velocities:
            sum[0] += v[0]
            sum[1] += v[1]
        sum[0] /= 8
        sum[1] /= 8
        return sum

    #(N/S, E/W) (m) (relative to centre)
    def GetPositionCurrent(self):
        return (111320 * (self.latitude - self.centre[0]), 111320 * (self.longitude * math.sin(self.latitude * math.pi / 180) - self.centre[1]* math.sin(self.centre[0] * math.pi / 180)))

    def GetPosition(self):
        x = 0
        y = 0
        for p in self.positions:
            x+=p[0]
            y+=[1]
        x /= 4
        y /= 4
        return [x,y]

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
                    self.positions.pop(0)
                    self.positions.append(self.GetPositionCurrent())



