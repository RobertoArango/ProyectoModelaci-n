from djikstra import Djikstra
from utilFunctions import *


def main():
    hola = Djikstra()


    hola.createVertex('CCS', 'Caracas', False) #0
    hola.createVertex('AUA', 'Aruba', True) #1
    hola.createVertex('BON', 'Bonaire', True) #2
    hola.createVertex('CUR', 'Curazao', True) #3
    hola.createVertex('SXM', 'San Martin', True) #4
    hola.createVertex('SDQ', 'Santo Domingo', True) #5
    hola.createVertex('SBH', 'San Bartolome', False) #6
    hola.createVertex('POS', 'Puerto España', False) #7
    hola.createVertex('BGI', 'Barbados', False) #8 
    hola.createVertex('FDF', 'Fort de France', False) #9
    hola.createVertex('PTP', 'Point a Pitre', False) #10

    hola.createMatrix()
    #showMatrix(hola.adjMat)

    hola.fillCell('CCS', 'AUA', 40.00)
    hola.fillCell('CCS', 'CUR', 35.00)
    hola.fillCell('CCS', 'BON', 60.00)
    hola.fillCell('CCS', 'SXM', 300.00)
    hola.fillCell('AUA', 'CUR', 15.00)
    hola.fillCell('AUA', 'BON', 15.00)
    hola.fillCell('CUR', 'BON', 15.00)
    hola.fillCell('CCS', 'SDQ', 180.00)
    hola.fillCell('SDQ', 'SXM', 50.00)
    hola.fillCell('SXM', 'SBH', 45.00)
    hola.fillCell('CCS', 'POS', 150.00)
    hola.fillCell('CCS', 'BGI', 180.00)
    hola.fillCell('POS', 'BGI', 35.00)
    hola.fillCell('POS', 'SXM', 90.00)
    hola.fillCell('BGI', 'SXM', 70.00)
    hola.fillCell('POS', 'PTP', 80.00)
    hola.fillCell('POS', 'FDF', 75.00)
    hola.fillCell('PTP', 'SXM', 100.00)
    hola.fillCell('PTP', 'SBH', 80.00)
    hola.fillCell('CUR', 'SXM', 80.00)
    hola.fillCell('AUA', 'SXM', 40.00)

    showMatrix(hola.adjMat)

    hola.forwardPass('CCS')
    hola.showCosts()
    

main()