import grovepi, time

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

class tdsReader():
    def __init__(self):
        self.timeSpan = 10
        self.measureInterval = 0.5
        self.measurements = []
        self.timeSinceMeasurement = 0
        for i in range(0, int(self.timeSpan // self.measureInterval)):
            self.measurements.append(0)
        
    def update(self, t):
        self.timeSinceMeasurement += t
        if (self.timeSinceMeasurement >= self.measureInterval):
            self.measurements.append(tdsRead())
            self.measurements.pop(0)
            self.timeSinceMeasurement = 0
            
    def getMovingAverage(self):
        total = 0
        for value in self.measurements:
            total += value
        return total / len(self.measurements)

class turbidityReader():
    def __init__(self):
        self.timeSpan = 10
        self.measureInterval = 0.5
        self.measurements = []
        self.timeSinceMeasurement = 0
        for i in range(0, int(self.timeSpan // self.measureInterval)):
            self.measurements.append(0)
        
    def update(self, t):
        self.timeSinceMeasurement += t
        if (self.timeSinceMeasurement >= self.measureInterval):
            self.measurements.append(turbidityRead())
            self.measurements.pop(0)
            self.timeSinceMeasurement = 0
            
    def getMovingAverage(self):
        total = 0
        for value in self.measurements:
            total += value
        return total / len(self.measurements)
    
class phReader():
    def __init__(self):
        self.timeSpan = 10
        self.measureInterval = 0.5
        self.measurements = []
        self.timeSinceMeasurement = 0
        for i in range(0, int(self.timeSpan // self.measureInterval)):
            self.measurements.append(0)
        
    def update(self, t):
        self.timeSinceMeasurement += t
        if (self.timeSinceMeasurement >= self.measureInterval):
            self.measurements.append(phRead())
            self.measurements.pop(0)
            self.timeSinceMeasurement = 0
            
    def getMovingAverage(self):
        total = 0
        for value in self.measurements:
            total += value
        return total / len(self.measurements)