from TDA_Grafo import Grafo, nodoVertice, nodoArista
from TDA_Grafo import insertar_vertice, insertar_arista, verVerticeAristas, barrido_amplitud, buscar_vertice
import random
import string


# Ejercicio 1
def aleatorio():
    grafo = Grafo()
    listaVertices = []
    aristas = [30, 3, 74, 1, 42, 19, 22, 12, 15, 20, 21, 9, 2, 14, 47, 66, 78, 70, 11, 57, 93, 7, 5, 3, 33, 89, 65, 64, 23, 40]
    print(len(aristas))
    for i in range(0, 15):
        ran = random.choice(string.ascii_letters)
        listaVertices.append(ran)
        insertar_vertice(grafo, ran)
    for i in aristas:
        insertar_arista(grafo, i, listaVertices[random.randint(0, len(listaVertices)-1)], listaVertices[random.randint(0, len(listaVertices)-1  )])

    ver = buscar_vertice(grafo, listaVertices[1])
    barrido_amplitud(grafo, ver)


aleatorio()
