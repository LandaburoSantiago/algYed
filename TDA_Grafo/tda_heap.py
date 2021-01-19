import random
"""Monticulo"""


class Heap():
    def __init__(self, tamanio):
        self.tamanio = 0
        self.vector = [None]*tamanio


def intercambio(a, b):
    a, b = b, a


def agregar(heap, dato):
    heap.vector[heap.tamanio] = dato
    flotar(heap, heap.tamanio)
    heap.tamanio += 1


def quitar(heap):
    heap.vector[0], heap.vector[heap.tamanio-1] = heap.vector[heap.tamanio-1], heap.vector[0]
    heap.tamanio -= 1
    hundir(heap, 0)
    return heap.vector[heap.tamanio]


def flotar(heap, indice):
    """Flota el elemento en la posicion del indice"""
    padre = (indice-1)//2
    while(indice > 0) and (heap.vector[padre][0] > heap.vector[indice][0]):
        heap.vector[padre], heap.vector[indice] = heap.vector[indice], heap.vector[padre]
        indice = padre
        padre = (padre-1)//2


def hundir(heap, indice):
    """Hunde el elemento en la posicion del indice"""
    # hi = Hijo izquierdo
    hi = 2*indice+1
    control = True
    while hi < heap.tamanio - 1 and control:
        may = hi
        # hd = Hijo derecho
        hd = hi + 1
        if hd <= heap.tamanio - 1 and heap.vector[hd][0] < heap.vector[hi][0]:
            may = hd
        if heap.vector[indice][0] > heap.vector[may][0]:
            heap.vector[indice], heap.vector[may] = heap.vector[may], heap.vector[indice]
        else:
            control = False
        hi = (2*may)+1


# cola de proridad
def arribo_H(H, prioridad, dato):
    agregar(H, [prioridad, dato])


def atencion_H(heap):
    aux = quitar(heap)
    return aux


def buscarHeap(heap, dato):
    for i in range(0, len(heap.vector)):
        if dato == heap.vector[i][1][0].info:
            return i
    return None


def buscarHeapPunto8(heap, dato):
    for i in range(0, len(heap.vector)):
        if dato == heap.vector[i][1][0].info['nombre']:
            return i
    return None


def heapsort(heap):
    """Metodo de ordenamiento monticulo"""
    aux = heap.tamanio
    for i in range(0, heap.tamanio-1):
        quitar(heap)
    heap.tamanio = aux


def cambiar_prioridad(heap, indice, prioridad):
    """Cambia la prioridad de un elemento y lo acomoda en el monticulo"""
    prioridad_anterior = heap.vector[indice][0]
    heap.vector[indice][0] = prioridad
    if(prioridad < prioridad_anterior):
        flotar(heap, indice)
    elif(prioridad > prioridad_anterior):
        hundir(heap, indice)


def monticulizar(heap):
    for i in len(heap.vector):
        flotar(heap)


def heap_vacio(heap):
    if heap.tamanio == 0:
        return True
    else:
        return False
