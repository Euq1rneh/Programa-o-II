def escreverPotencias(ficheiro, quantas=10):
    """Esta função irá escrever potências de expoente 2

    Args:
        ficheiro ([type]): Fichero que irá ser utilizado
        quantas (int, optional): Número de potências. Defaults to 10.
    """
    f = open(ficheiro, 'w')
    i = 1
    for _ in range(quantas):
        f.write(str(i)+'\n')
        i = i * 2
    f.close()

def lerImprimir(ficheiro):
    """Esta função irá ler e imprimir os conteúdos de um ficheiro

    Args:
        ficheiro ([type]): ficheiro a utilizar
    """
    f = open(ficheiro, 'r')
    for _ in f:
        print(_, end='')
    f.close()

def somar(ficheiro):
    """Irá somar os conteúdos de um ficheiro esta função deve ser usada apenas para ficheiros que contenham números 

    Args:
        ficheiro ([type]): [description]

    Returns:
        [int]: soma dos conteudos do ficheiro
    """
    f = open(ficheiro, 'r')
    soma = 0 
    for _  in f:
        soma = soma+int(_)
    f.close()
    return soma

def escreverWith(algo):
    """Irá escrever o que o utilizador desejar dentro de um fichero com o nome algo.txt

    Args:
        algo ([str]): conteudo a escrever
    """
    with open('algo.txt','w') as f:
        f.write(algo)

def contaLinhas(ficheiro):
    """Irá contar o número de linhas de um ficheiro

    Args:
        ficheiro ([type]): ficheiro a utilizar

    Returns:
        [int]: nº de linhas do fichero indicado
    """
    quantos = 0 
    with open(ficheiro, 'r') as f:
        for _ in f:
            quantos = quantos + 1
    return quantos

def contaLinhas_bis(ficheiro):
    """Irá contar o número de linhas de um ficheiro

    Args:
        ficheiro ([type]): ficheiro a utilizar

    Returns:
        [int]: nº de linhas do fichero indicado
    """
    quantos = 0 
    for _ in open(ficheiro, 'r'):
        quantos = quantos + 1
    ficheiro.close()
    return quantos

def copiar(leitura, escrita):
    """Irá copiar o conteudo de um ficheiro para outro

    Args:
        leitura ([type]): ficheiro a copiar 
        escrita ([type]): copia do ficheiro original
    """
    with open(leitura, 'r') as de, open(escrita, 'w') as para:
        conteudo = de.read()
        para.write(conteudo)

def conteudoLinhas(ficheiro):
    """Irá mostrar o conteudo das várias linhas de um ficheiro 

    Args:
        ficheiro ([type]): ficherio desejado

    Returns:
        [str]: conteudo das linhas
    """
    with open(ficheiro, 'r') as f:
        linhas = f.readlines()
    return [linhas.rstrip() for linha in linhas]

def conteudoLinhas_V2(ficheiro):
    """Irá mostrar o conteudo das várias linhas de um ficheiro 

    Args:
        ficheiro ([type]): ficherio desejado

    Returns:
        [str]: conteudo das linhas
    """
    with open(ficheiro, 'r') as f:
        _ = f.readlines()
    return f.read().splitlines()
