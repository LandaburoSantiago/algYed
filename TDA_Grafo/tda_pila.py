import random
import string
max = 10000

# Crea la clase Pila


class Pila():
    def __init__(self):
        self.tope = -1
        self.datos = []
        for i in range(0, max):
            self.datos.append(None)


# Apilar un dato

def apilar(pila, dato):
    pila.tope += 1
    pila.datos[pila.tope] = dato


# Saca un dato de la pila y lo devuelve

def desapilar(pila):
    aux = pila.datos[pila.tope]
    pila.tope = pila.tope - 1
    return aux


# Devuelve true si la pila esta llena


def pila_llena(pila):
    return pila.tope+1 == max


# Devuelve true si la pila esta vacia


def pila_vacia(pila):
    if pila.tope == -1:
        return True
    else:
        return False


# Devuelve el tamanio que tiene la pila en ese momento

def tamanio(pila):
    return pila.tope + 1


# Devuelve el dato que esta en la ultima posicion


def cima(pila):
    if pila_vacia(pila):
        return 'No hay datos'
    else:
        return pila.datos[pila.tope]


# Devuelve todos los datos de la pila

def barrido(pila):
    paux = Pila()
    while not pila_vacia(pila):
        dato = desapilar(pila)
        print(dato[1][0].info)
        apilar(paux, dato)
    while not pila_vacia(paux):
        apilar(pila, desapilar(paux))
    print('listo')


# Carga la pila completa con valores aleatorios

def carga_automatica(Pila):
    while not pila_llena(Pila):
        dato = random.randint(0, 800)
        apilar(Pila, dato)

# Carga la pila completa con letras aleatorias


def carga_automatica_letras(Pila):
    while not pila_llena(Pila):
        dato = random.choice(string.ascii_letters)
        apilar(Pila, dato)
