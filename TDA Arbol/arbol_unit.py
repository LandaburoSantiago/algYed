from tda_arbol import NodoArbol, NodoArbol2, insertarArbol, insertarArbol2, arbol_vacio, busqueda_arbol, preorden, inorden, postorden, reemplazar


def arbolMorse():
    lista_morse = [' ', 'E', 'T', 'I', 'A', 'N', 'M', 'S', 'U', 'R', 'W', 'D', 'K', 'G', 'O', 'H', 'V', 'F', ' ', 'L', ' ', 'P', 'J', 'B', 'X', 'C', 'Y', 'Z', 'Q', ' ', ' ', '5', '4', '3', '2', '1', '6', '7', '8', '9', '0']
    cod = [1000, 500, 1500, 250, 750, 1250, 1750, 225, 275, 725, 775, 1225, 1275, 1725, 1775, 112, 237, 265, 285, 612, 737, 765, 785, 1112, 1237, 1265, 1285, 1612, 1737, 1765, 1785, 55, 115, 247, 747, 795,1055, 1606, 1755, 1778, 1788]
    raiz = None
    for i in range(0, len(lista_morse)):
        raiz = insertarArbol2(raiz, lista_morse[i], cod[i])
    return raiz

# print(raiz.info)
# print(raiz.izq.info)
# print(raiz.der.info)
# izquierda = raiz.izq
# derecha = raiz.der
# print(izquierda.izq.info)
# print(izquierda.der.info)
# print(derecha.izq.info)
# print(derecha.der.info)

# var = raiz.izq
# var = var.der
# var = var.der
# var = var.izq
# print(var.info)


def descodificar(arbol, codigo):
    tam = len(codigo)
    aux = arbol
    descodificado = ''
    for i in range(0, tam):
        if codigo[i] == ' ':
            descodificado = descodificado + aux.info
            aux = arbol
        if codigo[i] == '.':
            if aux.izq is None:
                descodificado = descodificado + aux.info
                aux = arbol
            else:
                aux = aux.izq
        if codigo[i] == '-':
            if aux.der is None:
                descodificado = descodificado + aux.info
                aux = arbol
            else:
                aux = aux.der
        if codigo[i] == '/':
            descodificado = descodificado + ' '
            aux = arbol

    return descodificado
