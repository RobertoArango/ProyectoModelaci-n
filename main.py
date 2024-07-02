from djikstra import Djikstra
from utilFunctions import *
import json


def main():
    hola = Djikstra()

    with open('data.json', 'r') as archivo:
            data = json.load(archivo)

    vertices = data["vertex"]
    arcos = data["Arcs"]

    for i in vertices:
          hola.createVertex(i["code"], i["name"], i["visaReq"])

    #hola.createVertex('CCS', 'Caracas', False) #0
    #hola.createVertex('AUA', 'Aruba', True) #1
    #hola.createVertex('BON', 'Bonaire', True) #2
    #hola.createVertex('CUR', 'Curazao', True) #3
    #hola.createVertex('SXM', 'San Martin', True) #4
    #hola.createVertex('SDQ', 'Santo Domingo', True) #5
    #hola.createVertex('SBH', 'San Bartolome', False) #6
    #hola.createVertex('POS', 'Puerto España', False) #7
    #hola.createVertex('BGI', 'Barbados', False) #8 
    #hola.createVertex('FDF', 'Fort de France', False) #9
    #hola.createVertex('PTP', 'Point a Pitre', False) #10

    hola.createMatrix()
    #showMatrix(hola.adjMat)

    for i in arcos:
          hola.fillCell(i["orig"], i["dest"], i["cost"])

    #hola.fillCell('CCS', 'AUA', 40.00) # 0 - 1
    #hola.fillCell('CCS', 'CUR', 35.00) # 0 - 3
    #hola.fillCell('CCS', 'BON', 60.00) # 0 - 2
    #hola.fillCell('CCS', 'SXM', 300.00) # 0 - 4
    #hola.fillCell('AUA', 'CUR', 15.00) # 1 - 3
    #hola.fillCell('AUA', 'BON', 15.00) # 1 - 2
    #hola.fillCell('CUR', 'BON', 15.00) # 3 - 2
    #hola.fillCell('CCS', 'SDQ', 180.00) # 0 - 5
    #hola.fillCell('SDQ', 'SXM', 50.00) # 5 - 4
    #hola.fillCell('SXM', 'SBH', 45.00) # 4 - 6
    #hola.fillCell('CCS', 'POS', 150.00) # 0 - 7
    #hola.fillCell('CCS', 'BGI', 180.00) # 0 - 8
    #hola.fillCell('POS', 'BGI', 35.00) # 7 - 8
    #hola.fillCell('POS', 'SXM', 90.00) # 7 - 4
    #hola.fillCell('BGI', 'SXM', 70.00) # 8 - 4
    #hola.fillCell('POS', 'PTP', 80.00) # 7 - 10
    #hola.fillCell('POS', 'FDF', 75.00) # 7 - 9
    #hola.fillCell('PTP', 'SXM', 100.00) # 10 - 4
    #hola.fillCell('PTP', 'SBH', 80.00) # 10 - 6
    #hola.fillCell('CUR', 'SXM', 80.00) # 3 - 4
    #hola.fillCell('AUA', 'SXM', 40.00) # 1 - 4

    showMatrix(hola.adjMat)

    hola.forwardPass('CCS', False)
    hola.showCosts('FDF')
    

main()