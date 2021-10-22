#busca linear em listas

def busca_linear(l, x):     #complexidade O(n)
    """O elemento x pertence a lista l

    Args:
        l ([list]): A lista a procurar
        x ([any]): Elemento a procurar
    """
    for y in l: # n vezes
        if x == y: # 1
            return True # 1
    return False # 1

#def buscaLinear(l,x):   
#    return x in l

#Se a lista estiver ordenada (crescente)

def busca_em_lista_ordenada(l,x):
    for y in l:
        if x == y:
            return True
        if y > x:
            return False
    return False
#pior caso: o elemento nao se encontra na lista

#Serve se a lista estiver ordenada e os conteudos forem numeros
def busca_dicotomica(l, x):# complexidade: 
    """Permite fazer uma busca numa lista dividindo em listas mais pequenas

    Args:
        l ([list]): lista em que se procura o elemento
        x ([any]): elemento a procurar

    Returns:
        [bool]: retorna True ou False se o elemento se encontra ou nao na lista  
    """
    #encontramos?
    def busca(primeiro, ultimo):
        #nao encontramos?
        if primeiro > ultimo:
            return False
        meio = (primeiro + ultimo)//2 #exemplo (2+5)//2=3
        if l[meio] == x:
            return True
        if l[meio]<x:
            return busca(meio+1, ultimo)#procurar à direita
        else:
            return busca(primeiro, meio-1)#procura à esquerda
    return busca(0, len(l)-1)

# Ordenação

def ordenacao_por_insercao(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[j]<l[i]:
                l[i], l[j] = l[j], l[i]

# Ordenação por fusão

def fusao(l):
    resultado=[]
    i1, i2, =0, 0
    while i1<len(l1) and i2<len(l2):
        if l1[i1]<l2[i2]:
            resultado.append(l1[i1])
            i1+=1
        else:
            resultado.append(l2[i2])
            i2+=1
            #uma das listas esgotou
    while i1<len(l1):
        resultado.append(l1[i1])
        i1+=1
    while i2<len(l2):
        resultado.append(le[i2])
        i2+=1
    return resultado


def ordenacao_por_fusao(l):
    if len(l)<=1:
        return l[:]
    meio=len(l)//2
    esquerda=ordenacao_por_fusao(l[:meio])
    direita=ordenacao_por_fusao(l[meio:])
    return 
    