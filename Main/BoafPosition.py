import os

def GetLatitude():
    file = open("GPSDATA.txt", "r")
    return file.readline()

file = open("GPSDATA.txt", "r")
while True:
    print(file.readline())
