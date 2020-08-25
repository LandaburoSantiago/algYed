import random
import math

# NO HACE 11, 12, 13, 16, 19


class NodoLista():
    info = None
    sig = None

    def __str__(self):
        return "Info: " + str(self.info) + "Sig: " + str(self.sig)


class Lista():
    def __init__(self):
        self.tamanio = 0
        self.inicio = None


""" l= lista, dato= dato a cargar, campo= indice por el cual se ordena"""


def insertar(l, dato):
    """Inserta en lista, elemento deseado"""
    nodo = NodoLista()
    nodo.info = dato
    if (l.inicio is None) or (nodo.info < l.inicio.info):  # Si esta vacia o es el primero
        nodo.sig = l.inicio
        l.inicio = nodo
    else:  # Si va al medio o a lo ultimo
        anterior = l.inicio
        actual = l.inicio.sig
        while (actual is not None) and (actual.info <= nodo.info):
            actual = actual.sig
            anterior = anterior.sig
        nodo.sig = actual
        anterior.sig = nodo
    l.tamanio += 1


def insertarNodosArbol(l, dato):
    """Inserta en lista, elemento deseado"""
    nodo = NodoLista()
    nodo.info = dato
    if (l.inicio is None) or (nodo.info.info < l.inicio.info.info):  # Si esta vacia o es el primero
        nodo.sig = l.inicio
        l.inicio = nodo
    else:  # Si va al medio o a lo ultimo
        anterior = l.inicio
        actual = l.inicio.sig
        while (actual is not None) and (actual.info.info <= nodo.info.info):
            actual = actual.sig
            anterior = anterior.sig
        nodo.sig = actual
        anterior.sig = nodo
    l.tamanio += 1


def insertarEn(l, dato, pos):
    nodo = NodoLista()
    nodo.info = dato
    aux = l.inicio
    if (pos >= 0) and (pos <= l.tamanio):
        if (pos == 0):
            nodo.sig = l.inicio
            l.inicio = NodoLista()
        elif (pos < l.tamanio):
            for i in range(1, pos):
                aux = aux.sig
            nodo.sig = aux.sig
            aux.sig = nodo
        else:
            while aux.sig is not None:
                aux = aux.sig
            aux.sig = nodo
        l.tamanio += 1
    else:
        print("El indice " + str(pos) + " excede el tamanio de elementos que ")
        print("posee la lista")


def eliminarPrimero(l):
    out = l.inicio
    l.inicio = l.inicio.sig
    l.tamanio -= 1
    return out


def eliminar(l, dato, campo=0):
    """Elimina de la lista, el elemento deseado"""
    out = None
    if (l.inicio.info == dato):
        out = l.inicio.info
        l.inicio = l.inicio.sig
        l.tamanio -= 1
    else:
        anterior = l.inicio
        actual = anterior.sig
        while (actual is not None) and (actual.info[campo] < dato):  # Todo esto teniendo en cuenta que la lista va a estar ordenada
            actual = actual.sig
            anterior = anterior.sig
        if (actual is not None) and (actual.info[campo] == dato):  # Si el elemento no estaba al final de la lista
            out = actual.info                           # Y lo encontre
            anterior.sig = actual.sig
            l.tamanio -= 1

    return out


def eliminarTodos(l, dato):
    """Elimina de la lista toda las ocurrencias del dato ingresado"""
    if (l.inicio.info == dato):
        dato = l.inicio.info
        l.inicio = l.inicio.sig
        l.tamanio -= 1
    else:
        anterior = l.inicio
        actual = anterior.sig
        while (actual is not None) and (actual.info < dato):  # Todo esto teniendo en cuenta que la lista va a estar ordenada
            actual = actual.sig
            anterior = anterior.sig

        if actual is not None:
            while (actual is not None) and (actual.info == dato):
                actual = actual.sig
                l.tamanio -= 1
            anterior.sig = actual


def barridoLista(l):
    """Barrido de lista, imprimiendo en pantalla el elemento de cada nodo"""
    aux = l.inicio
    while (aux is not None):
        print(str(aux.info))
        aux = aux.sig


def busquedaLista(l, buscado, campo=0):
    """Devuelve posicion. -1 si no se encontro lo buscado"""
    pos = -1
    i = -1
    aux = l.inicio
    while (aux is not None) and (pos == -1):
        i += 1
        if (aux.info.info[campo] == buscado):
            pos = i
        aux = aux.sig

    return pos


def obtener_ultimo(l):
    aux = l.inicio
    ultimo = 0
    while (aux.sig is not None):
        ultimo = aux.sig.info
        aux = aux.sig

    return ultimo


def lista_vacia(l):
    return l.tamanio == 0
