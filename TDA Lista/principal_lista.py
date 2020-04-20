import random
import string
from tda_lista import Lista, insertar, barridoLista
from lista_unit import contar_nodos, eliminar_vocales, separa_pares, cargar_en_posicion, numeros_primos, superheroes, dos_listas, musica, numeros, starwars, pokemon
from lista_unit import proyecto_software, local_informatica, productos, vuelos, repositorio

# NO HACE 11, 12, 13, 19
# 16, 18

l1 = Lista()
l2 = Lista()
l3 = Lista()
lista_superheroes = Lista()
lista_canciones = Lista()
lista_starwars = Lista()
lista_entrenador_pokemon = Lista()
lista_vuelos = Lista()
lista_proyecto_software = Lista()
lista_stock_computacion = Lista()
lista_proveedores = Lista()
lista_productos = Lista()
usuarios_repositorio = Lista()

i = random.randint(0, 40)
print('Cantidad de nodos: ', i)
'''
for j in range(0, 20):
    insertar(l1, random.choice(string.letters))
    insertar(l2, random.randint(0, 40))
    insertar(l3, random.randint(15, 50))
'''
# Armando registros de superheroes
nombres_superHeroes = ['Thor', 'Shazam', 'Aquaman', 'Wolverine', 'Capitan america', 'Linterna verde']
casa = ['Marvel', 'DC', 'DC', 'Marvel', 'Marvel', 'DC']
anio_aparicion = [1962, 2011, 1941, 1974, 1941, 1940]
bio = ['Martillo, uno de los dioses mas poderosos', 'Fuerza sobrehumana', 'Fuerza y valor para retos', 'Traje bandera de estados unidos', 'Anillo de poder']

# Insertando en la lista
for l in range(0, 5):
    dato = [nombres_superHeroes[l], anio_aparicion[l], casa[l], bio[l]]
    insertar(lista_superheroes, dato)

# Armando registros de canciones
nombre_cancion = ['Crying Lightning', 'Parque Acuatico', 'Esperando el impacto', 'Where Is The Love?', 'La Rueda Magica']
artista = ['Artics Monkeys', 'El Kuelgue', 'Bersuit Vergarabat', 'The Black Eyed Peas', 'Fito Paez']
duracion = [3.43, 2.53, 3.34, 4.12, 3.54]
reproducciones = [19883309, 4147845, 7633770, 463109437, 762594]

# Insertando en la lista
for l in range(0, 5):
    dato = [nombre_cancion[l], artista[l], duracion[l], reproducciones[l]]
    insertar(lista_canciones, dato, 3)

# Armando registros de starwars
nombre_starwars = ['a', 'b', 'Darth Vader', 'Chewbacca', 'c', 'd']
altura = [1.12, 2.42, 1, 3.43, 2, 4]
edad = [490, 900, 320, 123, 555, 900]
genero = ['femenino', 'masculino', 'masculino', 'masculino', 'masculino', 'femenino', 'femenino']
especie = ['droide', 'humana', 'humana', 'droide', 'humana', 'droide']
planeta_natal = ['tierra', 'alderan', 'tierra', 'alderan', 'marte', 'saturno']
episodios = [1, 6, 3, 8, 3, 6]

for i in range(0, 5):
    dato = [nombre_starwars[i], altura[i], edad[i], genero[i], especie[i], planeta_natal[i], episodios[i]]
    insertar(lista_starwars, dato)


for i in range(0, 3):
    lista_pokemon = Lista()
    # Armando registro de Pokemon's
    nombre_pokemon = ['e', 'u', 'Pikachu', 's', 'f', 'r']
    nivel = [1, 6, 3, 8, 3, 6]
    tipo = ['fuego/planta', 'f', 'd', 'agua/volador', 'o', 'p']
    subtipo = ['y', 'k', 'j', 'c', 'b', 'n']

    # insertando en la lista
    for J in range(0, 2):
        dato = [nombre_pokemon[random.randint(0, 5)], nivel[random.randint(0, 5)], tipo[random.randint(0, 5)], subtipo[random.randint(0, 5)]]
        insertar(lista_pokemon, dato)

    # estructura_aux contiene las listas de pokemones
    # Armando registros de entrenadores Pokemon
    nombre_entrenador_pokemon = ['a', 'b', 'Ash Ketchup']
    cantidad_torneos = [1, 6, 3]
    batallas_perdidas = [4, 1, 5, 2]
    batallas_ganadas = [2, 4, 150, 4]

    dato = [nombre_entrenador_pokemon[i], cantidad_torneos[i], batallas_perdidas[i], batallas_ganadas[i], lista_pokemon]
    insertar(lista_entrenador_pokemon, dato)

# Armando registros para proyecto de software
tarea = ['dd', 'uu', 'tt']
costo = [12, 4, 55]
tiempo = [5, 18, 2]
fecha_inicio = ['12/3/2019', '2/5/2019', '1/7/2019']
persona = ['C', 'B', 'U']

# Insertando en la lista
for i in range(0, 3):
    dato = [tarea[i], costo[i], tiempo[i], fecha_inicio[i], persona[i]]
    insertar(lista_proyecto_software, dato)

# Armando registros de insumos de computacion
codigo = [1, 2, 3]
tipo = ['Disco solido', 'Teclado inalambrico', 'Pendrive']
marca = ['Samsung', 'Genius', 'Kingston']
modelo = ['aa', 'bb', 'cc']
precio = [2000, 400, 120]
stock = [4, 100, 9]

# Insertando en la lista
for i in range(0, 3):
    dato = [codigo[i], tipo[i], marca[i], modelo[i], precio[i], stock[i]]
    insertar(lista_stock_computacion, dato)

# Armando registros de lista de proveedores
codigo = [1, 7, 9]
tipo = ['Disco solido', 'Mouse', 'Auriculares']
marca = ['Samsung', 'Genius', 'Senheinser']
modelo = ['aa', 'ee', 'cc']
precio = [2000, 400, 11120]
stock = [4, 100, 9]

# Insertando en la lista
for i in range(0, 3):
    dato = [codigo[i], tipo[i], marca[i], modelo[i], precio[i], stock[i]]
    insertar(lista_proveedores, dato)

# Armando registros de lista de productos
nom_producto = ['E', 'Ho', 'Hi', 'Y', 'yy']
precio = [12, 33, 51, 66, 123]
calificacion = [3, 2, 5, 1, 3]

# Insertando en la lista
for i in range(0, 5):
    dato = [nom_producto[i], precio[i], calificacion[i]]
    insertar(lista_productos, dato)


for i in range(0, 3):
    lista_asientos = Lista()
    # Armando registros de asientos
    nro_asiento = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    clase = ['Turista', 'Primera clase']
    estado_asiento = ['Ocupado', 'Desocupado']
    persona = ['Marcos', ' ']

    # insertando en la lista
    for J in range(0, 5):
        aux = random.randint(0, 1)
        dato = [nro_asiento[random.randint(0, 14)], clase[random.randint(0, 1)], estado_asiento[aux], persona[aux]]
        insertar(lista_asientos, dato)

    # Armando registros de vuelos
    empresa = ['Aerolineas', 'Qatar', 'Turkish']
    nro_vuelo = [440, 120, 234]
    cantidad_asientos = [40, 50, 20]
    fecha = ['01/03/2020', '12/11/2019', '26/06/2020']
    origen = ['Buenos Aires', 'Tokio', 'Bogota']
    destino = ['New York', 'Atenas', 'Ciudad de Mexico']
    km = [1200, 4300, 2160]

    dato = [empresa[i], nro_vuelo[i], cantidad_asientos[i], fecha[i], origen[i], destino[i], km[i], lista_asientos]
    insertar(lista_vuelos, dato)

# Armando registros de repositorio
usuario = ['Pablo', 'Marcos', 'Delfina', 'Agustina', 'Juliana']
p = -1
for i in range(0, 5):
    lista_commit = Lista()
    fecha_commit = ['13/07/2019', '13/11/2018', '11/04/2019', '11/05/2019', '28/06/2019', '13/03/2018', '22/08/2019', '1/09/2019', '05/02/2019', '01/08/2018']
    hora_commit = ['22:09', '17:00', '10:30', '12:00', '20:23', '18:40', '16:55', '22:00', '03:30', '08:00']
    nombre_archivo = ['lista_unit.py', 'test.py', 'principal.py', 'tda_cola.py', 'app.py', 'test.py', 'principal_arbol.py', 'tda_arbol.py', 'test.py', 'tda_lista.py']
    lineas_agregadas = [0, 30, 6, 8, 50, 0, 32, 26, 44, 2]
    lineas_eliminadas = [0, 23, 0, 9, 14, 0, 10, 2, 35, 23]
    for j in range(0, 2):
        p += 1
        dato = [fecha_commit[i], hora_commit[i], nombre_archivo[i], lineas_agregadas[i], lineas_eliminadas]
    insertar(lista_commit, dato)
    datos = [usuario[i], lista_commit]
    insertar(usuarios_repositorio, datos)

# EJERCICIO 1
# print(contar_nodos(l1))

# EJERCICIO 2
# eliminar_vocales(l1)

# EJERCICIO 3
# separa_pares(l2)

# EJERCICIO 4
# cargar_en_posicion(l1, 'Fran', 8)
# barridoLista(l1)

# EJERCICIO 5
# numeros_primos(l2)

# EJERCICIO 6
# superheroes(lista_superheroes)

# EJERCICIO 7
# dos_listas(l2, l3)

# EJERCICIO 8
# numeros()

# EJERCICIO 9
# musica(lista_canciones)

# EJERCICIO 10
# starwars(lista_starwars)

# EJERCICIO 14
# pokemon(lista_entrenador_pokemon)

# EJERCICIO 15
# proyecto_software(lista_proyecto_software)

# EJERCICIO 16
# vuelos(lista_vuelos)

# EJERCICIO 17
# local_informatica(lista_stock_computacion, lista_proveedores)

# EJERCICIO 18
repositorio(usuarios_repositorio)

# EJERCICIO 20
# productos(lista_productos)
