from vertex import Vertex
from utilFunctions import *

class Djikstra:
    def __init__(self):

        self.nodes = []
        self.adjMat = []

    
    def createVertex(self, code ,name, visaReq):
        tempVert = Vertex(code, name, visaReq)
        self.nodes.append(tempVert)

    def createMatrix(self):
        for i in range(len(self.nodes)):
            self.adjMat.append([])
            for j in range(len(self.nodes)):
                self.adjMat[i].append(99999)

    def fillMatrix(self):
        print('Hola')
        
    def fillCell(self, orgCode, destCode, cost):
        orgId, orgNode = findVertex(self.nodes ,orgCode)
        destId, destNode = findVertex(self.nodes, destCode)

        self.adjMat[orgId][destId] = cost
        self.adjMat[destId][orgId] = cost

    

    def forwardPass(self, orgCode):
        currentId, currentNode = findVertex(self.nodes ,orgCode)
        currentNode.acc = 0

        nodeQueue = []


        while checkEnd(self.nodes):
            currentId, currentNode = findLowest(self.nodes)

            nodeQueue = findAdj(self.adjMat[currentId], self.nodes)

            for tempId in nodeQueue:
                if currentNode.acc + self.adjMat[currentId][tempId] < self.nodes[tempId].acc:
                    self.nodes[tempId].acc = currentNode.acc + self.adjMat[currentId][tempId]
                    self.nodes[tempId].predecesor = currentNode.code

            currentNode.visited = True

            
    def showCosts(self):
        for i in self.nodes:
            print(f'{i.code} {i.acc} predecesor: {i.predecesor}')