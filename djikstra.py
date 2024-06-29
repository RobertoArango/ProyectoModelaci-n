from vertex import Vertex
from utilFunctions import *

class Djikstra:
    def __init__(self):

        self.nodes = []
        self.adjMat = []
        self.visaMat = []
        self.nodeQueue = []

    
    def createVertex(self, code ,name):
        tempVert = Vertex(code, name, 99999, None)
        self.nodes.append(tempVert)

    def createMatrix(self):
        for i in range(len(self.nodes)):
            self.adjMat.append([])
            self.visaMat.append([])
            for j in range(len(self.nodes)):
                self.adjMat[i].append(999)
                self.visaMat[i].append(0)

    def fillMatrix(self):
        print('Hola')
        
    def fillCell(self, orgCode, destCode, cost, visaReq):
        orgId, orgNode = findVertex(self.nodes ,orgCode)
        destId, destNode = findVertex(self.nodes, destCode)
        self.adjMat[orgId][destId] = cost
        self.visaMat[orgId][destId] = visaReq

    

    def forwardPass(self, orgCode):
        currentId, currentNode = findVertex(self.nodes ,orgCode)
        currentNode.acc = 0

        while checkEnd(self.nodes):

            print(currentId)

            self.nodes[currentId].visited = True
            self.nodeQueue = findAdj(self.adjMat[currentId])

            for i in self.nodeQueue:
                if self.adjMat[currentId][i] + currentNode.acc < self.nodes[i].acc + currentNode.acc:
                    self.nodes[i].acc = currentNode.acc + self.adjMat[currentId][i]

            currentId, currentNode = findLowest(self.nodes)

    def showCosts(self):
        for i in self.nodes:
            print(i.acc)