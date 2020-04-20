from tda_pila import carga_automatica, Pila, barrido, apilar, carga_automatica_letras
from pila_unit import pila_pares, invertir, palindromo, ocurrencias
from pila_unit import reemplazar_ocurrencias, palabra_invertida, quicksort
from pila_unit import eliminar_elemento, factorial, pares_impares, vocales
from pila_unit import ordenados, cartas, parrafo, objetos_oficina, robot
from pila_unit import fibonacci, temperatura, palabras, restringir_valores


p = Pila()
carga_automatica(p)
pl = Pila()
carga_automatica_letras(pl)
v = [1, 6, 54, 6, 12, 7, 44, 2]

# EJERCICIO 1
# barrido(p)
# num = int(input("Ingrese el numero a evaluar: "))
# ocurrencias(p, num)
# barrido(p)

# EJERCICIO 2
# barrido(p)
# pila_pares(p)

# EJERCICIO 3
# num = int(input("Ingrese el numero a evaluar: "))
# reemplazar_ocurrencias(p, num)


# EJERCICIO 4
# invertir(p)

# EJERCICIO 5
# palindromo("neuquen")

# EJERCICIO 6
# pal = str(input("Ingrese la palabra: "))
# palabra_invertida(pal)
# ejecutar desde la terminal

# EJERCICIO 7
# barrido(p)
# elemento = int(input("Ingrese el i-esimo elemento que desea eliminar: "))
# eliminar_elemento(p, elemento)
# barrido(p)

# EJERCICCIO 8
# cartas()
# EJERCICIO 9
# factorial(4)

# EJERCICIO 10
# pares_impares(p)

# EJERCICIO 11
# vocales(pl)

# EJERCICIO 12
# ordenados()

# EJERCICIO 13
quicksort(v, 0, 7)
for i in range(0, 7):
    print(v[i])

# EJERCICIO 14
# cadena = 'Dado un parrafo que finaliza en punto, separa dicho parrafo en tres pilas vocales,consonantes, otros caracteres que no sean letras (signos de puntuacion numeros,espacios, etc). Luego utilizando las operaciones de pila resolver las siguientes consignas'
# parrafo(cadena)


# EJERCICIO 15
# objetos_oficina()

# EJERCICIO 16
# robot()

# EJERCICIO 17
# fibonacci(20)

# EJERCICIO 18
# temperatura()

# EJERCICIO 19
# palabras()

# EJERCICIO 20
# restringir_valores()
