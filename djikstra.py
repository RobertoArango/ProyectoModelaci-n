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

    

    def forwardPass(self, orgCode, hasVisa):
        currentId, currentNode = findVertex(self.nodes ,orgCode)
        currentNode.acc = 0

        nodeQueue = []

        if not hasVisa:
            for node in self.nodes:
                node.visited = node.visaReq

        while checkEnd(self.nodes):
            currentId, currentNode = findLowest(self.nodes)

            if currentNode.acc >= 99999:
                break

            nodeQueue = findAdj(self.adjMat[currentId], self.nodes)

            for tempId in nodeQueue:
                if currentNode.acc + self.adjMat[currentId][tempId] < self.nodes[tempId].acc:
                    self.nodes[tempId].acc = currentNode.acc + self.adjMat[currentId][tempId]
                    self.nodes[tempId].predecesor = currentNode.code
            currentNode.visited = True
    
    def menosEscalas(self, orgCode, destCode, hasVisa):
        orgId, orgNode = findVertex(self.nodes ,orgCode)
        destId, destNode = findVertex(self.nodes, destCode)

        if not hasVisa:
            for node in self.nodes:
                node.visited = node.visaReq

        orgNode.visited = True

        if self.adjMat[orgId][destId] < 99999:
            if not destNode.visited:
                destNode.acc = self.adjMat[orgId][destId]
                destNode.visited = True
                destNode.predecesor = orgNode.code
        else:
            cola = []
            searching = True
            tempAcc = 999999
            tempPre = None

            for i, j in enumerate(self.adjMat[orgId]):
                if j < 99999:
                    if not self.nodes[i].visited:
                        tempDicc = {"Node": self.nodes[i], "ID": i}
                        self.nodes[i].acc = j
                        self.nodes[i].visited = True
                        self.nodes[i].predecesor = orgNode.code
                        cola.append(tempDicc)
            
            while searching and len(cola) > 0:
                for i in cola:
                    if self.adjMat[i["ID"]][destId] < 99999:
                        if (i["Node"].acc + self.adjMat[i["ID"]][destId]) < tempAcc:
                            tempAcc = i["Node"].acc + self.adjMat[i["ID"]][destId]
                            tempPre = i["Node"].code
                            searching = False
                
                if searching:
                    tempCola = []
                    for i in cola:
                        for x, c in enumerate(self.adjMat[i["ID"]]):
                            if c < 99999:
                                if not self.nodes[x].visited:
                                    if (c + i["Node"].acc) < self.nodes[x].acc:
                                        dicc = {"Node": self.nodes[x], "ID": x}
                                        self.nodes[x].acc = c + i["Node"].acc
                                        for h, v in enumerate(tempCola):
                                            if v["Node"].code == self.nodes[x].code:
                                                tempCola.pop(h)
                                        self.nodes[x].predecesor = i["Node"].code
                                        tempCola.append(dicc)
                    cola = tempCola
                    for i in cola:
                        i["Node"].visited = True
                else:
                    destNode.acc = tempAcc
                    destNode.visited = True
                    destNode.predecesor = tempPre

            
    def showCosts(self, dest):
        for i in self.nodes:
            if i.code == dest:
                if i.predecesor == None:
                    print("Mano, no tienes ni fe, ni visa. No puedes viajar")
                else:
                    route = [dest]
                    tempPredecesor = i.predecesor
                    print(f'{i.code} {i.acc} predecesor: {i.predecesor}\n\n')
                    
                    while tempPredecesor != None:
                        route.append(tempPredecesor)
                        currentId, currentNode = findVertex(self.nodes ,tempPredecesor)
                        tempPredecesor = currentNode.predecesor
                    
                    indice = 1
                    print("Ruta:")
                    for i in reversed(route):
                        print(f'{indice}. {i}')
                        indice += 1