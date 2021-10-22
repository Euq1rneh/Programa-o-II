__author__='Henrique Marques, 57153'
def encontra_ocorrencias(procura, interesse):
    """Funcao que compara as palavras contidas em dois ficheiros
    e devolve um dicionario que contem o numero de occorrencias
    de uma palavras e as respetivas linhas em que esta aparece

    Args:
        procura ([file]): ficheiro no qual será feito a procura
        interesse ([file]): ficheiro que contem as palavras que iram ser procuradas

    Returns:
        [dict]: dicionario que contem o numero de ocorrencias de uma palavra e as linhas em que estas aparecem
    """
    dic={} #dcionario final
    conj=ler_palavras(interesse) #conjunto de palavras a procurar
    for i in conj:
        dic[i]=(contador(procura,i),linhas(procura,i))
    return dic

def ler_palavras(ficheiro):
    """Coloca as palavras de um ficheiro num conjunto
    Args:
        ficheiro ([file]): ficheiro a ler
    Returns:
        [set]: conjunto de palavras
    """
    with open(ficheiro, 'r',encoding='utf8')as f:
        conj=set(f.read().split()) #separa as palavras contidas num ficheiro em linhas
    return conj

def contador(ficheiro, word):
    """Conta o numero de vezes que uma palavra aparece num determinado texto

    Args:
        ficheiro ([file]): ficheiro a ler
        word ([str]): palavra a procurar

    Returns:
        [int]: numero de vezes que uma palavra aparece
    """
    count=0
    with open(ficheiro, 'r', encoding='utf8')as f:
        linhas=f.read().split(' ')
        #percorre todas as linhas de um ficheiro
        #e compara com a palavra recebida
        #se esta estiver contida na linha o contador
        #aumenta em incrementos de 1
        return linhas.count(word)        

def linhas(ficheiro, word):
    """Devolve a(s) linha(s) em que uma determinada palavra se encontra

    Args:
        ficheiro ([file]): ficheiro no qual se efetua a procura
        word ([str]): palavra a procurar

    Returns:
        [set]: conjunto que contem as linhas onde a palavra indicada se encontra
    """
    num_linha = 0
    conj_linhas = set()
    with open(ficheiro, 'r', encoding='utf8') as txt:
        for line in txt:    #percorre todas as linhas de um ficheiro
            num_linha += 1  #salvando sempre o numero da linha
            o=line.split(' ')   #lista que contem o texto dividido em palavras
            if word in o:    #se a palavra (tal e qual como foi escrita) estiver contida na lista acima é adicionada o numero da linha a um conjunto
                conj_linhas.add(num_linha)  
    return conj_linhas                      
