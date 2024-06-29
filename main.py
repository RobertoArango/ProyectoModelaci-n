from djikstra import Djikstra
from utilFunctions import *


def main():
    hola = Djikstra()

    for i in range(5):
        hola.createVertex(('a' + str(i)), "hola")

    hola.createMatrix()
    showMatrix(hola.adjMat, hola.visaMat)
    hola.fillCell('a0', 'a1', 14, 1)
    hola.fillCell('a1', 'a3', 18, 1)
    hola.fillCell('a3', 'a4', 51, 1)
    hola.fillCell('a4', 'a2', 20, 1 )
    showMatrix(hola.adjMat, hola.visaMat)

    hola.forwardPass('a0')
    hola.showCosts()
    

main()