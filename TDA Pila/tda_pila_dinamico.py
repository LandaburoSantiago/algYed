import random
import string


class NodoPila():
    info, sig = None, None


# Crea la clase Pila


class Pila():
    def __init__(self):
        self.tope = None
        self.tamanio = 0


# Apilar un dato


def apilar(pila, dato):
    aux = NodoPila()
    aux.info = dato
    aux.sig = pila.tope
    pila.tope = aux
    pila.tamanio += 1

# Saca un dato de la pila y lo devuelve


def desapilar(pila):
    dato = pila.tope.info
    pila.tope = pila.tope.sig
    pila.tamanio -= 1
    return dato


# Devuelve true si la pila esta llena


def pila_llena(pila):
    return False


# Devuelve true si la pila esta vacia


def pila_vacia(pila):
    if pila.tope is None:
        return True
    else:
        return False


# Devuelve el tamanio que tiene la pila en ese momento

def tamanio(pila):
    return pila.tamanio


# Devuelve el dato que esta en la ultima posicion


def cima(pila):
    if pila_vacia(pila):
        return 'No hay datos'
    else:
        return pila.tope.info


# Devuelve todos los datos de la pila

def barrido(pila):
    paux = Pila()
    while not pila_vacia(pila):
        dato = desapilar(pila)
        print(dato)
        apilar(paux, dato)
    while not pila_vacia(paux):
        apilar(pila, desapilar(paux))
    print('listo')


# Carga la pila completa con valores aleatorios

def carga_automatica(pila):
    while tamanio(pila) < 10:
        dato = random.randint(0, 800)
        apilar(pila, dato)

# Carga la pila completa con letras aleatorias


def carga_automatica_letras(pila):
    while tamanio(pila) < 10:
        dato = random.choice(string.ascii_letters)
        apilar(pila, dato)
