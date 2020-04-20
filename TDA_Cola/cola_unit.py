import string
import random
import time
from tda_pila import Pila, apilar, pila_vacia, desapilar, barrido
from tda_cola import Cola, barrido_cola, arribo, atencion
from tda_cola import cola_vacia, cola_llena, tamanio, frente


# EJERCICIO 1
def vocales(c):
    c_aux = Cola()
    while not cola_vacia(c):
        aux = atencion(c)
        aux.lower()
        if (aux == 'a') or (aux == 'e') or (aux == 'i') or (aux == 'o') or (aux == 'u'):
            print('Se elimino una vocal')
        else:
            arribo(c_aux, aux)
    c = c_aux
    barrido_cola(c)


# EJERCICIO 2
def invertir(c):
    pila_aux = Pila()
    print('Cola original')
    barrido_cola(c)
    while not cola_vacia(c):
        aux = atencion(c)
        apilar(pila_aux, aux)
    while not pila_vacia(pila_aux):
        aux = desapilar(pila_aux)
        arribo(c, aux)
    print('Cola invertida')
    barrido_cola(c)


# EJERCICIO 3
def palindromo(cadena):
    cadena.lower()
    aux = len(cadena)
    c = Cola()
    p = Pila()
    cadena_aux = ''
    for i in range(0, aux):
        arribo(c, cadena[i])
    while not cola_vacia(c):
        apilar(p, atencion(c))
    while not pila_vacia(p):
        cadena_aux = cadena_aux + desapilar(p)
    if cadena == cadena_aux:
        print("la palabra es un palindromo")
    else:
        print("no es un palindromo")


# EJERCICIO 4
def identificar_primos(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def eliminar_no_primos(c):
    c_aux = Cola()
    while not cola_vacia(c):
        valor = atencion(c)
        if identificar_primos(valor):
            print("Es primo")
            arribo(c_aux, valor)
    while not cola_vacia(c_aux):
        arribo(c, atencion(c_aux))
    print("Barrido cola aux")
    barrido_cola(c)


# EJERCICIO 5
def invertir_pila(p):
    c = Cola()
    barrido(p)
    while not pila_vacia(p):
        arribo(c, desapilar(p))
    while not cola_vacia(c):
        apilar(p, atencion(c))
    barrido(p)


# EJERCICIO 6
def contar_ocurrencias(c, elemento):
    cont = 0
    while not cola_vacia(c):
        aux = atencion(c)
        if aux == elemento:
            cont += 1
    print("Cantidad de ocurrencias: ", cont)


# EJERCICIO 7
def eliminar_lugar(c, lugar):
    c_aux = Cola()
    if lugar <= c.tamanio:
        for i in range(2, lugar):
            arribo(c_aux, atencion(c))
        aux = atencion(c)
        while not cola_vacia(c):
            arribo(c_aux, atencion(c))
        print('')
        barrido_cola(c_aux)
        print('El elemento quiitado fue: ', aux)
    else:
        print('La posicion dada no se encuentra en la cola...')


# EJERCICIO 8
def ordenado_automatico():
    c = Cola()
    c_aux = Cola()
    aux = 0
    elemento = int(input("Ingrese el elemento (-100 para no cargar mas): "))
    while (elemento != -100):
        if cola_llena(c):
            print("No hay mas espacio")
        else:
            if cola_vacia(c):
                arribo(c, elemento)
            else:
                aux = atencion(c)
                if elemento <= aux:
                    while not cola_vacia(c):
                        arribo(c_aux, atencion(c))
                    arribo(c, elemento)
                    arribo(c, aux)
                else:
                    while elemento > aux and not cola_vacia(c):
                        arribo(c_aux, aux)
                        aux = atencion(c)
                    if cola_vacia(c):
                        arribo(c_aux, aux)
                        arribo(c_aux, elemento)
                    else:
                        arribo(c_aux, elemento)
                        arribo(c_aux, aux)
                    while not cola_vacia(c):
                        arribo(c_aux, atencion(c))
                while not cola_vacia(c_aux):
                    arribo(c, atencion(c_aux))
            elemento = int(input("Ingrese el elemento (-100 para no cargar mas): "))
    barrido_cola(c)


# EJERCICIO 9
def rango(c):
    aux = atencion(c)
    min = aux
    max = min
    neg = 0
    while not cola_vacia(c):
        if aux < min:
            min = aux
        if aux > max:
            max = aux
        if aux < 0:
            neg += 1
        aux = atencion(c)
    print("El rango de los elementos es: ", max - min)
    print("La cantidad de numeros negativos es: ", neg)


# EJERCICIO 10
def fibonacci(n):
    c = Cola()
    c_aux = Cola()
    arribo(c, 1)
    arribo(c, 0)
    for i in range(1, n):
        aux1 = atencion(c)
        aux2 = atencion(c)
        sum = aux1 + aux2
        while not cola_vacia(c):
            arribo(c_aux, atencion(c))
        arribo(c, sum)
        arribo(c, aux1)
        arribo(c, aux2)
        while not cola_vacia(c_aux):
            arribo(c, atencion(c_aux))
    barrido_cola(c)


# EJERCICIO 11
def combinar_colas(c1, c2):
    c = Cola()
    aux1 = atencion(c1)
    aux2 = atencion(c2)
    while not cola_vacia(c1) and not cola_vacia(c2):
        if aux1 <= aux2:
            arribo(c, aux1)
            aux1 = atencion(c1)
        else:
            arribo(c, aux2)
            aux2 = atencion(c2)
    barrido_cola(c)


# EJERCICIO 12
def caracteres(c):
    c_digitos = Cola()
    c_otros = Cola()
    c_aux = Cola()
    contador = 0
    while not cola_vacia(c):
        aux = atencion(c)
        aux2 = ord(aux)
        if aux2 in range(48, 58):
            arribo(c_digitos, aux)
        else:
            arribo(c_otros, aux)
    while not cola_vacia(c_otros):
        aux = atencion(c_otros)
        aux2 = ord(aux)
        if aux2 in range(65, 91) or aux2 in range(97, 123):
            contador += 1
        arribo(c_aux, aux)
    while not cola_vacia(c_aux):
        arribo(c_otros, atencion(c_aux))
    print("Cola de digitos: ")
    barrido_cola(c_digitos)
    print("Cola de otros caracteres: ")
    barrido_cola(c_otros)
    print("Cantidad de letras en la cola de otros caracteres: ", contador)


# EJERCICIO 14
def valores_enteros(c1, c2):
    contador1 = 0
    contador2 = 0
    contador_primos1 = 0
    contador_primos2 = 0
    ac1 = 0
    ac2 = 0
    multiplo2_1 = 0
    multiplo3_1 = 0
    multiplo2_2 = 0
    multiplo3_2 = 0
    while not cola_vacia(c1) or not cola_vacia(c2):
        if not cola_vacia(c1):
            aux1 = atencion(c1)
            contador1 += 1
            ac1 = ac1 + aux1
            if identificar_primos(aux1):
                contador_primos1 += 1
            if aux1 & 2 == 0:
                multiplo2_1 += 1
            if aux1 & 3 == 0:
                multiplo3_1 += 1
        if not cola_vacia(c2):
            aux2 = atencion(c2)
            contador2 += 1
            ac2 = ac2 + aux2
            if identificar_primos(aux2):
                contador_primos2 += 1
            if aux2 & 2 == 0:
                multiplo2_2 += 1
            if aux2 & 3 == 0:
                multiplo3_2 += 1
    if c1 == c2:
        print("Las colas son iguales")
    else:
        print("Las colas son distintas")
    if contador1 == contador2:
        print("Tienen la misma cantidad de elementos")
    elif contador1 > contador2:
        print("La primer cola tiene mas elementos")
    else:
        print("La segunda cola tiene mas elementos")
    if ac1 == ac2:
        print("Son iguales con respecto a la sumatoria de elementos")
    elif ac1 > ac2:
        print("La primer cola es mayor con respecto a la sumatoria de elementos")
    else:
        print("La segunda cola es mayor con respecto a la sumatoria de elementos")
    if multiplo2_1 > 0 and multiplo3_1 > 0:
        print("La primer cola tiene multiplo de 2 y de 3")
    if multiplo2_2 > 0 and multiplo3_2 > 0:
        print("La segunda cola tiene multiplo de 2 y de 3")


# EJERCICIO 16
def simulacion_cola_ejecucion():
    cola_procesos = Cola()
    cola_tiempo = Cola()
    proceso = input("Ingrese el id_proceso: ")
    tiempo = float(input("Ingrese el tiempo de ejecucion: "))
    # carga de procesos con sus tiempos
    while tiempo > -1:
        arribo(cola_procesos, proceso)
        arribo(cola_tiempo, tiempo)
        proceso = input("Ingrese el id_proceso: ")
        tiempo = float(input("Ingrese el tiempo de ejecucion (Ingrese -1 para dejar de cargar): "))
    while not cola_vacia(cola_procesos):
        proceso = atencion(cola_procesos)
        tiempo = atencion(cola_tiempo)
        if tiempo > 4.5:
            aux_tiempo = tiempo - 4.5
            print("Atendiendo el proceso: ", proceso, "...")
            time.sleep(4.5)
            print("Se le agoto el quantum asignado por el procesador. Se coloca el proceso al final de la cola")
            arribo(cola_procesos, proceso)
            arribo(cola_tiempo, aux_tiempo)
            control = input("Desea cargar mas procesos?: si/no: ")
            control.lower()
            if control == 'si':
                while tiempo > -1:
                    proceso = input("Ingrese el id_proceso: ")
                    tiempo = float(input("Ingrese el tiempo de ejecucion: "))
                    arribo(cola_procesos, proceso)
                    arribo(cola_tiempo, tiempo)
                    proceso = input("Ingrese el id_proceso: ")
                    tiempo = float(input("Ingrese el tiempo de ejecucion *(Ingrese -1 para dejar de cargar)*: "))
        else:
            print("Atendiendo el proceso: ", proceso, "...")
            time.sleep(tiempo)
            print("El proceso se atendio por completo...")
            control = input("Desea cargar mas procesos?: si/no: ")
            control.lower()
            if control == 'si':
                while tiempo > -1:
                    proceso = input("Ingrese el id_proceso: ")
                    tiempo = float(input("Ingrese el tiempo de ejecucion: "))
                    arribo(cola_procesos, proceso)
                    arribo(cola_tiempo, tiempo)
                    proceso = input("Ingrese el id_proceso: ")
                    tiempo = float(input("Ingrese el tiempo de ejecucion *(Ingrese -1 para dejar de cargar)*: "))
    print("No hay mas procesos! ")


# EJERCICIO 17
def turnos():
    c_turnos = Cola()
    cola_1 = Cola()
    cola_2 = Cola()
    c_aux = Cola()
    cA, cC, cF, cB, cD, cE = 0, 0, 0, 0, 0, 0
    # carga de turnos
    for i in range(0, 1000):
        lista = ['A', 'B', 'C', 'D', 'E', 'F']
        cadena = random.choice(lista)
        cadena = cadena + random.choice(string.digits)
        cadena = cadena + random.choice(string.digits)
        cadena = cadena + random.choice(string.digits)
        arribo(c_turnos, cadena)
    while not cola_vacia(c_turnos):
        turno = atencion(c_turnos)
        if turno[0] == 'A' or turno[0] == 'C' or turno[0] == 'F':
            arribo(cola_1, turno)
        else:
            arribo(cola_2, turno)
    tc1 = tamanio(cola_1)
    tc2 = tamanio(cola_2)
    print("Cola con turnos 'A'; 'C'; 'F'")
    barrido_cola(cola_1)
    print("Cola con turnos 'B'; 'D'; 'E'")
    barrido_cola(cola_2)
    if tc1 > tc2:
        print("La cola con turnos 'A'; 'C'; 'F'; tiene mas elementos")
        while not cola_vacia(cola_1):
            aux = atencion(cola_1)
            if aux[0] == 'A':
                cA += 1
            elif aux[0] == 'C':
                cC += 1
            else:
                cF += 1
            arribo(c_aux, aux)
        while not cola_vacia(c_aux):
            arribo(cola_1, atencion(c_aux))
        if cA > cC and cA > cF:
            print("Hay mas turnos 'A'")
        elif cC > cA and cC > cF:
            print("Hay mas turnos 'C'")
        else:
            print("Hay mas turnos 'F'")
    else:
        print("La cola con turnos 'B'; 'D'; 'E'; tiene mas elementos")
        while not cola_vacia(cola_2):
            aux = atencion(cola_2)
            if aux[0] == 'B':
                cB += 1
            elif aux[0] == 'D':
                cD += 1
            else:
                cE += 1
            arribo(c_aux, aux)
        while not cola_vacia(c_aux):
            arribo(cola_1, atencion(c_aux))
        if cB > cD and cB > cE:
            print("Hay mas turnos 'B'")
        elif cD > cB and cD > cE:
            print("Hay mas turnos 'D'")
        else:
            print("Hay mas turnos 'E'")


# EJERCICIO 19
def buffer(cadena):
    cola_buffer_out = Cola()
    cola_buffer_in = Cola()
    aux = cadena.encode()
    cadena = ''
    for i in range(0, len(aux)):
        arribo(cola_buffer_out, aux[i])
    while not cola_vacia(cola_buffer_out):
        print("Enviando...")
        arribo(cola_buffer_in, atencion(cola_buffer_out))
        arribo(cola_buffer_in, atencion(cola_buffer_out))
    while not cola_vacia(cola_buffer_in):
        aux = atencion(cola_buffer_in)
        cadena = cadena + chr(aux)
    print(cadena)


# EJERCICIO 20
def cabinas_peaje():
    c1 = Cola()
    c2 = Cola()
    c3 = Cola()
    peajes = [c1, c2, c3]
    vehiculos = ['auto', 'camioneta', 'camion', 'colectivo']
    valor_auto = 35
    valor_camioneta = 43
    valor_camion = 61
    valor_colectivo = 58
    i = 0
    while i < 30:
        dato = random.choice(vehiculos)
        caux = random.choice(peajes)
        arribo(caux, dato)
        i += 1
    ac1 = 0
    ac2 = 0
    ac3 = 0
    while not cola_vacia(c1) or not cola_vacia(c2) or not cola_vacia(c3):
        if not cola_vacia(c1):
            aux = atencion(c1)
            if aux == 'auto':
                ac1 = ac1 + valor_auto
            elif aux == 'camioneta':
                ac1 = ac1 + valor_camioneta
            elif aux == 'camion':
                ac1 = ac1 + valor_camion
            else:
                ac1 = ac1 + valor_colectivo
        if not cola_vacia(c2):
            aux = atencion(c2)
            if aux == 'auto':
                ac2 = ac2 + valor_auto
            elif aux == 'camioneta':
                ac2 = ac2 + valor_camioneta
            elif aux == 'camion':
                ac2 = ac2 + valor_camion
            else:
                ac2 = ac2 + valor_colectivo
        if not cola_vacia(c3):
            aux = atencion(c3)
            if aux == 'auto':
                ac3 = ac3 + valor_auto
            elif aux == 'camioneta':
                ac3 = ac3 + valor_camioneta
            elif aux == 'camion':
                ac3 = ac3 + valor_camion
            else:
                ac3 = ac3 + valor_colectivo
    if (ac1 > ac2) and (ac1 > ac3):
        print("La primer cabina recaudo mas")
    elif (ac2 > ac1) and (ac2 > ac3):
        print("La segunda cabina recaudo mas")
    else:
        print("La tercer cabina recaudo mas")


# EJERCICIO 21
def generar_hora_aleatoria():
    hora = random.randint(0, 23)
    minutos = random.randint(0, 60)
    if len(str(hora)) == 1:
        hora = '0'+str(hora)
    if len(str(minutos)) == 1:
        minutos = '0'+str(minutos)
    hora_completa = str(hora) + ':' + str(minutos)
    return hora_completa


def aeropuerto():
    lista_aerolineas = ["Iberia", "Lufthansa", "Eurowings", "Air France", "Aerolineas Argentinas", "Avianca", "American Airlines", "Qatar Airways"]
    lista_tipo = ["Carga", "Pasajeros", "Negocios"]
    lista_aeropuertos = ["Aeropuerto A", "Aeropuerto B", "Aeropuerto C", "Aeropuerto D", "Aeropuerto E"]
    lista_tiempo_aterrizaje = [7, 10, 5]
    lista_tiempo_despegue = [9, 5, 3]
    lista_despegue = ['nombre_empresa', 'hora_salida', 'hora_llegada', 'aeropuerto_origen', 'aeropuerto_llegada', 'tipo']
    lista_aterrizaje = ['nombre_empresa', 'hora_salida', 'hora_llegada', 'aeropuerto_origen', 'aeropuerto_llegada', 'tipo']
    cola_despegue = Cola()
    cola_aterrizaje = Cola()
    # pis1, pis2, pis3 = False, False, False

    def ordenado_automatico():
        c = Cola()
        c_aux = Cola()
        aux = 0
        elemento = generar_hora_aleatoria()
        while not cola_llena(c):
            if cola_llena(c):
                print("No hay mas espacio")
            else:
                if cola_vacia(c):
                    arribo(c, elemento)
                else:
                    aux = atencion(c)
                    if elemento <= aux:
                        while not cola_vacia(c):
                            arribo(c_aux, atencion(c))
                        arribo(c, elemento)
                        arribo(c, aux)
                    else:
                        while elemento > aux and not cola_vacia(c):
                            arribo(c_aux, aux)
                            aux = atencion(c)
                        if cola_vacia(c):
                            arribo(c_aux, aux)
                            arribo(c_aux, elemento)
                        else:
                            arribo(c_aux, elemento)
                            arribo(c_aux, aux)
                        while not cola_vacia(c):
                            arribo(c_aux, atencion(c))
                    while not cola_vacia(c_aux):
                        arribo(c, atencion(c_aux))
                elemento = generar_hora_aleatoria()
        return c

    def generar_despegue_aleatorio():
        c_aux = Cola()
        cola = Cola()
        c_aux = ordenado_automatico()
        for i in range(0, 20):
            lista_despegue = ['nombre_empresa', 'hora_salida', 'hora_llegada', 'aeropuerto_origen', 'aeropuerto_llegada', 'tipo']
            lista_despegue[0] = random.choice(lista_aerolineas)
            lista_despegue[1] = atencion(c_aux)
            lista_despegue[2] = generar_hora_aleatoria()
            lista_despegue[3] = random.choice(lista_aeropuertos)
            lista_despegue[4] = random.choice(lista_aeropuertos)
            lista_despegue[5] = random.choice(lista_tipo)
            arribo(cola, lista_despegue)
        return cola

    def generar_aterrizaje_aleatorio():
        cola = Cola()
        for i in range(0, 20):
            lista_aterrizaje = ['nombre_empresa', 'hora_salida', 'hora_llegada', 'aeropuerto_origen', 'aeropuerto_llegada', 'tipo']
            lista_aterrizaje[0] = random.choice(lista_aerolineas)
            lista_aterrizaje[1] = generar_hora_aleatoria()
            lista_aterrizaje[5] = random.choice(lista_tipo)
            lista_aterrizaje[2] = generar_hora_aleatoria()
            lista_aterrizaje[3] = random.choice(lista_aeropuertos)
            lista_aterrizaje[4] = random.choice(lista_aeropuertos)
            arribo(cola, lista_aterrizaje)
        return cola

    # Carga cola_despegue
    cola_despegue = generar_despegue_aleatorio()
    # Carga de cola_aterrizaje
    cola_aterrizaje = generar_aterrizaje_aleatorio()

    while not cola_vacia(cola_despegue):
        hora_sistema = time.strftime("%H:%M")
        dato = frente(cola_despegue)
        if dato[1] < hora_sistema or cola_vacia(cola_aterrizaje):
            dato = atencion(cola_despegue)
            aux = input("El vuelo  va a despegar o va a ser reprogramado? (d = despegar ; r = reprogramar)")
            c_aux = Cola()
            if aux == "d" or aux == "r":
                if aux == 'd':
                    print("El vuelo de ", dato[5],  " de la empresa ", dato[0], " esta despegando...")
                    time.sleep(lista_tiempo_despegue[lista_tipo.index(dato[5])])
                elif aux == 'r':
                    while not cola_vacia(cola_despegue):
                        aux_cola = atencion(cola_despegue)
                        arribo(c_aux, aux_cola)
                    aux = input("Ingrese la hora de salida: ")
                    # Control para que el horario se mas tarde que el ultimo
                    while aux < aux_cola[1]:
                        print("El horario tiene que ser mas tarde que ", aux_cola[1])
                        aux = input("Ingrese la hora de salida: ")
                    while not cola_vacia(c_aux):
                        arribo(cola_despegue, atencion(c_aux))
                    dato[1] = aux
                    arribo(cola_despegue, dato)
                else:
                    while aux != 'd' or aux == 'r':
                        aux = input("Error ingrese d = despegar ; r = reprogramar")
                        aux.lower()
                    if aux == 'd' and aux == 'r':
                        if aux == 'd':
                            print("El vuelo de ", dato[5],  " de la empresa ", dato[0], " esta despegando...")
                            time.sleep(lista_tiempo_despegue[lista_tipo.index(dato[5])])
                        elif aux == 'r':
                            while not cola_vacia(cola_despegue):
                                aux_cola = atencion(cola_despegue)
                                arribo(c_aux, aux_cola)
                            aux = input("Ingrese la hora de salida: ")
                            # Control para que el horario se mas tarde que el ultimo
                            while aux < aux_cola[1]:
                                print("El horario tiene que ser mas tarde que ", aux_cola[1])
                                aux = input("Ingrese la hora de salida: ")
                            dato[1] = aux
                            arribo(cola_despegue, dato)
            aux = input("Desea agregar otro vuelo? (si/no): ")
            if aux == 'si':
                aux = input("Va a ingresar un despegue o un aterrizaje: (despegue/aterrizaje): ")
                aux.lower()
                if aux == 'despegue':
                    lista_despegue[0] = input("Ingrese el nombre de la empresa: ")
                    c_aux = Cola()
                    aux_cola = ''
                    # Ciclo para obtener el ultimo valor de la cola
                    while not cola_vacia(cola_despegue):
                        aux_cola = atencion(cola_despegue)
                        arribo(c_aux, aux_cola)
                    aux = input("Ingrese la hora de salida: ")
                    # Control para que el horario se mas tarde que el ultimo
                    while aux < aux_cola[1]:
                        print("El horario tiene que ser mas tarde que ", aux_cola[1])
                        aux = input("Ingrese la hora de salida: ")
                    lista_despegue[1] = aux
                    # volver a poner todos los valores en la cola_despegue
                    while not cola_vacia(c_aux):
                        arribo(cola_despegue, atencion(c_aux))
                    lista_despegue[2] = input("Ingrese la hora llegada: ")
                    lista_despegue[3] = input("Ingrese el aeropuerto de origen: ")
                    lista_despegue[4] = input("Ingrese el aeropuerto de destino: ")
                    aux = int(input("Ingrese el tipo de vuelo: (0 = carga ; 1 = pasajeros ; 2 = negocios) "))
                    lista_despegue[5] = lista_tipo[aux]
                    arribo(cola_despegue, lista_despegue)
                elif aux == 'aterrizaje':
                    lista_aterrizaje[0] = input("Ingrese el nombre de la empresa: ")
                    lista_aterrizaje[1] = input("Ingrese la hora de salida: ")
                    lista_aterrizaje[2] = input("Ingrese la hora llegada: ")
                    lista_aterrizaje[3] = input("Ingrese el aeropuerto de origen: ")
                    lista_aterrizaje[4] = input("Ingrese el aeropuerto de destino: ")
                    aux = int(input("Ingrese el tipo de vuelo: (0 = carga ; 1 = pasajeros ; 2 = negocios) "))
                    lista_aterrizaje[5] = lista_tipo[aux]
                    arribo(cola_aterrizaje, lista_aterrizaje)
        else:
            if not cola_vacia(cola_aterrizaje):
                dato = atencion(cola_aterrizaje)
                print("El vuelo de ", dato[5], " de la empresa ", dato[0], " esta aterrizando...")
                time.sleep(lista_tiempo_aterrizaje[lista_tipo.index(dato[5])])
                aux = input("Desea agregar otro vuelo? (si/no): ")
                if aux == 'si':
                    aux = input("Va a ingresar un despegue o un aterrizaje: (despegue/aterrizaje): ")
                    aux.lower()
                    if aux == 'despegue':
                        lista_despegue[0] = input("Ingrese el nombre de la empresa: ")
                        c_aux = Cola()
                        aux_cola = ''
                        # Ciclo para obtener el ultimo valor de la cola
                        while not cola_vacia(cola_despegue):
                            aux_cola = atencion(cola_despegue)
                            arribo(c_aux, aux_cola)
                        aux = input("Ingrese la hora de salida: ")
                        # Control para que el horario se mas tarde que el ultimo
                        while aux < aux_cola[1]:
                            print("El horario tiene que ser mas tarde que ", aux_cola[1])
                            aux = input("Ingrese la hora de salida: ")
                        lista_despegue[1] = aux
                        # volver a poner todos los valores en la cola_despegue
                        while not cola_vacia(c_aux):
                            arribo(cola_despegue, atencion(c_aux))
                        lista_despegue[2] = input("Ingrese la hora llegada: ")
                        lista_despegue[3] = input("Ingrese el aeropuerto de origen: ")
                        lista_despegue[4] = input("Ingrese el aeropuerto de destino: ")
                        aux = int(input("Ingrese el tipo de vuelo: (0 = carga ; 1 = pasajeros ; 2 = negocios) "))
                        lista_despegue[5] = lista_tipo[aux]
                        arribo(cola_despegue, lista_despegue)
                    elif aux == 'aterrizaje':
                        lista_aterrizaje[0] = input("Ingrese el nombre de la empresa: ")
                        lista_aterrizaje[1] = input("Ingrese la hora de salida: ")
                        lista_aterrizaje[2] = input("Ingrese la hora llegada: ")
                        lista_aterrizaje[3] = input("Ingrese el aeropuerto de origen: ")
                        lista_aterrizaje[4] = input("Ingrese el aeropuerto de destino: ")
                        aux = int(input("Ingrese el tipo de vuelo: (0 = carga ; 1 = pasajeros ; 2 = negocios) "))
                        lista_aterrizaje[5] = lista_tipo[aux]
                        arribo(cola_aterrizaje, lista_aterrizaje)
