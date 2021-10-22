import itertools as iter
def teste(lista, x):
    lista_flat=[]
    for sublista in lista:
        for num in sublista:
            lista_flat.append(num)
    return x in lista_flat


def teste2(lista, x):
    return x in iter.chain.from_iterable(lista)