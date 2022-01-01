import os, time

def GetLatitude():
    file = open("GPSDATA.txt", "r")
    ret = file.readlines()
    file.close()
    return ret[0]

def GetLongitude():
    file = open("GPSDATA.txt", "r")
    ret = file.readlines()
    file.close()
    return ret[1]

latitude = GetLatitude()
longitude = GetLongitude()

while True:
    print(GetLatitude())
    time.sleep(0.5)
