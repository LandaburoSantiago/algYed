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
    while heap.vector[padre] < heap.vector[indice] and padre >= 0:
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
        if hd <= heap.tamanio - 1 and heap.vector[hd] > heap.vector[hi]:
            may = hd
        if heap.vector[indice] < heap.vector[may]:
            heap.vector[indice], heap.vector[may] = heap.vector[may], heap.vector[indice]
        else:
            control = False
        hi = (2*may)+1


def atencion(heap):
    aux = quitar(heap)
    return aux


def heapsort(heap):
    """Metodo de ordenamiento monticulo"""
    aux = heap.tamanio
    for i in range(0, heap.tamanio-1):
        quitar(heap)
    heap.tamanio = aux


def monticulizar(heap):
    for i in len(heap.vector):
        flotar(heap)


h = Heap(20)
for i in range(0, 10):
    agregar(h, random.randint(0, 100))


print(h.vector)
vec = [None]*10
for i in range(0, 10):
    print(atencion(h))


print(vec)
