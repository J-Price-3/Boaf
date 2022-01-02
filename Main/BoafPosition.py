import os, time

longitude = 0
latitude = 0


def SetLatitude():
    file = open("GPSDATA.txt", "r")
    ret = file.readlines()
    file.close()
    try:
        latitude = float((ret[0])[1:10])
        ns = 1
        try:
            if((ret[2])[1] == "N"):
                ns = 1
            else:
                ns = -1
            latitude = ns * latitude
        except:
            return False
        return True
    except:
        return False

def SetLongitude():
    file = open("GPSDATA.txt", "r")
    ret = file.readlines()
    file.close()
    try:
        longitude = float((ret[1])[1:10])
        ew = 1
        try:
            if((ret[3])[1] == "E"):
                ew = 1
            else:
                ew = -1
            longitude = ew * longitude
        except:
            return False
        return True
    except:
        return False

SetLatitude()
SetLongitude()

while True:
    SetLatitude()
    SetLongitude()
    print(latitude)
    print(longitude)
    time.sleep(0.5)
