import random
import string
from tda_pila import apilar, desapilar, pila_llena, pila_vacia, tamanio, cima
from tda_pila import barrido, Pila


# EJERCICIO 1
def ocurrencias(p, elemento):
    c = 0
    aux = 0
    pila_aux = Pila()
    while not pila_vacia(p):
        aux = desapilar(p)
        if elemento == aux:
            c += 1
        apilar(pila_aux, aux)
    while not pila_vacia(pila_aux):
        apilar(p, desapilar(pila_aux))
    if c == 0:
        print("El elemento no existe en la pila")
    else:
        print("La cantidad de ocurrencias del elemento son: ", c)


# EJERCICIO 2
def pila_pares(p):
    pila_aux = Pila()
    aux = 0
    while not pila_vacia(p):
        aux = desapilar(p)
        if (aux % 2) == 0:
            apilar(pila_aux, aux)
    while not pila_vacia(pila_aux):
        apilar(p, desapilar(pila_aux))
    print('Pila con pares: ')
    barrido(p)


# EJERCICIO 3

def reemplazar_ocurrencias(p, elemento):
    c = 0
    aux = 0
    pila_aux = Pila()
    while not pila_vacia(p):
        aux = desapilar(p)
        if elemento == aux:
            c += 1
            aux = int(input("Ingrese un numero para reemplazar la ocurrencia"))
        apilar(pila_aux, aux)
    while not pila_vacia(pila_aux):
        apilar(p, desapilar(pila_aux))
    if c == 0:
        print("El elemento no existe en la pila")


# EJERCICIO 4

def invertir(p):
    pila_aux = Pila()
    print('Pila original: ')
    barrido(p)
    while not pila_vacia(p):
        apilar(pila_aux, desapilar(p))
    print('Pila invertida: ')
    barrido(pila_aux)


# EJERCICIO 5
def palindromo(cadena):
    p = Pila()
    aux = len(cadena)
    cadena_aux = ''
    for i in range(0, aux):
        car = cadena[i]
        apilar(p, car)
    while not pila_vacia(p):
        cadena_aux = cadena_aux + desapilar(p)
    if cadena == cadena_aux:
        print("la palabra es palindromo")


# EJERCICIO 6
def palabra_invertida(cadena):
    p = Pila()
    aux = len(cadena)
    cadena_aux = ''
    for i in range(0, aux):
        car = cadena[i]
        apilar(p, car)
    while not pila_vacia(p):
        cadena_aux = cadena_aux + desapilar(p)
    print(cadena_aux)


# EJERCICIO 7
def eliminar_elemento(p, pos):
    pila_aux = Pila()
    for i in range(0, pos):
        apilar(pila_aux, desapilar(p))
    desapilar(p)
    while not pila_vacia(pila_aux):
        apilar(p, desapilar(pila_aux))


# EJERCICIO 8
def ordenar_pila(p):
    aux = Pila()
    while not pila_vacia(p):
        cont = 0
        dato = desapilar(p)
        while not pila_vacia(aux) and (cima(aux) >= dato):
            apilar(p, desapilar(aux))
            cont += 1
        apilar(aux, dato)
        for i in range(0, cont):
            apilar(aux, desapilar(p))
    return aux


def cartas():
    p = Pila()
    po = Pila()
    pb = Pila()
    pe = Pila()
    pc = Pila()
    palos = ['Oro', 'Basto', 'Copa', 'Espada']
    while not pila_llena(p):
        num = random.randint(1, 13)
        palo = random.choice(palos)
        apilar(p, [num, palo])
    while not pila_vacia(p):
        aux = desapilar(p)
        if aux[1] == "Basto":
            apilar(pb, aux)
        if aux[1] == "Copa":
            apilar(pc, aux)
        if aux[1] == "Oro":
            apilar(po, aux)
        if aux[1] == "Espada":
            apilar(pe, aux)
    print("Mazo de basto")
    barrido(pb)
    print("Mazo de copa")
    barrido(pc)
    print("Mazo de oro")
    barrido(po)
    print("Mazo de espada")
    barrido(pe)
    pe = ordenar_pila(pe)
    print("Mazo de espada ordenados")
    barrido(pe)


# EJERCICIO 9
def factorial(num):
    p = Pila()
    aux = 1
    for i in range(1, num+1):
        apilar(p, i)
    while not pila_vacia(p):
        aux = aux*desapilar(p)
    print('El factorial de ', num, 'es', aux)


# EJERCICIO 10
def pares_impares(p):
    pila_pares = Pila()
    pila_impares = Pila()
    while not pila_vacia(p):
        aux = desapilar(p)
        if (aux % 2) == 0:
            apilar(pila_pares, aux)
        else:
            apilar(pila_impares, aux)
    print("Pila de pares:   --INICIO--")
    barrido(pila_pares)
    print("Pila de pares:    --FIN--")
    print("Pila de impares:     --INICIO--")
    barrido(pila_impares)
    print("Pila de impares:      --FIN--")


# EJERCICIO 11
def vocales(p):
    c = 0
    while not pila_vacia(p):
        aux = desapilar(p)
        aux.lower()
        if (aux == 'a') or (aux == 'e') or (aux == 'i') or (aux == 'o') or (aux == 'u'):
            c += 1
    print("La cantidad de vocales es: ", c)


# EJERCICIO 12
def ordenados():
    p = Pila()
    p_aux = Pila()
    aux = 0
    elemento = input("Ingrese el elemento (-100 para no cargar mas): ")
    int(elemento)
    while (elemento != -100):
        if pila_llena(p):
            print("No hay mas espacio")
        else:
            if pila_vacia(p):
                apilar(p, elemento)
            else:
                aux = desapilar(p)
                while elemento < aux and not pila_vacia(p):
                    apilar(p_aux, aux)
                    aux = desapilar(p)
                else:
                    if elemento < aux:
                        apilar(p, elemento)
                        apilar(p, aux)
                    else:
                        apilar(p, aux)
                        apilar(p, elemento)
                if not pila_vacia(p_aux):
                    while not pila_vacia(p_aux):
                        apilar(p, desapilar(p_aux))
            elemento = input("Ingrese el elemento (-100 para no cargar mas): ")
            int(elemento)
    barrido(p)


# EJERCICIO 13
def quicksort(v, pri, ult):
    p = Pila()
    apilar(p, [pri, ult])
    datos = []
    while not pila_vacia(p):
        datos = desapilar(p)
        i = datos[0]
        j = datos[1] - 1
        pivot = datos[1]
        while (i < j):
            while (v[i] <= v[pivot]) and (i < j):
                i += 1
            while (v[j] > v[pivot]) and (i < j):
                j -= 1
            if i <= j:
                v[i], v[j] = v[j], v[i]
        if v[pivot] < v[i]:
            v[pivot], v[i] = v[i], v[pivot]
        if datos[0] < j:
            apilar(p, [datos[0], j])
        if datos[1] > i:
            apilar(p, [i+1, datos[1]])


# EJERCICIO 14
def parrafo(cadena):
    pv = Pila()
    pc = Pila()
    po = Pila()
    pila_aux = Pila()
    cc = 0
    cv = 0
    co = 0
    ce = 0
    cn = 0
    cadena = cadena.lower()
    hay_z = 0
    i = 0
    while cadena[i] != '.':
        if (cadena[i] == 'a') or (cadena[i] == 'e') or (cadena[i] == 'i') or (cadena[i] == 'o') or (cadena[i] == 'u'):
            apilar(pv, cadena[i])
        else:
            aux = ord(cadena[i])
            if aux in range(97, 123):
                if aux == 122:
                    hay_z += 1
                apilar(pc, cadena[i])
            else:
                apilar(po, cadena[i])
        i += 1
    while not pila_vacia(pc):
        apilar(pila_aux, desapilar(pc))
        cc += 1
    while not pila_vacia(pila_aux):
        apilar(pc, desapilar(pila_aux))
    while not pila_vacia(pv):
        apilar(pila_aux, desapilar(pv))
        cv += 1
    while not pila_vacia(pila_aux):
        apilar(pv, desapilar(pila_aux))
    while not pila_vacia(po):
        aux = desapilar(po)
        aux = ord(aux)
        if aux == 32:
            ce += 1
        if aux in range(48, 58):
            cn += 1
        co += 1
        aux = chr(aux)
        apilar(pila_aux, aux)
    while not pila_vacia(pila_aux):
        apilar(po, desapilar(pila_aux))
    print("Cantidad de vocales: ", cv)
    print("Cantidad de consonantes: ", cc)
    print("Cantidad de caracteres especiales: ", co)
    print("Cantidad de numeros: ", cn)
    print("Cantidad de espacios: ", ce)
    porcentaje = (cv*100)/cc
    print("Porcentaje de vocales con respecto a consonantes: ", porcentaje)
    if hay_z > 0:
        print("Hay almenos una z")
    if co == cv:
        print("la cantidad de otros caracteres y las vocales son iguales")
    else:
        print("la cantidad de otros caracteres y las vocales no son iguales")


# EJERCICIO 15
def objetos_oficina():
    objetos = ["escritorio", "silla", "teclado", "mouse", "monitor", "gabinete"]
    peso = [10.5, 5, 0.800, 0.400, 2.5, 5]
    pila_oficina = Pila()
    for i in range(0, len(objetos)):
        apilar(pila_oficina, [peso[i], objetos[i]])
    pila_ordenada = ordenar_pila(pila_oficina)
    print('Pila ordenada')
    barrido(pila_ordenada)


# EJERCICIO 16
def robot():
    pila_robot = Pila()
    p_aux = Pila()
    direcciones = ["norte", "sur", "este", "oeste", "noreste", "noroeste", "sureste", "suroeste"]
    num_al = random.randint(5, 50)
    for i in range(1, num_al):
        apilar(pila_robot, random.choice(direcciones))
    print("Ida")
    barrido(pila_robot)
    while not pila_vacia(pila_robot):
        aux = desapilar(pila_robot)
        if aux == "norte":
            apilar(p_aux, "sur")
        if aux == "sur":
            apilar(p_aux, "norte")
        if aux == "este":
            apilar(p_aux, "oeste")
        if aux == "oeste":
            apilar(p_aux, "este")
        if aux == "norte":
            apilar(p_aux, "sur")
        if aux == "noreste":
            apilar(p_aux, "suroeste")
        if aux == "noroeste":
            apilar(p_aux, "sureste")
        if aux == "sureste":
            apilar(p_aux, "noroeste")
        if aux == "suroeste":
            apilar(p_aux, "noreste")
    while not pila_vacia(p_aux):
        apilar(pila_robot, desapilar(p_aux))
    print("")
    print("vuelta")
    barrido(pila_robot)


# EJERCICIO 17
def fibonacci(valor):
    p = Pila()
    p_aux = Pila()
    apilar(p, 0)
    apilar(p, 1)
    for i in range(1, valor):
        f1 = desapilar(p)
        f0 = desapilar(p)
        aux = f1 + f0
        apilar(p, f0)
        apilar(p, f1)
        apilar(p, aux)
    print("Fibonacci de: ", valor)
    barrido(p)


# EJERCICIO 18
def temperatura():
    p = Pila()
    p_aux = Pila()
    sum = 0
    c_encima = 0
    c_debajo = 0
    for i in range(0, 30):
        apilar(p, random.randint(15, 27))
    max = desapilar(p)
    min = max
    apilar(p, max)
    while not pila_vacia(p):
        aux = desapilar(p)
        sum = sum + aux
        if aux < min:
            min = aux
        if aux > max:
            max = aux
        apilar(p_aux, aux)
    media = sum/30
    while not pila_vacia(p_aux):
        aux = desapilar(p_aux)
        if aux > media:
            c_encima += 1
        elif aux < media:
            c_debajo += 1
        apilar(p, aux)
    print("Valor maximo de temperatura: ", max)
    print("Valor minimo de temperatura: ", min)
    print("Promedio del total de los valores: ", media)
    print("Valores por encima de la media: ", c_encima)
    print("Valores por debajo de la media: ", c_debajo)
    print("Lista de los valores: ")
    barrido(p)


# EJERCICIO 19
def palabras():
    serie_palabras = ["Guitarra", "Fotocopia", "Roedor", "Fecha", "Batir", "Horno", "Compartimiento", "Amazona", "Tabaco"]
    p = Pila()
    p_aux = Pila()
    for i in range(0, len(serie_palabras)):
        apilar(p, serie_palabras[i])
    print("Palabras con mas de 7 caracteres")
    while not pila_vacia(p):
        aux = desapilar(p)
        if len(aux) > 7:
            print(aux)
        apilar(p_aux, aux)
    while not pila_vacia(p_aux):
        apilar(p, desapilar(p_aux))
    print("")
    print("Lista de palabras")
    barrido(p)


# EJERCICIO 20
def restringir_valores():
    p = Pila()
    p_aux = Pila()
    while not pila_llena(p):
        apilar(p, random.randint(0, 800))
    print("Lista de valores: ")
    barrido(p)
    while not pila_vacia(p):
        aux = desapilar(p)
        if (aux % 2 == 0) or (aux % 3 == 0) or (aux % 5 == 0):
            apilar(p_aux, aux)
    while not pila_vacia(p_aux):
        apilar(p, desapilar(p_aux))
    print("")
    print("Lista de valores que son multiplos de 2, 3 o 5")
    barrido(p)
