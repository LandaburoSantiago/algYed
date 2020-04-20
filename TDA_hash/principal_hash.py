from tda_lista import Lista, insertar, busquedaLista, barridoLista


# EJERCICIO 1
def hash_palabra(palabra):
    aux = palabra[0]
    aux = ord(aux) - 65
    return aux


def diccionario(palabra, significado, tabla):
    dato = [palabra, significado]
    aux = hash_palabra(palabra)
    if tabla[aux] is None:
        lista = Lista()
        insertar(lista, dato)
        tabla[aux] = lista
    else:
        insertar(tabla[aux], dato)
    # print(tabla)


tabla = [None]*28

diccionario('E', 'r', tabla)
diccionario('Eppp', 'w', tabla)
diccionario('Eccccc', 'r', tabla)
diccionario('F', 'r', tabla)
diccionario('G', 'r', tabla)
diccionario('Q', 'r', tabla)
diccionario('Z', 'r', tabla)
diccionario('X', 'r', tabla)
print(tabla)
for i in range(0, len(tabla)):
    if tabla[i] is None:
        print('NADA')
    else:
        barridoLista(tabla[i])
