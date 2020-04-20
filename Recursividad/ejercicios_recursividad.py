# EJERCICIO 1
def fibonacci(n):
    if n == 1:
        return 0
    else:
        if n == 2:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)


# EJERCICIO 2
def sumatoria(n):
    if n == 0:
        return 0
    else:
        return n + sumatoria(n-1)


# EJERCICIO 3
def multiplicacion(n1, n2):
    if n2 == 0:
        return 0
    else:
        if n2 == 1:
            return n1
        else:
            return n1+multiplicacion(n1, n2-1)


# EJERCICIO 4
def potencia(b, e):
    if e == 0:
        return 1
    else:
        return b*potencia(b, e-1)


# EJERCICIO 5
def invertir_caracteres(cad):
    if len(cad) == 1:
        return cad
    else:
        return cad[len(cad)-1]+invertir_caracteres(cad[0:len(cad)-1])


# EJERCICIO 6
def calcular_serie(n):
    if n == 1:
        return 1
    else:
        return 1/n + calcular_serie(n-1)


# EJERCICIO 7
def binario(n):
    if n <= 1:
        return str(n)
    else:
        return binario(n // 2) + str(n % 2)


# EJERCICIO 8
def logaritmo(n, b):
    if n == b:
        return 1
    else:
        return 1+logaritmo(n/b, b)


# EJERCICIO 9
def contar_numeros(n):
    if n == 0:
        return 0
    else:
        return 1+contar_numeros(n//10)


# EJERCICIO 10
def invertir_numero(n):
    if n < 10:
        return n
    else:
        return (n % 10)*(10**contar_numeros(n//10))+invertir_numero(n//10)


# EJERCICIO 11
def euclides(n1, n2):
    if n1 % n2 == 0:
        return n2
    else:
        return euclides(n2, n1 % n2)


# EJERCICIO 12
def euclides_mcm(n1, n2):
    return n1*n2/euclides(n1, n2)


# EJERCICIO 13
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n//10)


# EJERCICIO 14
def raiz2(x, r, t):
    if (t == r):
        return (r)
    else:
        t = r
        r = (x / r + r) / 2
        return(raiz2(x, r, t))


def raiz(x):
    return raiz2(x, x, 0)


# EJERCICIO 15

def matriz(i, j, m):
    fc = len(m)
    if i == fc-1 and j == fc-1:
        return m[i][j]
    else:
        if j == fc-1:
            print (m[i][j])
            j = 0
            return matriz(i+1, j, m)
        else:
            print (m[i][j])
            return matriz(i, j+1, m)


def recorrer_matriz(m):
    i = 0
    j = 0
    return matriz(i, j, m)


# EJERCICIO 16
def quicksort(v, p, u):
    i = p
    j = u-1
    pivote = u
    while i < j:
        while v[i] <= v[pivote] and i <= j:
            i = i+1
        while v[j] > v[pivote] and j >= i:
            j = j-1
        if i < j:
            v[i], v[j] = v[j], v[i]
    if v[i] > v[pivote]:
        v[i], v[pivote] = v[pivote], v[i]
    if p < i:
        return quicksort(v, p, i-1)
    if u > i:
        return quicksort(v, i+1, u)


# EJERCICIO 17
def busqueda(vec, p, ul, buscado):
    if p < ul:
        med = (p+ul)//2
        if vec[med] == buscado:
            return med
        else:
            if vec[med] > buscado:
                return busqueda(vec, p, med-1, buscado)
            else:
                return busqueda(vec, med+1, ul, buscado)


# EJERCICIO 18
def matriz_laberinto(i, j, m):
    fc = len(m)
    if i == fc-1 and j == fc-1:
        return 'Salio del laberinto'
    else:
        if i == fc-1:
            if m[i][j+1] == 0:
                print('derecha')
                return matriz_laberinto(i, j+1, m)
            else:
                if m[i-1][j] == 0:
                    print('arriba')
                    m[i][j] = 1
                    return matriz_laberinto(i-1, j, m)
        else:
            if j == fc-1:
                if m[i+1][j] == 0:
                    print('abajo')
                    return matriz_laberinto(i+1, j, m)
                else:
                    if m[i][j-1] == 0:
                        print('izquierda')
                        m[i][j] = 1
                        return matriz_laberinto(i, j-1, m)
            else:
                if m[i+1][j] == 0:
                    print('arriba')
                    return matriz_laberinto(i+1, j, m)
                else:
                    if m[i][j+1] == 0:
                        print('derecha')
                        return matriz_laberinto(i, j+1, m)
                    else:
                        m[i][j] = 1
                        if m[i-1][j] == 0:
                            print('arriba')
                            return matriz_laberinto(i-1, j, m)


def laberinto(m):
    i = 0
    j = 0
    return matriz_laberinto(i, j, m)


# EJERCICIO 19
def torre_hanoi(d, a1, a2, a3):
    # d: cantidad de discos
    # a1; a2; a3: aguja 1 ; aguja 2; aguja 3
    c = 0
    if d <= 0:
        return 'Listo. La cantidad de movimientos fueron:', c
    else:
        torre_hanoi(d-1, a1, a3, a2)
        print('se mueve de aguja', a1, 'a aguja', a3)
        c = c+1
        torre_hanoi(d-1, a2, a1, a3)


# EJERCICIO 20
def formula(n):
    if n == 1:
        return 3
    else:
        if n >= 2:
            return formula(n-1) + 2
        else:
            print ('El numero ingresado no puede ser procesado')
