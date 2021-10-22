import math as m
import itertools
import operator as op
import functools
__author__ = "Henique Marques, 57153"

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
    """Conversor de latitude, longitude em distancias

    Args:
        graus (tuple): tuplo que contêm a latitude e longitude de uma cidade

    Returns:
        list: lista que contem os valores convertidos de graus para distancias

    >>> conversor((1, 1))
    (111.1949, 85.1102)

    >>> conversor((0, 0))
    (0.0, 0.0)

    >>> conversor((38.7452, -9.1604))
    (4308.26863948, -779.64347608)
    
    """
    return (graus[0]*111.1949,graus[1]*85.1102)

def difY(coord1, coord2):
    """Realiza a diferença entre duas coordenadas (Y)

    Args:
        coord1 (float / int): primeira coordenada
        coord2 (foat / int): segunda coordenada

    Returns:
        [float / int]: resultado da diferença

    >>> difY(1,-2)
    3.0
    """
    return m.fabs(coord1-coord2)

def distancia_pontos(p1, p2):
    """Calcula a distância entre 2 pontos

    Pre: 
    p1 e p2 são tuplos;
    p1 e p2 são pontos de um espaço bidimensional, ou seja, no formato (x , y);

    Args:
        p1 (foat ou int): primeiro ponto
        p2 (foat ou int): segundo ponto

    Returns:
        [float]: distância entre os pontos p1 e p2

    >>> distancia_pontos((1, 1), (1, 1))
    0.0
    
    >>> distancia_pontos((0, 1), (0, 0))
    1.0
    """
    distancia=m.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    return distancia


def distancia_itinerario(itinerario):
    """Calcula a distância total de um itinerário, somando 
    as distancias entre duas cidades consecutivas

    Pre: o itinerario necessita de ter pelo menos dois elementos;
         o itinerario necessita de estar na ordem pela qual os lugares iram ser visitados 

    Args:
        itinerario (list): lista que contem as várias cidades do itinerário

    Returns:
        float: Devolve o número de Km total do itinerário

    >>> distancia_itinerario(['Lisboa'])
    0

    >>> distancia_itinerario([])
    0

    >>> round(distancia_itinerario(['Lisboa', 'Setúbal', 'Coimbra', 'Aveiro', 'Viseu', 'Porto']), 3)
    419.256

    >>> round(distancia_itinerario(['Lisboa', 'Porto']), 3)
    271.407

    >>> round(distancia_itinerario(['Lisboa', 'Setúbal']), 3)
    33.509
    """
    dT=[] #distancia total
    coord = map(lambda x: cidades[x] , itinerario)
    distancias=list(map(conversor, coord))

    for n in range(len(distancias)-1):
        dT.append(distancia_pontos(distancias[n], distancias[n+1]))

    return sum(dT)



def adicionar_cidade(itinerario, cidade):
    """Adiciona uma cidade a um itinerário de modo a causar o menor desvio possível

    Pre:
        -Se o ititnerário se encontrar vazio a cidade tem que ser um input válido;
        -Sendo a cidade um input inválido o itinerário deve conter pelo menos um elemento;

    Args:
        itinerario (list): lista que contêm as cidades a visitar
        cidade (str)): cidade a adiconar 

    Returns:
        list: itinerário com a nova cidade incluída

    >>> adicionar_cidade(['Lisboa', 'Setúbal', 'Coimbra', 'Viseu', 'Porto'],  'Aveiro')
    ['Lisboa', 'Setúbal', 'Coimbra', 'Viseu', 'Aveiro', 'Porto']

    >>> adicionar_cidade(['Lisboa', 'Setúbal', 'Coimbra', 'Viseu', 'Porto'], '')
    ['Lisboa', 'Setúbal', 'Coimbra', 'Viseu', 'Porto']

    >>> adicionar_cidade([], 'Lisboa')
    ['Lisboa']

    >>> adicionar_cidade(['Lisboa', 'Setúbal', 'Coimbra', 'Viseu', 'Porto'], 'Viseu')
    ['Lisboa', 'Setúbal', 'Coimbra', 'Viseu', 'Porto']
    """
    if cidade=='':
        return itinerario

    if len(itinerario)==0:
        return [cidade]

    if cidade in itinerario:
        return itinerario
    
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



if __name__ == "__main__":
    import doctest
    doctest.testmod()