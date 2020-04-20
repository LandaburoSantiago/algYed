x = 10
lista = []


def prueba(num, l):
    l.append(num)
    num = num*2


prueba(x, lista)
print(x)
print(lista)
l1 = [5, 4]
l2 = l1
l2.append(7)
print(l2)
print(l1)
