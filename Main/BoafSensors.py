import grovepi, time
import RPi.GPIO as GPIO

#############################################
##
## Use the readers rather than the functions.
##
#############################################

#reads tds value (ppm)
def tdsRead():
    sensorValue = grovepi.analogRead(0)
    voltage = sensorValue*5/1024.0
    tdsValue = (133.42*voltage*voltage*voltage - 255.86*voltage*voltage + 857.39*voltage)*0.5
    return tdsValue

#reads turbidity in NTU
def turbidityRead():
    sensorValue = grovepi.analogRead(1)
    voltage = sensorValue * 5/1024.0
    turbidityValue = 8996 - 3505 * voltage + 338.5 * voltage * voltage
    return turbidityValue

#reads ph
def phRead():
    OFFSET = -3.8714
    K = 5.7143
    sensorValue = grovepi.analogRead(2)
    voltage = sensorValue * 5.0 / 1024
    phValue = K * voltage + OFFSET
    return phValue

class TdsReader():
    def __init__(self):
        self.timeSpan = 10
        self.measureInterval = 0.5
        self.measurements = []
        self.timeSinceMeasurement = 0
        for i in range(0, int(self.timeSpan // self.measureInterval)):
            self.measurements.append(0)
        
    def Update(self, t):
        self.timeSinceMeasurement += t
        if (self.timeSinceMeasurement >= self.measureInterval):
            self.measurements.append(tdsRead())
            self.measurements.pop(0)
            self.timeSinceMeasurement = 0
            
    def GetMovingAverage(self):
        total = 0
        for value in self.measurements:
            total += value
        return total / len(self.measurements)

class TurbidityReader():
    def __init__(self):
        self.timeSpan = 10
        self.measureInterval = 0.5
        self.measurements = []
        self.timeSinceMeasurement = 0
        for i in range(0, int(self.timeSpan // self.measureInterval)):
            self.measurements.append(0)
        
    def Update(self, t):
        self.timeSinceMeasurement += t
        if (self.timeSinceMeasurement >= self.measureInterval):
            self.measurements.append(turbidityRead())
            self.measurements.pop(0)
            self.timeSinceMeasurement = 0
            
    def GetMovingAverage(self):
        total = 0
        for value in self.measurements:
            total += value
        return total / len(self.measurements)
    
class PhReader():
    def __init__(self):
        self.timeSpan = 10
        self.measureInterval = 0.5
        self.measurements = []
        self.timeSinceMeasurement = 0
        for i in range(0, int(self.timeSpan // self.measureInterval)):
            self.measurements.append(0)
        
    def Update(self, t):
        self.timeSinceMeasurement += t
        if (self.timeSinceMeasurement >= self.measureInterval):
            self.measurements.append(phRead())
            self.measurements.pop(0)
            self.timeSinceMeasurement = 0
            
    def GetMovingAverage(self):
        total = 0
        for value in self.measurements:
            total += value
        return total / len(self.measurements)

class ObstacleDetector():
    def __init__(self):
        GPIO.setup(40, GPIO.IN)
        self.valid = True
        self.measureInterval = 0.1
        self.timeSinceMeasurement = 0

    def Update(self, t):
        self.timeSinceMeasurement += t
        if(self.timeSinceMeasurement >= self.measureInterval):
            self.valid = False
            if(GPIO.input(40) == 0):
                self.valid = True