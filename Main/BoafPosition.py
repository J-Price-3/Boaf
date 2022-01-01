import os, time

def GetLatitude():
    file = open("GPSDATA.txt", "r")
    ret = file.readlines()
    file.close()
    try:
        return (ret[0])[0:9]
    except:
        return -1

def GetLongitude():
    file = open("GPSDATA.txt", "r")
    ret = file.readlines()
    file.close()
    try:
        return (ret[1])[0:9]
    except:
        return -1

latitude = GetLatitude()
longitude = GetLongitude()

while True:
    print(GetLatitude())
    time.sleep(0.5)
