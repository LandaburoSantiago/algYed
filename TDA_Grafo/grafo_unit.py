from TDA_Grafo import Grafo, nodoVertice, nodoArista
from TDA_Grafo import insertar_vertice, insertar_arista, verVerticeAristas, barrido_amplitud, buscar_vertice, buscar_adyacentes
from TDA_Grafo import eliminar_vertice, verticeCA
import random
import string


# Ejercicio 1
def aleatorio():
    grafo = Grafo()
    listaVertices = []
    aristas = [30, 3, 74, 1, 42, 19, 22, 12, 15, 20, 21, 9, 2, 14, 47, 66, 78, 70, 11, 57, 93, 7, 5, 3, 33, 89, 65, 64, 23, 40]
    # Armando Grafo
    for i in range(0, 15):
        ran = random.choice(string.ascii_letters)
        listaVertices.append(ran)
        insertar_vertice(grafo, ran)
    for i in aristas:
        insertar_arista(grafo, i, listaVertices[random.randint(0, len(listaVertices)-1)], listaVertices[random.randint(0, len(listaVertices)-1  )])

    """ INCISO A"""
    # Para buscar los desconectados primero enliste los vertices que no tienen lista de aristas
    auxGrafo = grafo.inicio
    verticesSinAristas = []
    while auxGrafo is not None:
        if auxGrafo.adyacentes.tamanio == 0:
            verticesSinAristas.append(auxGrafo)
        auxGrafo = auxGrafo.sig

    # Busque en los adyacentes de cada vertice los vertices que obtuve en el algoritmo anterior
    desconectados = []
    auxGrafo = grafo.inicio
    aux = ''
    for i in range(0, len(verticesSinAristas)):
        # Variable 'loApuntan' es para controlar si el vertice evaluado esta en alguna lista de adyasencia de algun otro vertice
        loApuntan = False
        while auxGrafo is not None:
            if auxGrafo.adyacentes.tamanio != 0:
                aux = buscar_adyacentes(auxGrafo, verticesSinAristas[i].info)
            if aux != -1:
                loApuntan = True
            auxGrafo = auxGrafo.sig
        if loApuntan is False:
            desconectados.append(verticesSinAristas[i])

    # Y en 'desconectados' se almacenan esos vertices osea los que no tienen lista de aristas
    # y los que no son apuntados por ningun otro vertice
    print('Se eliminan los desconectados...')
    for i in desconectados:
        print(eliminar_vertice(grafo, i.info))

    """INCISO B"""
    # Auxiliar con el inicio del grafo
    auxGrafo = grafo.inicio
    # Inicializamos una variable con el primer nodo del grafo para controlar el mayor
    may = auxGrafo
    # Inicializamos una lista por si los mayores son mas de uno
    mayores = []
    # Iteramos por todos los vertices del grafo
    while auxGrafo is not None:
        # algoritmo para determinar la meyor cantidad de adyacentes por cada vertice
        if auxGrafo.adyacentes.tamanio > may.adyacentes.tamanio:
            may = auxGrafo
        auxGrafo = auxGrafo.sig
    # inicializamos nuevamente una variable con el inicio del grafo
    auxGrafo = grafo.inicio
    # lo agregamos a la lista que va a contener a los mayores
    mayores.append(may)
    while auxGrafo is not None:
        # Algoritmo para determinar si hay otros grafos con la misma cantidad de aristas que el mayor
        if auxGrafo != may:
            if auxGrafo.adyacentes.tamanio == may.adyacentes.tamanio:
                mayores.append(auxGrafo)
        auxGrafo = auxGrafo.sig

    print('El/los nodo con mayor cantidad de aristas es...')
    for i in mayores:
        print(i.info)

    """INCISO C"""
    # Inicializamos una variable con el inicio del grafo
    verticeBuscado = grafo.inicio
    vertices = []
    i = 0
    while verticeBuscado is not None:
        auxGrafo = grafo.inicio
        verAux = [None, 0]
        verAux[0] = verticeBuscado
        while auxGrafo is not None:
            aux = buscar_adyacentes(auxGrafo, verticeBuscado.info)
            if aux != -1:
                verAux[1] += 1
            auxGrafo = auxGrafo.sig
        vertices.append(verAux)
        verticeBuscado = verticeBuscado.sig
    may = vertices[0]
    for i in vertices:
        if i[1] > may[1]:
            may = i
    print('El/los nodos que mas aristas llegan a el son')
    for i in vertices:
        if i[1] == may[1]:
            print(i[0].info, 'le llegan', i[1], 'aristas.')

    """INCISO D"""
    # Ya habia hecho una lista con vertices que no tienen aristas
    print('Los vertices que no tienen aristas, por lo tanto no conectan a ningun otro nodo son...')
    for i in verticesSinAristas:
        print(i.info)
    """INCISO E"""
    # Usando el atributo tamanio de el grafo saque la cantidad de nodos que tiene
    print('El grafo esta compuesto por: ', grafo.tamanio)
    """INCISO F"""
    # Inicializando variable contador en 0
    c = 0
    # inicializando auxiliar para manejar el grafo
    auxGrafo = grafo.inicio
    while auxGrafo is not None:
        # Realizo una busceda en la lista de ayasencia con su propio info
        aux = buscar_adyacentes(auxGrafo, auxGrafo.info)
        if aux != -1:
            # si la funcion me devuelve distinto de -1 quiere decir que encntro
            c += 1
        auxGrafo = auxGrafo.sig
    print('La cantidad de nodos que tiene una arista hacia si mismo son: ', c)

    """INCISO G"""
    # Inicializamos variable para manejar el grafo
    auxGrafo = grafo.inicio
    # Inicializamos variable con el primer nodo de la lista de adyasencia
    may = auxGrafo.adyacentes.inicio
    # Inicializamos variable para almacenar el Origen
    origen = None
    while auxGrafo is not None:
        # por cada vertice inicializamos la variable aristas con el inicio de la lista de adyasencia
        aristas = auxGrafo.adyacentes.inicio
        while aristas is not None:
            if aristas.peso > may.peso:
                origen = auxGrafo
                may = aristas
            aristas = aristas.sig
        auxGrafo = auxGrafo.sig

    print('Origen: ', origen.info, 'Destino: ', may.destino, 'Peso: ', may.peso)


aleatorio()
