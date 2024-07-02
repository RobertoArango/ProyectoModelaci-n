import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph(directed=True)
acti = [
    
]

def set_edge_colors(graph, edge_list, color):
    edge_colors = ['black' if edge not in edge_list else color for edge in graph.edges()]
    return edge_colors

def drawGraph(acti, criticalRoute):
    for activity in acti: #itera dentro de la lista las actividades y sus predecesores
        G.add_node(activity[0])
        if len(activity[2]) == 0:
            print('primer nodo')
            print(activity[0])
            pass
        else:
            for pre in activity[2]:
                print(f'Para {activity[0]} sus predecesores son:')
                print(pre)
                G.add_edge(pre, activity[0])


    print(G)

    edge_colors = set_edge_colors(G, criticalRoute, 'red')  # Cambia los colores de las aristas 

    pos = nx.circular_layout(G)  # Posicionamiento de los nodos
    nx.draw(G, pos, with_labels=True, edge_color=edge_colors)  # Dibuja el grafo con los colores de las aristas actualizados

    plt.show()