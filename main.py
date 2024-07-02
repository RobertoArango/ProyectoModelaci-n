from djikstra import Djikstra
from utilFunctions import *
import json


def main():
    hola = Djikstra()
    b = True
    origen = 0
    destino = 0
    visa = False
    corto = False

    with open('data.json', 'r') as archivo:
            data = json.load(archivo)

    vertices = data["vertex"]
    arcos = data["Arcs"]

    for i in vertices:
          hola.createVertex(i["code"], i["name"], i["visaReq"])

    hola.createMatrix()

    for i in arcos:
          hola.fillCell(i["orig"], i["dest"], i["cost"])

    #showMatrix(hola.adjMat)

    while b:
        a = True
        while a:
            print("\n\nBIENVENIDO A METROTRAVEL\n")
            for i, j in enumerate(hola.nodes):
                print(f"{i+1}. {hola.nodes[i].name} ({hola.nodes[i].code})")
            print(f"{len(hola.nodes)+1}. Salir")
            try:
                origen = int(input("¿Desde donde está viajando camarada?: "))
                if origen not in range(1, len(hola.nodes)+2):
                    print("\nRespuesta inválida\n")
                else:
                    a = False
                
            except Exception as e:
                print("\nRespuesta inválida\n")

        if origen != len(hola.nodes) + 1:
            a = True
            while a:
                for i, j in enumerate(hola.nodes):
                    print(f"{i+1}. {hola.nodes[i].name} ({hola.nodes[i].code})")
                try:
                    destino = int(input("Hacia donde está viajando camarada?: "))
                    if destino not in range(1, len(hola.nodes)+1):
                        print("\nRespuesta inválida\n")
                    else:
                        a = False
                except Exception as e:
                    print("\nRespuesta inválida\n")
            
            a = True
            while a:
                print("¿Tienes Visa?:")
                print("1. Sí")
                print("2. No")
                try:
                    visa = int(input(""))
                    if visa not in range(1, 3):
                        print("\nRespuesta inválida\n")
                    else:
                        a = False
                except Exception as e:
                    print("\nRespuesta inválida\n")
            
            a = True
            while a:
                print("¿Cómo quieres viajar?:")
                print("1. Con el menor costo")
                print("2. Con menos escalas")
                try:
                    corto = int(input(""))
                    if corto not in range(1, 3):
                        print("\nRespuesta inválida\n")
                    else:
                        a = False
                except Exception as e:
                    print("\nRespuesta inválida\n")
            
            orig = hola.nodes[origen-1].code
            dest = hola.nodes[destino-1].code
            if corto == 1:
                if visa == 1:
                    hola.forwardPass(orig, True)
                else:
                    hola.forwardPass(orig, False)
                hola.showCosts(dest)
            else:
                if visa == 1:
                    hola.menosEscalas(orig, dest, True)
                    hola.showCosts(dest)
                else:
                    if not hola.nodes[origen-1].visaReq:
                        hola.menosEscalas(orig, dest, False)
                        hola.showCosts(dest)
                    else:
                        print("Mano, ¿Cómo estás en este sitio sin visa? Reportado.")
            
            for i, j in enumerate(hola.nodes):
                hola.nodes[i].acc = 999999
                hola.nodes[i].visited = False
                hola.nodes[i].predecesor = None
                
        else:
            b = False
            print("Chao")
            

    #hola.forwardPass('CCS', False)
    #hola.menosEscalas('CCS', 'AUA', False)
    #hola.showCosts('AUA')
    

main()