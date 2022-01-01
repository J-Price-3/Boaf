import os, time

def GetLatitude():
    file = open("GPSDATA.txt", "r")
    return file.readline()


file = open("GPSDATA.txt", "r")
while True:
    print(file.read())
    time.sleep(1)
