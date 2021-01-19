from tda_cola import Cola, arribo, atencion, cola_vacia
from tda_pila import Pila, apilar, desapilar, barrido, pila_vacia
from tda_heap import Heap, arribo_H, atencion_H, heap_vacio, buscarHeap, cambiar_prioridad, flotar, hundir, buscarHeapPunto8
import math


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


class verticeCA():
    # este objeto sera para almacenar el vertice con la cantidad de aristas que lo apuntan.
    def __init__(self):
        self.vertice = nodoVertice()
        self.cantidadAristas = 0


def insertar_vertice(grafo, dato, campo=0):
    nodo = nodoVertice(dato)
    if (grafo.inicio is None) or (nodo.info[campo] < grafo.inicio.info[campo]):
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        act = grafo.inicio.sig
        ant = grafo.inicio
        while (act is not None) and (act.info[campo] <= nodo.info[campo]):
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


def insertar_arista(grafo, dato, origen, destino, campo=0):
    '''Si los vertices de origen y destino existen, insertar arista'''
    ori = buscar_vertice(grafo, origen, campo)
    des = buscar_vertice(grafo, destino, campo)

    if (ori is not None) and (des is not None):

        if grafo.dirigido:
            agregar_arista(ori.adyacentes, dato, des.info)
        else:
            agregar_arista(ori.adyacentes, dato, des.info)
            agregar_arista(des.adyacentes, dato, ori.info)


def buscar_verticePunto8(grafo, buscado, campo=0):
    aux = grafo.inicio
    while (aux is not None) and (aux.info['nombre'] != buscado):
        if aux.info['nombre'] == buscado:
            return aux
        aux = aux.sig
    return aux


def agregar_aristaPunto8(lista_adyacentes, dato, destino, campo=0):  # Las aristas se ordenan por peso en la lista
    nodo_arista = nodoArista(destino, dato)
    if (lista_adyacentes.inicio is None) or (nodo_arista.peso[campo]['distancia'] < lista_adyacentes.inicio.peso[campo]['distancia']):
        nodo_arista.sig = lista_adyacentes.inicio
        lista_adyacentes.inicio = nodo_arista
    else:
        act = lista_adyacentes.inicio.sig
        ant = lista_adyacentes.inicio
        while (act is not None) and (act.peso[campo]['distancia'] <= nodo_arista.peso[campo]['distancia']):
            act = act.sig
            ant = ant.sig
        nodo_arista.sig = act
        ant.sig = nodo_arista
    lista_adyacentes.tamanio += 1


def insertar_aristaPunto8(grafo, dato, origen, destino, campo=0):
    '''Si los vertices de origen y destino existen, insertar arista'''
    ori = buscar_verticePunto8(grafo, origen)
    des = buscar_verticePunto8(grafo, destino)

    if (ori is not None) and (des is not None):

        if grafo.dirigido:
            agregar_aristaPunto8(ori.adyacentes, dato, des.info, campo)
        else:
            agregar_aristaPunto8(ori.adyacentes, dato, des.info, campo)
            agregar_aristaPunto8(des.adyacentes, dato, ori.info, campo)


def buscar_arista(vertice, buscado):
    aux = vertice.adyacentes.inicio
    while (aux is not None) and (aux.destino != buscado):
        aux = aux.sig
    return aux


def buscar_adyacentes(vertice, buscado):
    """Devuelve posicion. -1 si no se encontro lo buscado"""
    pos = -1
    i = -1
    aux = vertice.adyacentes.inicio
    while (aux is not None) and (pos == -1):
        i += 1
        if (aux.destino == buscado):
            pos = aux.destino
        aux = aux.sig
    return pos


def buscar_vertice(grafo, buscado, campo=0):
    aux = grafo.inicio
    while (aux is not None) and (aux.info[campo] != buscado):
        if aux.info == buscado:
            return aux
        aux = aux.sig
    return aux


def barrido_profundidad(grafo, vertice, campo=0):
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            print(vertice.info)
            adyacentes = vertice.adyacentes.inicio
            while adyacentes is not None:
                aux_adyacente = buscar_vertice(grafo, adyacentes.destino[campo], campo)
                if not aux_adyacente.visitado:
                    barrido_profundidad(grafo, aux_adyacente, campo)
                adyacentes = adyacentes.sig
        vertice = vertice.sig


def barrido_prof(grafo, vertice):
    marcar_no_visitado(grafo)
    barrido_profundidad(grafo, vertice)


def barrido_amplitud(grafo, vertice, campo=0):
    marcar_no_visitado(grafo)
    cola = Cola()
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            arribo(cola, vertice)
            while not cola_vacia(cola):
                nodo = atencion(cola)
                print(nodo.info)
                adyacente = nodo.adyacentes.inicio
                while adyacente is not None:
                    nodo_aux = buscar_vertice(grafo, adyacente.destino[campo], campo)
                    if not nodo_aux.visitado:
                        nodo_aux.visitado = True
                        arribo(cola, nodo_aux)
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
            if aux.adyacentes.tamanio != 0:
                eliminar_arista(aux.adyacentes, dato)
            aux = aux.sig
    return dato


def eliminar_arista(vertice, clave):
    dato = None
    if vertice.inicio.destino == clave:
        dato = vertice.inicio.destino
        vertice.inicio = vertice.inicio.sig
        vertice.tamanio -= 1
    else:
        ant = vertice.inicio
        act = vertice.inicio.sig
        while (act is not None) and (act.destino != clave):
            ant = act
            act = act.sig
        if (act is not None):
            dato = act.destino
            ant.sig = act.sig
            vertice.tamanio -= 1
    return dato


def kruskal(grafo, campo=0):
    """Algoritmo de Kruskal para hallar el árbol de expansión mínimo."""
    bosque = []
    aristas = Heap(grafo.tamanio ** 2)
    aux = grafo.inicio
    while(aux is not None):
        bosque.append([aux.info[campo]])
        adyac = aux.adyacentes.inicio
        while(adyac is not None):
            arribo_H(aristas, [aux.info[campo], adyac.destino[campo]], adyac.peso)
            adyac = adyac.sig
        aux = aux.sig
    while(len(bosque) > 1 and not heap_vacio(aristas)):
        dato = atencion_H(aristas)[0]
        origen = None
        for elemento in bosque:
            if(dato[0] in elemento):
                origen = bosque.pop(bosque.index(elemento))
                break
        destino = None
        for elemento in bosque:
            if(dato[1] in elemento):
                destino = bosque.pop(bosque.index(elemento))
                break
        if(origen is not None and destino is not None):
            if(len(origen) > 1 and len(destino) == 1):
                destino = [dato[0], dato[1]]
            elif(len(destino) > 1 and len(origen) == 1):
                origen = [dato[0], dato[1]]
            elif(len(destino) > 1 and len(origen) > 1):
                origen += [dato[0], dato[1]]
            bosque.append(origen + destino)
        else:
            bosque.append(origen)
    return bosque[0]


def dijkstra(grafo, origen, destino, campo=0):
    from math import inf
    '''Camino mas corto entre dos nodos'''
    no_visitados = Heap(grafo.tamanio)
    camino = Pila()
    aux = grafo.inicio
    while aux is not None:
        if aux.info[campo] == origen:
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
            if (no_visitados.vector[pos][0] > dato[0] + aux.peso):
                no_visitados.vector[pos][1][1] = dato[1][0].info[campo]
                cambiar_prioridad(no_visitados, pos, dato[0]+aux.peso)
            aux = aux.sig
    return camino


def dijkstraPunto8(grafo, origen, destino, campo=0):
    from math import inf
    '''Camino mas corto entre dos nodos'''
    no_visitados = Heap(grafo.tamanio)
    camino = Pila()
    aux = grafo.inicio
    while aux is not None:
        if aux.info['nombre'] == origen:
            arribo_H(no_visitados, 0, [aux, None])
        else:
            arribo_H(no_visitados, inf, [aux, None])
        aux = aux.sig
    while not heap_vacio(no_visitados):
        dato = atencion_H(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while aux is not None:
            pos = buscarHeapPunto8(no_visitados, aux.destino['nombre'])
            if (no_visitados.vector[pos][0] > dato[0] + aux.peso[0][campo]):
                no_visitados.vector[pos][1][1] = dato[1][0].info['nombre']
                cambiar_prioridad(no_visitados, pos, dato[0]+aux.peso[0][campo])
            aux = aux.sig
    return camino


def dijkstraPunto9(grafo, origen, destino):
    from math import inf
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
            if (no_visitados.vector[pos][0] > dato[0] + aux.peso):
                no_visitados.vector[pos][1][1] = dato[1][0].info
                cambiar_prioridad(no_visitados, pos, dato[0]+aux.peso)
            aux = aux.sig
    return camino


def dijkstraPunto10(grafo, origen, destino, campo=0):
    from math import inf
    '''Camino mas corto entre dos nodos'''
    no_visitados = Heap(grafo.tamanio)
    camino = Pila()
    aux = grafo.inicio
    while aux is not None:
        if aux.info['nombre'] == origen:
            arribo_H(no_visitados, 0, [aux, None])
        else:
            arribo_H(no_visitados, inf, [aux, None])
        aux = aux.sig
    while not heap_vacio(no_visitados):
        dato = atencion_H(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while aux is not None:
            pos = buscarHeapPunto8(no_visitados, aux.destino['nombre'])
            if (no_visitados.vector[pos][0] > dato[0] + aux.peso):
                no_visitados.vector[pos][1][1] = dato[1][0].info['nombre']
                cambiar_prioridad(no_visitados, pos, dato[0]+aux.peso)
            aux = aux.sig
    return camino


def dijkstraAristas(grafo, origen, destino, campo=0):
    from math import inf
    '''Camino mas corto entre dos nodos'''
    no_visitados = Heap(grafo.tamanio)
    camino = Pila()
    aux = grafo.inicio
    while aux is not None:
        if aux.info['nombre'] == origen:
            arribo_H(no_visitados, 0, [aux, None])
        else:
            arribo_H(no_visitados, inf, [aux, None])
        aux = aux.sig
    while not heap_vacio(no_visitados):
        dato = atencion_H(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while aux is not None:
            pos = buscarHeapPunto8(no_visitados, aux.destino['nombre'])
            if (no_visitados.vector[pos][0] > dato[0] + 1):
                no_visitados.vector[pos][1][1] = dato[1][0].info['nombre']
                cambiar_prioridad(no_visitados, pos, dato[0]+1)
            aux = aux.sig
    return camino


def dijkstraAristasPunto5(grafo, origen, destino, campo=0):
    from math import inf
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
            if (no_visitados.vector[pos][0] > dato[0] + 1):
                no_visitados.vector[pos][1][1] = dato[1][0].info
                cambiar_prioridad(no_visitados, pos, dato[0]+1)
            aux = aux.sig
    return camino


def caminoMasCorto(grafo, origen, destino, campo=0):
    camino = dijkstra(grafo, origen, destino, campo)
    pila = Pila()
    while(not pila_vacia(camino)):
        dato = desapilar(camino)
        if(destino == dato[1][0].info[campo]):
            apilar(pila, dato[1][0].info[campo])
            destino = dato[1][1]
    while(not pila_vacia(pila)):
        print(desapilar(pila))


def caminoMasCortoPunto8(grafo, origen, destino, campo=0):
    camino = dijkstraPunto8(grafo, origen, destino, campo)
    pila = Pila()
    while(not pila_vacia(camino)):
        dato = desapilar(camino)
        if(destino == dato[1][0].info['nombre']):
            apilar(pila, dato[1][0].info['nombre'])
            destino = dato[1][1]
    while(not pila_vacia(pila)):
        print(desapilar(pila))


def caminoMasCortoPunto9(grafo, origen, destino):
    camino = dijkstraPunto9(grafo, origen, destino)
    pila = Pila()
    while(not pila_vacia(camino)):
        dato = desapilar(camino)
        if(destino == dato[1][0].info):
            apilar(pila, dato[1][0].info)
            destino = dato[1][1]
    while(not pila_vacia(pila)):
        print(desapilar(pila))


def caminoMasCortoPunto10(grafo, origen, destino, campo=0):
    camino = dijkstraPunto10(grafo, origen, destino, campo)
    pila = Pila()
    while(not pila_vacia(camino)):
        dato = desapilar(camino)
        if(destino == dato[1][0].info['nombre']):
            apilar(pila, dato[1][0].info['nombre'])
            destino = dato[1][1]
    while(not pila_vacia(pila)):
        print(desapilar(pila))


def caminoMasCortoAristas(grafo, origen, destino, campo=0):
    camino = dijkstraAristas(grafo, origen, destino, campo)
    pila = Pila()
    while(not pila_vacia(camino)):
        dato = desapilar(camino)
        if(destino == dato[1][0].info['nombre']):
            apilar(pila, dato[1][0].info['nombre'])
            destino = dato[1][1]
    while(not pila_vacia(pila)):
        print(desapilar(pila))


def caminoMasCortoAristasPunto5(grafo, origen, destino, campo=0):
    camino = dijkstraAristasPunto5(grafo, origen, destino, campo)
    pila = Pila()
    while(not pila_vacia(camino)):
        dato = desapilar(camino)
        if(destino == dato[1][0].info):
            apilar(pila, dato[1][0].info)
            destino = dato[1][1]
    while(not pila_vacia(pila)):
        print(desapilar(pila))


def verVerticeAristas(g):
    aux = g.inicio
    while aux is not None:
        print("Vertice", aux.info, "Aristas de este:")
        aux2 = aux.adyacentes.inicio
        while aux2 is not None:
            print(aux2.destino, aux2.peso)
            aux2 = aux2.sig
        print()
        aux = aux.sig
