import os, time

def GetLatitude():
    file = open("GPSDATA.txt", "r")
    ret = file.readlines()
    file.close()
    try:
        print(ret[2])
        return float((ret[0])[0:9])
    except:
        return 0

def GetLongitude():
    file = open("GPSDATA.txt", "r")
    ret = file.readlines()
    file.close()
    try:
        return float((ret[1])[0:9])
    except:
        return 0

latitude = GetLatitude()
longitude = GetLongitude()

while True:
    print(GetLatitude())
    print(GetLongitude())
    time.sleep(0.5)
