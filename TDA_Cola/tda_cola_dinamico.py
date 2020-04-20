import random
import string


class NodoCola():
    info, sig = None, None


class Cola():
    def __init__(self):
        self.tamanio = 0
        self.frente = None
        self.final = None


def arribo(cola, dato):
    aux = NodoCola()
    aux.info = dato
    if cola.final is None:
        cola.frente = aux
    else:
        cola.final.sig = aux
    cola.final = aux
    cola.tamanio += 1


def atencion(cola):
    aux = cola.frente.info
    cola.frente = cola.frente.sig
    if cola.frente is None:
        cola.final = cola.frente
    cola.tamanio -= 1
    return aux


# Si la cola esta vacia devuelve True
def cola_vacia(cola):
    if cola.tamanio == 0:
        return True
    else:
        return False


# Devuelve siempre false porque es dinamico
def cola_llena(cola):
    return False


# Devuelve e tamanio de la cola
def tamanio(cola):
    return cola.tamanio


# Muestra todos los elementos que estan en la cola
def barrido_cola(cola):
    cola_aux = Cola()
    while not cola_vacia(cola):
        aux = atencion(cola)
        print(aux)
        arribo(cola_aux, aux)
    while not cola_vacia(cola_aux):
        aux = atencion(cola_aux)
        arribo(cola, aux)
    print("Listo")


# El elemento que esta al frente lo mueve al final
def mover_al_final(cola):
    aux = cola.frente
    cola.frente = cola.final
    cola.final = aux


# Carga la cola con 20 numeros aleatorios
def carga_automatica(cola):
    for i in range(0, 20):
        dato = random.randint(-10, 20)
        arribo(cola, dato)


# Carga la cola con 20 letras aleatorias
def carga_automatica_letras(cola):
    for i in range(0, 20):
        dato = random.choice(string.ascii_letters)
        arribo(cola, dato)


# Carga toda la cola con caracteres
def carga_automatica_caracteres(cola):
    while not cola_llena(cola):
        dato = random.choice(chr())
        arribo(cola, dato)


# Devuelve el elemento que esta en el frente
def frente(cola):
    return cola.frente.info
