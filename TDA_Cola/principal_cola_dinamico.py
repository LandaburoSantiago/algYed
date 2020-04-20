from tda_cola_dinamico import Cola, carga_automatica, carga_automatica_letras, barrido_cola, arribo, atencion, cola_vacia, carga_automatica_caracteres
from cola_unit_dinamico import vocales, invertir, palindromo, eliminar_no_primos, invertir_pila
from cola_unit_dinamico import combinar_colas, contar_ocurrencias, eliminar_lugar, ordenado_automatico
from cola_unit_dinamico import rango, fibonacci, caracteres, cabinas_peaje, valores_enteros
from cola_unit_dinamico import simulacion_cola_ejecucion, turnos, buffer, aeropuerto

import tda_pila
import random

p = tda_pila.Pila()
c_letras = Cola()
c = Cola()
cola1 = Cola()
carga_automatica_letras(c_letras)
carga_automatica(c)
# carga_automatica(cola1)
tda_pila.carga_automatica(p)

for i in range(0, 14):
    dato = random.randint(0, 400)
    arribo(cola1, dato)


"""EJERCICIO 11"""
c1 = Cola()
c2 = Cola()
for i in range(0, 9):
    arribo(c1, random.randint(0, 50))
    arribo(c2, random.randint(0, 50))


def ordenar_cola(c):
    i = 0
    v = []
    while not cola_vacia(c):
        v.append(atencion(c))
    v.sort()
    for i in range(0, len(v)):
        arribo(c, v[i])


ordenar_cola(c1)
ordenar_cola(c2)
""" EJERCICIO 11"""


# EJERCICIO 1
# vocales(c_letras)

# EJERCICIO 2
# invertir(c)

# EJERCICIO 3
# palindromo('neuquen')

# ANDA MASOMENOS
# EJERCICIO 4
# barrido_cola(c)
# eliminar_no_primos(c)

# EJERCICIO 5
# invertir_pila(p)

# EJERCICIO 6
# contar_ocurrencias(c, 523)

# EJERCICIO 7
# eliminar_lugar(c, 6)

# EJERCICIO 8
# ordenado_automatico()

# EJERCICIO 9
# rango(c)

# EJERCICIO 10
# fibonacci(6)

# EJERCICIO 11
# combinar_colas(c1, c2)

# EJERCICIO 12
# caracteres(c_letras)

# EJERCICIO 14
# valores_enteros(c, cola1)

# EJERCICIO 16
# simulacion_cola_ejecucion()

# EJERCICIO 17
# turnos()

# EJERCICIO 19
# buffer(input("Ingrese una palabra: "))

# EJERCICIO 20
# cabinas_peaje()

# EJERCICIO 21
# aeropuerto()
