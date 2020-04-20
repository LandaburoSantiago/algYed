class NodoArbol():
    izq, der, info = None, None, None


class NodoArbol2():
    izq, der, info, cod = None, None, None, None


def insertarArbol(raiz, dato):
    if raiz is None:
        raiz = NodoArbol()
        raiz.info = dato
    else:
        if dato < raiz.info:
            raiz.izq = insertarArbol(raiz.izq, dato)
        else:
            raiz.der = insertarArbol(raiz.der, dato)

    return raiz


def insertarArbol2(raiz, dato, codigo):
    if raiz is None:
        raiz = NodoArbol()
        raiz.info = dato
        raiz.cod = codigo
    else:
        if codigo < raiz.cod:
            raiz.izq = insertarArbol2(raiz.izq, dato, codigo)
        else:
            raiz.der = insertarArbol2(raiz.der, dato, codigo)

    return raiz


def arbol_vacio(raiz):
    return raiz is None


def busqueda_arbol(raiz, buscado):
    pos = None
    if raiz is not None:
        if raiz.info == buscado:
            pos = raiz
        else:
            if buscado < raiz.info:
                pos = busqueda_arbol(raiz.izq, buscado)
            else:
                pos = busqueda_arbol(raiz.der, buscado)
    return pos


# BARRIDOS
def preorden(raiz):
    if raiz is not None:
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)


def postorden(raiz):
    if raiz is not None:
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)





def reemplazar(raiz):
    aux = None
    if raiz.der is not None:
        raiz.der = reemplazar(raiz.der)
    else:
        aux = raiz
        raiz = raiz.izq

    return raiz, aux


def eliminar(raiz, clave):
    x = None
    if raiz is not None:
        if clave < raiz.info:
            raiz.izq, x = eliminar(raiz.izq, clave)
        elif clave > raiz.info:
            raiz.der, x = eliminar(raiz.der, clave)
        else:
            x = raiz.info
            if raiz.izq is None:
                raiz = raiz.der
            elif raiz.der is None:
                x = raiz.info
                raiz = raiz.izq
            else:
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.info = aux.info
    return raiz, x
