import random
import string
max = 20


class Cola():
    def __init__(self):
        self.datos = []
        for i in range(0, max):
            self.datos.append(None)
        self.frente = 0
        self.final = -1
        self.tamanio = 0


# Llega un nuevo dato a la cola
def arribo(cola, dato):
    cola.final += 1
    cola.datos[cola.final] = dato
    if cola.frente == -1:
        cola.frente += 1
    cola.tamanio += 1
    if cola.final == max-1:
        cola.final = -1


# Se atiende el elemento que esta adelante de la cola y se elimina
def atencion(cola):
    aux = cola.datos[cola.frente]
    cola.frente += 1
    # tenes que resetear el indice frente como lo haces con final en la arribo
    if cola.frente == max-1:
        cola.frente = 0
    cola.tamanio -= 1
    if cola.tamanio == 0:
        cola.frente = 0
        cola.final = -1
    return aux


# Si la cola esta vacia devuelve True
def cola_vacia(cola):
    if cola.tamanio == 0:
        return True
    else:
        return False


# Si la cola esta llena devuelve True
def cola_llena(cola):
    if cola.tamanio == max:
        return True
    else:
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


# Carga toda la cola con numeros enteros aleatorios
def carga_automatica(cola):
    while not cola_llena(cola):
        dato = random.randint(-10, 20)
        arribo(cola, dato)


# Carga toda la cola con letras aleatorias
def carga_automatica_letras(cola):
    while not cola_llena(cola):
        dato = random.choice(string.ascii_letters)
        arribo(cola, dato)


# Carga toda la cola con caracteres
def carga_automatica_caracteres(cola):
    while not cola_llena(cola):
        dato = random.choice(chr())
        arribo(cola, dato)


# Devuelve el elemento que esta en el frente
def frente(cola):
    return cola.datos [cola.frente]
