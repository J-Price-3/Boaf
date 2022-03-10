import time, math

class Node():
    def __init__(self, xy, parent):
        self.xPos = xy[0]
        self.yPos = xy[1]
        self.parent = parent
        self.blocked = False
        self.visited = False

class Pathfinder():
    def __init__(self, posReader, obstacleDetector):
        self.posReader = posReader
        self.obstacleDetector = obstacleDetector
        self.visited = []
        self.toVisit = []
        self.currentRoundedCoords = [0, 0]
        self.currentNode = Node([0, 0], None)

    def NodeStatus(self, nodeCoords):
        for i in range(len(self.visited)):
            if self.visited[i].xPos == nodeCoords[0] and self.visited[i].yPos == nodeCoords[1]:
                return 2
        for i in range(len(self.toVisit)):
            if self.toVisit[i].xPos == nodeCoords[0] and self.toVisit[i].yPos == nodeCoords[1]:
                return 1
        return 0

    def RoundCoords(self, coords):
        return [round(coords[0]), round(coords[1])]

    def Pathfind(self):

        if(not self.currentNode.visited):
            self.visited.append(self.currentNode)
            self.currentNode.visited = True

        self.currentRoundedCoords = self.RoundCoords(self.posReader.GetPosition())

        status = self.NodeStatus([self.currentRoundedCoords[0]+1,self.currentRoundedCoords[1]])
        if (status == 0):
            self.toVisit.append(Node([self.currentRoundedCoords[0]+1,self.currentRoundedCoords[1]], self.currentNode))
        
        status = self.NodeStatus([self.currentRoundedCoords[0]-1,self.currentRoundedCoords[1]])
        if (status == 0):
            self.toVisit.append(Node([self.currentRoundedCoords[0]-1,self.currentRoundedCoords[1]], self.currentNode))

        status = self.NodeStatus([self.currentRoundedCoords[0],self.currentRoundedCoords[1]+1])
        if (status == 0):
            self.toVisit.append(Node([self.currentRoundedCoords[0],self.currentRoundedCoords[1]+1], self.currentNode))

        status = self.NodeStatus([self.currentRoundedCoords[0],self.currentRoundedCoords[1]-1])
        if (status == 0):
            self.toVisit.append(Node([self.currentRoundedCoords[0],self.currentRoundedCoords[1]-1], self.currentNode))
        
        try:
            self.currentNode = self.toVisit[len(self.toVisit)-1]
            self.toVisit.pop(len(self.toVisit)-1)
        except:
            self.currentNode = None

    def Backtrack(self):
        self.currentNode.visited = True
        self.visited.append(self.currentNode)
        self.currentNode = self.currentNode.parent

    def Update(self):
        if(not self.obstacleDetector.valid):
            self.Backtrack()
        elif(self.posReader.GetDistance([self.currentNode.xPos, self.currentNode.yPos]) < 0.1):
            self.Pathfind()
    
    def Done(self):
        if(self.currentNode == None):
            return True
        return False
        