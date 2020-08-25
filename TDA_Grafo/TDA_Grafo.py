from tda_cola import Cola, arribo, atencion, cola_vacia
from tda_pila import Pila, apilar, desapilar
from tda_heap import Heap, arribo_H, atencion_H, heap_vacio, buscarHeap
# from math import inf


class Grafo():
    def __init__(self, dirigido=True):
        self.inicio = None
        self.tamanio = 0
        self.dirigido = dirigido


class nodoVertice():
    def __init__(self, info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = listaAristas()


class nodoArista():
    # info de vertice(peso), el siguiente nodo vertice de la lista de vertices
    # y su destino o sea el nodo vertice destino que seria
    def __init__(self, destino, peso=0):
        self.peso = peso
        self.destino = destino
        self.sig = None


class listaAristas():
    '''lista de lista, crea lista vacia'''
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def insertar_vertice(grafo, dato):
    nodo = nodoVertice(dato)
    if (grafo.inicio is None) or (nodo.info < grafo.inicio.info):
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        act = grafo.inicio.sig
        ant = grafo.inicio
        while (act is not None) and (act.info <= nodo.info):
            act = act.sig
            ant = ant.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1


def agregar_arista(lista_adyacentes, dato, destino):  # Las aristas se ordenan por peso en la lista
    nodo_arista = nodoArista(destino, dato)
    if (lista_adyacentes.inicio is None) or (nodo_arista.peso < lista_adyacentes.inicio.peso):
        nodo_arista.sig = lista_adyacentes.inicio
        lista_adyacentes.inicio = nodo_arista
    else:
        act = lista_adyacentes.inicio.sig
        ant = lista_adyacentes.inicio
        while (act is not None) and (act.peso <= nodo_arista.peso):
            act = act.sig
            ant = ant.sig
        nodo_arista.sig = act
        ant.sig = nodo_arista
    lista_adyacentes.tamanio += 1


def insertar_arista(grafo, dato, origen, destino):
    '''Si los vertices de origen y destino existen, insertar arista'''
    ori = buscar_vertice(grafo, origen)
    des = buscar_vertice(grafo, destino)
    if (ori is not None) and (des is not None):
        if grafo.dirigido:
            agregar_arista(ori.adyacentes, dato, des.info)
        else:
            agregar_arista(ori.adyacentes, dato, des.info)
            agregar_arista(des.adyacentes, dato, ori.info)


def buscar_arista(vertice, buscado):
    aux = vertice.adyacentes.inicio
    while (aux is not None) and (aux.destino != buscado):
        aux = aux.sig
    return aux


def buscar_vertice(grafo, buscado):
    aux = grafo.inicio
    while (aux is not None) and (aux.info != buscado):
        aux = aux.sig
    return aux


def barrido_profundidad(grafo, vertice):
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            print(vertice.info)
            adyacentes = vertice.adyacentes.inicio
            while adyacentes is not None:
                aux_adyacente = buscar_vertice(grafo, adyacentes.destino)
                # print(aux_adyacente)
                if not aux_adyacente.visitado:
                    barrido_profundidad(grafo, aux_adyacente)
                adyacentes = adyacentes.sig
        vertice = vertice.sig


def barrido_prof(grafo, vertice):
    marcar_no_visitado(grafo)
    barrido_profundidad(grafo, vertice)


def barrido_amplitud(grafo, vertice):
    marcar_no_visitado(grafo)
    cola = Cola()
    while vertice is not None:
        print(vertice.visitado)
        if not vertice.visitado:
            vertice.visitado = True
            arribo(cola, vertice)
            while not cola_vacia(cola):
                nodo = atencion(cola)
                print(nodo.info)
                adyacente = nodo.adyacentes.inicio
                while adyacente is not None:
                    adyacente = buscar_vertice(grafo, adyacente.destino)
                    if not adyacente.visitado:
                        adyacente.visitado = True
                        arribo(cola, adyacente)
                    adyacente = adyacente.sig
    vertice = vertice.sig


# terminar
def existe_paso():
    resultado = True
    if not origen.visitado:
        origen.visitado = True
        vadyacente = origen.adyacentes.inicio
        while (vadyacente is not None) and (not resultado):
            adyacente = buscar_vertice(grafo, vadyacente.origen)


def marcar_no_visitado(grafo):
    '''Marca todos los vertices como no visitado'''
    aux = grafo.inicio
    while aux is not None:
        aux.visitado = False
        aux = aux.sig


def eliminar_vertice(grafo, clave):
    dato = None
    if grafo.inicio.info == clave:
        dato = grafo.inicio.info
        grafo.inicio = grafo.inicio.sig
        grafo.tamanio -= 1
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while (act is not None) and (act.info != clave):
            ant = act
            act = act.sig
        if (act is not None):
            dato = act.info
            ant.sig = act.sig
            grafo.tamanio -= 1
    if(dato is not None):
        aux = grafo.inicio
        while aux is not None:
            eliminar_arista(aux.adyacentes, dato)
    return dato


def eliminar_arista(vertice, clave):
    dato = None
    if vertice.inicio.info == clave:
        dato = vertice.inicio.info
        vertice.inicio = vertice.inicio.sig
        vertice.tamanio -= 1
    else:
        ant = vertice.inicio
        act = vertice.inicio.sig
        while (act is not None) and (act.info != clave):
            ant = act
            act = act.sig
        if (act is not None):
            dato = act.info
            ant.sig = act.sig
            vertice.tamanio -= 1
    return dato


def Kruskal(grafo):
    '''Arbol de expansion minima'''
    bosque = []
    aristas = Heap(grafo.tamanio**2)
    aux = grafo.inicio
    while aux is not None:
        bosque.append([aux.info])
        adyacentes = aux.adyacentes.inicio
        while adyacentes is not None:
            arribo_H(aristas, [aux.info, adyacentes.destino], adyacentes.info)
            adyacentes = adyacentes.sig
        aux = aux.sig
    while (len(bosque[0]) == 1) and (not heap_vacio(aristas)):
        dato = atencion_H(aristas)
        origen = None
        for elemento in bosque:
            if dato[1][0] in elemento:
                origen = bosque.pop(bosque.index(elemento))
        destino = None


def dijkstra(grafo, origen, destino):
    '''Camino mas corto entre dos nodos'''
    no_visitados = Heap(grafo.tamanio)
    camino = Pila()
    aux = grafo.inicio
    while aux is not None:
        if aux.info == origen:
            arribo_H(no_visitados, 0, [aux, None])
        else:
            arribo_H(no_visitados, inf, [aux, None])
        aux = aux.sig
    while not heap_vacio(no_visitados):
        dato = atencion_H(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while aux is not None:
            pos = buscarHeap(no_visitados, aux.destino)
            if (no_visitados.vector[pos][0] > dato[0] + aux.info):
                no_visitados.vector[pos][1][1] = dato[1][0].info
    return camino


g = Grafo(True)

insertar_vertice(g, "A")
insertar_vertice(g, "B")
insertar_vertice(g, "Z")
insertar_vertice(g, "C")
insertar_vertice(g, "D")
insertar_vertice(g, "E")
insertar_vertice(g, "F")


insertar_arista(g, 10, "A", "B")
insertar_arista(g, 5, "A", "C")
insertar_arista(g, 2, "C", "F")
insertar_arista(g, 15, "F", "E")
insertar_arista(g, 32, "E", "D")
insertar_arista(g, 32, "D", "B")


def verVerticeAristas(g):
    aux = g.inicio
    while aux is not None:
        print("Vertice", aux.info, "Aristas de este:")
        aux2 = aux.adyacentes.inicio
        while aux2 is not None:
            print(aux2.destino)
            aux2 = aux2.sig
        print()
        aux = aux.sig
