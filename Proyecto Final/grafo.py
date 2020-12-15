import networkx as nx
import matplotlib.pyplot as plt

def mostrar_grafo():
    Grafo = nx.Graph()
    Grafo.add_node("A")      # add_node("n") agrega "n" como nodo del grafo
    Grafo.add_node("E")
    Grafo.add_node("I")
    Grafo.add_edge("A","E")  # add_edge("e") agrega "e" como borde de un nodo
    Grafo.add_edge("E","I")
    Grafo.add_edge("I","U")
    print(nx.info(Grafo))
    nx.draw(Grafo)
    plt.show()