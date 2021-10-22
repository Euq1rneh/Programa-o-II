import itertools
import math as m
import functools

cidades = {'Lisboa': (38.7452, -9.1604), 
           'Vila Nova de Gaia': (41.1333, -8.6167),
           'Porto': (41.1495, -8.6108),
           'Braga': (41.5333, -8.4167),
           'Matosinhos': (41.2077, -8.6674),
           'Amadora': (38.75, -9.2333),
           'Almada': (38.6803, -9.1583),
           'Oeiras': (38.697, -9.3017),
           'Gondomar': (41.15, -8.5333),
           'Guimarães': (41.445, -8.2908),
           'Odivelas': (38.8, -9.1833),
           'Coimbra': (40.2111, -8.4291),
           'Vila Franca de Xira': (38.95, -8.9833),
           'Maia': (41.2333, -8.6167),
           'Leiria': (39.7431, -8.8069),
           'Setúbal': (38.5243, -8.8926),
           'Viseu': (40.6667, -7.9167),
           'Valongo': (41.1833, -8.5),
           'Viana do Castelo': (41.7, -8.8333),
           'Paredes': (41.2, -8.3333),
           'Vila do Conde': (41.35, -8.75),
           'Torres Vedras': (39.0833, -9.2667),
           'Barreiro': (38.6609, -9.0733),
           'Aveiro': (40.6389, -8.6553),
           'Queluz': (38.7566, -9.2545),
           'Mafra': (38.9333, -9.3333),
           'Penafiel': (41.2, -8.2833),
           'Loulé': (37.144, -8.0235)}

def conversor(graus):
    return (graus[0]*111.1949,graus[1]*85.1102)


def distancia_pontos(p1, p2):

    distancia=m.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    return distancia


def difY(coord1, coord2):
    return m.fabs(coord1-coord2)

def distancia_itinerario(itinerario):
    dT=[]
    coord = map(lambda x: cidades[x] , itinerario)
    distancias=list(map(conversor, coord))

    for n in range(len(distancias)-1):
        dT.append(distancia_pontos(distancias[n], distancias[n+1]))

    return sum(dT)

def adicionar_cidade(itinerario, cidade):
    
    comparacoes=[]
    cidadeY=cidades[cidade][1]
    coordY = list(map(lambda x: cidades[x][1], itinerario))
    
    for n in range(len(coordY)):
        comparacoes.append(difY(coordY[n], cidadeY))

    add = comparacoes.index(min(comparacoes))

    if add == 0:
        itinerario.insert(1, cidade)

    elif add == (len(itinerario)-1):
        itinerario.insert((len(itinerario)-1), cidade)
    
    elif comparacoes[add]<comparacoes[add-1]:
        itinerario.insert(add-1, cidade)
    
    elif comparacoes[add]>comparacoes[add+1]:
        itinerario.insert(add+2, cidade)

    return itinerario



def construir_itinerario(origem, destino,lista_cidades):
    """Contrói um itinerário de forma a gerar a melhor forma de percorrer o mesmo

    Pre:
        -Deve conter pelo menos uma origem e um destino

    Args:
        origem (str): Primeira cidade do itinerário
        destino (str]): Última cidade do itinerário
        lista_cidades (list): lista que contém as várias cidades que iram pertencer ao itinerário

    Returns:
        list: itinerário final

    >>> construir_itinerario('Lisboa', 'Porto', ['Viseu', 'Coimbra', 'Aveiro', 'Setúbal'])
    ['Lisboa', 'Setúbal', 'Coimbra', 'Viseu', 'Aveiro', 'Porto']

    >>> construir_itinerario('Lisboa', 'Porto', [])
    ['Lisboa', 'Porto']
    
    >>> construir_itinerario('Porto', 'Lisboa', ['Viseu', 'Coimbra', 'Aveiro', 'Setúbal'])
    ['Porto', 'Aveiro', 'Viseu', 'Coimbra', 'Setúbal', 'Lisboa']

    >>> construir_itinerario( 'Almada', 'Aveiro', ['Lisboa', 'Coimbra', 'Leiria', 'Torres Vedras', 'Mafra'])
    ['Almada', 'Lisboa', 'Mafra', 'Torres Vedras', 'Leiria', 'Coimbra', 'Aveiro']
    """
    validas=[]
    it = [origem, destino]
    combinacoes = itertools.chain(it, lista_cidades)
    for i in itertools.permutations(combinacoes):
        
        if i[0]==origem and i[len(i)-1]==destino:
            validas.append(i)

    validas_list = list(map(lambda x: list(x), validas))
    distancias_it = list(map(distancia_itinerario, validas_list))

    return validas_list[distancias_it.index(min(distancias_it))]
    



 








"""
    itinerario=[origem]
    dest = conversor(cidades[destino])
    coord = list(map(lambda x: cidades[x], lista_cidades))


    coord_to_distancias = list(map(conversor, coord))
    distancias = list(map(lambda x: distancia_pontos(dest , x), coord_to_distancias))
    duplas_coord_city = sorted(list(map(lambda x,y:(x,y), distancias, lista_cidades)), reverse=True)
    lista_City_Order = list(map(lambda x: x[1], duplas_coord_city)) #alterar para distancias

    itinerario_f = list(itertools.chain(itinerario, lista_City_Order))
    itinerario_f.append(destino)

    return itinerario_f
"""
