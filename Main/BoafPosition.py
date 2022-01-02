import os, time

longitude = 0
latitude = 0


class PositionReader():
    def __init__(self):
        self.latitude = 0
        self.longitude = 0
        self.timeSince = 0
    
    def SetLatitude(self):
        file = open("GPSDATA.txt", "r")
        ret = file.readlines()
        file.close()
        try:
            self.latitude = float((ret[0])[0:10])
            ns = 1
            try:
                if((ret[2])[0] == "N"):
                    ns = 1
                else:
                    ns = -1
                self.latitude = ns * self.latitude
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
            self.longitude = float((ret[1])[0:10])
            ew = 1
            try:
                if((ret[3])[0] == "E"):
                    ew = 1
                else:
                    ew = -1
                self.longitude = ew * self.longitude
            except:
                return False
            return True
        except:
            return False

    def Update(self, deltaT):
        self.timeSince += deltaT
        if(self.timeSince >= 0.5):
            self.SetLatitude()
            self.SetLongitude()
            self.timeSince = 0
    



