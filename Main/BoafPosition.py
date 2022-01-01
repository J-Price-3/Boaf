import os, time

def GetLatitude():
    file = open("GPSDATA.txt", "r")
    ret = file.readlines()
    file.close()
    return ret



while True:
    print(GetLatitude())
    time.sleep(5)
