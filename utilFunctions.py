from vertex import Vertex
from djikstra import *

def findVertex(nodes, code):
        for tempNumb, tempVer in enumerate(nodes):
            if code == tempVer.code:
                return tempNumb, tempVer
            
        print(f'No se encontro nodo {code}')
        return None

def showMatrix(adjMat, visaMat):
     print(f'''{adjMat}
           \n
           {visaMat}''')
     
def checkEnd(nodeList):
     
    endBool = False

    for node in nodeList:
          if not node.visited:
               print(node.visited)
               endBool = True
               return endBool
          
    return endBool  

def findLowest(nodeList):

    tempId, tempNode = findNotVisited(nodeList)

    for id, node in enumerate(nodeList):
        if node.acc < tempNode.acc and not node.visited:
             tempNode = node
             tempId = id

    return tempId, tempNode

def findNotVisited(nodeList):
     
     for tempId, tempNode in enumerate(nodeList):
          if not tempNode.visited:
               return tempId, tempNode

def findAdj(adjRow):
    adjList = []
    for i in range(len(adjRow)):
        if adjRow[i] < 999:
            adjList.append(i)
    
    return adjList