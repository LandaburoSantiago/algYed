from tda_lista import insertar, insertarEn, eliminar, eliminarTodos, barridoLista, busquedaLista, lista_vacia, Lista, NodoLista, obtener_ultimo
import time
# NO HACE 11, 12, 13, 16, 19


# EJERCICIO 1
def contar_nodos(l):
    aux = l.inicio
    c = 0
    while (aux is not None):
        c += 1
        aux = aux.sig
    return c


# EJERCICIO 2
def eliminar_vocales(l):
    aux = l.inicio
    while (aux is not None):
        if ord(aux.info.lower()) == 97 or ord(aux.info.lower()) == 101 or ord(aux.info.lower()) == 105 or ord(aux.info.lower()) == 111 or ord(aux.info.lower()) == 117:
            eliminar(l, aux.info)
            print('Se elimino', aux.info)
        aux = aux.sig
    barridoLista(l)


# EJERCICIO 3
def separa_pares(l):
    lista_pares = Lista()
    aux = l.inicio
    while (aux is not None):
        if (aux.info % 2) == 0:
            insertar(lista_pares, aux.info)
            eliminar(l, aux.info)
        aux = aux.sig
    print('Lista de pares: ')
    barridoLista(lista_pares)
    print('Lista de impares')
    barridoLista(l)


# EJERCICIO 4
def cargar_en_posicion(l, dato, pos):
    pos = pos - 1
    nodo = NodoLista()
    nodo.info = dato
    aux = l.inicio
    if (pos >= 0) and (pos <= l.tamanio):
        if (pos == 0):
            nodo.sig = l.inicio
            l.inicio = NodoLista()
        elif (pos < l.tamanio):
            for i in range(1, pos):
                aux = aux.sig
            nodo.sig = aux.sig
            aux.sig = nodo
        else:
            while aux.sig is not None:
                aux = aux.sig
            aux.sig = nodo
    else:
        print("El indice " + str(pos) + " excede el tamanio de elementos que ")
        print("posee la lista")


# EJERCICIO 5
def identificar_primos(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def numeros_primos(l):
    aux = l.inicio
    while (aux is not None):
        if identificar_primos(aux.info):
            eliminar(l, aux.info)
        aux = aux.sig
    print('Lista sin primos')
    barridoLista(l)


# EJERCICIO 6
def superheroes(l):
    aux = l.inicio
    while (aux is not None):
        dato = aux.info
        if dato[0] == "Linterna Verde":
            eliminar(l, aux.info)
        if dato[0] == "Wolverine":
            print('Anio de aparicion de Wolverine: ', dato[1])
        if dato[0] == "Ant-Man":
            aux.info[3] = "Marvel"
        if dato[3].find("traje") >= 0 or dato[3].find("armadura") >= 0:
            print('Nombre: ', dato[0])
        if dato[1] < 1963:
            print('Nombre: ', dato[0])
            print('Casa: ', dato[2])
        aux = aux.sig


# EJERCICIO 7
def dos_listas(l1, l2):

    # def concatenar(l1, l2):
    #     lista_aux = Lista()
    #     lista_aux = l1
    #     aux = l2.inicio
    #     while (aux is not None):
    #         insertar(lista_aux, aux.info)
    #         aux = aux.sig
    #     print('Lista concantenadas: ')
    #     barridoLista(lista_aux)

    def omitir_repetidos(l1, l2):
        lista_aux = Lista()
        lista_aux = l1
        aux = l2.inicio
        print('Lista 1')
        barridoLista(l1)
        print('Lista 2')
        barridoLista(l2)
        c = 0
        while (aux is not None):
            if busquedaLista(lista_aux, aux.info) == -1:
                insertar(lista_aux, aux.info)
            else:
                c += 1
            aux = aux.sig
        print('Cantidad de repetidos: ', c)
        print('Lista concatenada sin repeticiones: ')
        barridoLista(lista_aux)

    def eliminarNodos(l1):
        aux = l1.inicio
        while (aux is not None):
            eliminar(l1, aux.info)
            aux = aux.sig
        print('Lista vacia')
        barridoLista(l1)

    # print('Punto a): ')
    # concatenar(l1, l2)
    print('Punto b) y c): ')
    omitir_repetidos(l1, l2)
    print('Punto d): ')
    eliminarNodos(l1)


# EJERCICIO 8
def numeros():
    lista = Lista()
    control_primos = False
    control_impares = False
    pos = 1
    for i in range(0, 10):
        num = int(input('Ingrese el numero'))
        if (num < -999) or (num > 999):
            print("El numero esta fuera de rango -999;999")
        else:
            if busquedaLista(lista, num) == -1:
                if identificar_primos(num):
                    if lista.tamanio == 0:
                        insertar(lista, num)
                        control_primos = True
                    else:
                        if control_primos:
                            ultimo = obtener_ultimo(lista)
                            diferencia = num - ultimo
                            if diferencia >= 14 or diferencia <= -14:
                                insertarEn(lista, num, pos)
                                pos += 1
                        else:
                            ultimo = obtener_ultimo(lista)
                            diferencia = num - ultimo
                            if diferencia >= 14 or diferencia <= -14:
                                if control_impares:
                                    if (num % 2) == 0:
                                        control_primos = True
                                        insertarEn(lista, num, pos)
                                        pos += 1
                                    else:
                                        print("No cumple con las condiciones")
                                else:
                                    insertarEn(lista, num, pos)
                                    pos += 1
                else:
                    if (num % 2) != 0:
                        if lista.tamanio == 0:
                            insertar(lista, num)
                            control_impares = True
                        else:
                            if control_primos:
                                ultimo = obtener_ultimo(lista)
                                diferencia = num - ultimo
                                if diferencia >= 14 or diferencia <= -14:
                                    ultimo = obtener_ultimo(lista)
                                    if (ultimo % 2) == 0:
                                        insertarEn(lista, num, pos)
                                        pos += 1
                                        control_primos = True
                                        control_impares = True
                                    else:
                                        print("No cumple con las condiciones")
                            else:
                                if control_impares:
                                    print("No cumple con las condiciones")
                                else:
                                    ultimo = obtener_ultimo(lista)
                                    print(ultimo)
                                    if (ultimo % 2) == 0:
                                        insertarEn(lista, num, pos)
                                        pos += 1
                                        control_primos = False
                                        control_impares = True
                    else:
                        if identificar_primos(num):
                            if control_primos:
                                ultimo = obtener_ultimo(lista)
                                diferencia = num - ultimo
                                if diferencia == 14 or diferencia == -14:
                                    insertarEn(lista, num, pos)
                                    pos += 1
                            else:
                                ultimo = obtener_ultimo(lista)
                                diferencia = num - ultimo
                                if diferencia == 14 or diferencia == -14:
                                    control_primos = True
                                    insertarEn(lista, num, pos)
                                    pos += 1
                        else:
                            control_primos = False
                            control_impares = False
                            insertarEn(lista, num, pos)
                            pos += 1
            else:
                print("El numero ya se encuentra en la lista")
    barridoLista(lista)


# Chequear error
# EJERCICIO 9

def musica(l):
    lista_artics_monkeys = Lista()
    aux = l.inicio
    max_duracion = aux.info[2]
    info = ''
    while (aux is not None):
        if aux.info[1] == 'Artics Monkeys':
            insertar(lista_artics_monkeys, aux.info[0])
        if aux.info[2] > max_duracion:
            info = aux.info
            max_duracion = aux.info[2]
        aux = aux.sig

    print('La cancion mas larga es: ', info[0])
    print('El artista es: ', info[1])
    print('La duracion es es: ', info[2])
    print('La cantidad de reproducciones es: ', info[3])
    print('Canciones de Artic Monkeys: ')
    barridoLista(lista_artics_monkeys)
    print("Lista ordenada por cantidad de reproducciones (TOP 5): ")
    barridoLista(l)


# Falta punto i
# EJERCICIO 10
def starwars(l):
    lista_femeninos = Lista()
    lista_droide = Lista()
    """
        personajes_4567 = personajes que aparecen en los
        episodios 4, 5, 6, 7
    """
    personajes_4567 = Lista()
    """
        personajesMas850 = personajes que tienen mas de
        850 anios
    """
    personajesMas850 = Lista()
    """
        personajesMas850 = lista de personajes que aparecen
        en episodios que no sean el 4,5,6
    """
    lista_aux_episodios = Lista()
    lista_humanos = Lista()
    # Listado de alutras menor a 70
    lista_altura_menor = Lista()
    lista_episodios_chewbacca = Lista()
    aux = l.inicio
    while (aux is not None):
        if aux.info[3] == 'femenino':
            insertar(lista_femeninos, aux.info[0])
        if aux.info[4] == 'droide' and (aux.info[6] > 0 or aux.info[6] <= 6):
            insertar(lista_droide, aux.info[0])
        if aux.info[6] == 4 or aux.info[6] == 5 or aux.info[6] == 6 or aux.info[6] == 7:
            insertar(personajes_4567, aux.info[0])
        if aux.info[6] != 4 or aux.info[6] != 5 or aux.info[6] != 6:
            insertar(lista_aux_episodios, aux.info)
        if aux.info[0] == 'Darth Vader':
            info_darth = aux.info
        if aux.info[2] >= 850:
            insertar(personajesMas850, aux.info)
        if aux.info[4] == 'humana' and aux.info[5] == 'Alderan':
            insertar(lista_humanos, aux.info[0])
        if aux.info[1] < 70:
            insertar(lista_altura_menor, aux.info)
        if aux.info[0] == 'Chewbacca':
            insertar(lista_episodios_chewbacca, aux.info)
        aux = aux.sig

    aux = personajes_4567.inicio
    while (aux is not None):
        control = busquedaLista(lista_aux_episodios, aux.info[0])
        if control == -1:
            eliminar(l, aux.info)
        aux = aux.sig

    aux = personajesMas850.inicio
    may_edad = 0
    while (aux is not None):
        if aux.info[2] > may_edad:
            may_edad = aux.info
        aux = aux.sig

    print('Personajes de genero femenino: ')
    barridoLista(lista_femeninos)
    print('Personajes de especie Droide que aparecen en los primeros 6 episodios: ')
    barridoLista(lista_droide)
    print('Informacion de Darth Vader: ')
    print(info_darth)
    print('Personajes que aparecen en el episodio VII y en los 3 anteriores: ')
    barridoLista(personajes_4567)
    print('Personajes mayores a 850 anios')
    barridoLista(personajesMas850)
    print('Y el mayor es: ')
    print(may_edad)
    print('Personajes de especie humana y planeta de origen Alderan')
    barridoLista(lista_humanos)
    print('Info de personajes con altura menor a 70')
    barridoLista(lista_altura_menor)
    print('Episodios en el que aparece Chewbacca')
    barridoLista(lista_episodios_chewbacca)


# Falta punto h
# EJERCICIO 14
def pokemon(lista_entrenadores):
    lista_mas_ganadores = Lista()
    lista_mas_porcentaje = Lista()
    lista_determinado_pokemon = Lista()
    entrenador_mas_ganador = ''
    mas_ganador = 0
    sum_nivel = 0
    aux = lista_entrenadores.inicio
    c_pokemon = 0
    c_entrenador = 0
    control_tipo = -1
    mismo_pokemon = 0
    entrenador = input('Ingrese el nombre del entrenador que desea buscar: ')
    var_pokemon = input('Ingrese el nombre del pokemon que desea buscar: ')
    while (aux is not None):
        if aux.info[0] == entrenador:
            aux_lista_pokemon = aux.info[4].inicio
            while (aux_lista_pokemon is not None):
                c_pokemon += 1
                sum_nivel = sum_nivel + aux_lista_pokemon.info[1]
                aux_lista_pokemon = aux_lista_pokemon.sig
            prom_nivel = sum_nivel / c_pokemon

        if aux.info[1] > 3:
            insertar(lista_mas_ganadores, aux.info)

        if aux.info[1] > mas_ganador:
            entrenador_mas_ganador = aux.info
            mas_ganador = aux.info[1]

        total_batallas = aux.info[2] + aux.info[3]
        porcentaje_batallas = (aux.info[3]*total_batallas)/100
        if porcentaje_batallas > 79:
            insertar(lista_mas_porcentaje, aux.info)

        aux_lista_pokemon = aux.info[4].inicio
        while (aux_lista_pokemon is not None):
            if aux_lista_pokemon.info[0] == var_pokemon:
                c_entrenador += 1
            if aux_lista_pokemon.info[2] == 'fuego/planta' or aux_lista_pokemon.info[2] == 'agua/volador':
                control_tipo += 1
                insertar(lista_determinado_pokemon, aux.info)
            aux_lista_pokemon = aux_lista_pokemon.sig
        control = busquedaLista(aux.info[4], var_pokemon)
        if control != -1:
            mismo_pokemon += 1
        aux = aux.sig

    aux = entrenador_mas_ganador[4].inicio
    may_nivel = 0
    while (aux is not None):
        if aux.info[1] > may_nivel:
            pok = aux.info
            may_nivel = aux.info[1]
        aux = aux.sig

    print('La cantidad de pokemons del entrenador ', entrenador, ' son: ', c_pokemon)
    print('------------------------------------------------------------')
    print('Entrenadores que ganaron + de 3 torneos: ')
    barridoLista(lista_mas_ganadores)
    print('------------------------------------------------------------')
    print('Pokemon de mayor nivel del entrenador con mayor cantidad de torneos: ')
    print(pok)
    print('------------------------------------------------------------')
    print('Entrenadores cuyo porcentaje de batallas ganadas sea mayor a 79: ')
    barridoLista(lista_mas_porcentaje)
    print('------------------------------------------------------------')
    print('Entrenadores con pokemon de fuego/planta o agua/volador')
    barridoLista(lista_determinado_pokemon)
    print('------------------------------------------------------------')
    print('Promedio de nivel de pokemon del entrenador ', entrenador)
    print(prom_nivel)
    print('------------------------------------------------------------')
    print('Cantidad de entrenadores que tienen al pokemon ', var_pokemon, ': ', mismo_pokemon)


# EJERCICIO 15
def proyecto_software(lista):
    aux = lista.inicio
    lista_actividades = Lista()
    tareas_entre_fechas = Lista()
    costo = 0
    sum_tiempo = 0
    fecha1 = time.strftime("11/3/2019")
    fecha2 = time.strftime("14/11/2019")
    c = 0
    persona = input('Ingrese una persona para ver activiades realizadas: ')
    while (aux is not None):
        sum_tiempo = sum_tiempo + aux.info[2]
        c += 1
        costo = costo + aux.info[1]
        if aux.info[4] == persona:
            insertar(lista_actividades, aux.info[0])
        if time.strftime(aux.info[3]) >= fecha1 and time.strftime(aux.info[3]) <= fecha2:
            insertar(tareas_entre_fechas, aux.info)
        aux = aux.sig
    print("Actiividades realizadas por ", persona)
    barridoLista(lista_actividades)
    print("Tareas realizadas entre ", fecha1, " y ", fecha2)
    barridoLista(tareas_entre_fechas)
    prom_tiempo = sum_tiempo/c
    print("Tiempo promedio de las tareas: ", prom_tiempo)


# EJERCICIO 16
def vuelos(l):
    aux = l.inicio
    listado_atenas = Lista()
    turista_libre = Lista()
    totales_vuelos = Lista()
    programados = Lista()
    lista_aux = Lista()
    fecha = input('Ingrese la fecha para consultar vuelos: ')
    while (aux is not None):
        if aux.info[5] == 'Atenas':
            insertar(listado_atenas, aux.info)
        aux_lista_asientos = aux.info[7].inicio
        km = aux.info[6]
        total = 0
        while(aux_lista_asientos is not None):
            if aux_lista_asientos.info[2] == 'Desocupado':
                if aux_lista_asientos.info[1] == 'Turista':
                    insertar(turista_libre, aux.info)
                    break
            if aux_lista_asientos.info[2] == 'Ocupado':
                if aux_lista_asientos.info[1] == 'Turista':
                    total = total + (350*km)
                else:
                    total = total + (988*km)
            aux_lista_asientos = aux_lista_asientos.sig
        datos = [aux.info[1], total]
        insertar(totales_vuelos, datos)
        if aux.info[3] == fecha:
            insertar(programados, aux.info)
        aux = aux.sig
    nro_vuelo = int(input('Ingrese el numero de vuelo: '))
    nro = int(input('Ingrese el numero del asiento: '))
    clase = input('Ingrese la clase: ')
    estado_asiento = 'Ocupado'
    persona = input('Ingrese el nombre de la persona')
    datos_venta_pasaje = [nro, clase, estado_asiento, persona]
    pos = busquedaLista(l, nro_vuelo, 1)
    if pos == -1:
        print('El vuelo no existe')
    else:
        aux = l.inicio
        if pos == 0:
            insertar(aux.info[7], datos_venta_pasaje)
            print('Pasaje vendido')
        else:
            for i in range(0, pos+1):
                aux = aux.sig
            insertar(aux.info[7], datos_venta_pasaje)
            print('Pasaje vendido')
    vuelo_eliminar = int(input('Ingrese el numerod de vuelo que desea eliminar: '))
    pos = busquedaLista(l, vuelo_eliminar, 1)
    if pos == -1:
        print('El vuelo no existe')
    else:
        aux = l.inicio
        if pos == 0:
            lista_aux = aux.info[7]
        else:
            for i in range(0, pos+1):
                aux = aux.sig
            lista_aux = aux.info[7]
        eliminar(l, vuelo_eliminar, 1)
    print('Vuelos programados para la fecha ', fecha, ' :')
    barridoLista(programados)
    print('Vuelos con destino a Atenas: ')
    barridoLista(listado_atenas)
    print('Vuelos con asientos de clase turista disponibles: ')
    barridoLista(turista_libre)
    print('Total recaudado por cada vuelo: ')
    barridoLista(totales_vuelos)
    print('Se elimino el vuelo ', vuelo_eliminar, '. Listado de pasajeros: ')
    barridoLista(lista_aux)


# EJERCICIO 17
def local_informatica(lista_stock, lista_proveedores):
    lista_disco_solido = Lista()
    lista_teclado_inalambrico = Lista()
    lista_aux = Lista()
    lista_aux1 = Lista()
    aux_proveedores = lista_proveedores.inicio
    aux_stock = lista_stock.inicio
    while (aux_proveedores is not None):
        encontrado = False
        while (aux_stock is not None) and (encontrado is False):
            if (aux_proveedores.info[0] == aux_stock.info[0]):
                aux_stock.info[5] = aux_stock.info[5] + aux_proveedores.info[5]
                encontrado = True
            aux_stock = aux_stock.sig
        if encontrado is False:
            insertar(lista_stock, aux_proveedores.info)
        aux_proveedores = aux_proveedores.sig
    aux_stock = lista_stock.inicio
    while (aux_stock is not None):
        if (aux_stock.info[1] == 'Pendrive') and (aux_stock.info[2] == 'Kingston'):
            eliminar(lista_stock, aux_stock.info)
        if (aux_stock.info[1] == 'Disco solido'):
            insertar(lista_disco_solido, aux_stock.info)
        elif aux_stock.info[1] == 'Teclado inalambrico':
            insertar(lista_teclado_inalambrico, aux_stock.info)
        aux_stock = aux_stock.sig

    aux_disco_solido = lista_disco_solido.inicio
    aux_teclado_inalambrico = lista_teclado_inalambrico.inicio
    costo_disco_solido = 0
    costo_teclado_inalambrico = 0
    while (aux_disco_solido is not None) or (aux_teclado_inalambrico is not None):
        costo_disco_solido = costo_disco_solido + (aux_disco_solido.info[4] * aux_disco_solido.info[5])
        costo_teclado_inalambrico = costo_teclado_inalambrico + (aux_teclado_inalambrico.info[4] * aux_teclado_inalambrico.info[5])
        aux_disco_solido = aux_disco_solido.sig
        aux_teclado_inalambrico = aux_teclado_inalambrico.sig

    aux_stock = lista_stock.inicio
    while (aux_stock is not None):
        insertar(lista_aux, aux_stock.info, 1)
        insertar(lista_aux1, aux_stock.info, 2)
        aux_stock = aux_stock.sig
    print('------------------------------------------------------------')
    print("Listado ordenado por tipo: ")
    barridoLista(lista_aux)
    print('------------------------------------------------------------')
    print("Listado ordenado por marca: ")
    barridoLista(lista_aux1)
    print('------------------------------------------------------------')
    print('Costo de existencia del disco solido: ', costo_disco_solido)
    print('Costo de existencia del teclado inalambrico: ', costo_teclado_inalambrico)
    print('------------------------------------------------------------')
    barridoLista(lista_stock)


# EJERCICIO 18
def repositorio(lista):
    cambios = Lista()
    sin_lineas = Lista()
    aux = lista.inicio
    max = aux.info[1].tamanio
    usuario_mas_commit = aux.info[0]
    aux_commit = aux.info[1].inicio
    max_lineas = aux_commit.info[3]
    usuario_mas_lineas = aux.info[0]
    min_lineas = aux_commit.info[4]
    usuario_menos_lineas = aux.info
    while(aux is not None):
        if aux.info[1].tamanio > max:
            usuario_mas_commit = aux.info[0]
            max = aux.info[1].tamanio
        aux_commit = aux.info[1].inicio
        while(aux_commit is not None):
            if time.strftime(aux_commit.info[1]) > time.strftime('19:45'):
                if aux_commit.info[2] == 'test.py':
                    insertar(cambios, aux.info[0])

            if aux_commit.info[3] > max_lineas:
                usuario_mas_lineas = aux.info[0]
                max_lineas = aux_commit.info[3]

            if aux_commit.info[3] < min_lineas:
                min_lineas = aux_commit.info[4]
                usuario_menos_lineas = aux.info

            if aux_commit.info[3] == 0 and aux_commit.info[4] == 0:
                insertar(sin_lineas, aux.info[0])
                
            aux_commit = aux_commit.sig
        aux = aux.sig

    print('Usuario con mayor cantidad de commits: ', usuario_mas_commit)
    print('Usuario con mayor cantidad de lineas agregadas: ', usuario_mas_lineas)
    print('Usuario con menor cantidad de lineas agregadas: ', usuario_menos_lineas)
    print('Usuarios que realizaron cambios en Test.py despues de las 19:45: ')
    barridoLista(cambios)
    print('Usuarios que realizaron commits sin agregar ni eliminar lineas: ')
    barridoLista(sin_lineas)

# EJERCICIO 20
def productos(lista):
    lista_aux = Lista()
    calificacion_3 = Lista()
    productos_h = Lista()
    prod = input('Ingrese el producto: ')
    aux = lista.inicio
    while (aux is not None):
        if aux.info[0] == prod:
            print('Datos del producto: ')
            print(aux.info)
        if aux.info[2] == 3:
            insertar(calificacion_3, aux.info, 1)
        if aux.info[0][0] == 'h' or aux.info[0][0] == 'H':
            insertar(productos_h, aux.info)
        aux = aux.sig

    campo = input('Para ordenar por nombre ingrese 0; Para ordenar por calificacion ingrese 2: ')
    aux = lista.inicio
    while (aux is not None):
        insertar(lista_aux, aux.info, campo)
        aux = aux.sig
    if campo == '0':
        print('Lista ordenada por nombre: ')
        barridoLista(lista_aux)
    elif campo == '2':
        print('Listado ordenado por calificacion: ')
        barridoLista(lista_aux)
    else:
        print('ERROR!')
    print('Producto mas barato de calificacion 3: ', calificacion_3.inicio.info)
    print('Precio de los productos que empiezan con H: ')
    barridoLista(productos_h)
