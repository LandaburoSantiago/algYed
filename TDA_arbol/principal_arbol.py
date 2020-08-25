from arbol_unit import descodificar, arbolMorse, numeros_enteros, expresion_matematica, hijos, super_villanos, nodo_maximo, nodo_minimo, directorio
from arbol_unit import manejo_arbol, niveles, indice_summerville, comprimir_descomprimir
from arbol_unit import nueveNiveles, indicesArchivo, nanoSatelites, calculoFrecuencias
from arbol_unit import misiones_superheroes, pokemones, armeria, libros
from arbol_unit import decision_meteorologica, tabla, dioses_griegos
from tda_arbol import insertarArbol, imprimirArbol, inorden, preorden, postorden

# EJERCICIO 1
# numeros_enteros()

# EJERCICIO 2
# print(expresion_matematica('268*54+4*6-5*6'))

# EJERCICIO 3
# indice_summerville()

# EJERCICIO 4
arbol = None
arbol = insertarArbol(arbol, 2)
arbol = insertarArbol(arbol, 2)
arbol = insertarArbol(arbol, 2)
arbol = insertarArbol(arbol, 2)
arbol = insertarArbol(arbol, 2)
arbol = insertarArbol(arbol, 7)
arbol = insertarArbol(arbol, 1)
arbol = insertarArbol(arbol, 3)
arbol = insertarArbol(arbol, 13)
arbol = insertarArbol(arbol, 5)
arbol = insertarArbol(arbol, 9)
arbol = insertarArbol(arbol, 23)
imprimirArbol(arbol)
preorden(arbol)
hijos(arbol)

# EJERCICIO 5
# super_villanos()

# EJERCICIO 6
# directorio()

# EJERCICIO 7
# imprimirArbol(arbol)
# inorden(arbol)
# minimo = nodo_minimo(arbol)
# maximo = nodo_maximo(arbol)
# print(minimo.info)
# print(maximo.info)

# EJERCICIO 8
# comprimir_descomprimir('AM1F', '100101100')

# EJERCICIO 9
# niveles(arbol, 3)

# EJERCICIO 10
# manejo_arbol(arbol)

# EJERCICIO 11
# nueveNiveles()

# EJERCICIO 12
# misiones_superheroes('Estrategica')

# EJERCICIO 13
# msj1 = ".--. .- ... . / .-.. --- / --.- ..- . / .--. .- ... . / -- .- .- -. .- / .--. .-. --- -- . - . -- . / .- .-.. --. --- /--.- ..- . / ...- .- / ... . --. ..- .. .-. / ... .. . -. -.. --- / ..- ... - . -.. / -. --- / ..- -. / ... --- .-.. -.. .- -.. --- / .--. . .-. ..-. . -.-. - --- / ... .. -. --- / ..- -. / -... ..- . -. /.... --- -- -... .-. . .-.-."
# msj2 = "-. --- ... --- - .-. --- ... / ... --- -- --- ... / .-.. --- ... / -- .- .-.. -.. .. - --- ... / --. ..- .- .-. -.. .. .- -. . ... / -.. . / .-.. .- / --. .- .-.. .- -..- .. .- .-.-."
# msj3 = "-.-- --- / ... --- .-.. --- / .- -.-. - ..- --- / -.-. --- -- --- / ... .. / . -. / ...- . .-. -.. .- -.. / .-.. --- / ... ..- .--. .. . .-. .- / - --- -.. --- .-.-."
# msj4 = "-.-. .... .. -.-. --- ... / . ... - --- -.-- / .-.. .-.. . ...- .- -. -.. --- / .-.. .- / ..-. .. . ... - .- / .... .- -.-. .. .- / ..- ... - . -.. . ... .-.-."
# msj5 = ".--. --- -.. .-. .. .- / .... .-  -.-. . .-. / . ... - --- / - --- -.. --- / . .-.. / -.. .. .- .-.-."
#
# arbol = arbolMorse()

# print('Dr. Abraham Erskine: ')
# print(descodificar(arbol, msj1))
# print('Rocket Raccoon: ')
# print(descodificar(arbol, msj2))
# print(descodificar(arbol, msj3))
# print('Tony Stark: ')
# print(descodificar(arbol, msj4))
# print('Steve Rogers: ')
# print(descodificar(arbol, msj5))

# EJERCICIO 14
# indicesArchivo()

# EJERCICICO 15
# nanoSatelites()

# EJERCICIO 16
# pokemones()

# EJERCICIO 17
# armeria()

# EJERCICIO 18
# libros()

# EJERCICIO 19
# decision_meteorologica()

# EJERCICIO 20
# dioses_griegos()

# EJERCICIO 21
# tabla()

# EJERCICIO 22
# calculoFrecuencias()
