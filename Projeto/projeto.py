from collections import defaultdict
import csv
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import re
import itertools

def ler_csv(ficheiro):
    """Lê um ficheiro CSV por colunas

    Args:
        ficheiro (file): ficheiro csv a ler

    Returns:
        [dict]: Dicionário em que as chaves são o nome das colunas do ficheiro e os valores são os dados contidos nessas colunas
    """

    columns = defaultdict(list) 

    with open(ficheiro) as f:
        reader = csv.DictReader(f) 
        for row in reader: 
            for (k,v) in row.items(): 
                columns[k].append(v) 
                                 
    return columns

def filtrarDados(ficheiro):
    """Função responsável por filtrar os dados necessários para a realização do gráfico anos

    Args:
       ficheiro (file): ficheiro csv a ler

    Returns:
        [list]: lista que contém: os anos presentes no ficheiro e uma lista ordenada que contem tuplos com os jogadores do mesmo jogo
    """
    listaAnos = []
    dados = ler_csv(ficheiro)
    dadosAnos = dados["end_time"]
    dadosNomesBrancos = dados["white_username"]
    dadosNomesPretos = dados["black_username"]

    for _ in dadosAnos:
        listaAnos.append(re.findall(r"[0-9][0-9][0-9][0-9]", _))

    Onesie = list(itertools.chain.from_iterable(listaAnos))#todos os anos (repetidos)
    anos = list(dict.fromkeys(Onesie))#lista com anos diferentes
    
    return [anos, sorted(list(zip(Onesie, dadosNomesBrancos, dadosNomesPretos)))]

def Njogos(ficheiro):
    """Função responsável por contar o número de jogos que aconteceram por ano

    Args:
        ficheiro (file): ficheiro csv a ler

    Returns:
        [list]: lista com o número de jogos jogados em cada ano (ordenada de forma por ano de forma crescente)
    """
    listaAnos = []
    Jogos = {}
    n=0
    dados = ler_csv(ficheiro)
    dadosAnos = dados["end_time"]

    for _ in dadosAnos:
        listaAnos.append(re.findall(r"[0-9][0-9][0-9][0-9]", _))

    Onesie = sorted(list(itertools.chain.from_iterable(listaAnos)))
    anos = list(dict.fromkeys(Onesie))

    for _ in anos:
        for x in Onesie:
            if x in _:
                n+=1
        Jogos[_]=n
        n=0
    
    return Jogos.values()

def anos(ficheiro):
    """Função que realiza um gráfico que mostra o número de jogos que ocorreram por cada ano assim como o numero de jogadores diferentes por ano

    Args:
        ficheiro (file): ficheiro csv a ler
    """
    dados = filtrarDados(ficheiro)
    ordenadasE = Njogos(ficheiro)
    jogadorAno = {}
    listaAux = []
    abcissas = sorted(dados[0])

    for x in abcissas:
        for e in sorted(dados[1]):
            if x == e[0]:
                listaAux.append(e[1])
                listaAux.append(e[2])
        jogadorAno[x] = listaAux    
        listaAux = []
    ordenadasD = list(map(lambda x: len(x), map(lambda x: dict.fromkeys(x), jogadorAno.values())))

    fig, ax = plt.subplots()
    plt.title('Jogos e Jogadoras por Ano')
    ax2 = ax.twinx()
    ax.bar(abcissas, ordenadasE, color = 'green', label = "Jogos" )
    ax2.plot(abcissas, ordenadasD, color = 'blue', label = "Jogadoras Diferentes")
    
    ax.set_xlabel('Ano')
    ax.set_ylabel('Jogos', color = 'green')
    ax2.set_ylabel('Jogadoras diferentes', color = 'blue')

    ax.legend(loc ="center left")
    ax2.legend(loc = "upper left")

    ax2.set_ylim(ymin=0)
    plt.show()

def filtrarDados2(ficheiro):
    """Função responsável por filtrar os dados necessários para a realização do gráfico Classes

    Args:
        ficheiro (file): ficheiro csv a ler

    Returns:
        [tuple]: devolve um tuplo de dicionários em que: 
                        -rapidDic, dailyDic, bulletDic,blitzDic, graf5
                são dicionários que contêm o número de jogos jogados em cada formato pertencente a cada classe
    """
    dados = ler_csv(ficheiro)
    Time = dados["time_control"]
    Classes = dados["time_class"]

    graf5 ={}#valores grafico 5
    
    timeClass = list(dict.fromkeys(Classes))

    aux = list(map(lambda x: {x:Classes.count(x)} , timeClass))
    for _ in aux:
        graf5.update(_)

    blitz = []
    for e in list(zip(Classes, Time)):
        
        if e[0] == 'blitz':
            blitz.append(e[1])
    
    blitzTime = dict.fromkeys(blitz)
    blitzDic = {}
    
    blitzCount = list(map(lambda x: {x:blitz.count(x)}, blitzTime))
    for _ in blitzCount:
        blitzDic.update(_)
    
    rapid = []

    for e in list(zip(Classes, Time)):
        if e[0] == 'rapid':
            rapid.append(e[1])

    rapidTime = dict.fromkeys(rapid)
    rapidDic = {}

    rapidCount = list(map(lambda x: {x:rapid.count(x)}, rapidTime))
    for _ in rapidCount:
        rapidDic.update(_)

    daily = []

    for e in list(zip(Classes, Time)):
        if e[0] == 'daily':
            daily.append(e[1])

    dailyTime = dict.fromkeys(daily)
    dailyDic = {}

    dailyCount = list(map(lambda x: {x:daily.count(x)}, dailyTime))
    for _ in dailyCount:
        dailyDic.update(_)

    bullet = []

    for e in list(zip(Classes, Time)):
        if e[0] == 'bullet':
            bullet.append(e[1])

    bulletTime = dict.fromkeys(bullet)
    bulletDic = {}

    bulletCount = list(map(lambda x: {x:bullet.count(x)}, bulletTime))
    for _ in bulletCount:
        bulletDic.update(_)

    return rapidDic, dailyDic, bulletDic, blitzDic, graf5

def classes(ficheiro, numero):
    """Função responsável por desenhar cinco gráficos que mostram a distribuição de jogos por formato de jogo

    Args:
         ficheiro (file): ficheiro csv a ler
        numero (int): número de formatos a mostrar
    """
    dados = filtrarDados2(ficheiro)
    
    conjunto1=sorted(list(map(lambda x: (dados[0][x], x), dados[0])), reverse=True)
    orde1 = list(map(lambda x: x[0], conjunto1))
    orde1Q = orde1[:numero]
    abs1 = list(map(lambda x: x[1], conjunto1))
    abs1Q = abs1[:numero]

    conjunto2 = sorted(list(map(lambda x: (dados[1][x], x), dados[1])), reverse=True)
    orde2 = list(map(lambda x: x[0], conjunto2))
    orde2Q = orde2[:numero]
    abs2 = list(map(lambda x: x[1], conjunto2))
    abs2Q = abs2[:numero]

    conjunto3 = sorted(list(map(lambda x: (dados[2][x], x), dados[2])), reverse=True)
    orde3 = list(map(lambda x: x[0], conjunto3))
    orde3Q = orde3[:numero]
    abs3 = list(map(lambda x: x[1], conjunto3))
    abs3Q = abs3[:numero]

    conjunto4 = sorted(list(map(lambda x: (dados[3][x], x), dados[3])), reverse=True)
    orde4 = list(map(lambda x: x[0], conjunto4))
    orde4Q = orde4[:numero]
    abs4 = list(map(lambda x: x[1], conjunto4))
    abs4Q = abs4[:numero]

    abs5 = sorted(list(dados[4].keys()))
    orde5 = list(map(lambda x: dados[4][x], abs5))
    
    fig, axs = plt.subplots(nrows=2, ncols=3)
    axs[0, 0].set_xlabel("Formato do Jogo", fontsize= 8)
    axs[0, 1].set_xlabel("Formato do Jogo", fontsize= 8)
    axs[0, 2].set_xlabel("Formato do Jogo", fontsize= 8)
    axs[1, 0].set_xlabel("Formato do Jogo", fontsize= 8)
    axs[1, 1].set_xlabel("Formato do Jogo", fontsize= 8)

    axs[0, 0].set_ylabel("#Jogos", fontsize= 8)
    axs[0, 1].set_ylabel("#Jogos", fontsize= 8)
    axs[0, 2].set_ylabel("#Jogos", fontsize= 8)
    axs[1, 0].set_ylabel("#Jogos", fontsize= 8)
    axs[1, 1].set_ylabel("#Jogos", fontsize= 8)

    axs[0, 0].set_title('rapid', fontsize= 11)
    axs[0, 0].bar(abs1Q, orde1Q)
    axs[0, 0].set_xticklabels(abs1Q, rotation=90, fontsize=8)

    axs[0, 1].set_title('daily', fontsize= 11)
    axs[0, 1].bar(abs2Q , orde2Q)
    axs[0, 1].set_xticklabels(abs2Q, rotation=90, fontsize=8)
    axs[0, 1].set_yticks(ticks=[0, 200, 400])

    axs[0, 2].set_title('bullet', fontsize= 11)
    axs[0, 2].bar(abs3Q, orde3Q)
    axs[0, 2].set_xticklabels(abs3Q, rotation=90, fontsize=8)
    axs[0, 2].set_yticks(ticks=[0, 20000, 40000])

    axs[1, 0].set_title('blitz', fontsize= 11)
    axs[1, 0].bar(abs4Q, orde4Q)
    axs[1, 0].set_xticklabels(abs4Q, rotation=90, fontsize=8 )

    axs[1, 1].set_title('time_class', fontsize= 11)
    axs[1, 1].bar(abs5, orde5)
    axs[1, 1].set_xticklabels(abs5, rotation=90, fontsize=8)
    
    fig.delaxes(axs[1, 2])
    plt.tight_layout(pad=0.5)
    plt.show()

def filtrarDados3(ficheiro):
    """Função responsável por filtrar os dados necessários para a realização do gráfico Vitórias

    Args:
       ficheiro (file): ficheiro csv a ler

    Returns:
        [tuple]: tuplo que contem 4 listas que contêm o número de jogos com peças brancas e pretas e 2 listas que contêm as vitórias com peças brancas e pretas respetivamente (por utilizador)
    """
    dados = ler_csv(ficheiro)
    
    WUsersResult = list(zip(dados["white_username"], dados["white_result"]))
    BUsersResult = list(zip(dados["black_username"], dados["black_result"]))
    WinsWhite = Counter(sorted(list(itertools.filterfalse(lambda x: x[1] != "win" , WUsersResult))))
    WinsBlack = Counter(sorted(list(itertools.filterfalse(lambda x: x[1] != "win" , BUsersResult))))
    WUserAll =  Counter(list(map( lambda x: x[0], WUsersResult)))
    BUserAll = Counter(list(map(lambda x: x[0], BUsersResult)))
    listaAllPreta = sorted(BUserAll.items(),key=lambda x:x[1], reverse=True)
    listaAllBranca = sorted(WUserAll.items(),key=lambda x:x[1], reverse=True)
    listaVitoriasBranca = sorted(WinsWhite.items(),key=lambda x:x[1], reverse=True)
    listaVitoriasPreta = sorted(WinsBlack.items(),key=lambda x:x[1], reverse=True)
    
    return listaAllBranca, listaAllPreta, listaVitoriasBranca, listaVitoriasPreta 

def vitorias(ficheiro, lista_nomes, numero): 
    """Gráfico que mostra o número de vitórias que cada utilizador tem com peças brancas e peças pretas

    Args:
        ficheiro (file): ficheiro csv a ler
        lista_nomes (list): lista de nomes de jogadores a comparar (Case Sensitive)
        numero (int): número de jogadores a mostrar 
    """
    dados = filtrarDados3(ficheiro)
    numero0 = dados[0]
    numero1 = dados[1]
    numero2 = dados[2]
    numero3 = dados[3]
    
    if lista_nomes != None:
        lista_CVitoriasB = list(itertools.filterfalse(lambda x: x[0][0] not in lista_nomes, numero2))
        lista_CVitoriasP = list(itertools.filterfalse(lambda x: x[0][0] not in lista_nomes, numero3)) 
        lista_coisasB = list(itertools.filterfalse(lambda x: x[0] not in lista_nomes, numero0))
        lista_coisasP = list(itertools.filterfalse(lambda x: x[0] not in lista_nomes, numero1))  
        
        winsCoisaB = list(map(lambda x, y: x[1]/y[1], lista_CVitoriasB, lista_coisasB)) #ordenadasB
        winsCoisaP = list(map(lambda x, y: x[1]/y[1], lista_CVitoriasP, lista_coisasP)) #ordenadasP
        abcissas2 = list(map(lambda x: x[0], lista_coisasB))
        labels = abcissas2[:len(lista_nomes)]
        x = np.arange(len(labels))
        width = 0.35

        
        fig, ax = plt.subplots()
        ax.bar(x - width/2, winsCoisaB[:len(lista_nomes)], width, label='peças Brancas', color = "lightgray")
        ax.bar(x + width/2, winsCoisaP[:len(lista_nomes)], width, label='peças Pretas', color = "black")

        ax.set_ylabel('Percentagens')
        ax.set_xlabel('Jogadoras')
        ax.set_title('Percentagem de vitórias jogando com \npeçasbrancas / pretas', fontsize = 10)
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation = 90, fontsize = 8)
        ax.legend()
        
        plt.show()
       
    else:
    
        winsB = list(map(lambda x, y: x[1]/y[1], numero2, numero0)) #ordenadasB
        winsP = list(map(lambda x, y: x[1]/y[1], numero3, numero1)) #ordenadasP
        abcissas = list(map(lambda x: x[0], numero0))

        labels = abcissas[:numero]
        x = np.arange(len(labels))
        width = 0.35

        fig, ax = plt.subplots()
        ax.bar(x - width/2, winsB[:numero], width, label='peças Brancas', color = "lightgray")
        ax.bar(x + width/2, winsP[:numero], width, label='peças Pretas', color = "black")

        ax.set_ylabel('Percentagens')
        ax.set_xlabel('Jogadoras')
        ax.set_title('Percentagem de vitórias jogando com \npeçasbrancas / pretas', fontsize = 10)
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation = 90, fontsize = 8)
        ax.legend()
        
        plt.show()
    
def filtrarDados4(ficheiro, jogada):
    """Função responsável por filtrar os dados necessários para a realização do gráfico Seguinte

    Args:
        ficheiro (file): ficheiro csv a ler
        jogada (str): jogada inicial

    Returns:
        [list]: lista que contêm o número de vezes que certa peça foi movida depois de uma jogada inicial em particular
    """
    dados = ler_csv(ficheiro)
    jogadas = dados["pgn"]

    listaMoves = []
    listaPares = []
    
    for x in list(map(lambda x: x[:50], jogadas)):
        if jogada in x[:5] :
            listaMoves.append(x)

    padrao= r'[a-z][1-8]|[A-Z][a-z][1-8]'
    for _ in listaMoves:
        listaPares.append(re.findall(padrao, _))

    listaParesFiltrada = itertools.filterfalse(lambda x: len(x)>2, listaPares)

    listaQuaseNormal=list(itertools.filterfalse(lambda x: x==jogada , itertools.chain.from_iterable(listaParesFiltrada) ))
    contador = Counter(listaQuaseNormal)
    return sorted(contador.items(),key=lambda x:x[1], reverse=True)


def seguinte(ficheiro, jogada ,numero=5):
    """Gráfico que mostra as percentagens de jogadas mais prováveis depois de determinada jogada

    Args:
        ficheiro (file): ficheiro csv a ler
        jogada (str): jogada inicial
        numero (int, optional): número de jogadas a mostrar. Defaults to 5.
    """
    dados = filtrarDados4(ficheiro, jogada)
    total = sum(map(lambda x : x[1], dados ))
    probabilidades =list(map(lambda x: x/total, map(lambda x : x[1], dados )))
    abcissas = list(map(lambda x : x[0], dados ))

    plt.title('Jogadas mais prováveis depois de ' + jogada)
    plt.ylabel('Probabilidade')
    plt.xlabel('Jogadas')
    plt.bar(abcissas[:numero], probabilidades[:numero])
    plt.show()

def filtrarDados5(ficheiro):
    """Função responsável por filtrar os dados necessários para a realização do gráfico Mate

    Args:
        ficheiro (file): ficheiro csv a ler

    Returns:
        [tuple]: tuplo que contém 2 dicionários que contêm o número de vitórias e o número de xeque-mates que cada jogador obteve, respetivamente
    """
    dados = ler_csv(ficheiro)

    Users = dict.fromkeys(dados["white_username"]+dados["black_username"])
    WUsersResult = list(zip(dados["white_username"], dados["white_result"]))
    BUsersResult = list(zip(dados["black_username"], dados["black_result"]))

    UserGames = sorted(list(zip(WUsersResult, BUsersResult)))
    Wins = sorted(list(itertools.filterfalse(lambda x: x[1] != "win" , WUsersResult)) + list(itertools.filterfalse(lambda x: x[1] != "win" , BUsersResult)))
    
    UserGamesWinCKM = list(itertools.filterfalse(lambda x: x[0][1] == "timeout" or x[0][1] == "resigned" or x[0][1] == "abandoned" or x[0][1] == "repetition" or x[0][1] == "insufficient" or x[0][1] == "agreed" or x[0][1] == "timevsinsufficient" or x[0][1] == "bughousepartnerlose" or x[0][1] == "stalemate" or x[0][1] == "50move" or x[1][1] == "timeout" or x[1][1] == "resigned" or x[1][1] == "abandoned" or x[1][1] == "repetition" or x[1][1] == "insufficient" or x[1][1] == "agreed" or x[1][1] == "timevsinsufficient" or x[1][1] == "bughousepartnerlose" or x[1][1] == "stalemate" or x[1][1] == "50move",  UserGames))

    WinCnt =  Counter(U[0] for U in Wins)
    CheckMCnt =  Counter(U[0][0] for U in UserGamesWinCKM if U[1][1] == "checkmated") + Counter(U[1][0] for U in UserGamesWinCKM if U[0][1] == "checkmated")
    
    return WinCnt, CheckMCnt
    
def mate(ficheiro, numero):
    """Gráfico que mostra as percentagens de xeque-mate, jogos ganhos e jogos ganhos por xeque-mate de cada jogador

    Args:
        ficheiro (file): ficheiro csv a ler
        numero (int): número de jogadores a mostrar

    """

    dados = filtrarDados5(ficheiro)

    Wins = sorted(dados[0].items(), key=lambda x: x[1], reverse=True)
    CheckM = sorted(dados[1].items(), key=lambda x: x[1], reverse=True)

    abss = list(map(lambda x: x[0], Wins))
    ordeWins = list(map(lambda x: x[1], Wins))
    ordeCheck = list(map(lambda x: x[1], CheckM))
    
    ratio = list(map(lambda x,y: x/y, ordeCheck, ordeWins))



    labels = abss[:numero]
    x = np.arange(len(labels))
    width = 0.35  

    fig, ax = plt.subplots()
    ax2 = ax.twinx()
    ax.bar(x - width/2, ordeCheck[:numero], width, label='Jogos ganhos por xeque-mate', color = "lightgray")
    ax.bar(x + width/2, ordeWins[:numero], width, label='Jogos ganhos', color = "blue")

    ax2.plot(abss[:numero], ratio[:numero], color = 'red', label = "Percentagem de xeque-mate")

    ax.set_ylabel('#Jogos')
    ax.set_title('Percentagem de xeque-mate, \njogos ganhos e jogos ganhos por xeque-mate', fontsize = 10)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation = 90, fontsize = 8)
    ax2.set_ylabel("#Percentagem de xeque-mate")
    ax2.legend(loc ="center left")
    ax.legend()

    plt.show()



def extrair(ficheiro, regExp, coluna, novoFicheiro):
    """Função que estrai o conteúdo de determinada coluna de um ficheiro csv para outro ficheiro csv novo

    Args:
        ficheiro (file): ficheiro a csv a ler
        regExp (str): expressão regular responsável por filtrar os resultados desejados
        coluna (str): nome da coluna a extrair 
        novoFicheiro (file): nome do novo ficheiro
    """
    dados = ler_csv(ficheiro)
    dadosExtract= dados[coluna]
    filtered = []

    for _ in dadosExtract:
        if re.findall(regExp,_):
            filtered.append(_)

    with open(novoFicheiro, 'w') as f:
        writer = csv.writer(f, delimiter = "\n")
        writer.writerow(filtered)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()    
    group.add_argument('-c', type=int, help="Número de resultados a mostrar", default=5)
    group.add_argument("-u", help="Nomes dos jogadores a comparar (pelo menos 2)", nargs = "+", default = None)

    parser.add_argument('ficheiro', help='Nome do ficheiro')
    parser.add_argument("funcao", help="Nome da função a utilizar", choices=["anos", "classes","vitorias", "seguinte", "mate", "extrair"])
    parser.add_argument("-j", help="Primeira Jogada", default="e4")
    parser.add_argument("-r", help="Expressão regular para filtrar o ficheiro", type=str, default= r".*")
    parser.add_argument("-d", help="Coluna do ficheiro", default="wgm_username", type=str)
    parser.add_argument("-o", help="Nome do novo ficheiro", default="out.csv")
    
    args = parser.parse_args()

    if args.funcao == "anos":
        anos(args.ficheiro)
    elif args.funcao == "classes":
        classes(args.ficheiro, numero=args.c)
    elif  args.funcao == "vitorias":
        vitorias(args.ficheiro, args.u, args.c)
    elif  args.funcao == "seguinte":
        seguinte(args.ficheiro, args.j, args.c)
    elif args.funcao == "mate":
        mate(args.ficheiro, numero=args.c)
    elif args.funcao == "extrair":
        extrair(args.ficheiro, regExp = args.r, coluna = args.d, novoFicheiro = args.o)