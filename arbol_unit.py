from tda_arbol import NodoArbol, NodoArbol2, insertarArbol, insertarArbol2
from tda_arbol import busqueda_proximidad, NodoArbolN, insertarTree
from tda_arbol import altura, nodos_nivel, ArbolHuffman, es_hoja
from tda_arbol import busqueda_desordenados, imprimirArbol
from tda_arbol import arbol_vacio, busqueda_arbol, preorden, inorden, postorden
from tda_arbol import busqueda_desordenados2, busquedaProximidadDesordenados, busquedaOcurrenciasProximidad
from tda_arbol import reemplazar, eliminar, altura, ver_repetidos, pares, resolver_expresion
from tda_arbol import contar_nodos, arbol_completo, busqueda_arbolCampo
from tda_arbol import busquedaOcurrencias, insertarReportesArmeria
from tda_arbol import busqueda_arbolAtributoCodigo, eliminarCampo
from TDA_archivo import abrir, cerrar, leer, guardar, modificar, eliminarArchivo
from tda_lista import Lista, insertar, eliminar, barridoLista, eliminarPrimero, insertarNodosArbol
from tda_lista import busquedaLista
from sys import getsizeof
import time
import random


# EJERCICIO 1
def numeros_enteros():
    raiz = None
    for i in range(0, 10):
        raiz = insertarArbol(raiz, random.randint(0, 10))
    print('Preorden: ')
    preorden(raiz)
    print('Inorden: ')
    inorden(raiz)
    print('Postorden: ')
    postorden(raiz)
    numero = int(input('Ingrese un numero: '))
    numero = busqueda_arbol(raiz, numero)
    if numero is not None:
        print('El numero se encuentra en el arbol.')
    for i in range(0, 3):
        numero = int(input('Ingrese un numero: '))
        control = busqueda_arbol(raiz, numero)
        if control is not None:
            eliminar(raiz, numero)
        else:
            while control is None:
                print('No se encontro.')
                numero = int(input('Ingrese un numero: '))
                control = busqueda_arbol(raiz, numero)
            eliminar(raiz, numero)
    print('Altura sub arbol izquierdo: ')
    print(altura(raiz.izq))
    print('Altura sub arbol derecho: ')
    print(altura(raiz.der))

    repetidos = []
    repetidos = ver_repetidos(raiz, -1, repetidos)
    print(repetidos)

    cantidad_pares, cantidad_impares = pares(raiz, 0, 0)
    print('Cantidad de pares: ', cantidad_pares)
    print('Cantidad de impares: ', cantidad_impares)


# EJERCICIO 2
def expresion_matematica(expresion):
    vec = []
    termino = ''
    for i in range(0, len(expresion)):
        if expresion[i] == '+' or expresion[i] == '/' or expresion[i] == '-' or expresion[i] == '*':
            vec.append(termino)
            vec.append(expresion[i])
            termino = ''
        else:
            termino = termino + expresion[i]
        if i == len(expresion)-1:
            vec.append(termino)
    # vec = expresion separada en terminos
    lista_nodos = []
    i = 0
    nodo1, nodo2 = None, None
    while len(vec) > 1:
        if vec[i].isdigit():
            i += 1
        else:
            dato = vec[0:i]
            dato = dato[0]
            nodo1 = NodoArbol()
            nodo1.info = dato
            lista_nodos.append(nodo1)
            operador = vec[i]
            nodo2 = NodoArbol()
            nodo2.info = operador
            lista_nodos.append(nodo2)
            vec = vec[i+1:]
            i = 0
    nodo1 = NodoArbol()
    nodo1.info = vec[0]
    """ Arboles con operaciones de bajo nivel """
    lista_nodos.append(nodo1)
    for i in range(0, len(lista_nodos)):
        nodo_aux1, nodo_aux2 = None, None
        if lista_nodos[i].info == '*' or lista_nodos[i].info == '/':
            nodo_aux1 = NodoArbol()
            nodo_aux2 = NodoArbol()
            nodo_aux1 = lista_nodos[i+1]
            nodo_aux2 = lista_nodos[i-1]
            lista_nodos[i].der = nodo_aux1
            lista_nodos[i].izq = nodo_aux2
            lista_nodos[i+1] = NodoArbol()
            lista_nodos[i-1] = NodoArbol()
    i = len(lista_nodos)-1
    while i > -1:
        if lista_nodos[i].info is None:
            lista_nodos.pop(i)
        i -= 1
    """ Arboles con operaciones de alto nivel """
    for i in range(0, len(lista_nodos)):
        nodo_aux1, nodo_aux2 = None, None
        if lista_nodos[i].info == '+' or lista_nodos[i].info == '-':
            nodo_aux1 = NodoArbol()
            nodo_aux2 = NodoArbol()
            nodo_aux1 = lista_nodos[i+1]
            nodo_aux2 = lista_nodos[i-1]
            lista_nodos[i].der = nodo_aux1
            lista_nodos[i].izq = nodo_aux2
            lista_nodos[i+1] = NodoArbol()
            lista_nodos[i-1] = NodoArbol()
    i = len(lista_nodos)-1
    while i > -1:
        if lista_nodos[i].info is None:
            lista_nodos.pop(i)
        i -= 1
    arbol = NodoArbol()
    aux = len(lista_nodos)
    i = 0
    while i < aux-1:
        lista_nodos[i+1].izq = lista_nodos[i]
        i += 1
    arbol = lista_nodos[len(lista_nodos)-1]
    expresion = []
    resolver_expresion(arbol, expresion)
    for i in range(0, len(expresion)):
        if expresion[i] == '*':
            a = expresion[i-1] * expresion[i+1]
            expresion[i-1] = None
            expresion[i+1] = None
            expresion[i] = a
        if expresion[i] == '/':
            a = expresion[i-1] * expresion[i+1]
            expresion[i-1] = None
            expresion[i+1] = None
            expresion[i] = a
    while i > -1:
        if expresion[i] is None:
            expresion.pop(i)
        i -= 1
    for i in range(0, len(expresion)):
        if expresion[i] == '+':
            a = expresion[i-1] + expresion[i+1]
            expresion[i-1] = None
            expresion[i] = None
            expresion[i+1] = a
        if expresion[i] == '-':
            a = expresion[i-1] - expresion[i+1]
            expresion[i-1] = None
            expresion[i] = None
            expresion[i+1] = a
    i = len(expresion)-1
    while i > -1:
        if expresion[i] is None:
            expresion.pop(i)
        i -= 1
    return expresion


# EJERCICIO 3
def transformacion(datos):
    arbol = None
    aux = datos.keys()
    for i in aux:
        if arbol is None:
            arbol = insertarTree(arbol, ["0"])
            dato = [datos[i][0]]
            arbol.izq = insertarTree(arbol.izq, dato)
            aux_arbol = arbol.izq
            for j in range(1, len(datos[i])):
                dato = [datos[i][j]]
                aux_arbol.der = insertarTree(aux_arbol.der, dato)
                aux_arbol = aux_arbol.der
        else:
            buscado = busqueda_desordenados(arbol, i, 0)
            dato = [datos[i][0]]
            buscado.izq = insertarTree(buscado.izq, dato)
            aux_buscado = buscado.izq
            for j in range(1, len(datos[i])):
                dato = [datos[i][j]]
                aux_buscado.der = insertarTree(aux_buscado.der, dato)
                aux_buscado = aux_buscado.der
    return arbol


def contar_capitulos(arbol, contador=0):
    if arbol is not None:
        if arbol.info[0].count('.') == 1:
            contador += 1
        contador = contar_capitulos(arbol.izq, contador)
        contador = contar_capitulos(arbol.der, contador)
    return contador


def agregarInfo(arbol, vec):
    if arbol is not None:
        arbol.info.append(vec.pop())
        agregarInfo(arbol.izq, vec)
        agregarInfo(arbol.der, vec)
    return arbol


def indice_summerville():
    diccionario_indices = {}
    diccionario_indices['0'] = []
    archivo = open("/home/santiago/github/TDA_arbol/indice_summerville.txt", "r")
    linea = archivo.readline()
    while linea:
        linea_aux = '0'
        i = 0
        aux = '0'
        if len(linea) != 1:
            while linea[i] != " ":
                if linea[i] != " ":
                    aux = aux + linea[i]
                i += 1
        linea_aux = linea_aux + aux
        if aux.count('.') == 1:
            diccionario_indices['0'].append(aux)
            diccionario_indices[aux] = []
        if aux.count('.') == 2:
            contador = 0
            while aux[contador] != '.':
                contador += 1
            aux_clave = aux[0:contador]+'.'
            if len(aux_clave)+2 == len(aux):
                diccionario_indices[aux_clave].append(aux)
                diccionario_indices[aux] = []
        if aux.count('.') == 3:
            contador = 0
            while aux[contador] != '.':
                contador += 1
            aux_clave = aux[0:contador+2]+'.'
            if len(aux_clave)+2 == len(aux):
                diccionario_indices[aux_clave].append(aux)
            elif len(aux_clave)+3 == len(aux):
                diccionario_indices[aux_clave].append(aux)
        linea = archivo.readline()
    archivo.close()
    lista = []
    for i in diccionario_indices:
        if len(diccionario_indices[i]) == 0:
            lista.append(i)
    for i in lista:
        diccionario_indices.pop(i, None)
    arbol = transformacion(diccionario_indices)
    archivo = open("/home/santiago/github/TDA_arbol/indice_summerville.txt", "r")
    linea = archivo.readline()
    particion_str = []
    particion_str.append('NADA')
    numero = []
    numero.append('NADA')
    while linea:
        aux = ''
        if len(linea) > 1:
            contador = 0
            while linea[contador] != ' ':
                contador += 1
            aux = linea[contador+1:]
            contador = 0
            while not aux[contador].isdigit():
                contador += 1
            titulo = aux[0:contador]
            nro_pag = aux[contador:]
            particion_str.append(titulo)
            numero.append(nro_pag)
        linea = archivo.readline()
    archivo.close()
    particion_str.reverse()
    numero.reverse()
    arbol = agregarInfo(arbol, particion_str)
    arbol = agregarInfo(arbol, numero)
    """ Resolucion del ejercicio"""
    print('Indice ordenado')
    print('Indice     -     Titulo         -     Nro-pag')
    preorden(arbol)
    indice_particular = busqueda_desordenados(arbol, 'Disenio de software de tiempo real ', 1)
    print('Indice correspondiente al titulo Disenio de software de tiempo real: ')
    print(indice_particular.info[0][1:])
    print('Cantidad de capitulos del libro: ')
    print(contar_capitulos(arbol))
    modelo_metrica = []
    modelo_metrica = busquedaOcurrenciasProximidad(arbol, 'modelo', modelo_metrica, 1)
    modelo_metrica = busquedaOcurrenciasProximidad(arbol, 'metricas', modelo_metrica, 1)
    print('Temas que contienen la palabra modelo y metricas: ')
    for i in range(0, len(modelo_metrica)):
        print(modelo_metrica[i].info)


# EJERCICIO 4
def hijos(nodo):
    hijo_izq = nodo.izq
    hijo_der = nodo.der
    print("info del hijo izquierdo: ", hijo_izq.info)
    print("info del hijo derecho: ", hijo_der.info)
    return hijo_izq, hijo_der


# EJERCICIO 5
def almacenar_super_villanos():
    nombre = ['a', 'b', 'e', 'Doctor Stange', 'u', 'p', 'j', 't', 'i', "Cfran"]
    que_es = [True, False]
    arbol = None
    for i in range(0, len(nombre)):
        lista = ['Nombre', 'Que es']
        lista[0] = nombre[i]
        lista[1] = que_es[random.randint(0, 1)]
        arbol = insertarArbol(arbol, lista)
    return arbol


def listar_villanos(arbol, listado):
    if arbol is not None:
        listar_villanos(arbol.izq, listado)
        if arbol.info[1] is False:
            listado.append(arbol.info[0])
        listar_villanos(arbol.der, listado)


def separar_personajes(arbol, arbol_villanos, arbol_superheroes):
    if arbol is not None:
        arbol_villanos, arbol_superheroes = separar_personajes(arbol.izq, arbol_villanos, arbol_superheroes)
        if arbol.info[1] is False:
            arbol_villanos = insertarArbol(arbol_villanos, arbol.info)
        else:
            arbol_superheroes = insertarArbol(arbol_superheroes, arbol.info)
        arbol_villanos, arbol_superheroes = separar_personajes(arbol.der, arbol_villanos, arbol_superheroes)
    return arbol_villanos, arbol_superheroes


def superheroes_c(arbol, d):
    if arbol is not None:
        superheroes_c(arbol.izq, d)
        if arbol.info[1] is True and arbol.info[0][0] == "C":
            d.append(arbol.info)
        superheroes_c(arbol.der, d)


def super_villanos():
    personajes = None
    personajes = almacenar_super_villanos()
    listado_villanos = []
    listar_villanos(personajes, listado_villanos)
    print("Listado ordenado de villanos: ")
    print(listado_villanos)
    cantidad_superheroes_c = []
    superheroes_c(personajes, cantidad_superheroes_c)
    print("Listado de superheroes que comienzan con c: ")
    print(cantidad_superheroes_c)
    buscado = busqueda_proximidad(personajes, 'Doctor')
    if buscado is not None:
        buscado.info[0] = 'Doctor Strange'
    arbol_superheroes = None
    arbol_villanos = None
    arbol_villanos, arbol_superheroes = separar_personajes(personajes, arbol_villanos, arbol_superheroes)
    print("Arbol de villanos: ")
    inorden(arbol_villanos)
    print("Arbol de superheroes: ")
    inorden(arbol_superheroes)
    cantidad_superheroes = 0
    cantidad_superheroes = contar_nodos(arbol_superheroes, cantidad_superheroes)
    print("Son", cantidad_superheroes, "superheroes.")
    print("Superheroes ordenados de manera descendiente: ")
    postorden(arbol_superheroes)
    cantidad_villanos = 0
    cantidad_villanos = contar_nodos(arbol_villanos, cantidad_villanos)
    print("Cantidad de nodos del arbol superheroes: ", cantidad_superheroes)
    print("Cantidad de nodos del arbol villanos: ", cantidad_villanos)
    print("Barrido ordenado del arbol de superheroes: ")
    inorden(arbol_superheroes)
    print("barrido ordenado del arbol de villanos: ")
    inorden(arbol_villanos)


# EJERCICIO 6
def transformacion_con_corte(datos):
    """
        TRUE = directorio
        FALSE = archivo
    """
    arbol = None
    aux = datos.keys()
    aux.sort()
    for i in aux:
        if arbol is None:
            lista = ["c:/", True]
            arbol = insertarTree(arbol, lista)
            if datos[i][0].find('.') != -1:
                lista = [datos[i][0], False]
            else:
                lista = [datos[i][0], True]
            arbol.izq = insertarTree(arbol.izq, lista)
            aux_arbol = arbol.izq
            for j in range(1, len(datos[i])):
                if datos[i][j].find('.') != -1:
                    lista = [datos[i][j], False]
                else:
                    lista = [datos[i][j], True]
                aux_arbol.der = insertarTree(aux_arbol.der, lista)
                aux_arbol = aux_arbol.der
        else:
            buscado = busqueda_desordenados(arbol, i[3:])
            if datos[i][0].find('.') != -1:
                lista = [datos[i][0], False]
            else:
                lista = [datos[i][0], True]
            buscado.izq = insertarTree(buscado.izq, lista)
            aux_buscado = buscado.izq
            for j in range(1, len(datos[i])):
                if datos[i][j].find('.') != -1:
                    lista = [datos[i][j], False]
                else:
                    lista = [datos[i][j], True]
                aux_buscado.der = insertarTree(aux_buscado.der, lista)
                aux_buscado = aux_buscado.der
    return arbol


def mostrar_contenido(arbol, carpeta_buscada):
    carpeta = busqueda_desordenados(arbol, carpeta_buscada)
    print(carpeta.izq.info)
    aux = carpeta.izq
    while aux.der is not None:
        print(aux.der.info)
        aux = aux.der


def contar_archivos(arbol, carpeta_buscada):
    c = 0
    carpeta = busqueda_desordenados(arbol, carpeta_buscada)
    if carpeta.izq.info[1] is False:
        c += 1
    aux = carpeta.izq
    while aux.der is not None:
        if aux.der.info[1] is False:
            c += 1
        aux = aux.der
    return c


def mostrar_archivos(raiz):
    if raiz is not None:
        mostrar_archivos(raiz.izq)
        if raiz.info[1] is False:
            print(raiz.info[0])
        mostrar_archivos(raiz.der)


def directorio():
    diccionario_directorio = {
        "01-c:/": ["arduino", "documento", "libros", "escritorio", "imagenes", "musica", "nodeprojects", "plantillas", "prueba cluster", "pythonprojects"],
        "02-arduino": ["libraries"],
        "03-libraries": ["readme.txt"],
        "04-documento": ["archivo.pdf", "colores arduinos"],
        "05-libros": ["9781782175858-THINKING_IN_JAVASCRIPT.pdf", "python for google app engine.pdf", "Python para todos.pdf", "Redis.pdf", "The majesty of vue.js.pdf"],
        "06-escritorio": ["prueba"],
        "07-imagenes": ["GitHub.png", "master_yoda.jpg", "Star_Wars_Saga.png"],
        "08-nodeprojects": ["api", "Star Wars"],
        "09-api": ["package-lock.json"],
        "91-Star Wars": ["apii", "docker-compose.yml", "dockerfile"],
        "92-prueba cluster": ["Sietemil", "redis.config"],
        "93-Sietemil": ["cluster-config.conf"],
        "94-pythonprojects": ["libro alg", "prueba_apis", "vue-flask"],
        "95-prueba_apis": ["autocomplete.py"],
        "96-vue-flask": ["app.py", "readme.md", "static", "templates"]
    }

    arbol = transformacion_con_corte(diccionario_directorio)
    inorden(arbol)
    print("Contenido de la carpeta imagenes: ")
    mostrar_contenido(arbol, 'imagenes')
    a = diccionario_directorio.keys()
    print(a)
    for i in a:
        print("Carpeta: ", i[3:])
        print("Tiene ", contar_archivos(arbol, i[3:]), " archivos.")
    print("Archivos: ")
    mostrar_archivos(arbol)


# EJERCICIO 7
def nodo_minimo(arbol):
    if arbol.izq is not None:
        arbol = nodo_minimo(arbol.izq)
    return arbol


def nodo_maximo(arbol):
    if arbol.der is not None:
        arbol = nodo_maximo(arbol.der)

    return arbol


# EJERCICIO 8
def comprimir(mensaje, tabla_codificacion):
    mensaje_comprimido = ''
    for i in mensaje:
        mensaje_comprimido = mensaje_comprimido + tabla_codificacion[i]
    return mensaje_comprimido


def descomprimir(mensaje, arbol):
    mensaje_descomprimido = ''
    aux = arbol
    for i in mensaje:
        if i == '0':
            aux = aux.izq
            if es_hoja(aux) is True:
                mensaje_descomprimido = mensaje_descomprimido + aux.info[1]
                aux = arbol
        else:
            aux = aux.der
            if es_hoja(aux) is True:
                mensaje_descomprimido = mensaje_descomprimido + aux.info[1]
                aux = arbol
    return mensaje_descomprimido


def comprimir_descomprimir(mensaje_comrimir, mensaje_descomprimir=''):
    """No anduvo ejecutandolo desde la consola de ubuntu"""
    simbolos = ['A', 'F', '1', '3', '0', 'M', 'T']
    frecuencia = [0.2, 0.17, 0.13, 0.21, 0.05, 0.09, 0.15]
    lista_datos = Lista()
    for i in range(0, len(simbolos)):
        dato = []
        dato = [frecuencia[i], simbolos[i]]
        aux = None
        aux = insertarArbol(aux, dato)
        insertarNodosArbol(lista_datos, aux)
    a = ArbolHuffman(lista_datos)
    diccionario_codificacion = {
        'A': '00',
        '3': '01',
        '1': '100',
        '0': '1010',
        'M': '1011',
        'T': '110',
        'F': '111'
    }
    mensaje_comprimido = comprimir(mensaje_comrimir, diccionario_codificacion)
    print('Mensaje ', mensaje_comrimir, ' comprimido: ')
    print(mensaje_comprimido)
    print('!----------------------------------------------!')
    mensaje_descomprimido = descomprimir(mensaje_descomprimir, a)
    print('Mensaje ', mensaje_descomprimir, ' descomprimido: ')
    print(mensaje_descomprimido)


# EJERCICIO 9
def contarNodosNivel(raiz, nivel, nivel_act=0, cont=0):
    if raiz is not None:
        if nivel-2 == nivel_act:
            if raiz.izq is not None:
                cont += 1
            if raiz.der is not None:
                cont += 1
        nivel_act += 1
        cont = contarNodosNivel(raiz.izq, nivel, nivel_act, cont)
        cont = contarNodosNivel(raiz.der, nivel, nivel_act, cont)
    else:
        nivel_act = 0
    return cont


arbol = None
arbol = insertarArbol(arbol, 2)
arbol = insertarArbol(arbol, 7)
arbol = insertarArbol(arbol, 1)
arbol = insertarArbol(arbol, 3)
arbol = insertarArbol(arbol, 13)
arbol = insertarArbol(arbol, 5)
arbol = insertarArbol(arbol, 9)
arbol = insertarArbol(arbol, 23)


def niveles(arbol, nivel):
    print('Si el nivel ', nivel, " estuviera completo tendria ", nodos_nivel(nivel), "nodos.")
    print('El nivel ', nivel, ' tiene', contarNodosNivel(arbol, nivel), ' nodos')


# EJERCICIO 10
# A
arbol = None
arbol = insertarArbol(arbol, 2)
arbol = insertarArbol(arbol, 7)
arbol = insertarArbol(arbol, 1)
arbol = insertarArbol(arbol, 3)
arbol = insertarArbol(arbol, 13)
arbol = insertarArbol(arbol, 5)
arbol = insertarArbol(arbol, 9)
arbol = insertarArbol(arbol, 23)
# preorden(arbol)


# B y C
def contar_hojas(raiz, cont=0):
    if raiz is not None:
        if raiz.izq is None and raiz.der is None:
            cont += 1
            print(raiz.info)
        cont = contar_hojas(raiz.izq, cont)
        cont = contar_hojas(raiz.der, cont)
    return cont


def ver_padre(raiz, hijo, padre=None):
    if raiz is not None:
        if raiz.izq is not None:
            if raiz.izq.info == hijo:
                padre = raiz
        if raiz.der is not None:
            if raiz.der.info == hijo:
                padre = raiz
        padre = ver_padre(raiz.izq, hijo, padre=padre)
        padre = ver_padre(raiz.der, hijo, padre=padre)
    return padre


def manejo_arbol(arbol):
    aux = 0
    aux = contar_nodos(arbol, aux)
    print ("La cantidad de nodos son: ", aux)
    print("Las hojas son:")
    aux1 = contar_hojas(arbol)
    print("La cantidad de hojas son: ", aux1)
    aux2 = ver_padre(arbol, 1)
    print("El padre es: ", aux2.info)
    print('La altura del arbol es: ')
    print(altura(arbol))


# EJERCICIO 11
def generar_bosque(raiz, nivel, lista_bosque, nivel_act=0):
    if raiz is not None:
        if nivel-2 == nivel_act:
            if raiz.izq is not None:
                lista_bosque.append(raiz.izq)
            if raiz.der is not None:
                lista_bosque.append(raiz.der)
        nivel_act += 1
        generar_bosque(raiz.izq, nivel, lista_bosque, nivel_act)
        generar_bosque(raiz.der, nivel, lista_bosque, nivel_act)
    else:
        nivel_act = 0
    return lista_bosque


def nueveNiveles():
    arbol = None
    cantidad_nodos = 0
    for i in range(0, 9):
        pote = 2**i
        cantidad_nodos = cantidad_nodos + pote
    for i in range(1, cantidad_nodos):
        arbol = insertarArbol(arbol, i)
    lista_nivel2 = []
    lista_nivel2 = generar_bosque(arbol, 2, lista_nivel2)
    lista_nivel3 = []
    lista_nivel3 = generar_bosque(arbol, 3, lista_nivel3)
    print('Cantidad de nodos del primer nivel: ', contar_nodos(arbol))
    print('Barrido preorden del primer nivel: ')
    preorden(arbol)
    print('Cantidad de nodos del segundo nivel: ')
    aux = 0
    for i in lista_nivel2:
        aux += 1
        print('Arbol ', aux)
        print(contar_nodos(i))
        print('Barrido preorden del segundo nivel arbol ', aux)
        preorden(i)
    print('Cantidad de nodos del tercer nivel: ')
    aux = 0
    for i in lista_nivel3:
        aux += 1
        print('Arbol ', aux)
        print(contar_nodos(i))
        print('Barrido preorden del tercer nivel arbol ', aux)
        preorden(i)
    aux = 0
    lista_bosque = []
    lista_bosque.append(arbol)
    for i in lista_nivel2:
        lista_bosque.append(i)
    for i in lista_nivel3:
        lista_bosque.append(i)
    aux = 0
    for i in lista_bosque:
        if contar_nodos(i) > aux:
            aux = aux + contar_nodos(i)
            arbol_mas_nodos = i
    print('El arbol con mas nodos es: ')
    preorden(arbol_mas_nodos)
    aux = 0
    for i in lista_bosque:
        aux += 1
        if arbol_completo(i):
            print('Arbol ', aux, ' esta completo.')
        else:
            print('Arbol ', aux, ' esta incompleto.')


# EJERCICIO 12
def decicionSuperheroes():
    arbol = None
    lista = ['Estrategica', ['Spiderman', 'Doctor Strange'], 'Destruccion', ['Hulk', 'Spiderman', 'Thor'], 'Intergalactica', ['Guardianes de la galaxia', 'Capitana Marvel'], 'Recuperacion', ['Ant-man', 'Capitan America', 'Spiderman', 'Black Widow'], 'Defensa', ['Capitan America', 'Spiderman', 'Iron-Man']]
    cod = [1000, 500, 2000, 1500, 3000, 2500, 4000, 3500, 5000, 4500]
    for i in range(0, len(lista)):
        arbol = insertarArbol2(arbol, lista[i], cod[i])
    return arbol


def misiones_superheroes(mision):
    arbol = decicionSuperheroes()
    decision = False
    superHeroes = ''
    while decision is not True and arbol is not None:
        if arbol.info == mision:
            superHeroes = arbol.izq.info
            decision = True
        else:
            arbol = arbol.der

    if len(superHeroes) > 0:
        print('Los superheroes indicados para esta mision son: ')
        print(superHeroes)
    else:
        print('No se encontro o la mision o los superheroes')


# EJERCICIO 13
def arbolMorse():
    lista_morse = [' ', 'E', 'T', 'I', 'A', 'N', 'M', 'S', 'U', 'R', 'W', 'D', 'K', 'G', 'O', 'H', 'V', 'F', ' ', 'L', ' ', 'P', 'J', 'B', 'X', 'C', 'Y', 'Z', 'Q', ' ', ' ', '5', '4', '3', '2', '1', '6', '7', '8', '9', '0']
    cod = [1000, 500, 1500, 250, 750, 1250, 1750, 225, 275, 725, 775, 1225, 1275, 1725, 1775, 112, 237, 265, 285, 612, 737, 765, 785, 1112, 1237, 1265, 1285, 1612, 1737, 1765, 1785, 55, 115, 247, 747, 795, 1055, 1606, 1755, 1778, 1788]
    raiz = None
    for i in range(0, len(lista_morse)):
        raiz = insertarArbol2(raiz, lista_morse[i], cod[i])
    return raiz


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


# EJERCICIO 14
class PersonajesStarWars():
    nombre, altura, peso, estado = None, None, None, None


def archivo_personajes():
    eliminarArchivo('personajesStarWars.db')
    nombre = ['Chewbacca', 'Darth Vader', 'Yoda', 'Luke Skywalker', 'R2-D2', 'C3PO', 'Obi-Wan Kenobi', 'Boba Fett']
    altura = []
    peso = []
    for i in range(0, len(nombre)):
        altura.append(random.uniform(0.3, 3))
        peso.append(random.uniform(1, 100))
    archivo = abrir('personajesStarWars.db')
    ruta = 'personajesStarWars.db'
    for i in range(0, len(nombre)):
        personaje = PersonajesStarWars()
        personaje.nombre = nombre[i]
        personaje.altura = altura[i]
        personaje.peso = peso[i]
        personaje.estado = True
        guardar(archivo, personaje)
    archivo.close()
    return ruta


def armarArbolNombre(ruta_archivo):
    archivo = abrir(ruta_archivo)
    arbol = None
    indice = 0
    dato_archivo = leer(archivo, indice)
    while dato_archivo is not None:
        dato_arbol = []
        if dato_archivo.estado:
            dato_arbol.append(dato_archivo.nombre)
            dato_arbol.append(indice)
            arbol = insertarArbol(arbol, dato_arbol)
        indice += 1
        dato_archivo = leer(archivo, indice)
    archivo.close()
    return arbol


def armarArbolAltura(ruta_archivo):
    archivo = abrir(ruta_archivo)
    arbol = None
    indice = 0
    dato_archivo = leer(archivo, indice)
    while dato_archivo is not None:
        dato_arbol = []
        if dato_archivo.estado:
            dato_arbol.append(dato_archivo.altura)
            dato_arbol.append(indice)
            arbol = insertarArbol(arbol, dato_arbol)
        indice += 1
        dato_archivo = leer(archivo, indice)
    archivo.close()
    return arbol


def armarArbolPeso(ruta_archivo):
    archivo = abrir(ruta_archivo)
    arbol = None
    indice = 0
    dato_archivo = leer(archivo, indice)
    while dato_archivo is not None:
        dato_arbol = []
        if dato_archivo.estado:
            dato_arbol.append(dato_archivo.peso)
            dato_arbol.append(indice)
            arbol = insertarArbol(arbol, dato_arbol)
        indice += 1
        dato_archivo = leer(archivo, indice)
    archivo.close()
    return arbol


def altaPersonaje(ruta_archivo):
    """Da de alta un personaje en el archivo y actualiza el arbol"""
    archivo = abrir(ruta_archivo)
    personaje = PersonajesStarWars()
    personaje.nombre = input('Ingrese el nombre del personaje: ')
    personaje.altura = input('Ingrese la altura del personaje: ')
    personaje.peso = input('Ingrese el peso del personaje: ')
    personaje.estado = True
    guardar(archivo, personaje)
    archivo.close()
    arbol = armarArbolNombre(ruta_archivo)
    return arbol


def buscar(arbol, buscado):
    """Busca por nombre del personaje"""
    """DEVUELVE INDICE EN EL ARCHIVO"""
    dato = busqueda_arbolCampo(arbol, buscado)
    if dato is None:
        print('No se encontro')
    else:
        return dato.info[1]


def modificacion(ruta_archivo, indice):
    """Mediante el indice obtenido del arbol obtiene el dato en el archivo"""
    """Devuelve el arbol actualizado"""
    archivo = abrir(ruta_archivo)
    dato = leer(archivo, indice)
    print('Nombre: ', dato.nombre)
    print('Altura: ', dato.altura)
    print('Peso: ', dato.peso)
    control = ''
    control = input('Desea modificar el nombre? - s = Si  n = No: ')
    if control == 's':
        dato.nombre = input('Ingrese el nuevo nombre: ')
    control = ''
    control = input('Desea modificar la altura? - s = Si  n = No: ')
    if control == 's':
        dato.alutra = input('Ingrese la altura nueva: ')
    control = ''
    control = input('Desea modificar el peso? - s = Si  n = No: ')
    if control == 's':
        dato.peso = input('Ingrese el peso nuevo: ')
    modificar(archivo, dato, indice)
    archivo.close()
    arbol = armarArbolNombre(ruta_archivo)
    return arbol


def baja(ruta_archivo, indice):
    """ BAJA LOGICA por el campo de ESTADO"""
    """Mediante el indice obtenido del arbol obtiene el dato en el archivo"""
    archivo = abrir(ruta_archivo)
    dato = leer(archivo, indice)
    dato.estado = False
    modificar(archivo, dato, indice)
    archivo.close()
    arbol = armarArbolNombre(ruta_archivo)
    return arbol


def consulta(ruta_archivo, indice):
    archivo = abrir(ruta_archivo)
    dato = leer(archivo, indice)
    print('Nombre del personaje: ')
    print(dato.nombre)
    print('Altura del personaje: ')
    print(dato.altura)
    print('Peso del personaje: ')
    print(dato.peso)


def listadoIndicesPeso(arbol, listado=[]):
    if arbol is not None:
        listado = listadoIndicesPeso(arbol.izq)
        if arbol.info[0] < 75:
            listado.append(arbol.info)
        listado = listadoIndicesPeso(arbol.der)
    return listado


def listadoIndicesAltura(arbol, listado=[]):
    if arbol is not None:
        listado = listadoIndicesAltura(arbol.izq)
        if arbol.info[0] > 1:
            listado.append(arbol.info)
        listado = listadoIndicesAltura(arbol.der)
    return listado


def listadoAlfabeticamente(ruta_archivo, lista):
    archivo = abrir(ruta_archivo)
    lista_ordenada = []
    for i in lista:
        lista_ordenada.append(leer(archivo, i[1]))
    lista_ordenada = sorted(lista_ordenada, key=lambda PersonajesStarWars: PersonajesStarWars.nombre)
    return lista_ordenada


def indicesArchivo():
    """Cada vez que se ejecute esta funcion el archivo vuelve a tener
    los mismos datos que se le setea en la funcion archivo_personajes"""
    """Datos seteados en archivo_personajes"""
    ruta_archivo = archivo_personajes()
    arbol = armarArbolNombre(ruta_archivo)
    imprimirArbol(arbol)
    """Alta"""
    print('!------------------------------------------!')
    arbol = altaPersonaje(ruta_archivo)
    imprimirArbol(arbol)
    """Modificacion"""
    print('!------------------------------------------!')
    indice = buscar(arbol, 'Chewbacca')
    arbol = modificacion(ruta_archivo, indice)
    imprimirArbol(arbol)
    """Baja"""
    print('!------------------------------------------!')
    indice = buscar(arbol, 'Chewbaccax')
    arbol = baja(ruta_archivo, indice)
    imprimirArbol(arbol)
    """Consulta"""
    indice = buscar(arbol, 'Yoda')
    consulta(ruta_archivo, indice)
    print('!------------------------------------------------!')
    indice = buscar(arbol, 'Boba Fett')
    consulta(ruta_archivo, indice)
    arbolPeso = armarArbolPeso(ruta_archivo)
    arbolAltura = armarArbolAltura(ruta_archivo)
    listadoPeso = listadoIndicesPeso(arbolPeso)
    print('!----------------------------------------------!')
    listadoAltura = listadoIndicesAltura(arbolAltura)
    print('Listado ordenado alfabeticamente de los personajes que pesan menos de 75kg: ')
    lista_ordenada = listadoAlfabeticamente(ruta_archivo, listadoPeso)
    for i in range(len(lista_ordenada)):
        print('Nombre: ')
        print(lista_ordenada[i].nombre)
        print('Peso: ')
        print(lista_ordenada[i].peso)
    print('!----------------------------------------------!')
    print('Listado ordenado alfabeticamente de los personajes que miden mas de 1m: ')
    lista_ordenada = listadoAlfabeticamente(ruta_archivo, listadoAltura)
    for i in range(len(lista_ordenada)):
        print('Nombre: ')
        print(lista_ordenada[i].nombre)
        print('Peso: ')
        print(lista_ordenada[i].altura)


# EJERCICIO 15
def comprimirPalabras(mensaje, tabla_codificacion):
    mensaje_comprimido = ''
    aux = ''
    for i in mensaje:
        if i == '-':
            mensaje_comprimido = mensaje_comprimido + tabla_codificacion[aux]
            aux = ''
        else:
            aux = aux+i
    return mensaje_comprimido


def nanoSatelites():
    """No anduvo ejecutandolo desde la consola de ubuntu"""
    simbolos = ['Despejado', 'Nublado', 'Lluvia', 'Baja', 'Alta', '1', '2', '3', '5', '7', '8']
    frecuencia = [0.22, 0.15, 0.03, 0.26, 0.14, 0.05, 0.01, 0.035, 0.06, 0.02, 0.025]
    lista_datos = Lista()
    for i in range(0, len(simbolos)):
        dato = []
        dato = [frecuencia[i], simbolos[i]]
        aux = None
        aux = insertarArbol(aux, dato)
        insertarNodosArbol(lista_datos, aux)
    a = ArbolHuffman(lista_datos)
    diccionario_codificacion = {
        'Despejado': '00',
        'Nublado': '111',
        'Lluvia': '01110',
        'Baja': '10',
        'Alta': '110',
        '1': '0100',
        '2': '010110',
        '3': '01111',
        '5': '0110',
        '7': '010111',
        '8': '01010'
    }
    mensaje_comprimido = comprimirPalabras('Nublado-Baja-1-5-7-', diccionario_codificacion)
    print('Tamanio del mensaje comprimido: ', mensaje_comprimido)
    print(getsizeof(mensaje_comprimido))
    mensaje_descomprimido = descomprimir(mensaje_comprimido, a)
    print('Tamanio del mensaje descomprimido: ', mensaje_descomprimido)
    print(getsizeof(mensaje_descomprimido))


# EJERCICIO 16
class Pokemon():
    nombre, numero, tipo, debilidad = None, None, None, None


def archivo_pokemon():
    eliminarArchivo('pokemon.db')
    nombre = ['Bulbasaur', 'BulIvysaur', 'Charmander', 'Charizard', 'Squirtle', 'Butterfree', 'Pidgeotto', 'BulRattata', 'Weedle', 'BulPikachu', 'Raichu', 'Meowth', 'Growlithe', 'Tentacool', 'Weepinbell']
    lista_tipo = ['Normal', 'Lucha', 'Volador', 'Veneno', 'Tierra', 'Roca']
    lista_debil = ['Jolteon', 'Lycanroc', 'Tyrantrum', 'Fuego', 'Electrico', 'Agua']
    numero = []
    tipo = []
    debilidad = []
    for i in range(0, len(nombre)):
        numero.append(random.randint(1, len(nombre)))
        tipo.append(random.choice(lista_tipo))
        debilidad.append(random.choice(lista_debil))
    archivo = abrir('pokemon.db')
    ruta = 'pokemon.db'
    for i in range(0, len(nombre)):
        pokemon = Pokemon()
        pokemon.nombre = nombre[i]
        pokemon.numero = numero[i]
        pokemon.tipo = tipo[i]
        pokemon.debilidad = debilidad[i]
        guardar(archivo, pokemon)
    archivo.close()
    return ruta


def armarArbolPokemon(ruta_archivo):
    archivo = abrir(ruta_archivo)
    arbol = None
    indice = 0
    dato_archivo = leer(archivo, indice)
    while dato_archivo is not None:
        dato_arbol = []
        dato_arbol.append(dato_archivo.nombre)
        dato_arbol.append(indice)
        arbol = insertarArbol(arbol, dato_arbol)
        indice += 1
        dato_archivo = leer(archivo, indice)
    archivo.close()
    return arbol


def armarArbolNumero(ruta_archivo):
    archivo = abrir(ruta_archivo)
    arbol = None
    indice = 0
    dato_archivo = leer(archivo, indice)
    while dato_archivo is not None:
        dato_arbol = []
        dato_arbol.append(dato_archivo.numero)
        dato_arbol.append(indice)
        arbol = insertarArbol(arbol, dato_arbol)
        indice += 1
        dato_archivo = leer(archivo, indice)
    archivo.close()
    return arbol


def buscarProximidad(arbol, buscado):
    """Busca por nombre del personaje"""
    """DEVUELVE INDICE EN EL ARCHIVO"""
    dato = []
    dato = busquedaOcurrenciasProximidad(arbol, buscado, dato)
    if dato is None:
        print('No se encontro')
    else:
        return dato


def buscarOcurrencias(arbol, buscado, dato=[]):
    """Busca por nombre del personaje"""
    """DEVUELVE INDICE EN EL ARCHIVO"""
    dato = busquedaOcurrencias(arbol, buscado, dato)
    if dato is None:
        print('No se encontro')
    else:
        return dato


def armarArbolTipo(ruta_archivo):
    archivo = abrir(ruta_archivo)
    arbol = None
    indice = 0
    dato_archivo = leer(archivo, indice)
    while dato_archivo is not None:
        dato_arbol = []
        dato_arbol.append(dato_archivo.tipo)
        dato_arbol.append(indice)
        arbol = insertarArbol(arbol, dato_arbol)
        indice += 1
        dato_archivo = leer(archivo, indice)
    archivo.close()
    return arbol


def armarArbolDebilidad(ruta_archivo):
    archivo = abrir(ruta_archivo)
    arbol = None
    indice = 0
    dato_archivo = leer(archivo, indice)
    while dato_archivo is not None:
        dato_arbol = []
        dato_arbol.append(dato_archivo.debilidad)
        dato_arbol.append(indice)
        arbol = insertarArbol(arbol, dato_arbol)
        indice += 1
        dato_archivo = leer(archivo, indice)
    archivo.close()
    return arbol


def tiposPokemon(arbol, tipos=[], aux=''):
    if arbol is not None:
        tipos = tiposPokemon(arbol.izq)
        aux = arbol.info[0]
        if (aux in tipos) is False:
            tipos.append(aux)
        tipos = tiposPokemon(arbol.der)
    return tipos


def pokemones():
    ruta = archivo_pokemon()
    arbolNombre = armarArbolPokemon(ruta)
    arbolNumero = armarArbolNumero(ruta)
    arbolTipo = armarArbolTipo(ruta)
    arbolDebilidad = armarArbolDebilidad(ruta)
    buscarNumero = int(input('Ingrese un numero de pokemon que desea buscar: '))
    # Linea de la funcion buscar : 869
    indices = None
    indices = buscar(arbolNumero, buscarNumero)
    dato = []
    print('!-----------------------------------------------------------!')
    if indices is not None:
        archivo = abrir(ruta)
        print('Datos del pokemon buscado por numero: ')
        dato = leer(archivo, indices)
        print('Nombre: ', dato.nombre)
        print('Numero: ', dato.numero)
        print('Tipo: ', dato.tipo)
        print('Debilidad: ', dato.debilidad)
        archivo.close()
    indices = None
    """Probado ingresando Bul"""
    print('!-----------------------------------------------------------!')
    buscarNombre = input('Ingrese el nombre del pokemon que desea buscar: ')
    dato = []
    indices = buscarProximidad(arbolNombre, buscarNombre)
    if indices is not None:
        for i in indices:
            archivo = abrir(ruta)
            print('Datos del pokemon buscado por Nombre: ')
            dato = leer(archivo, i.info[1])
            print('Nombre: ', dato.nombre)
            print('Numero: ', dato.numero)
            print('Tipo: ', dato.tipo)
            print('Debilidad: ', dato.debilidad)
            archivo.close()
    indices = None
    print('!-----------------------------------------------------------!')
    buscarTipo = input('Ingrese el tipo que desea buscar: ')
    dato = []
    indices = buscarOcurrencias(arbolTipo, buscarTipo, dato)
    if indices is not None:
        for i in indices:
            archivo = abrir(ruta)
            print('Datos del pokemon buscado por tipo: ')
            dato = leer(archivo, i.info[1])
            print('Nombre: ', dato.nombre)
            print('Numero: ', dato.numero)
            print('Tipo: ', dato.tipo)
            print('Debilidad: ', dato.debilidad)
            archivo.close()
    print('!-----------------------------------------------------------!')
    print('Pokemones debiles contra Jolteon: ')
    indices = None
    dato = []
    indices = buscarOcurrencias(arbolDebilidad, 'Jolteon', dato)
    if indices is not None:
        for i in indices:
            archivo = abrir(ruta)
            print('Datos del pokemon buscado por numero: ')
            dato = leer(archivo, i.info[1])
            print('Nombre: ', dato.nombre)
            print('Debilidad: ', dato.debilidad)
            archivo.close()
    print('!-----------------------------------------------------------!')
    print('Pokemones debiles contra Lycanroc: ')
    indices = None
    dato = []
    indices = buscarOcurrencias(arbolDebilidad, 'Lycanroc', dato)
    if indices is not None:
        for i in indices:
            archivo = abrir(ruta)
            print('Datos del pokemon buscado por numero: ')
            dato = leer(archivo, i.info[1])
            print('Nombre: ', dato.nombre)
            print('Debilidad: ', dato.debilidad)
            archivo.close()
    print('!-----------------------------------------------------------!')
    print('Pokemones debiles contra Tyrantrum: ')
    indices = None
    dato = []
    indices = buscarOcurrencias(arbolDebilidad, 'Tyrantrum', dato)
    if indices is not None:
        for i in indices:
            archivo = abrir(ruta)
            print('Datos del pokemon buscado por numero: ')
            dato = leer(archivo, i.info[1])
            print('Nombre: ', dato.nombre)
            print('Debilidad: ', dato.debilidad)
            archivo.close()
    print('!-----------------------------------------------------------!')
    lista_tipos = tiposPokemon(arbolTipo)
    print(lista_tipos)
    for i in lista_tipos:
        aux = []
        aux = busquedaOcurrencias(arbolTipo, i, aux)
        print('Cantidad de pokemones de tipo ', i, ': ')
        print(len(aux))


# EJERCICIO 17
class Mision():
    general, fecha, codigo_blaster, estado_blaster, tipo_soldado = None, None, None, None, None


def cantidadFallas(arbol, general, contador=0):
    if arbol is not None:
        contador = cantidadFallas(arbol.izq, general, contador=contador)
        if arbol.info.general == general:
            if arbol.info.estado_blaster is True:
                contador += 1
        contador = cantidadFallas(arbol.der, general, contador=contador)
    return contador


def cantidadMisiones(arbol, general, contador=0):
    if arbol is not None:
        contador = cantidadMisiones(arbol.izq, general, contador=contador)
        if arbol.info.general == general:
            print('Tipo de soldado en la mision: ', arbol.info.tipo_soldado)
            contador += 1
        contador = cantidadMisiones(arbol.der, general, contador=contador)
    return contador


def cantidadSoldados(arbol, soldado, contador_soldado=0, contador_falla=0):
    if arbol is not None:
        contador_soldado, contador_falla = cantidadSoldados(arbol.izq, soldado, contador_soldado=contador_soldado, contador_falla=contador_falla)
        if arbol.info.tipo_soldado == soldado:
            if arbol.info.estado_blaster:
                contador_falla += 1
            contador_soldado += 1
        contador_soldado, contador_falla = cantidadSoldados(arbol.der, soldado, contador_soldado=contador_soldado, contador_falla=contador_falla)
    return contador_soldado, contador_falla


def blasterEnFecha(arbol, fecha, contador_blaster=0, contador_falla=0):
    if arbol is not None:
        contador_blaster, contador_falla = blasterEnFecha(arbol.izq, fecha, contador_blaster=contador_blaster, contador_falla=contador_falla)
        if arbol.info.fecha == fecha:
            print('Codigo del blaster: ', arbol.info.codigo_blaster)
            contador_blaster += 1
            if arbol.info.estado_blaster:
                contador_falla += 1
        contador_blaster, contador_falla = blasterEnFecha(arbol.der, fecha, contador_blaster=contador_blaster, contador_falla=contador_falla)
    return contador_blaster, contador_falla


def armeria():
    """
        TRUE = Fallo
        False = No Fallo
    """
    arbol = None
    general = ['Kylo Ren', 'General Hux', 'Capitana Phasma']
    fechas_mision = []
    for i in range(0, 20):
        dia = str(random.randint(1, 30))
        mes = str(random.randint(1, 12))
        anio = str(random.randint(1990, 2012))
        fecha = time.strftime(dia+'/'+mes+'/'+anio)
        fechas_mision.append(fecha)
    estado = [True, False]
    tipo_soldado = ['Imperial Stromtrooper', 'Imperial Scout Trooper', 'Imperial Death Trooper', 'Sith Trooper', 'First Order Stromtrooper']
    reporte = Mision()
    reporte.general = random.choice(general)
    reporte.fecha = random.choice(fechas_mision)
    reporte.codigo_blaster = '75961380'
    reporte.estado_blaster = random.choice(estado)
    reporte.tipo_soldado = random.choice(tipo_soldado)
    arbol = insertarReportesArmeria(arbol, reporte)
    for i in range(0, 9999):
        codigo = ''
        j = 0
        while j != 8:
            digito = str(random.randint(0, 9))
            if digito in codigo:
                """Nada"""
            else:
                codigo = codigo + digito
                j += 1
        reporte = Mision()
        reporte.general = random.choice(general)
        reporte.fecha = random.choice(fechas_mision)
        reporte.codigo_blaster = codigo
        reporte.estado_blaster = random.choice(estado)
        reporte.tipo_soldado = random.choice(tipo_soldado)
        arbol = insertarReportesArmeria(arbol, reporte)
    for i in general:
        contador = 0
        contador = cantidadFallas(arbol, i, contador)
        print('Cantidad de armas que fallaron con el general: ', i)
        print(contador)
    print('Info del general Kylo Ren: ')
    cantidad_misiones = cantidadMisiones(arbol, 'Kylo Ren')
    print('Cantidad de misiones de Kylo Ren: ', cantidad_misiones)
    cantidad_soldados, cantidad_fallas = cantidadSoldados(arbol, 'Sith Trooper')
    print('Cantidad de misiones de Sith Trooper: ', cantidad_soldados)
    print('Cantidad de fallas de blaster: ', cantidad_fallas)
    fecha = random.choice(fechas_mision)
    print('Codigos de blasters en la fecha: ', fecha)
    cantidad_blasters, cantidad_fallas = blasterEnFecha(arbol, fecha)
    promedio = 0
    if cantidad_fallas != 0:
        promedio = cantidad_blasters / cantidad_fallas
    print('El promedio de falla de blaster en la fecha fue de: ', promedio)
    codigo_blaster = busqueda_arbolAtributoCodigo(arbol, '75961380')
    if codigo_blaster is None:
        print('No se econtro blaster con ese codigo')
    else:
        print('General: ', codigo_blaster.info.general)
        print('Fecha: ', codigo_blaster.info.general)
        print('Codigo: ', codigo_blaster.info.codigo_blaster)
        print('Estado: ', codigo_blaster.info.estado_blaster)
        print('Tipo de soldado: ', codigo_blaster.info.tipo_soldado)


# EJERCICIO 18
class Libro():
    titulo, isbn, autores, editorial, cantidadPaginas = None, None, None, None, None


def archivo_libro():
    eliminarArchivo('libros.db')
    """ DATOS NECESARIOS PARA EL EJERCICIO"""
    titulos = ['Algoritmos', 'Bases de Datos', 'NoSQL for Mere Mortals', 'Libro A', 'Libro B', 'Libro C', 'Libro D', 'Libro E']
    autores = ['Tanenbaum', 'Connolly', 'Rowling', 'Riordan']
    libro = Libro()
    libro.titulo = 'Mineria de Datos'
    libro.isbn = '9788420546391'
    libro.autores = 'Autor A'
    libro.editorial = 'Editorial A'
    libro.cantidadPaginas = 340
    archivo = abrir('libros.db')
    guardar(archivo, libro)
    for i in range(0, len(titulos)):
        isbn = ''
        for j in range(0, 9):
            isbn = isbn + str(random.randint(0, 9))
        libro = Libro()
        libro.titulo = titulos[i]
        libro.autores = random.choice(autores)
        libro.isbn = isbn
        libro.editorial = 'editorial'+str(i)
        libro.cantidadPaginas = random.randint(50, 1000)
        guardar(archivo, libro)
    archivo.close()
    """ DATOS NECESARIOS PARA EL EJERCICIO FIN"""
    archivo = abrir('libros.db')
    ruta = 'libros.db'
    titulo = 'libro'
    autor = 'autor'
    editorial = 'editorial'
    for i in range(0, 100):
        isbn = ''
        for j in range(0, 9):
            isbn = isbn + str(random.randint(0, 9))
        libro = Libro()
        libro.titulo = titulo+str(i)
        libro.autores = autor+str(i)
        libro.isbn = isbn
        libro.editorial = editorial+str(i)
        libro.cantidadPaginas = random.randint(50, 1000)
        guardar(archivo, libro)
    archivo.close()
    return ruta


def armarArbolLibro(ruta_archivo):
    archivo = abrir(ruta_archivo)
    arbol = None
    indice = 0
    dato_archivo = leer(archivo, indice)
    while dato_archivo is not None:
        dato_arbol = []
        dato_arbol.append(dato_archivo.titulo)
        dato_arbol.append(indice)
        arbol = insertarArbol(arbol, dato_arbol)
        indice += 1
        dato_archivo = leer(archivo, indice)
    archivo.close()
    return arbol


def armarArbolIsbn(ruta_archivo):
    archivo = abrir(ruta_archivo)
    arbol = None
    indice = 0
    dato_archivo = leer(archivo, indice)
    while dato_archivo is not None:
        dato_arbol = []
        dato_arbol.append(dato_archivo.isbn)
        dato_arbol.append(indice)
        arbol = insertarArbol(arbol, dato_arbol)
        indice += 1
        dato_archivo = leer(archivo, indice)
    archivo.close()
    return arbol


def armarArbolAutor(ruta_archivo):
    archivo = abrir(ruta_archivo)
    arbol = None
    indice = 0
    dato_archivo = leer(archivo, indice)
    while dato_archivo is not None:
        dato_arbol = []
        dato_arbol.append(dato_archivo.autores)
        dato_arbol.append(indice)
        arbol = insertarArbol(arbol, dato_arbol)
        indice += 1
        dato_archivo = leer(archivo, indice)
    archivo.close()
    return arbol


def armarArbolCantPag(ruta_archivo):
    archivo = abrir(ruta_archivo)
    arbol = None
    indice = 0
    dato_archivo = leer(archivo, indice)
    while dato_archivo is not None:
        dato_arbol = []
        dato_arbol.append(dato_archivo.cantidadPaginas)
        dato_arbol.append(indice)
        arbol = insertarArbol(arbol, dato_arbol)
        indice += 1
        dato_archivo = leer(archivo, indice)
    archivo.close()
    return arbol


def consultarAutores(ruta, arbol, autor):
    print('!----------------------------------------------!')
    indices = []
    indices = busquedaOcurrencias(arbol, autor, indices)
    archivo = abrir(ruta)
    for i in indices:
        dato = leer(archivo, i.info[1])
        print('Titulo: ', dato.titulo)
        print('Isbn: ', dato.isbn)
        print('Autor: ', dato.autores)
        print('Editorial: ', dato.editorial)
        print('Cantidad de paginas: ', dato.cantidadPaginas)
    print('!----------------------------------------------!')
    archivo.close()


def consultarTitulos(ruta, arbol, titulo):
    indices = []
    indices = busquedaOcurrenciasProximidad(arbol, titulo, indices)
    archivo = abrir(ruta)
    for i in indices:
        dato = leer(archivo, i.info[1])
        print('Titulo: ', dato.titulo)
        print('Isbn: ', dato.isbn)
        print('Autor: ', dato.autores)
        print('Editorial: ', dato.editorial)
        print('Cantidad de paginas: ', dato.cantidadPaginas)
    print('!----------------------------------------------!')
    archivo.close()


def consultaIsbn(ruta, arbol, isbn):
    indice = busqueda_arbolCampo(arbol, isbn)
    archivo = abrir(ruta)
    dato = leer(archivo, indice.info[1])
    print('Titulo: ', dato.titulo)
    print('Isbn: ', dato.isbn)
    print('Autor: ', dato.autores)
    print('Editorial: ', dato.editorial)
    print('Cantidad de paginas: ', dato.cantidadPaginas)
    archivo.close()


def librosMas876(ruta, arbol, lista=[]):
    if arbol is not None:
        if arbol.info[0] >= 876:
            lista.append(arbol)
            lista = librosMas876(ruta, arbol.der, lista=lista)
            lista = librosMas876(ruta, arbol.izq, lista=lista)
        else:
            lista = librosMas876(ruta, arbol.der, lista=lista)
    return lista


def libros():
    ruta = archivo_libro()
    arbol_titulo = armarArbolLibro(ruta)
    arbol_isbn = armarArbolIsbn(ruta)
    arbol_autor = armarArbolAutor(ruta)
    arbol_paginas = armarArbolCantPag(ruta)
    """Busqueda por autores"""
    print('Consulta del autor Tanenbaum')
    consultarAutores(ruta, arbol_autor, 'Tanenbaum')
    print('Consulta del autor Connolly')
    consultarAutores(ruta, arbol_autor, 'Connolly')
    print('Consulta del autor Rowling')
    consultarAutores(ruta, arbol_autor, 'Rowling')
    print('Consulta del autor Riordan')
    consultarAutores(ruta, arbol_autor, 'Riordan')
    """Busqueda por titulo """
    print('Consulta del titulo Mineria de datos')
    consultarTitulos(ruta, arbol_titulo, 'Mineria')
    print('Consulta del titulo Algoritmos')
    consultarTitulos(ruta, arbol_titulo, 'Alg')
    print('Consulta del titulo Bases de Datos')
    consultarTitulos(ruta, arbol_titulo, 'Bases')
    masPaginas = []
    masPaginas = librosMas876(ruta, arbol_paginas, masPaginas)
    archivo = abrir(ruta)
    for i in masPaginas:
        dato = leer(archivo, i.info[1])
        print('Titulo: ', dato.titulo)
        print('Isbn: ', dato.isbn)
        print('Autor: ', dato.autores)
        print('Editorial: ', dato.editorial)
        print('Cantidad de paginas: ', dato.cantidadPaginas)
    print('!----------------------------------------------!')
    archivo.close()
    print('Consulta del libro con Isbn 9788420546391: ')
    consultaIsbn(ruta, arbol_isbn, '9788420546391')
    print('!----------------------------------------------!')
    busc_autor = busqueda_arbolCampo(arbol_titulo, 'NoSQL for Mere Mortals')
    if busc_autor is not None:
        print('Autor del libro NoSQL for Mere Mortals: ')
        archivo = abrir(ruta)
        dato = leer(archivo, busc_autor.info[1])
        print(dato.autores)


# EJERCICIO 19
def decision_meteorologica():
    data = [['Visibilidad', 15], ['Humedad', 70], 'Despejado', ['Viento', 8.7], ['Visibilidad', 8], ['Viento', 5], 'Parcialmente Nublado', ['Presion', 1013], ['Humedad', 92], 'Despejado', 'Nublado', ['Humedad', 96], ['Viento', 7.2], ['Visibilidad', 12], ['Viento', 12.2], 'Nublado', 'Mayormente Nublado', ['Presion', 1018], 'Nublado', 'Despejado', 'Mayormente Nublado', 'Lluvia', 'Nublado', ['Visibilidad', 1], 'Nublado', 'Lluvia', 'Mayormente Nublado']
    cod = [3000, 2000, 3010, 1000, 2800, 800, 1500, 2500, 2960, 700, 900, 2400, 2700, 2950, 2990, 2300, 2450, 2600, 2750, 2925, 2955, 2980, 2995, 2550, 2650, 2525, 2578]
    arbol = None
    for i in range(0, len(data)):
        arbol = insertarArbol2(arbol, data[i], cod[i])
    temperatura = 40
    presion = 4
    humedad = 80
    visibilidad = 13
    viento = 2
    datos = {
        'Temperatura': temperatura,
        'Presion': presion,
        'Humedad': humedad,
        'Visibilidad': visibilidad,
        'Viento': viento
    }
    pronostico = ''
    while pronostico == '' and arbol is not None:
        if datos[arbol.info[0]] <= arbol.info[1]:
            if arbol.izq.izq is not None:
                arbol = arbol.izq
            else:
                pronostico = arbol.izq.info
                print(pronostico)
        else:
            if arbol.der.der is not None:
                arbol = arbol.der
            else:
                pronostico = arbol.der.info
                print(pronostico)


# EJERCICO 20
def transformacionDioses(datos):
    arbol = None
    aux = datos.keys()
    for i in aux:
        if arbol is None:
            lista = 'Ouranos'
            arbol = insertarTree(arbol, lista)
            lista = datos[i][0]
            arbol.izq = insertarTree(arbol.izq, lista)
            aux_arbol = arbol.izq
            for j in range(1, len(datos[i])):
                lista = datos[i][j]
                aux_arbol.der = insertarTree(aux_arbol.der, lista)
                aux_arbol = aux_arbol.der
        else:
            buscado = busqueda_desordenados(arbol, i[3:])
            lista = datos[i][0]
            buscado.izq = insertarTree(buscado.izq, lista)
            aux_buscado = buscado.izq
            for j in range(1, len(datos[i])):
                lista = datos[i][j]
                aux_buscado.der = insertarTree(aux_buscado.der, lista)
                aux_buscado = aux_buscado.der
    return arbol


def barrido_hermanos(raiz):
    raiz = raiz.izq
    print(raiz.info)
    while raiz.der is not None:
        raiz = raiz.der
        print(raiz.info)


def buscar_padre(arbol, dios, lista=[], encontrado=False):
    if arbol.izq is not None:
        if arbol.der is not None:
            if arbol.info[0] == dios:
                encontrado = True
            lista.append(arbol.info)
            lista, encontrado = buscar_padre(arbol.der, dios, lista=lista)
        else:
            if arbol.info[0] == dios:
                encontrado = True
            lista.append(arbol.info)

            lista, encontrado = buscar_padre(arbol.izq, dios, lista=lista)
    elif arbol.der is not None:
        if arbol.info[0] == dios:
            encontrado = True
        lista.append(arbol.info)
        lista, encontrado = buscar_padre(arbol.der, dios, lista=lista)
    else:
        if arbol.info[0] == dios:
            encontrado = True
        lista.append(arbol.info)
    return lista, encontrado


def barridoInordenDioses(arbol):
    if arbol is not None:
        barridoInordenDioses(arbol.izq)
        print('Nombre del dios: ', arbol.info[0])
        print('Nombre de la madre: ', arbol.info[1])
        barridoInordenDioses(arbol.der)


def dioses_griegos():
    dioses = {
        '01-Ouranos': [['Themis', 'Gaia', 'Descripcion'], ['Mnemosyne', 'Gaia', 'Descripcion'], ['Hyperon', 'Gaia', 'Descripcion'], ['Theia', 'Gaia', 'Descripcion'], ['Krios', 'Gaia', 'Descripcion'], ['Kronos', 'Gaia', 'Descripcion'], ['Rhea', 'Gaia', 'Descripcion'], ['Kdios', 'Gaia', 'Descripcion'], ['Phobe', 'Gaia', 'Descripcion'], ['Iapetos', 'Gaia', 'Descripcion'], ['Okeanos', 'Gaia', 'Descripcion'], ['Tethys', 'Gaia', 'Descripcion']],
        '02-Hyperon': [['Helios', 'Theia', 'Descripcion'], ['Eos', 'Theia', 'Descripcion'], ['Selene', 'Theia', 'Descripcion']],
        '03-Kronos': [['Hades', 'Rhea', 'Descripcion'], ['Demeter', 'Rhea', 'Descripcion'], ['Poseidon', 'Rhea', 'Descripcion'], ['Hestia', 'Rhea', 'Descripcion'], ['Hera', 'Rhea', 'Descripcion'], ['Zeus', 'Rhea', 'Descripcion']],
        '04-Kdios': [['Leto', 'Phobe', 'Descripcion']],
        '05-Iapetos': [['Prometheus', '-', 'Descripcion'], ['Epimetheus', '-', 'Descripcion'], ['Atlas', '-', 'Descripcion']],
        '06-Okeanos': [['Pleione', 'Tethys', 'Descripcion']],
        '07-Atlas': [['Maia', 'Pleione', 'Descripcion']],
        '08-Zeus': [['Persephone', 'Demeter', 'Descripcion'], ['Ares', 'Hera', 'Descripcion'], ['Hephaistos', 'Hera', 'Descripcion'], ['Athena', '-', 'Descripcion'], ['Apolo', 'Leto', 'Descripcion'], ['Artemis', 'Leto', 'Descripcion'], ['Dionysos', 'Semele', 'Descripcion'], ['Hermes', 'Maia', 'Descripcion']],
        '09-Ares': [['Phobes', 'Aphrodite', 'Descripcion'], ['Deimos', 'Aphrodite', 'Descripcion'], ['Eros', 'Aphrodite', 'Descripcion'], ['Humerios', 'Aphrodite', 'Descripcion']],
        '10-Hermes': [['Hermaphrodite', 'Aphrodite', 'Descripcion'], ['Pan', 'Penelope', 'Descripcion']]
    }
    arbol = transformacionDioses(dioses)
    barrido_hermanos(arbol)
    busqueda = busqueda_desordenados(arbol, 'Zeus')
    print('!---------------------------------------------!')
    print('Hijos de Zeus: ')
    barrido_hermanos(busqueda)
    print('Barrido inorden: ')
    inorden(arbol)
    print('Barrido preorden: ')
    preorden(arbol)
    # padre = []
    # padre = buscar_padre(arbol, 'Mnemosyne', padre)
    print('Barrido inorden con el nombre de la madre: ')
    barridoInordenDioses(arbol)
    madre = []
    madre = busquedaOcurrencias(arbol, 'Theia', madre, 1)
    print('Los hijos de Tea son: ')
    for i in madre:
        print(i.info)


# EJERCICIO 21
def vencedores(arbol, listado_vencedores=[]):
    if arbol is not None:
        listado_vencedores = vencedores(arbol.izq, listado_vencedores=listado_vencedores)
        if arbol.info[1] != '-':
            listado_vencedores.append(arbol.info[1])
        listado_vencedores = vencedores(arbol.der, listado_vencedores=listado_vencedores)
    return listado_vencedores


def criaturasDerrotadasPor(arbol, vencedor, listado=[]):
    if arbol is not None:
        listado = criaturasDerrotadasPor(arbol.izq, vencedor, listado=listado)
        if arbol.info[1] == vencedor:
            listado.append(arbol.info[0])
        listado = criaturasDerrotadasPor(arbol.der, vencedor, listado=listado)
    return listado


def tabla():
    criatura = ['Ceto', 'Tifon', 'Equidna', 'Dino', 'Pefredo', 'Enio', 'Escila', 'Caribdis', 'Euriale', 'Esteno', 'Medusa', 'Ladon', 'Aguila del Caucaso', 'Quimera', 'Hidra de Lerna', 'Leon de Nemea', 'Esfinge', 'Dragon de la Colquida', 'Cerbero', 'Cerda de Cromion ', 'Ortro', 'Toro de Creta', 'Jabali de Calidon ', 'Carcinos ', 'Gerion', 'Cloto ', 'Laquesis', 'Atropos', 'Minotauro de Creta', 'Harpias', 'Argos Panoptes', 'Aves del Estinfalo', 'Talos', 'Sirenas', 'Piton', 'Cierva de Cerinea ', 'Basilisco', 'Jabali de Erimanto']
    derrotado_por = ['-', 'Zeus', 'Argos Panoptes', '-', '-', '-', '-', '-', '-', '-', 'Perseo', 'Heracles', '-', 'Belerofonte', 'Heracles', 'Heracles', 'Edipo', '-', '-', 'Teseo', 'Heracles', 'Teseo', 'Atalanta', '-', 'Heracles', '-', '-', '-', 'Teseo', '-', 'Hermes', '-', 'Medea', '-', 'Apolo', '-', '-', '-']
    arbol = None
    for i in range(0, len(criatura)):
        datos_tabla = []
        datos_tabla.append(criatura[i])
        datos_tabla.append(derrotado_por[i])
        datos_tabla.append('Breve descripcion')
        arbol = insertarArbol(arbol, datos_tabla)
    print('Barrido inorden: ')
    inorden(arbol)
    buscar = busqueda_arbolCampo(arbol, 'Talos')
    print("Criatura: ", buscar.info[0])
    print("Derrotado por: ", buscar.info[1])
    print("Descripcion: ", buscar.info[2])
    venc = []
    venc = vencedores(arbol, venc)
    venc_aux = []
    for i in venc:
        if i in venc_aux:
            """NADA"""
        else:
            venc_aux.append(i)
    for i in range(0, len(venc_aux)):
        aux = venc.count(venc_aux[i])
        venc_aux[i] = str(aux)+venc_aux[i]
    venc_aux.sort()
    venc_aux.reverse()
    print('Los Heroes o Dioses mas vencedores son: ')
    for i in range(0, 3):
        print(venc_aux[i][1:])
    derrotados = []
    derrotados = criaturasDerrotadasPor(arbol, 'Heracles', derrotados)
    print('Las criaturas derrotadas por Heracles son: ')
    print(derrotados)
    noDerrotadas = []
    noDerrotadas = criaturasDerrotadasPor(arbol, '-', noDerrotadas)
    print('Las criaturas no derrotadas son: ')
    print(noDerrotadas)
    eliminar, clave = eliminarCampo(arbol, 'Basilisco')
    eliminar, clave = eliminarCampo(arbol, 'Sirenas')
    buscar = busqueda_arbolCampo(arbol, 'Aves del Estinfalo')
    buscar.info[1] = 'Heracles'
    buscar.info[2] = 'Heracles derroto varias aves'
    buscar = busqueda_arbolCampo(arbol, 'Ladon')
    buscar.info[0] = 'Dragon Ladon'


# EJERCICIO 22
def calculoFrecuencias():
    simbolos = ['A', 'B', 'C', 'D', 'E', 'G', 'I', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', ' ', ',']
    cantidad = [11, 2, 4, 3, 14, 3, 6, 6, 3, 6, 7, 4, 1, 10, 4, 3, 4, 2, 17, 2]
    frecuencia = []
    acu = 0
    for i in cantidad:
        acu = acu+i
    for i in range(0, len(simbolos)):
        aux = float(cantidad[i]) / float(acu)
        frecuencia.append(aux)
    lista_datos = Lista()
    for i in range(0, len(simbolos)):
        dato = []
        dato = [frecuencia[i], simbolos[i]]
        aux = None
        aux = insertarArbol(aux, dato)
        insertarNodosArbol(lista_datos, aux)
    """ INTERCAMBIOS """
    aux = busquedaLista(lista_datos, 'V', 1)
    aux2 = lista_datos.inicio
    for i in range(0, aux):
        aux2 = aux2.sig
    aux2.info.info[1] = ','

    aux = busquedaLista(lista_datos, ',', 1)
    aux2 = lista_datos.inicio
    for i in range(0, aux):
        aux2 = aux2.sig
    aux2.info.info[1] = 'V'

    aux = busquedaLista(lista_datos, 'B', 1)
    aux2 = lista_datos.inicio
    for i in range(0, aux):
        aux2 = aux2.sig
    aux2.info.info[1] = 'V'

    aux = busquedaLista(lista_datos, 'V', 1)
    aux2 = lista_datos.inicio
    for i in range(0, aux):
        aux2 = aux2.sig
    aux2.info.info[1] = 'B'
    a = ArbolHuffman(lista_datos)
    mensaje1 = '10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100'
    mensaje2 = '0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010'
    mensaje1_descomprimido = descomprimir(mensaje1, a)
    mensaje2_descomprimido = descomprimir(mensaje2, a)
    print(mensaje1_descomprimido)
    print(mensaje2_descomprimido)
    print('Tamanio del mensaje 1 original: ', getsizeof(mensaje1_descomprimido))
    print('Tamanio del mensaje 2 original: ', getsizeof(mensaje2_descomprimido))
    print('!-------------------------------------------------------------------!')
    print('Tamanio del mensaje 1 comprimido: ', getsizeof(mensaje1))
    print('Tamanio del mensaje 2 comprimido: ', getsizeof(mensaje2))
