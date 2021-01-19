from TDA_Grafo import Grafo, nodoVertice, nodoArista, eliminar_arista
from TDA_Grafo import insertar_vertice, insertar_arista, verVerticeAristas, barrido_amplitud, buscar_vertice, buscar_adyacentes
from TDA_Grafo import eliminar_vertice, dijkstra, kruskal, caminoMasCorto, barrido_profundidad, marcar_no_visitado, insertar_aristaPunto8
from TDA_Grafo import dijkstraPunto8, caminoMasCortoPunto8, caminoMasCortoAristas, caminoMasCortoPunto9, caminoMasCortoPunto10
from TDA_Grafo import caminoMasCortoAristasPunto5
from tda_pila import barrido, desapilar, pila_vacia, apilar, Pila
from cargar_info import redPunto4
import random
import string


# Ejercicio 1
def aleatorio():
    grafo = Grafo()
    listaVertices = []
    aristas = [30, 3, 74, 1, 42, 19, 22, 12, 15, 20, 21, 9, 2, 14, 47, 66, 78, 70, 11, 57, 93, 7, 5, 3, 33, 89, 65, 64, 23, 40]
    # Armando Grafob

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


# Ejercicio 2

def digrafo():
    grafo = Grafo(dirigido=True)
    gNodirigido = Grafo(dirigido=False)
    vertices = ['A', 'B', 'C', 'D', 'E']
    """INCISO A Y B"""
    for i in vertices:
        insertar_vertice(grafo, i)
        insertar_vertice(gNodirigido, i)

    insertar_arista(grafo, 1, 'A', 'B')
    insertar_arista(grafo, 17, 'A', 'C')
    insertar_arista(grafo, 24, 'A', 'E')
    insertar_arista(grafo, 2, 'B', 'C')
    insertar_arista(grafo, 2, 'C', 'B')
    insertar_arista(grafo, 3, 'C', 'D')
    insertar_arista(grafo, 11, 'D', 'D')
    insertar_arista(gNodirigido, 4, 'A', 'B')
    insertar_arista(gNodirigido, 9, 'A', 'C')
    insertar_arista(gNodirigido, 5, 'A', 'E')
    insertar_arista(gNodirigido, 12, 'B', 'C')
    insertar_arista(gNodirigido, 1, 'C', 'D')

    arbolExpansionMinima = kruskal(gNodirigido)
    """INCISO C"""
    print('Arbol de expansion minima: ')
    print(arbolExpansionMinima)

    """INCISO D"""
    insertar_arista(grafo, random.randint(0, 100), 'E', 'C')
    """INCISO E"""
    caminoMasCorto(grafo, 'A', 'D')


# Ejercicio 3

def empresaTelefonica():
    antenas = Grafo(dirigido=False)
    codigo = ['A', 'U', 'R', 'W', 'L', 'X', 'E', 'Y']
    latitud = [10.599, 17.3945, 38.68329, 11.003, 9.5532, 12.5542, 20.771, -12.40484]
    longitud = [5.249, -12.1297, 8.7822, -6.3573, 14.77322, -22.1232, 14.41712, 7.85246]
    velocidad = [5, 10, 20, 10, 8, 5, 10, 20]

    for i in range(0, len(codigo)):
        infoAntena = {
            'codigo': codigo[i],
            'ubicacion': [latitud[i], longitud[i]],
            'velocidad': velocidad[i]
        }
        insertar_vertice(antenas, infoAntena, 'codigo')

    insertar_arista(antenas, 200, 'A', 'E', 'codigo')
    insertar_arista(antenas, 350, 'E', 'Y', 'codigo')
    insertar_arista(antenas, 1000, 'X', 'W', 'codigo')
    insertar_arista(antenas, 550, 'Y', 'R', 'codigo')
    insertar_arista(antenas, 50, 'W', 'L', 'codigo')
    insertar_arista(antenas, 90, 'L', 'Y', 'codigo')
    insertar_arista(antenas, 85, 'A', 'X', 'codigo')
    insertar_arista(antenas, 150, 'X', 'R', 'codigo')
    insertar_arista(antenas, 76, 'R', 'U', 'codigo')
    """INCISO C"""
    print('El tamanio del grafo es de: ', antenas.tamanio, 'nodos.')
    """INCISO D"""
    print('El camino mas corto para transmitir de la antena X a la Y es:')
    caminoMasCorto(antenas, 'X', 'Y', 'codigo')
    """INCISO E"""
    print('El arbol de expansion minima es;')
    expansionMinima = kruskal(antenas, 'codigo')
    print(expansionMinima)
    """INCISO F"""
    print('Info de la antena X')
    buscado = buscar_vertice(antenas, 'X', 'codigo')
    print(buscado.info)


# EJERCICIO 4
def red_local():
    localhost = redPunto4()
    insertar_arista(localhost, 3, 'Arch', 'Switch02', 'nombre')
    """Al insertar la arista de Fedora con Switch 2 el algorimo de dijkstra no funciona bien"""
    # insertar_arista(localhost, 56, 'Switch02', 'Fedora', 'nombre')
    insertar_arista(localhost, 5, 'Parrot', 'Switch02', 'nombre')
    insertar_arista(localhost, 12, 'MongoDB', 'Switch02', 'nombre')
    insertar_arista(localhost, 40, 'Manjaro', 'Switch02', 'nombre')
    insertar_arista(localhost, 61, 'Switch02', 'Router03', 'nombre')
    insertar_arista(localhost, 25, 'Red Hat', 'Router02', 'nombre')
    insertar_arista(localhost, 9, 'Guarani', 'Router02', 'nombre')
    insertar_arista(localhost, 50, 'Router02', 'Router03', 'nombre')
    insertar_arista(localhost, 37, 'Router02', 'Router01', 'nombre')
    insertar_arista(localhost, 43, 'Router01', 'Router03', 'nombre')
    insertar_arista(localhost, 29, 'Router01', 'Switch01', 'nombre')
    insertar_arista(localhost, 80, 'Mint', 'Switch01', 'nombre')
    insertar_arista(localhost, 22, 'Printer', 'Switch01', 'nombre')
    insertar_arista(localhost, 18, 'Ubuntu', 'Switch01', 'nombre')
    insertar_arista(localhost, 17, 'Debian', 'Switch01', 'nombre')

    """INCISO B"""
    manjaro = buscar_vertice(localhost, 'Manjaro', 'nombre')
    red_hat = buscar_vertice(localhost, 'Red Hat', 'nombre')
    fedora = buscar_vertice(localhost, 'Fedora', 'nombre')
    print('Barrido en profundidad desde Manjaro')
    barrido_profundidad(localhost, manjaro, 'nombre')
    print('Barrido en amplitud desde Manjaro')
    barrido_amplitud(localhost, manjaro, 'nombre')
    print('Barrido en profundidad desde Red Hat')
    marcar_no_visitado(localhost)
    barrido_profundidad(localhost, red_hat, 'nombre')
    print('Barrido en amplitud desde Red Hat')
    barrido_amplitud(localhost, red_hat, 'nombre')
    print('Barrido en profundidad desde Fedora')
    marcar_no_visitado(localhost)
    barrido_profundidad(localhost, fedora, 'nombre')
    print('Barrido en amplitud desde Fedora')
    barrido_amplitud(localhost, fedora, 'nombre')

    """INCISO C"""
    print('El camino mas corto para imprimir desde Manjaro es: ')
    caminoMasCorto(localhost, 'Manjaro', 'Printer', 'nombre')
    print('El camino mas corto para imprimir desde Red Hat es: ')
    caminoMasCorto(localhost, 'Red Hat', 'Printer', 'nombre')
    print('El camino mas corto para imprimir desde Fedora es: ')
    caminoMasCorto(localhost, 'Fedora', 'Printer', 'nombre')

    """INCISO D"""
    print('Arbol de expansion minima: ')
    expansionMinima = kruskal(localhost, 'nombre')
    print(expansionMinima)

    """A PARTIR DE ACA NO ANDA NADA """
    """INCISO E"""
    vertice = localhost.inicio
    caminos = []
    # Buscando todos los vertices de tipo "PC"
    while vertice is not None:
        if vertice.info['tipo'] == 'PC':
            caminos.append(dijkstra(localhost, vertice.info, 'Guarani', 'nombre'))
        vertice = vertice.sig

    """Tampoco me anda dijkstra para las PC FEDORA, MINT, UBUNTU"""
    pesos = []
    for i in caminos:
        destino = 'Guarani'
        pila = Pila()
        while(not pila_vacia(i)):
            dato = desapilar(i)
            if(destino == dato[1][0].info['nombre']):
                apilar(pila, dato)
                destino = dato[1][1]
        while(not pila_vacia(pila)):
            peso = desapilar(pila)
        pesos.append(peso)

    """INCISO F"""
    switch01 = buscar_vertice(localhost, 'Switch01', 'nombre')
    adyacentes = switch01.adyacentes.inicio
    pc = []
    while adyacentes is not None:
        if adyacentes.destino['tipo'] == 'PC':
            pc.append(adyacentes.destino)
        adyacentes = adyacentes.sig
    caminoMasCorto(localhost, 'Mint', 'MongoDB', 'nombre')

    """INCISO G"""
    # eliminar_arista


# EJERCICIO 5
def dioses():
    dioses_griegos = ['ouranos', 'gaia', 'themis', 'minemosyne', 'hyperion',
                        'theia', 'krios', 'kronos', 'rhea', 'kdios','phoibe', 'iapetos',
                        'okeanos', 'tethys', 'helios', 'eos', 'selene', 'prometheus',
                        'epimetheus', 'atlas', 'pleione', 'hades', 'demeter', 'poseidon','hestia', 'hera',
                        'zeus', 'leto', 'semele', 'maia', 'persephone', 'aphrodite', 'ares',
                        'hephaistos', 'athena', 'apollo', 'artemis', 'dionysos', 'hermes',
                        'penelopeia', 'phobos', 'deimos', 'eros', 'himerios',
                        'hermaprhodite', 'pan']
    arbol_genealogico = Grafo()
    for i in dioses_griegos:
        insertar_vertice(arbol_genealogico, i)

    aux = arbol_genealogico.inicio

    """ INCISO B """
    """ INICIO DE LA CARGA DE LAS RELACIONES """
    # Insertando aristas
    insertar_arista(arbol_genealogico, 'hijo', 'gaia', 'ouranos')
    insertar_arista(arbol_genealogico, 'madre', 'ouranos', 'gaia')
    insertar_arista(arbol_genealogico, 'pareja', 'ouranos', 'gaia')

    insertar_arista(arbol_genealogico, 'hijo', 'ouranos', 'themis')
    insertar_arista(arbol_genealogico, 'hijo', 'ouranos', 'minemosyne')
    insertar_arista(arbol_genealogico, 'hijo', 'ouranos', 'hyperion')
    insertar_arista(arbol_genealogico, 'hijo', 'ouranos', 'theia')
    insertar_arista(arbol_genealogico, 'hijo', 'ouranos', 'krios')
    insertar_arista(arbol_genealogico, 'hijo', 'ouranos', 'kronos')
    insertar_arista(arbol_genealogico, 'hijo', 'ouranos', 'rhea')
    insertar_arista(arbol_genealogico, 'hijo', 'ouranos', 'kdios')
    insertar_arista(arbol_genealogico, 'hijo', 'ouranos', 'phoibe')
    insertar_arista(arbol_genealogico, 'hijo', 'ouranos', 'iapetos')
    insertar_arista(arbol_genealogico, 'hijo', 'ouranos', 'okeanos')
    insertar_arista(arbol_genealogico, 'hijo', 'ouranos', 'tethys')

    # Buscamos el vertice del padre
    padre = buscar_vertice(arbol_genealogico, 'ouranos')
    relaciones_padre = padre.adyacentes.inicio
    madre = None
    encontrado = False
    # En sus relaciones buscamos a su pareja
    while relaciones_padre is not None and encontrado is False:
        if relaciones_padre.peso == 'pareja':
            madre = buscar_vertice(arbol_genealogico, relaciones_padre.destino)
            # Creamos la relacion de la madre con el padre
            insertar_arista(arbol_genealogico, 'pareja', madre.info, padre.info)
            encontrado = True
        relaciones_padre = relaciones_padre.sig

    # Creamos la relacion de madre de la pareja con sus hijos
    # Creamos la relacion de cada hijo con la madre
    # Creamos la relacion de cada hijo con el padre
    relaciones_padre = padre.adyacentes.inicio
    while relaciones_padre is not None:
        if relaciones_padre.peso == 'hijo':
            aux_relaciones = padre.adyacentes.inicio
            while aux_relaciones is not None:
                if relaciones_padre.destino != aux_relaciones.destino:
                    if aux_relaciones.peso == 'hijo':
                        insertar_arista(arbol_genealogico, 'hermano', relaciones_padre.destino, aux_relaciones.destino)
                aux_relaciones = aux_relaciones.sig
            insertar_arista(arbol_genealogico, 'hijo', madre.info, relaciones_padre.destino)
            insertar_arista(arbol_genealogico, 'madre', relaciones_padre.destino, madre.info)
            insertar_arista(arbol_genealogico, 'padre', relaciones_padre.destino, padre.info)
        relaciones_padre = relaciones_padre.sig

    insertar_arista(arbol_genealogico, 'pareja', 'hyperion', 'theia')
    insertar_arista(arbol_genealogico, 'hijo', 'hyperion', 'helios')
    insertar_arista(arbol_genealogico, 'hijo', 'hyperion', 'eos')
    insertar_arista(arbol_genealogico, 'hijo', 'hyperion', 'selene')

    # Buscamos el vertice del padre
    padre = buscar_vertice(arbol_genealogico, 'hyperion')
    relaciones_padre = padre.adyacentes.inicio
    madre = None
    encontrado = False
    # En sus relaciones buscamos a su pareja
    while relaciones_padre is not None and encontrado is False:
        if relaciones_padre.peso == 'pareja':
            madre = buscar_vertice(arbol_genealogico, relaciones_padre.destino)
            # Creamos la relacion de la madre con el padre
            insertar_arista(arbol_genealogico, 'pareja', madre.info, padre.info)
            encontrado = True
        relaciones_padre = relaciones_padre.sig

    # Creamos la relacion de madre de la pareja con sus hijos
    # Creamos la relacion de cada hijo con la madre
    # Creamos la relacion de cada hijo con el padre
    relaciones_padre = padre.adyacentes.inicio
    while relaciones_padre is not None:
        if relaciones_padre.peso == 'hijo':
            aux_relaciones = padre.adyacentes.inicio
            while aux_relaciones is not None:
                if relaciones_padre.destino != aux_relaciones.destino:
                    if aux_relaciones.peso == 'hijo':
                        insertar_arista(arbol_genealogico, 'hermano', relaciones_padre.destino, aux_relaciones.destino)
                aux_relaciones = aux_relaciones.sig
            insertar_arista(arbol_genealogico, 'hijo', madre.info, relaciones_padre.destino)
            insertar_arista(arbol_genealogico, 'madre', relaciones_padre.destino, madre.info)
            insertar_arista(arbol_genealogico, 'padre', relaciones_padre.destino, padre.info)
        relaciones_padre = relaciones_padre.sig

    insertar_arista(arbol_genealogico, 'pareja', 'kronos', 'rhea')
    insertar_arista(arbol_genealogico, 'hijo', 'kronos', 'hades')
    insertar_arista(arbol_genealogico, 'hijo', 'kronos', 'demeter')
    insertar_arista(arbol_genealogico, 'hijo', 'kronos', 'poseidon')
    insertar_arista(arbol_genealogico, 'hijo', 'kronos', 'hestia')
    insertar_arista(arbol_genealogico, 'hijo', 'kronos', 'hera')
    insertar_arista(arbol_genealogico, 'hijo', 'kronos', 'zeus')

    # Buscamos el vertice del padre
    padre = buscar_vertice(arbol_genealogico, 'kronos')
    relaciones_padre = padre.adyacentes.inicio
    madre = None
    encontrado = False
    # En sus relaciones buscamos a su pareja
    while relaciones_padre is not None and encontrado is False:
        if relaciones_padre.peso == 'pareja':
            madre = buscar_vertice(arbol_genealogico, relaciones_padre.destino)
            # Creamos la relacion de la madre con el padre
            insertar_arista(arbol_genealogico, 'pareja', madre.info, padre.info)
            encontrado = True
        relaciones_padre = relaciones_padre.sig

    # Creamos la relacion de madre de la pareja con sus hijos
    # Creamos la relacion de cada hijo con la madre
    # Creamos la relacion de cada hijo con el padre
    relaciones_padre = padre.adyacentes.inicio
    while relaciones_padre is not None:
        if relaciones_padre.peso == 'hijo':
            aux_relaciones = padre.adyacentes.inicio
            while aux_relaciones is not None:
                if relaciones_padre.destino != aux_relaciones.destino:
                    if aux_relaciones.peso == 'hijo':
                        insertar_arista(arbol_genealogico, 'hermano', relaciones_padre.destino, aux_relaciones.destino)
                aux_relaciones = aux_relaciones.sig
            insertar_arista(arbol_genealogico, 'hijo', madre.info, relaciones_padre.destino)
            insertar_arista(arbol_genealogico, 'madre', relaciones_padre.destino, madre.info)
            insertar_arista(arbol_genealogico, 'padre', relaciones_padre.destino, padre.info)
        relaciones_padre = relaciones_padre.sig

    insertar_arista(arbol_genealogico, 'pareja', 'kdios', 'phoibe')
    insertar_arista(arbol_genealogico, 'hijo', 'kdios', 'leto')

    # Buscamos el vertice del padre
    padre = buscar_vertice(arbol_genealogico, 'kdios')
    relaciones_padre = padre.adyacentes.inicio
    madre = None
    encontrado = False
    # En sus relaciones buscamos a su pareja
    while relaciones_padre is not None and encontrado is False:
        if relaciones_padre.peso == 'pareja':
            madre = buscar_vertice(arbol_genealogico, relaciones_padre.destino)
            # Creamos la relacion de la madre con el padre
            insertar_arista(arbol_genealogico, 'pareja', madre.info, padre.info)
            encontrado = True
        relaciones_padre = relaciones_padre.sig

    # Creamos la relacion de madre de la pareja con sus hijos
    # Creamos la relacion de cada hijo con la madre
    # Creamos la relacion de cada hijo con el padre
    relaciones_padre = padre.adyacentes.inicio
    while relaciones_padre is not None:
        if relaciones_padre.peso == 'hijo':
            aux_relaciones = padre.adyacentes.inicio
            while aux_relaciones is not None:
                if relaciones_padre.destino != aux_relaciones.destino:
                    if aux_relaciones.peso == 'hijo':
                        insertar_arista(arbol_genealogico, 'hermano', relaciones_padre.destino, aux_relaciones.destino)
                aux_relaciones = aux_relaciones.sig
            insertar_arista(arbol_genealogico, 'hijo', madre.info, relaciones_padre.destino)
            insertar_arista(arbol_genealogico, 'madre', relaciones_padre.destino, madre.info)
            insertar_arista(arbol_genealogico, 'padre', relaciones_padre.destino, padre.info)
        relaciones_padre = relaciones_padre.sig

    insertar_arista(arbol_genealogico, 'hijo', 'iapetos', 'prometheus')
    insertar_arista(arbol_genealogico, 'hijo', 'iapetos', 'epimetheus')
    insertar_arista(arbol_genealogico, 'hijo', 'iapetos', 'atlas')

    padre = buscar_vertice(arbol_genealogico, 'iapetos')
    relaciones_padre = padre.adyacentes.inicio
    encontrado = False
    # Creamos la relacion de cada hijo con el padre
    while relaciones_padre is not None:
        if relaciones_padre.peso == 'hijo':
            aux_relaciones = padre.adyacentes.inicio
            while aux_relaciones is not None:
                if relaciones_padre.destino != aux_relaciones.destino:
                    if aux_relaciones.peso == 'hijo':
                        insertar_arista(arbol_genealogico, 'hermano', relaciones_padre.destino, aux_relaciones.destino)
                aux_relaciones = aux_relaciones.sig
            insertar_arista(arbol_genealogico, 'padre', relaciones_padre.destino, padre.info)
        relaciones_padre = relaciones_padre.sig

    insertar_arista(arbol_genealogico, 'pareja', 'okeanos', 'tethys')
    insertar_arista(arbol_genealogico, 'hijo', 'okeanos', 'pleione')

    # Buscamos el vertice del padre
    padre = buscar_vertice(arbol_genealogico, 'okeanos')
    relaciones_padre = padre.adyacentes.inicio
    madre = None
    encontrado = False
    # En sus relaciones buscamos a su pareja
    while relaciones_padre is not None and encontrado is False:
        if relaciones_padre.peso == 'pareja':
            madre = buscar_vertice(arbol_genealogico, relaciones_padre.destino)
            # Creamos la relacion de la madre con el padre
            insertar_arista(arbol_genealogico, 'pareja', madre.info, padre.info)
            encontrado = True
        relaciones_padre = relaciones_padre.sig

    # Creamos la relacion de madre de la pareja con sus hijos
    # Creamos la relacion de cada hijo con la madre
    # Creamos la relacion de cada hijo con el padre
    relaciones_padre = padre.adyacentes.inicio
    while relaciones_padre is not None:
        if relaciones_padre.peso == 'hijo':
            aux_relaciones = padre.adyacentes.inicio
            while aux_relaciones is not None:
                if relaciones_padre.destino != aux_relaciones.destino:
                    if aux_relaciones.peso == 'hijo':
                        insertar_arista(arbol_genealogico, 'hermano', relaciones_padre.destino, aux_relaciones.destino)
                aux_relaciones = aux_relaciones.sig
            insertar_arista(arbol_genealogico, 'hijo', madre.info, relaciones_padre.destino)
            insertar_arista(arbol_genealogico, 'madre', relaciones_padre.destino, madre.info)
            insertar_arista(arbol_genealogico, 'padre', relaciones_padre.destino, padre.info)
        relaciones_padre = relaciones_padre.sig

    insertar_arista(arbol_genealogico, 'pareja', 'atlas', 'pleione')
    insertar_arista(arbol_genealogico, 'hijo', 'atlas', 'maia')

    # Buscamos el vertice del padre
    padre = buscar_vertice(arbol_genealogico, 'atlas')
    relaciones_padre = padre.adyacentes.inicio
    madre = None
    encontrado = False
    # En sus relaciones buscamos a su pareja
    while relaciones_padre is not None and encontrado is False:
        if relaciones_padre.peso == 'pareja':
            madre = buscar_vertice(arbol_genealogico, relaciones_padre.destino)
            # Creamos la relacion de la madre con el padre
            insertar_arista(arbol_genealogico, 'pareja', madre.info, padre.info)
            encontrado = True
        relaciones_padre = relaciones_padre.sig

    # Creamos la relacion de madre de la pareja con sus hijos
    # Creamos la relacion de cada hijo con la madre
    # Creamos la relacion de cada hijo con el padre
    relaciones_padre = padre.adyacentes.inicio
    while relaciones_padre is not None:
        if relaciones_padre.peso == 'hijo':
            aux_relaciones = padre.adyacentes.inicio
            while aux_relaciones is not None:
                if relaciones_padre.destino != aux_relaciones.destino:
                    if aux_relaciones.peso == 'hijo':
                        insertar_arista(arbol_genealogico, 'hermano', relaciones_padre.destino, aux_relaciones.destino)
                aux_relaciones = aux_relaciones.sig
            insertar_arista(arbol_genealogico, 'hijo', madre.info, relaciones_padre.destino)
            insertar_arista(arbol_genealogico, 'madre', relaciones_padre.destino, madre.info)
            insertar_arista(arbol_genealogico, 'padre', relaciones_padre.destino, padre.info)
        relaciones_padre = relaciones_padre.sig

    insertar_arista(arbol_genealogico, 'pareja', 'zeus', 'demeter')
    insertar_arista(arbol_genealogico, 'hijo', 'zeus', 'persephone')

    # Buscamos el vertice del padre
    padre = buscar_vertice(arbol_genealogico, 'zeus')
    relaciones_padre = padre.adyacentes.inicio
    madre = None
    encontrado = False
    # En sus relaciones buscamos a su pareja
    while relaciones_padre is not None and encontrado is False:
        if relaciones_padre.peso == 'pareja':
            madre = buscar_vertice(arbol_genealogico, relaciones_padre.destino)
            # Creamos la relacion de la madre con el padre
            insertar_arista(arbol_genealogico, 'pareja', madre.info, padre.info)
            encontrado = True
        relaciones_padre = relaciones_padre.sig

    # Creamos la relacion de madre de la pareja con sus hijos
    # Creamos la relacion de cada hijo con la madre
    # Creamos la relacion de cada hijo con el padre
    relaciones_padre = padre.adyacentes.inicio
    while relaciones_padre is not None:
        if relaciones_padre.peso == 'hijo':
            insertar_arista(arbol_genealogico, 'hijo', madre.info, relaciones_padre.destino)
            insertar_arista(arbol_genealogico, 'madre', relaciones_padre.destino, madre.info)
            insertar_arista(arbol_genealogico, 'padre', relaciones_padre.destino, padre.info)
        relaciones_padre = relaciones_padre.sig

    insertar_arista(arbol_genealogico, 'pareja', 'zeus', 'hera')
    insertar_arista(arbol_genealogico, 'hijo', 'zeus', 'ares')
    insertar_arista(arbol_genealogico, 'hijo', 'zeus', 'hephaistos')

    # Buscamos el vertice del padre
    padre = buscar_vertice(arbol_genealogico, 'zeus')
    relaciones_padre = padre.adyacentes.inicio
    madre = None
    encontrado = False
    # En sus relaciones buscamos a su pareja
    while relaciones_padre is not None and encontrado is False:
        if relaciones_padre.peso == 'pareja':
            if relaciones_padre.destino == 'hera':
                madre = buscar_vertice(arbol_genealogico, relaciones_padre.destino)
                # Creamos la relacion de la madre con el padre
                insertar_arista(arbol_genealogico, 'pareja', madre.info, padre.info)
                encontrado = True
        relaciones_padre = relaciones_padre.sig

    # Creamos la relacion de madre de la pareja con sus hijos
    # Creamos la relacion de cada hijo con la madre
    # Creamos la relacion de cada hijo con el padre
    relaciones_padre = padre.adyacentes.inicio
    while relaciones_padre is not None:
        if relaciones_padre.peso == 'hijo':
            if relaciones_padre.destino == 'ares' or relaciones_padre.destino == 'hephaistos':
                insertar_arista(arbol_genealogico, 'hijo', madre.info, relaciones_padre.destino)
                insertar_arista(arbol_genealogico, 'madre', relaciones_padre.destino, madre.info)
                insertar_arista(arbol_genealogico, 'padre', relaciones_padre.destino, padre.info)
        relaciones_padre = relaciones_padre.sig

    insertar_arista(arbol_genealogico, 'pareja', 'zeus', 'leto')
    insertar_arista(arbol_genealogico, 'hijo', 'zeus', 'apollo')
    insertar_arista(arbol_genealogico, 'hijo', 'zeus', 'artemis')

    # Buscamos el vertice del padre
    padre = buscar_vertice(arbol_genealogico, 'zeus')
    relaciones_padre = padre.adyacentes.inicio
    madre = None
    encontrado = False
    # En sus relaciones buscamos a su pareja
    while relaciones_padre is not None and encontrado is False:
        if relaciones_padre.peso == 'pareja':
            if relaciones_padre.destino == 'leto':
                madre = buscar_vertice(arbol_genealogico, relaciones_padre.destino)
                # Creamos la relacion de la madre con el padre
                insertar_arista(arbol_genealogico, 'pareja', madre.info, padre.info)
                encontrado = True
        relaciones_padre = relaciones_padre.sig

    # Creamos la relacion de madre de la pareja con sus hijos
    # Creamos la relacion de cada hijo con la madre
    # Creamos la relacion de cada hijo con el padre
    relaciones_padre = padre.adyacentes.inicio
    while relaciones_padre is not None:
        if relaciones_padre.peso == 'hijo':
            if relaciones_padre.destino == 'apollo' or relaciones_padre.destino == 'artemis':
                insertar_arista(arbol_genealogico, 'hijo', madre.info, relaciones_padre.destino)
                insertar_arista(arbol_genealogico, 'madre', relaciones_padre.destino, madre.info)
                insertar_arista(arbol_genealogico, 'padre', relaciones_padre.destino, padre.info)
        relaciones_padre = relaciones_padre.sig

    insertar_arista(arbol_genealogico, 'pareja', 'zeus', 'semele')
    insertar_arista(arbol_genealogico, 'hijo', 'zeus', 'dionysos')

    # Buscamos el vertice del padre
    padre = buscar_vertice(arbol_genealogico, 'zeus')
    relaciones_padre = padre.adyacentes.inicio
    madre = None
    encontrado = False
    # En sus relaciones buscamos a su pareja
    while relaciones_padre is not None and encontrado is False:
        if relaciones_padre.peso == 'pareja':
            if relaciones_padre.destino == 'semele':
                madre = buscar_vertice(arbol_genealogico, relaciones_padre.destino)
                # Creamos la relacion de la madre con el padre
                insertar_arista(arbol_genealogico, 'pareja', madre.info, padre.info)
                encontrado = True
        relaciones_padre = relaciones_padre.sig

    # Creamos la relacion de madre de la pareja con sus hijos
    # Creamos la relacion de cada hijo con la madre
    # Creamos la relacion de cada hijo con el padre
    relaciones_padre = padre.adyacentes.inicio
    while relaciones_padre is not None:
        if relaciones_padre.peso == 'hijo':
            if relaciones_padre.destino == 'dionysos':
                insertar_arista(arbol_genealogico, 'hijo', madre.info, relaciones_padre.destino)
                insertar_arista(arbol_genealogico, 'madre', relaciones_padre.destino, madre.info)
                insertar_arista(arbol_genealogico, 'padre', relaciones_padre.destino, padre.info)
        relaciones_padre = relaciones_padre.sig

    insertar_arista(arbol_genealogico, 'pareja', 'zeus', 'maia')
    insertar_arista(arbol_genealogico, 'hijo', 'zeus', 'hermes')

    # Buscamos el vertice del padre
    padre = buscar_vertice(arbol_genealogico, 'zeus')
    relaciones_padre = padre.adyacentes.inicio
    madre = None
    encontrado = False
    # En sus relaciones buscamos a su pareja
    while relaciones_padre is not None and encontrado is False:
        if relaciones_padre.peso == 'pareja':
            if relaciones_padre.destino == 'maia':
                madre = buscar_vertice(arbol_genealogico, relaciones_padre.destino)
                # Creamos la relacion de la madre con el padre
                insertar_arista(arbol_genealogico, 'pareja', madre.info, padre.info)
                encontrado = True
        relaciones_padre = relaciones_padre.sig

    # Creamos la relacion de madre de la pareja con sus hijos
    # Creamos la relacion de cada hijo con la madre
    # Creamos la relacion de cada hijo con el padre
    relaciones_padre = padre.adyacentes.inicio
    while relaciones_padre is not None:
        if relaciones_padre.peso == 'hijo':
            aux_relaciones = padre.adyacentes.inicio
            while aux_relaciones is not None:
                if relaciones_padre.destino != aux_relaciones.destino:
                    if aux_relaciones.peso == 'hijo':
                        insertar_arista(arbol_genealogico, 'hermano', relaciones_padre.destino, aux_relaciones.destino)
                aux_relaciones = aux_relaciones.sig
            if relaciones_padre.destino == 'hermes':
                insertar_arista(arbol_genealogico, 'hijo', madre.info, relaciones_padre.destino)
                insertar_arista(arbol_genealogico, 'madre', relaciones_padre.destino, madre.info)
                insertar_arista(arbol_genealogico, 'padre', relaciones_padre.destino, padre.info)
        relaciones_padre = relaciones_padre.sig

    insertar_arista(arbol_genealogico, 'pareja', 'ares', 'aphrodite')
    insertar_arista(arbol_genealogico, 'padre', 'ares', 'phobos')
    insertar_arista(arbol_genealogico, 'padre', 'ares', 'deimos')
    insertar_arista(arbol_genealogico, 'padre', 'ares', 'eros')
    insertar_arista(arbol_genealogico, 'padre', 'ares', 'himerios')

    # Buscamos el vertice del padre
    padre = buscar_vertice(arbol_genealogico, 'ares')
    relaciones_padre = padre.adyacentes.inicio
    madre = None
    encontrado = False
    # En sus relaciones buscamos a su pareja
    while relaciones_padre is not None and encontrado is False:
        if relaciones_padre.peso == 'pareja':
            madre = buscar_vertice(arbol_genealogico, relaciones_padre.destino)
            # Creamos la relacion de la madre con el padre
            insertar_arista(arbol_genealogico, 'pareja', madre.info, padre.info)
            encontrado = True
        relaciones_padre = relaciones_padre.sig

    # Creamos la relacion de madre de la pareja con sus hijos
    # Creamos la relacion de cada hijo con la madre
    # Creamos la relacion de cada hijo con el padre
    relaciones_padre = padre.adyacentes.inicio
    while relaciones_padre is not None:
        if relaciones_padre.peso == 'hijo':
            insertar_arista(arbol_genealogico, 'hijo', madre.info, relaciones_padre.destino)
            insertar_arista(arbol_genealogico, 'madre', relaciones_padre.destino, madre.info)
            insertar_arista(arbol_genealogico, 'padre', relaciones_padre.destino, padre.info)
        relaciones_padre = relaciones_padre.sig

    insertar_arista(arbol_genealogico, 'pareja', 'hermes', 'aphrodite')
    insertar_arista(arbol_genealogico, 'hijo', 'hermes', 'hermaprhodite')

    # Buscamos el vertice del padre
    padre = buscar_vertice(arbol_genealogico, 'hermes')
    relaciones_padre = padre.adyacentes.inicio
    madre = None
    encontrado = False
    # En sus relaciones buscamos a su pareja
    while relaciones_padre is not None and encontrado is False:
        if relaciones_padre.peso == 'pareja':
            madre = buscar_vertice(arbol_genealogico, relaciones_padre.destino)
            # Creamos la relacion de la madre con el padre
            insertar_arista(arbol_genealogico, 'pareja', madre.info, padre.info)
            encontrado = True
        relaciones_padre = relaciones_padre.sig

    # Creamos la relacion de madre de la pareja con sus hijos
    # Creamos la relacion de cada hijo con la madre
    # Creamos la relacion de cada hijo con el padre
    relaciones_padre = padre.adyacentes.inicio
    while relaciones_padre is not None:
        if relaciones_padre.peso == 'hijo':
            insertar_arista(arbol_genealogico, 'hijo', madre.info, relaciones_padre.destino)
            insertar_arista(arbol_genealogico, 'madre', relaciones_padre.destino, madre.info)
            insertar_arista(arbol_genealogico, 'padre', relaciones_padre.destino, padre.info)
        relaciones_padre = relaciones_padre.sig

    madre = buscar_vertice(arbol_genealogico, 'aphrodite')
    relaciones_madre = madre.adyacentes.inicio
    while relaciones_madre is not None:
        if relaciones_madre.peso == 'hijo':
            aux_relaciones = madre.adyacentes.inicio
            while aux_relaciones is not None:
                if relaciones_madre.destino != aux_relaciones.destino:
                    if aux_relaciones.peso == 'hijo':
                        insertar_arista(arbol_genealogico, 'hermano', relaciones_madre.destino, aux_relaciones.destino)
                aux_relaciones = aux_relaciones.sig
        relaciones_madre = relaciones_madre.sig

    insertar_arista(arbol_genealogico, 'pareja', 'hermes', 'penelopeia')
    insertar_arista(arbol_genealogico, 'hijo', 'hermes', 'pan')

    # Buscamos el vertice del padre
    padre = buscar_vertice(arbol_genealogico, 'hermes')
    relaciones_padre = padre.adyacentes.inicio
    madre = None
    encontrado = False
    # En sus relaciones buscamos a su pareja
    while relaciones_padre is not None and encontrado is False:
        if relaciones_padre.peso == 'pareja':
            if relaciones_padre.destino == 'penelopeia':
                madre = buscar_vertice(arbol_genealogico, relaciones_padre.destino)
                # Creamos la relacion de la madre con el padre
                insertar_arista(arbol_genealogico, 'pareja', madre.info, padre.info)
                encontrado = True
        relaciones_padre = relaciones_padre.sig

    # Creamos la relacion de madre de la pareja con sus hijos
    # Creamos la relacion de cada hijo con la madre
    # Creamos la relacion de cada hijo con el padre
    relaciones_padre = padre.adyacentes.inicio
    while relaciones_padre is not None:
        if relaciones_padre.peso == 'hijo':
            aux_relaciones = padre.adyacentes.inicio
            while aux_relaciones is not None:
                if relaciones_padre.destino != aux_relaciones.destino:
                    if aux_relaciones.peso == 'hijo':
                        insertar_arista(arbol_genealogico, 'hermano', relaciones_padre.destino, aux_relaciones.destino)
                aux_relaciones = aux_relaciones.sig
            if relaciones_padre.destino == 'pan':
                insertar_arista(arbol_genealogico, 'hijo', madre.info, relaciones_padre.destino)
                insertar_arista(arbol_genealogico, 'madre', relaciones_padre.destino, madre.info)
                insertar_arista(arbol_genealogico, 'padre', relaciones_padre.destino, padre.info)
        relaciones_padre = relaciones_padre.sig

    # PAREJAS SIN HIJOS
    insertar_arista(arbol_genealogico, 'pareja', 'hades', 'persephone')
    insertar_arista(arbol_genealogico, 'pareja', 'persephone', 'hades')
    insertar_arista(arbol_genealogico, 'pareja', 'aphrodite', 'hephaistos')
    insertar_arista(arbol_genealogico, 'pareja', 'hephaistos', 'aphrodite')

    """ FIN DE LA CARGA DE LAS RELACIONES """

    """ INCISO C """
    dios = buscar_vertice(arbol_genealogico, 'zeus')
    relaciones = dios.adyacentes.inicio
    print('------------------------------------')
    print('Los hijos de Zeus son: ')
    while relaciones is not None:
        if relaciones.peso == 'hijo':
            print(relaciones.destino.capitalize())
        relaciones = relaciones.sig
    print('------------------------------------')
    """ INCISO D """
    diosa = buscar_vertice(arbol_genealogico, 'hera')
    relaciones = diosa.adyacentes.inicio
    padre = None
    madre = None
    hermanos = []
    hijos = []
    while relaciones is not None:
        if relaciones.peso == 'padre':
            padre = relaciones.destino
        elif relaciones.peso == 'madre':
            madre = relaciones.destino
        elif relaciones.peso == 'hermano':
            hermanos.append(relaciones.destino)
        elif relaciones.peso == 'hijo':
            hijos.append(relaciones.destino)
        relaciones = relaciones.sig
    print('------------------------------------')
    print('Siendo Hera la diosa elegida..')
    print('Su padre es: ')
    print(padre.capitalize())
    print('Su madre es :')
    print(madre.capitalize())
    print('Sus hermanos son: ')
    print(hermanos)
    print('Sus hijos son: ')
    print(hijos)
    print('------------------------------------')
    """ INCISO E """
    grafo = arbol_genealogico.inicio
    vertice = None
    while grafo is not None and vertice is None:
        if grafo.adyacentes.tamanio == 2:
            vertice = grafo
        grafo = grafo.sig

    print('Desde el vertice de la diosa Maia hay una relacion directa. Es hacia: ')
    print(vertice.adyacentes.inicio.destino, 'su relacion es: ', vertice.adyacentes.inicio.peso)
    """ INCISO F """
    print('------------------------------------')
    print('Siendo Zeus y Eros. El camino mas corto entr ellos es:  ')
    caminoMasCortoAristasPunto5(arbol_genealogico, 'ouranos', 'zeus')
    print('------------------------------------')
    """ INCISO G """
    print('------------------------------------')
    print('Barrido en profundidad: ')
    barrido_profundidad(arbol_genealogico, arbol_genealogico.inicio)
    print('Barrido en amplitud')
    marcar_no_visitado(arbol_genealogico)
    barrido_amplitud(arbol_genealogico, arbol_genealogico.inicio)
    print('------------------------------------')
    """ INCISO H """
    print('------------------------------------')
    grafo = arbol_genealogico.inicio
    while grafo is not None:
        print('DIOS: ', grafo.info)
        relaciones = grafo.adyacentes.inicio
        encontrado = False
        while relaciones is not None and encontrado is False:
            if relaciones.peso == 'madre':
                print('Su madre es: ', relaciones.destino)
                encontrado = True
            relaciones = relaciones.sig
        if encontrado is False:
            print('No tiene madre')
        grafo = grafo.sig
    print('------------------------------------')
    """ INCISO I """
    def buscar_ancestro_madre(dios):
        if dios is None:
            return 'fin'
        else:
            madre = dios.adyacentes.inicio
            encontrado = False
            while madre is not None and encontrado is False:
                if madre.peso == 'madre':
                    aux = buscar_vertice(arbol_genealogico, madre.destino)
                    encontrado = True
                madre = madre.sig
            if encontrado:
                adyacentes = aux.adyacentes.inicio
                padre = None
                while adyacentes is not None and padre is None:
                    if adyacentes.peso == 'pareja':
                        padre = buscar_vertice(arbol_genealogico, adyacentes.destino)
                    adyacentes = adyacentes.sig
                if padre is not None:
                    print('----------------GENERACION-----------------')
                    print(aux.info.capitalize())
                    print(padre.info.capitalize())
                    print('---------------------------------')
                else:
                    print('----------------GENERACION-----------------')
                    print(aux.info.capitalize())
                    print('---------------------------------')
                return buscar_ancestro_madre(aux)
            else:
                return buscar_ancestro_madre(None)

    dios = buscar_vertice(arbol_genealogico, 'maia')
    print('ANCESTROS de Maia')
    buscar_ancestro_madre(dios)

    """ INCISO J """
    print('--------------NIETOS DE KRONOS--------------')
    kronos = buscar_vertice(arbol_genealogico, 'kronos')
    adyacentes = kronos.adyacentes.inicio
    nietos = []
    while adyacentes is not None:
        if adyacentes.peso == 'hijo':
            hijo = buscar_vertice(arbol_genealogico, adyacentes.destino)
            adyacentes_hijo = hijo.adyacentes.inicio
            while adyacentes_hijo is not None:
                if adyacentes_hijo.peso == 'hijo':
                    if (adyacentes_hijo.destino in nietos) is False:
                        print(adyacentes_hijo.destino.capitalize())
                        nietos.append(adyacentes_hijo.destino)
                adyacentes_hijo = adyacentes_hijo.sig
        adyacentes = adyacentes.sig
    print('-----------------------------------------------')

    """ INCISO K """
    print('--------------HIJOS DE TEA--------------')
    theia = buscar_vertice(arbol_genealogico, 'theia')
    adyacentes = theia.adyacentes.inicio
    while adyacentes is not None:
        if adyacentes.peso == 'hijo':
            print(adyacentes.destino.capitalize())
        adyacentes = adyacentes.sig

    """ INCISO I """
    # CONSULTAR CON WALTER


# EJERCICIO 6
def reperesentacion_grafo():
    grafo = Grafo()

    # Insertando vertices al grafo
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    for i in letras:
        insertar_vertice(grafo, i)

    # Insertando aristas al grafo
    insertar_arista(grafo, 15, 'A', 'B')
    insertar_arista(grafo, 19, 'A', 'C')
    insertar_arista(grafo, 13, 'A', 'D')
    insertar_arista(grafo, 2, 'B', 'C')
    insertar_arista(grafo, 20, 'B', 'E')
    insertar_arista(grafo, 12, 'B', 'F')
    insertar_arista(grafo, 5, 'C', 'E')
    insertar_arista(grafo, 9, 'C', 'F')
    insertar_arista(grafo, 27, 'C', 'G')
    insertar_arista(grafo, 39, 'D', 'F')
    insertar_arista(grafo, 45, 'D', 'G')
    insertar_arista(grafo, 1, 'E', 'F')
    insertar_arista(grafo, 3, 'F', 'G')

    """INCISO A"""
    vertice_A = buscar_vertice(grafo, 'A')
    vertice_C = buscar_vertice(grafo, 'C')
    vertice_F = buscar_vertice(grafo, 'F')

    # barrido en profundidad desde A
    print('Barrido en profundidad desde A')
    barrido_profundidad(grafo, vertice_A)
    print('-------------------------------')
    # barrido en amplitud desde A
    print('Barrido en amplitud desde A')
    barrido_amplitud(grafo, vertice_A)
    print('-------------------------------')
    marcar_no_visitado(grafo)
    # barrido en profundidad desde C
    print('Barrido en profundidad desde C')
    barrido_profundidad(grafo, vertice_C)
    print('-------------------------------')
    # barrido en amplitud desde C
    print('Barrido en amplitud desde C')
    barrido_amplitud(grafo, vertice_C)
    print('-------------------------------')
    marcar_no_visitado(grafo)
    # barrido en profundidad desde F
    print('Barrido en profundidad desde F')
    barrido_profundidad(grafo, vertice_F)
    print('-------------------------------')
    # barrido en amplitud desde F
    print('Barrido en amplitud desde F')
    barrido_amplitud(grafo, vertice_F)
    print('-------------------------------')
    marcar_no_visitado(grafo)

    """ INCISO B"""
    # Camino mas corto desde A hasta F
    print('Camino mas corto desde A hasta F')
    caminoMasCorto(grafo, 'A', 'F')
    print('-------------------------------')
    # Camino mas corto desde C hasta D
    print('Camino mas corto desde C hasta D')
    """NO HAY CAMINO DE C HASTA D"""
    caminoMasCorto(grafo, 'C', 'D')
    print('-------------------------------')
    # Camino mas corto desde B hasta G
    print('Camino mas corto desde B hasta G')
    caminoMasCorto(grafo, 'B', 'G')
    print('-------------------------------')

    """ INCISO C """
    # Agregando aristas
    insertar_arista(grafo, random.randint(1, 46), 'C', 'A')
    insertar_arista(grafo, random.randint(1, 46), 'C', 'B')
    insertar_arista(grafo, random.randint(1, 46), 'G', 'D')

    # Camino mas corto desde A hasta F
    print('Camino mas corto desde A hasta F')
    caminoMasCorto(grafo, 'A', 'F')
    print('-------------------------------')
    # Camino mas corto desde C hasta D
    print('Camino mas corto desde C hasta D')
    """NO HAY CAMINO DE C HASTA D"""
    caminoMasCorto(grafo, 'C', 'D')
    print('-------------------------------')
    # Camino mas corto desde B hasta G
    print('Camino mas corto desde B hasta G')
    caminoMasCorto(grafo, 'B', 'G')
    print('-------------------------------')

    """ INCISO D """
    matriz_adyasencia = []
    vertice = grafo.inicio
    while vertice is not None:
        fila = [0]*grafo.tamanio
        lista_adyacentes = vertice.adyacentes
        aux = lista_adyacentes.inicio
        while aux is not None:
            if aux.destino == 'A':
                fila[0] = 1
            elif aux.destino == 'B':
                fila[1] = 1
            elif aux.destino == 'C':
                fila[2] = 1
            elif aux.destino == 'D':
                fila[3] = 1
            elif aux.destino == 'E':
                fila[4] = 1
            elif aux.destino == 'F':
                fila[5] = 1
            elif aux.destino == 'G':
                fila[6] = 1
            aux = aux.sig
        matriz_adyasencia.append(fila)
        vertice = vertice.sig

    print("La matriz de adyasencia es: ")
    for fila in matriz_adyasencia:
        for valor in fila:
            print("\t", valor, end="")
        print()


# EJERCICIO 7
def grafo_social():
    grafo = Grafo(True)
    grafo_nodirigido = Grafo(False)
    # Lista de nombres de personas random
    personas = ['Lucas', 'Maria', 'Santiago', 'Sofia', 'Martin', 'Agustin', 'Nahuel', 'Dylan', 'Lisandro']

    # Carga de los nombres en los vertices
    for i in personas:
        insertar_vertice(grafo, i)
        insertar_vertice(grafo_nodirigido, i)

    # Insertando aristas random al grafo dirigido. El peso tiene la forma [retweets/megusta, red social]
    insertar_arista(grafo, [30, 'Twitter'], 'Santiago', 'Lucas')
    insertar_arista(grafo, [130, 'Twitter'], 'Santiago', 'Sofia')
    insertar_arista(grafo, [20, 'Twitter'], 'Lucas', 'Santiago')
    insertar_arista(grafo, [100, 'Twitter'], 'Sofia', 'Santiago')
    insertar_arista(grafo, [40, 'Twitter'], 'Martin', 'Nahuel')
    insertar_arista(grafo, [32, 'Twitter'], 'Nahuel', 'Santiago')
    insertar_arista(grafo, [60, 'Twitter'], 'Maria', 'Martin')
    insertar_arista(grafo, [73, 'Twitter'], 'Lucas', 'Lisandro')
    insertar_arista(grafo, [10, 'Facebook'], 'Maria', 'Sofia')
    insertar_arista(grafo, [6, 'Facebook'], 'Sofia', 'Maria')
    insertar_arista(grafo, [100, 'Facebook'], 'Agustin', 'Maria')
    insertar_arista(grafo, [200, 'Facebook'], 'Maria', 'Agustin')
    insertar_arista(grafo, [40, 'Facebook'], 'Dylan', 'Lisandro')
    insertar_arista(grafo, [40, 'Facebook'], 'Lisandro', 'Dylan')
    insertar_arista(grafo, [24, 'Facebook'], 'Nahuel', 'Agustin')
    insertar_arista(grafo, [54, 'Facebook'], 'Agustin', 'Nahuel')
    insertar_arista(grafo, [75, 'Instagram'], 'Sofia', 'Santiago')
    insertar_arista(grafo, [89, 'Instagram'], 'Santiago', 'Sofia')
    insertar_arista(grafo, [36, 'Instagram'], 'Lucas', 'Maria')
    insertar_arista(grafo, [58, 'Instagram'], 'Martin', 'Dylan')
    insertar_arista(grafo, [39, 'Instagram'], 'Agustin', 'Lisandro')
    insertar_arista(grafo, [64, 'Instagram'], 'Lisandro', 'Agustin')
    insertar_arista(grafo, [97, 'Instagram'], 'Maria', 'Martin')

    # Insertando aristas random al grafo No dirigido. El peso tiene la forma [retweets/megusta, red social]
    insertar_arista(grafo_nodirigido, [30, 'Twitter'], 'Santiago', 'Lucas')
    insertar_arista(grafo_nodirigido, [130, 'Twitter'], 'Santiago', 'Sofia')
    insertar_arista(grafo_nodirigido, [40, 'Twitter'], 'Martin', 'Nahuel')
    insertar_arista(grafo_nodirigido, [60, 'Twitter'], 'Maria', 'Martin')
    insertar_arista(grafo_nodirigido, [73, 'Twitter'], 'Lucas', 'Lisandro')
    insertar_arista(grafo_nodirigido, [10, 'Facebook'], 'Maria', 'Sofia')
    insertar_arista(grafo_nodirigido, [200, 'Facebook'], 'Maria', 'Agustin')
    insertar_arista(grafo_nodirigido, [60, 'Facebook'], 'Dylan', 'Lisandro')
    insertar_arista(grafo_nodirigido, [54, 'Facebook'], 'Agustin', 'Nahuel')
    insertar_arista(grafo_nodirigido, [89, 'Instagram'], 'Santiago', 'Sofia')
    insertar_arista(grafo_nodirigido, [36, 'Instagram'], 'Lucas', 'Maria')
    insertar_arista(grafo_nodirigido, [58, 'Instagram'], 'Martin', 'Dylan')
    insertar_arista(grafo_nodirigido, [39, 'Instagram'], 'Agustin', 'Lisandro')
    insertar_arista(grafo_nodirigido, [97, 'Instagram'], 'Maria', 'Martin')

    """ INCISO C """
    # CONSULTAR CON WALTER
    arbolExpansionMinima = kruskal(grafo_nodirigido)
    print(arbolExpansionMinima)
    """ INCISO D"""
    # Conectar a Lucas con Sofia a traves de Twitter
    print('------Conectar a Lucas con Sofia a traves de Twitter------')
    lucas = buscar_vertice(grafo, 'Lucas')
    adyacentes_lucas = lucas.adyacentes.inicio
    encontrado = False
    adyacentes_twitter = []
    while adyacentes_lucas is not None and encontrado is False:
        if adyacentes_lucas.peso[1] == 'Twitter':
            adyacentes_twitter.append(adyacentes_lucas.destino)
            if adyacentes_lucas.destino == 'Sofia':
                print('Sofia fue encontrada directamente.')
                encontrado = True
        adyacentes_lucas = adyacentes_lucas.sig
    if encontrado is False:
        print('Camino: ')
        lucas.visitado = True
        i = 0
        no_encontrado = False
        while encontrado is False and no_encontrado is False:
            aux = buscar_vertice(grafo, adyacentes_twitter[i])
            if aux is not None:
                if aux.visitado is False:
                    print(aux.info)
                    adyacentes = aux.adyacentes.inicio
                    while adyacentes is not None and encontrado is False:
                        if adyacentes.peso[1] == 'Twitter':
                            adyacentes_twitter.append(adyacentes.destino)
                            if adyacentes.destino == 'Sofia':
                                print('Sofia fue encontrada')
                                encontrado = True
                        adyacentes = adyacentes.sig
                    if encontrado is False:
                        aux.visitado = True
                        adyacentes_twitter[i] = None
            if adyacentes_twitter[len(adyacentes_twitter)-1] is None:
                no_encontrado = True
            i += 1
    print('--------------------------------------------------------')
    marcar_no_visitado(grafo)
    """ INCISO E """
    # Conectar a Dylan con Sofia a traves de Twitter
    print('-----Conectar a Dylan con Santiago a traves de cualquier red social------')
    dylan = buscar_vertice(grafo, 'Dylan')
    adyacentes_dylan = dylan.adyacentes.inicio
    adyacentes_redes = []
    encontrado = False
    while adyacentes_dylan is not None and encontrado is False:
        adyacentes_redes.append(adyacentes_dylan.destino)
        if adyacentes_dylan.destino == 'Santiago':
            print('Santiago fue encontrado directamente.')
            encontrado = True
        adyacentes_dylan = adyacentes_dylan.sig
    if encontrado is False:
        print('Camino: ')
        dylan.visitado = True
        i = 0
        no_encontrado = False
        while encontrado is False and no_encontrado is False:
            aux = buscar_vertice(grafo, adyacentes_redes[i])
            if aux is not None:
                if aux.visitado is False:
                    print(aux.info)
                    adyacentes = aux.adyacentes.inicio
                    while adyacentes is not None and encontrado is False:
                        print(adyacentes.destino)
                        adyacentes_redes.append(adyacentes.destino)
                        if adyacentes.destino == 'Santiago':
                            print('Santiago fue encontrado')
                            encontrado = True
                        adyacentes = adyacentes.sig
                    if encontrado is False:
                        aux.visitado = True
                        adyacentes_redes[i] = None
            if adyacentes_redes[len(adyacentes_redes)-1] is None:
                no_encontrado = True
            i += 1
    print('--------------------------------------------')
    marcar_no_visitado(grafo)
    """ INCISO F"""
    print('--------------- Seguidores de instagram de Sofia----------------')
    vertices = grafo.inicio
    while vertices is not None:
        if vertices.info != 'Sofia':
            adyacentes = vertices.adyacentes.inicio
            encontrado = False
            while adyacentes is not None and encontrado is False:
                if adyacentes.peso[1] == 'Instagram':
                    if adyacentes.destino == 'Sofia':
                        print(vertices.info)
                        encontrado = True
                adyacentes = adyacentes.sig
        vertices = vertices.sig
    print('---------------------------------------------------------------')

# EJERCICIO 8
def aeropuertos():
    grafo = Grafo(False)
    # AEROPUERTOS MAS CONOCIDOS
    """
        Argentina: Ezeiza | -34.8149121505933, -58.534847311246004
        China: Pudong | 31.14841348264381, 121.80847542689538
        Brasil: Sao Paulo-Guarulhos | -23.430010834828643, -46.47305347752575
        Tailandia: Suvarnabhumi | 13.693401422824873, 100.74830601373012
        Grecia: Eleftherios Venizelos | 37.93824260994538, 23.946442313906932
        Alemania: Frankfurt Um Main | 50.03769047304524, 8.562421915907622
        Francia: Charles de Gaulle | 49.009659804434214, 2.5481162014305663
        Estados Unidos: Los Angeles | 33.94162448341231, -118.40854073166189
        Japon: Narita Jasiko | 38.81092152463861, 142.01762405987498
        Jamaica: Norman Manley | 17.93744239961703, -76.77875746884283
    """
    nombres_aeropuertos = ['Ezeiza', 'Pudong', 'Sao Paulo-Guarulhos', 'Suvarnabhumi', 'Eleftherios Venizelos', 'Frankfurt Um Main', 'Charles de Gaulle', 'Los Angeles', 'Narita Jasiko', 'Norman Manley']
    # UBICACION [LATITUD, LONGITUD]
    # FUENTE GOOGLE MAPS
    ubicacion = [[-34.8149121505933, -58.534847311246004], [31.14841348264381, 121.80847542689538], [-23.430010834828643, -46.47305347752575],
                    [13.693401422824873, 100.74830601373012], [37.93824260994538, 23.946442313906932],
                    [50.03769047304524, 8.562421915907622],
                    [49.009659804434214, 2.5481162014305663],
                    [33.94162448341231, -118.40854073166189], [38.81092152463861, 142.01762405987498],
                    [17.93744239961703, -76.77875746884283]]
    # FUENTE WIKIPEDIA
    pistas = [2, 5, 2, 2, 2, 4, 4, 4, 2, 1]
    """ INCISO C """
    # HACER
    """ INCISO D """
    for i in range(0, len(nombres_aeropuertos)):
        aeropuerto = {
            'nombre': nombres_aeropuertos[i],
            'ubicacion': ubicacion[i],
            'cantidad_pistas': pistas[i]
        }
        insertar_vertice(grafo, aeropuerto, 'nombre')

    """
        PARA EL EJERCICIO SE TOMA EL VALOR DE LA PLATA EN PESOS Y LA DISTANCIA EN KM
        PRECIOS SACADOS DE GOOGLE FLIGHTS Y DISTANCIA www.entfernungsrechner.net
    """

    # Vuelos Argentina - Brasil Brasil-Argentina
    empresa = ['Aerolineas Argentina', 'LATAM', 'Turkish Airlines']
    hora_salida = ['8:45', '10:45', '13:25']
    hora_arribo = ['10:45', '12:45', '15:25']
    vuelos = []
    for i in range(0, len(empresa)):
        vuelo = {
            'nombre_empresa': empresa[i],
            'hora_salida': hora_salida[i],
            'hora_arribo': hora_arribo[i],
            'costo': 20000,
            'duracion': 2,
            'distancia': 1716
        }
        vuelos.append(vuelo)
    insertar_arista(grafo, vuelos, 'Ezeiza', 'Sao Paulo-Guarulhos', 'nombre')

    # Vuelos Argentina - Estados Unidos Estados Unidos - Argentina
    empresa = ['Aerolineas Argentina', 'American', 'Aeromexico']
    hora_salida = ['8:45', '7:10', '22:00']
    hora_arribo = ['1:45', '00:10', '15:00']
    vuelos = []
    for i in range(0, len(empresa)):
        vuelo = {
            'nombre_empresa': empresa[i],
            'hora_salida': hora_salida[i],
            'hora_arribo': hora_arribo[i],
            'costo': 50000,
            'duracion': 17,
            'distancia': 9000
        }
        vuelos.append(vuelo)
    insertar_aristaPunto8(grafo, vuelos, 'Ezeiza', 'Los Angeles')

    # Vuelos Brasil - Estados Unidos Estados Unidos - Brasil
    empresa = ['Delta', 'American', 'United']
    hora_salida = ['23:20', '23:30', '12:13']
    hora_arribo = ['15:20', '15:30', '04:13']
    vuelos = []
    for i in range(0, len(empresa)):
        vuelo = {
            'nombre_empresa': empresa[i],
            'hora_salida': hora_salida[i],
            'hora_arribo': hora_arribo[i],
            'costo': 40000,
            'duracion': 16,
            'distancia': 9000
        }
        vuelos.append(vuelo)
    insertar_aristaPunto8(grafo, vuelos, 'Sao Paulo-Guarulhos', 'Los Angeles')

    # Vuelos Brasil - Jamaica Jamaica - Brasil
    empresa = ['American', 'COPA', 'LATAM']
    hora_salida = ['00:05', '12:13', '13:55']
    hora_arribo = ['15:05', '03:13', '04:55']
    vuelos = []
    for i in range(0, len(empresa)):
        vuelo = {
            'nombre_empresa': empresa[i],
            'hora_salida': hora_salida[i],
            'hora_arribo': hora_arribo[i],
            'costo': 46000,
            'duracion': 15,
            'distancia': 4546
        }
        vuelos.append(vuelo)
    insertar_aristaPunto8(grafo, vuelos, 'Sao Paulo-Guarulhos', 'Norman Manley')

    # Vuelos Brasil - Greacia Grecia - Brasil
    empresa = ['Qatar Airways', 'SWISS', 'Lufthansa']
    hora_salida = ['02:15', '17:25', '19:35']
    hora_arribo = ['19:15', '10:25', '12:35']
    vuelos = []
    for i in range(0, len(empresa)):
        vuelo = {
            'nombre_empresa': empresa[i],
            'hora_salida': hora_salida[i],
            'hora_arribo': hora_arribo[i],
            'costo': 85500,
            'duracion': 17,
            'distancia': 10000
        }
        vuelos.append(vuelo)
    insertar_aristaPunto8(grafo, vuelos, 'Sao Paulo-Guarulhos', 'Eleftherios Venizelos')

    # Vuelos Jamaica - Estados Unidos Estados Unidos - Jamaica
    empresa = ['Jet Blue', 'American', 'Delta']
    hora_salida = ['10:22', '15:42', '09:00']
    hora_arribo = ['11:22', '04:25', '22:00']
    vuelos = []
    for i in range(0, len(empresa)):
        vuelo = {
            'nombre_empresa': empresa[i],
            'hora_salida': hora_salida[i],
            'hora_arribo': hora_arribo[i],
            'costo': 32000,
            'duracion': 13,
            'distancia': 3700
        }
        vuelos.append(vuelo)
    insertar_aristaPunto8(grafo, vuelos, 'Norman Manley', 'Los Angeles')

    # Vuelos Jamaica - Grecia Grecia - Jamaica
    empresa = ['Caribbean Airlines', 'Delta', 'Caribbean Airlines']
    hora_salida = ['09:00', '09:30', '10:00']
    hora_arribo = ['04:30', '04:30', '06:00']
    vuelos = []
    for i in range(0, len(empresa)):
        vuelo = {
            'nombre_empresa': empresa[i],
            'hora_salida': hora_salida[i],
            'hora_arribo': hora_arribo[i],
            'costo': 120000,
            'duracion': 20,
            'distancia': 9000
        }
        vuelos.append(vuelo)
    insertar_aristaPunto8(grafo, vuelos, 'Norman Manley', 'Eleftherios Venizelos')

    # Vuelos Estados Unidos - Francia Francia - Estados Unidos
    empresa = ['Turkish Airlines', 'Jet Blue', 'Air France']
    hora_salida = ['18:25', '08:52', '15:25']
    hora_arribo = ['09:25', '23:52', '06:25']
    vuelos = []
    for i in range(0, len(empresa)):
        vuelo = {
            'nombre_empresa': empresa[i],
            'hora_salida': hora_salida[i],
            'hora_arribo': hora_arribo[i],
            'costo': 100000,
            'duracion': 15,
            'distancia': 9000
        }
        vuelos.append(vuelo)
    insertar_aristaPunto8(grafo, vuelos, 'Los Angeles', 'Charles de Gaulle')

    # Vuelos Estados Unidos - Japon Japon - Estados Unidos
    empresa = ['Air Canada', 'JAL', 'United']
    hora_salida = ['7:00', '12:00', '08:16']
    hora_arribo = ['19:00', '00:00', '20:16']
    vuelos = []
    for i in range(0, len(empresa)):
        vuelo = {
            'nombre_empresa': empresa[i],
            'hora_salida': hora_salida[i],
            'hora_arribo': hora_arribo[i],
            'costo': 81000,
            'duracion': 12,
            'distancia': 8000
        }
        vuelos.append(vuelo)
    insertar_aristaPunto8(grafo, vuelos, 'Los Angeles', 'Narita Jasiko')

    # Vuelos Estados Unidos - China China - Estados Unidos
    empresa = ['EVA Air', 'Air Canada', 'China Southern']
    hora_salida = ['23:05', '07:00', '22:20']
    hora_arribo = ['07:05', '15:00', '06:20']
    vuelos = []
    for i in range(0, len(empresa)):
        vuelo = {
            'nombre_empresa': empresa[i],
            'hora_salida': hora_salida[i],
            'hora_arribo': hora_arribo[i],
            'costo': 125000,
            'duracion': 20,
            'distancia': 16000
        }
        vuelos.append(vuelo)
    insertar_aristaPunto8(grafo, vuelos, 'Los Angeles', 'Pudong')

    # Vuelos Estados Unidos - Tailandia Tailandia - Estados Unidos
    empresa = ['ANA', 'Singapore', 'Qatar Airways']
    hora_salida = ['00:05', '22:25', '14:55']
    hora_arribo = ['01:05', '23:25', '15:55']
    vuelos = []
    for i in range(0, len(empresa)):
        vuelo = {
            'nombre_empresa': empresa[i],
            'hora_salida': hora_salida[i],
            'hora_arribo': hora_arribo[i],
            'costo': 75000,
            'duracion': 25,
            'distancia': 13000
        }
        vuelos.append(vuelo)
    insertar_aristaPunto8(grafo, vuelos, 'Los Angeles', 'Suvarnabhumi')

    # Vuelos Japon - China China - Japon
    empresa = ['ANA', 'Singapore', 'Qatar Airways']
    hora_salida = ['13:05', '13:25', '22:30']
    hora_arribo = ['16:05', '16:25', '00:30']
    vuelos = []
    for i in range(0, len(empresa)):
        vuelo = {
            'nombre_empresa': empresa[i],
            'hora_salida': hora_salida[i],
            'hora_arribo': hora_arribo[i],
            'costo': 100000,
            'duracion': 3,
            'distancia': 1700
        }
        vuelos.append(vuelo)
    insertar_aristaPunto8(grafo, vuelos, 'Pudong', 'Narita Jasiko')

    # Vuelos China - Tailandia Tailandia - China
    empresa = ['Xiamen', 'China Southern', 'Shangai Airlines']
    hora_salida = ['14:30', '18:30', '16:05']
    hora_arribo = ['18:30', '22:30', '20:05']
    vuelos = []
    for i in range(0, len(empresa)):
        vuelo = {
            'nombre_empresa': empresa[i],
            'hora_salida': hora_salida[i],
            'hora_arribo': hora_arribo[i],
            'costo': 100000,
            'duracion': 4,
            'distancia': 2000
        }
        vuelos.append(vuelo)
    insertar_aristaPunto8(grafo, vuelos, 'Pudong', 'Suvarnabhumi')

    # Vuelos Tailandia - Grecia Grecia - Tailandia
    empresa = ['Emirates', 'KLM', 'Qatar Airways']
    hora_salida = ['01:04', '00:40', '01:50']
    hora_arribo = ['14:04', '13:40', '14:50']
    vuelos = []
    for i in range(0, len(empresa)):
        vuelo = {
            'nombre_empresa': empresa[i],
            'hora_salida': hora_salida[i],
            'hora_arribo': hora_arribo[i],
            'costo': 51000,
            'duracion': 13,
            'distancia': 7900
        }
        vuelos.append(vuelo)
    insertar_aristaPunto8(grafo, vuelos, 'Suvarnabhumi', 'Eleftherios Venizelos')

    # Vuelos Grecia - Alemania Alemania - Grecia
    empresa = ['SWISS', 'Aegean', 'Austrian']
    hora_salida = ['13:45', '08:35', '15:15']
    hora_arribo = ['16:45', '11:35', '18:15']
    vuelos = []
    for i in range(0, len(empresa)):
        vuelo = {
            'nombre_empresa': empresa[i],
            'hora_salida': hora_salida[i],
            'hora_arribo': hora_arribo[i],
            'costo': 16000,
            'duracion': 3,
            'distancia': 1800
        }
        vuelos.append(vuelo)
    insertar_aristaPunto8(grafo, vuelos, 'Eleftherios Venizelos', 'Frankfurt Um Main')

    # Vuelos Grecia - Francia Francia - Grecia
    empresa = ['Aegean', 'Austrian', 'Turkish Airlines']
    hora_salida = ['08:40', '15:15', '10:15']
    hora_arribo = ['16:45', '11:35', '18:15']
    vuelos = []
    for i in range(0, len(empresa)):
        vuelo = {
            'nombre_empresa': empresa[i],
            'hora_salida': hora_salida[i],
            'hora_arribo': hora_arribo[i],
            'costo': 16500,
            'duracion': 3,
            'distancia': 2000
        }
        vuelos.append(vuelo)
    insertar_aristaPunto8(grafo, vuelos, 'Eleftherios Venizelos', 'Charles de Gaulle')

    # Vuelos Francia - Alemania Alemania - Francia
    empresa = ['Aegean', 'Austrian', 'Turkish Airlines']
    hora_salida = ['08:40', '15:15', '10:15']
    hora_arribo = ['16:45', '11:35', '18:15']
    vuelos = []
    for i in range(0, len(empresa)):
        vuelo = {
            'nombre_empresa': empresa[i],
            'hora_salida': hora_salida[i],
            'hora_arribo': hora_arribo[i],
            'costo': 10600,
            'duracion': 1,
            'distancia': 500
        }
        vuelos.append(vuelo)
    insertar_aristaPunto8(grafo, vuelos, 'Charles de Gaulle', 'Frankfurt Um Main')

    """ INCISO D """
    print("El camino mas corto desde Argentina|EZEIZA a Tailandia|SUVARNABHUMI en cuanto a distancia: ")
    caminoMasCortoPunto8(grafo, 'Ezeiza', 'Suvarnabhumi', 'distancia')
    print('--------------------------------------------------------------------------------')
    print("El camino mas corto desde Argentina|EZEIZA a Tailandia|SUVARNABHUMI en cuanto a tiempo")
    caminoMasCortoPunto8(grafo, 'Ezeiza', 'Suvarnabhumi', 'duracion')
    print('--------------------------------------------------------------------------------')
    print("El camino mas corto desde Argentina|EZEIZA a Tailandia|SUVARNABHUMI en cuanto a costos")
    caminoMasCortoPunto8(grafo, 'Ezeiza', 'Suvarnabhumi', 'costo')
    print('--------------------------------------------------------------------------------')
    print("El camino mas corto desde Argentina|EZEIZA a Tailandia|SUVARNABHUMI en cuanto a escalas")
    caminoMasCortoAristas(grafo, 'Ezeiza', 'Suvarnabhumi')
    print('--------------------------------------------------------------------------------')

    """ INCISO E """
    aeropuertos = grafo.inicio

    print('Los aeropuertos que se pueden arribar desde Grecia|ELEFTHERIOS VENIZELOS son: ')
    while aeropuertos is not None:
        if aeropuertos.info['nombre'] != 'Eleftherios Venizelos':
            print('Camino: ------------------------------------------------')
            caminoMasCortoAristas(grafo, 'Eleftherios Venizelos', aeropuertos.info['nombre'])
            print('---------------------------------------------------------')
        aeropuertos = aeropuertos.sig


# EJERCICIO 9
def planetas_starwars():
    planetas = ['Alderaan', 'Endor', 'Dagobah', 'Hoth', 'Tatooine', 'Kamino',
                'Naboo', 'Mustafar', 'Scarif', 'Bespin',
                'Atollon', 'Christophsis', 'Cantonica', 'Dathomir',
                'Florrum', 'Iego', 'Kessel']
    galaxia = Grafo(False)
    """ INCISO A """
    for i in planetas:
        insertar_vertice(galaxia, i)

    """ INCISO B """
    vertices = galaxia.inicio
    print(vertices.info)
    while vertices is not None:
        for i in range(0, 4):
            control = False
            while control is False:
                destino = planetas[random.randint(0, len(planetas)-1)]
                if vertices.info != destino:
                    encontrado = False
                    aux = vertices.adyacentes.inicio
                    while aux is not None and encontrado is False:
                        if aux.destino == destino:
                            encontrado = True
                        aux = aux.sig
                    if encontrado is False:
                        insertar_arista(galaxia, random.randint(0, 100), vertices.info, destino)
                        control = True
        vertices = vertices.sig

    """ INCISO C """
    arbolExpansionMinima = kruskal(galaxia)
    print('Arbol de expasion minima: ---------------')
    print(arbolExpansionMinima)
    print('------------------------------------------')

    """ INCISO D """
    print('Camino mas corto desde Tatooine hasta Dagobah----')
    caminoMasCortoPunto9(galaxia, 'Tatooine', 'Dagobah')
    print('--------------------------------------------------')
    print('Camino mas corto desde Alderaan hasta Endor----')
    caminoMasCortoPunto9(galaxia, 'Alderaan', 'Endor')
    print('--------------------------------------------------')
    print('Camino mas corto desde Alderaan hasta Endor----')
    caminoMasCortoPunto9(galaxia, 'Hoth', 'Tatooine')
    print('--------------------------------------------------')

    """ INCISO E """
    aux = galaxia.inicio
    print('Los planetas a los que se puede llegar desde Tatooine son: ')
    while aux is not None:
        camino = dijkstra(galaxia, 'Tatooine', aux.info)
        pila = Pila()
        destino = aux.info
        while(not pila_vacia(camino)):
            dato = desapilar(camino)
            if(destino == dato[1][0].info):
                apilar(pila, dato[1][0].info)
                destino = dato[1][1]
        while(not pila_vacia(pila)):
            aux_destino = desapilar(pila)
        aux = aux.sig
        if aux_destino != 'Tatooine':
            print('-----------------------------------------')
            print(aux_destino)
            print('-----------------------------------------')


# EJERCICIO 10
def turismo():
    grafo = Grafo(False)
    templos = ['Atenas-Partenon', 'Zeus-Olimpia', 'Hera-Olimpia'
                , 'Apolo-Delfos', 'Poseidon-Sunion',
                'Artemisa-Efeso', 'Teatro de Dionisio-Acropolis']
    # UBICACION [LATITUD, LONGITUD]
    # FUENTE GOOGLE MAPS
    ubicacion = [[37.971714549213665, 23.726695139636362], [37.96946913895125, 23.7330785396364], [37.63901896894981, 21.629868051271313],
                    [38.48243125601429, 22.501357741501735], [37.65793557078878, 24.015114987216666],
                    [37.949740790915016, 27.363995672166027],
                    [37.97056876782258, 23.727823110800973]]
    """ INCISO B """
    for i in range(0, len(templos)):
        templo = {
            'nombre': templos[i],
            'ubicacion': ubicacion[i],
        }
        insertar_vertice(grafo, templo, 'nombre')
    """ INCISO A """
    vertice = grafo.inicio
    while vertice is not None:
        aux = grafo.inicio
        while aux is not None:
            if aux.info != vertice.info:
                adyacentes = vertice.adyacentes.inicio
                encontrado = False
                while adyacentes is not None and encontrado is False:
                    if adyacentes.destino == aux.info:
                        encontrado = True
                    adyacentes = adyacentes.sig
                if encontrado is False:
                    insertar_arista(grafo, random.randint(0, 150), vertice.info, aux.info, 'nombre')
            aux = aux.sig
        vertice = vertice.sig

    """ INCISO C """
    arbolExpansionMinima = kruskal(grafo, 'nombre')
    print(arbolExpansionMinima)

    """ INCISO D """
    caminoMasCortoPunto10(grafo, 'Atenas-Partenon', 'Apolo-Delfos')
