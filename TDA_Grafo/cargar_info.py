from TDA_Grafo import Grafo, nodoVertice, nodoArista, insertar_vertice


def redPunto4():
    grafo = Grafo(dirigido=False)
    tipo = ['Servidor', 'Laptop', 'PC', 'Router', 'Switch', 'Impresora']
    servidores = ['Guarani', 'MongoDB']
    laptop = ['Red Hat', 'Debian', 'Arch']
    pc = ['Manjaro', 'Parrot', 'Fedora', 'Mint', 'Ubuntu']
    impresora = ['Printer']
    switch = ['Switch01', 'Switch02']
    router = ['Router01', 'Router02', 'Router03']
    for i in servidores:
        infoRed = {
            'tipo': tipo[0],
            'nombre': i
        }
        insertar_vertice(grafo, infoRed, 'nombre')
    for i in laptop:
        infoRed = {
            'tipo': tipo[1],
            'nombre': i
        }
        insertar_vertice(grafo, infoRed, 'nombre')
    for i in pc:
        infoRed = {
            'tipo': tipo[2],
            'nombre': i
        }
        insertar_vertice(grafo, infoRed, 'nombre')
    for i in router:
        infoRed = {
            'tipo': tipo[3],
            'nombre': i
        }
        insertar_vertice(grafo, infoRed, 'nombre')
    for i in switch:
        infoRed = {
            'tipo': tipo[4],
            'nombre': i
        }
        insertar_vertice(grafo, infoRed, 'nombre')
    for i in impresora:
        infoRed = {
            'tipo': tipo[5],
            'nombre': i
        }
        insertar_vertice(grafo, infoRed, 'nombre')

    return grafo
