from tda_lista import Lista, eliminarPrimero, insertar, insertarNodosArbol


class NodoArbol():
    izq, der, info, altura = None, None, None, 0


class NodoArbol2():
    izq, der, info, cod = None, None, None, None


class NodoArbolN():
    hijos, info, altura = Lista(), None, 0


def altura(raiz):
    if raiz is None:
        return 0
    else:
        return raiz.altura


def actualizar_altura(raiz):
    if altura(raiz.izq) > altura(raiz.der):
        raiz.altura = altura(raiz.izq)+1
    else:
        raiz.altura = altura(raiz.der)+1
    return raiz


def insertarArbol(raiz, dato):
    if raiz is None:
        raiz = NodoArbol()
        raiz.info = dato
    else:
        if dato < raiz.info:
            raiz.izq = insertarArbol(raiz.izq, dato)
        else:
            raiz.der = insertarArbol(raiz.der, dato)
    raiz = actualizar_altura(raiz)
    raiz = balancear(raiz)
    return raiz


def insertarTree(raiz, dato):
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


def insertarReportesArmeria(raiz, dato):
    if raiz is None:
        raiz = NodoArbol()
        raiz.info = dato
    else:
        if dato.codigo_blaster < raiz.info.codigo_blaster:
            raiz.izq = insertarReportesArmeria(raiz.izq, dato)
        else:
            raiz.der = insertarReportesArmeria(raiz.der, dato)
    raiz = actualizar_altura(raiz)
    raiz = balancear(raiz)
    return raiz


def arbol_vacio(raiz):
    return raiz is None


def busqueda_desordenados(raiz, buscado, campo=0, pos=0):
    if raiz is not None:
        pos = busqueda_desordenados(raiz.izq, buscado, campo=campo, pos=pos)
        if raiz.info[campo] == buscado:
            pos = raiz
        pos = busqueda_desordenados(raiz.der, buscado, campo=campo, pos=pos)
    return pos


def busqueda_desordenados2(raiz, buscado, pos=0):
    if raiz is not None:
        pos = busqueda_desordenados2(raiz.izq, buscado, pos=pos)
        if raiz.info == buscado:
            pos = raiz
        pos = busqueda_desordenados2(raiz.der, buscado, pos=pos)
    return pos


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


def busqueda_arbolCampo(raiz, buscado, campo=0):
    pos = None
    if raiz is not None:
        if raiz.info[campo] == buscado:
            pos = raiz
        else:
            if buscado < raiz.info[campo]:
                pos = busqueda_arbolCampo(raiz.izq, buscado)
            else:
                pos = busqueda_arbolCampo(raiz.der, buscado)
    return pos


def busqueda_proximidad(raiz, buscado, campo=0):
    pos = None
    if raiz is not None:
        if buscado in raiz.info[campo]:
            pos = raiz
        else:
            if buscado < raiz.info[campo]:
                pos = busqueda_proximidad(raiz.izq, buscado)
            else:
                pos = busqueda_proximidad(raiz.der, buscado)
    return pos


def busquedaProximidadDesordenados(raiz, buscado, campo=0):
    '''Realiza busqueda por proximidad por campo seleccionado'''
    aux = None
    if (raiz is not None):
        if (buscado in raiz.info[campo]):
            return raiz
        else:
            aux = busquedaProximidadDesordenados(raiz.izq, buscado, campo)
            if aux is None:
                aux = busquedaProximidadDesordenados(raiz.der, buscado, campo)
    return aux


def busquedaOcurrenciasProximidad(raiz, buscado, aux=[], campo=0):
    '''Realiza busqueda por proximidad por campo seleccionado'''
    if (raiz is not None):
        if (buscado in raiz.info[campo]):
            aux.append(raiz)
        aux = busquedaOcurrenciasProximidad(raiz.izq, buscado, aux, campo)
        aux = busquedaOcurrenciasProximidad(raiz.der, buscado, aux, campo)
    return aux


def busquedaOcurrencias(raiz, buscado, aux=[], campo=0):
    '''Realiza busqueda por proximidad por campo seleccionado'''
    if (raiz is not None):
        if (buscado == raiz.info[campo]):
            aux.append(raiz)
        aux = busquedaOcurrencias(raiz.izq, buscado, aux, campo)
        aux = busquedaOcurrencias(raiz.der, buscado, aux, campo)
    return aux


def busqueda_arbolAtributoCodigo(raiz, buscado):
    pos = None
    if raiz is not None:
        if raiz.info.codigo_blaster == buscado:
            pos = raiz
        else:
            if buscado < raiz.info.codigo_blaster:
                pos = busqueda_arbolAtributoCodigo(raiz.izq, buscado)
            else:
                pos = busqueda_arbolAtributoCodigo(raiz.der, buscado)
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


def tratar_expresion(a):
    if a.isdigit():
        a = int(a)
        return a
    else:
        return a


def resolver_expresion(raiz, lista):
    if raiz is not None:
        resolver_expresion(raiz.izq, lista)
        lista.append(tratar_expresion(raiz.info))
        resolver_expresion(raiz.der, lista)


def ver_repetidos(raiz, aux, lista_repetidos):
    if raiz is not None:
        ver_repetidos(raiz.izq, aux, lista_repetidos)
        if raiz.info == aux:
            lista_repetidos.append(raiz.info)
        aux = raiz.info
        ver_repetidos(raiz.der, aux, lista_repetidos)
    return lista_repetidos


def pares(raiz, contar_pares, contar_impares):
    if raiz is not None:
        pares(raiz.izq, contar_pares, contar_impares)
        if raiz.info % 2 == 0:
            contar_pares += 1
        else:
            contar_impares += 1
        pares(raiz.der, contar_pares, contar_impares)
    return contar_pares, contar_impares


def reemplazar(raiz):
    aux = None
    if raiz.der is not None:
        raiz.der, aux = reemplazar(raiz.der)
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


def eliminarCampo(raiz, clave, campo=0):
    x = None
    if raiz is not None:
        if clave < raiz.info[campo]:
            raiz.izq, x = eliminarCampo(raiz.izq, clave)
        elif clave > raiz.info[campo]:
            raiz.der, x = eliminarCampo(raiz.der, clave)
        else:
            x = raiz.info[campo]
            if raiz.izq is None:
                raiz = raiz.der
            elif raiz.der is None:
                x = raiz.info[campo]
                raiz = raiz.izq
            else:
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.info[campo] = aux.info[campo]
    return raiz, x


# control = true ; rotar a la derecha | control = False rotar a la izquierda
def rotacion_simple(raiz, control):
    if control:
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz
    actualizar_altura(raiz)
    actualizar_altura(aux)
    raiz = aux
    return raiz


def contar_nodos(arbol, c=0):
    if arbol is not None:
        c = contar_nodos(arbol.izq, c)
        c += 1
        c = contar_nodos(arbol.der, c)
    return c


# control = true ; rotar a la derecha | control = False rotar a la izquierda
def rotacion_doble(raiz, control):
    if control:
        raiz.izq = rotacion_simple(raiz.izq, False)
        raiz = rotacion_simple(raiz, True)
    else:
        raiz.der = rotacion_simple(raiz.der, True)
        raiz = rotacion_simple(raiz, False)
    return raiz


def balancear(raiz):
    if raiz is not None:
        if altura(raiz.izq) - altura(raiz.der) == 2:
            if altura(raiz.izq.izq) >= altura(raiz.izq.der):
                raiz = rotacion_simple(raiz, True)
            else:
                raiz = rotacion_doble(raiz, True)
        elif altura(raiz.der) - altura(raiz.izq) == 2:
            if altura(raiz.der.der) >= altura(raiz.der.izq):
                raiz = rotacion_simple(raiz, False)
            else:
                raiz = rotacion_doble(raiz, False)
    return raiz


def imprimirArbol(raiz, espacios=0):
    ''' Imprime arbol, girado hacia la izquierda'''
    if raiz is not None:
        espacios += 5
        imprimirArbol(raiz.der, espacios)
        print(" " * espacios, str(raiz.info))
        imprimirArbol(raiz.izq, espacios)


def nodos_nivel(nivel):
    """Devuelve la cantidad de nodos tiene el nivel si esta completo"""
    nivel -= 1
    return 2**nivel


def arbol_completo(arbol):
    alt = altura(arbol)
    cantidad_nodos = 0
    for i in range(0, alt):
        cantidad_nodos = cantidad_nodos + (2**i)
    if contar_nodos(arbol) == cantidad_nodos:
        return True
    else:
        return False


def es_hoja(nodo):
    if nodo.izq is None and nodo.der is None:
        return True
    else:
        return False


def ArbolHuffman(lista):
    '''Devuelve la raiz de un arbol de huffman a partir de tabla de
    concurrencias dada'''
    while lista.tamanio > 1:
        nod1 = eliminarPrimero(lista)
        nod2 = eliminarPrimero(lista)
        info = [(nod1.info.info[0]+nod2.info.info[0]), None]
        nod3 = NodoArbol()
        nod3.info = info
        nod3.izq = nod1.info
        nod3.der = nod2.info
        insertarNodosArbol(lista, nod3)

    return lista.inicio.info
