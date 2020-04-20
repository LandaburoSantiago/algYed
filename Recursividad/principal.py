from ejercicios_recursividad import fibonacci, sumatoria, multiplicacion
from ejercicios_recursividad import potencia, invertir_caracteres
from ejercicios_recursividad import calcular_serie, binario, logaritmo
from ejercicios_recursividad import contar_numeros, invertir_numero
from ejercicios_recursividad import euclides, euclides_mcm, suma_digitos
from ejercicios_recursividad import raiz, busqueda, recorrer_matriz, laberinto
from ejercicios_recursividad import quicksort, torre_hanoi, formula


# RECURSIVIDAD

# EJERCICIO 1
print(fibonacci(4))

# EJERCICIO 2
print(sumatoria(4))

# EJERCICIO 3
print(multiplicacion(2, 4))

# EJERCICIO 4
print(potencia(2, 4))

# EJERCICIO 5
print(invertir_caracteres('hola'))

# EJERCICIO 6     #CONSULTAR
print(calcular_serie(4))

# EJERCICIO 7
print(binario(2))

# EJERCICIO 8
print(logaritmo(8, 2))

# EJERCICIO 9
print(contar_numeros(1223))

# EJERCICIO 10
print(invertir_numero(123))

# EJERCICIO 11
print(euclides(130, 44))

# EJERCICIO 12
print(euclides_mcm(1032, 180))

# EJERCICIO 13
print(suma_digitos(222))

# EJERCICIO 14
print(raiz(25))

# EJERCICIO 15
m = [[9, 5, 7], [8, 2, 11], [10, 4, 6]]
v = [1, 2, 3, 4, 5]
print('matriz')
print(recorrer_matriz(m))
print('matriz')
# EJERCICIO 16
vec = [4, 2, 3, 5, 12, 7]
quicksort(vec, 0, len(vec)-1)
print(vec)
# EJERCICIO 17
print(busqueda(v, 0, 4, 3))
# EJERCICIO 18
ml = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]
print(laberinto(ml))
# EJERCICIO 19
print(torre_hanoi(3, '1', '2', '3'))
# EJERCICIO 20
print(formula(4))
