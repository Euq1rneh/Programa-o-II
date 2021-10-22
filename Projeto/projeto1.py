import csv
from typing import Iterator
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import re
import itertools
import functools

def ler_csv(nome_ficheiro):
    """Ler um ficheiro CSV

    Args:
        nome_ficheiro (str): O nome do ficheiro

    Returns:
        list[list][str]: O conteúdo do ficheiro. 
            Cada elemento da lista contém uma linha do ficheiro CSV.
            Cada string corresponde a um valor no ficheiro CSV.
    """
    with open(nome_ficheiro, 'r') as ficheiro_csv:
        return list(csv.reader(ficheiro_csv))

def filtrarDados(ficheiro):
    listaAnos = []
    dados = ler_csv(ficheiro)
    dadosAnos = map(lambda x: x[4], dados)
    dadosNomesBrancos = list(map(lambda x: x[9], dados))
    dadosNomesPretos = list(map(lambda x: x[12], dados))
    
    nomesBrancos = itertools.filterfalse(lambda x:x=="white_username", dadosNomesBrancos)
    nomesPretos = itertools.filterfalse(lambda x:x=="black_username", dadosNomesPretos)

    for _ in dadosAnos:
        listaAnos.append(re.findall(r"[0-9][0-9][0-9][0-9]", _))

    Onesie = list(itertools.chain.from_iterable(listaAnos))#todos os anos (repetidos)
    anos = list(dict.fromkeys(Onesie))#lista com anos diferentes
    
    return [anos, sorted(list(zip(Onesie, nomesBrancos, nomesPretos)))]

def Njogos(ficheiro):
    listaAnos = []
    Jogos = {}
    n=0
    dados = ler_csv(ficheiro)
    dadosAnos = map(lambda x: x[4], dados)

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
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
def filtrarDados2(ficheiro):
    dados = ler_csv(ficheiro)
    Time = list(itertools.filterfalse(lambda x: x == "time_control", map(lambda x: x[3], dados)))
    Classes = list(itertools.filterfalse(lambda x : x == 'time_class', map(lambda x: x[6], dados)))

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

# def filtrarDados2():
#     dados = ler_csv("xadrez.csv")
#     Classes = list(itertools.filterfalse(lambda x : x == 'time_class', map(lambda x: x[6], dados)))

#     graf5 ={}#valores grafico 5
    
#     timeClass = list(dict.fromkeys(Classes))

#     aux = list(map(lambda x: {x:Classes.count(x)} , timeClass))
#     for _ in aux:
#         graf5.update(_)

#     rapid = rapidDados()
#     daily = dailyDados()
#     bullet = bulletDados()
#     blitz = blitzDados()

#     return rapid, daily, bullet, blitz, graf5

# def rapidDados():
#     dados = ler_csv("xadrez.csv")
#     Time = list(itertools.filterfalse(lambda x: x == "time_control", map(lambda x: x[3], dados)))
#     Classes = list(itertools.filterfalse(lambda x : x == 'time_class', map(lambda x: x[6], dados)))

#     rapid = []

#     for e in list(zip(Classes, Time)):
#         if e[0] == 'rapid':
#             rapid.append(e[1])

#     rapidTime = dict.fromkeys(rapid)
#     rapidDic = {}

#     rapidCount = list(map(lambda x: {x:rapid.count(x)}, rapidTime))
#     for _ in rapidCount:
#         rapidDic.update(_)

    
#     return rapidDic

# def dailyDados():
#     dados = ler_csv("xadrez.csv")
#     Time = list(itertools.filterfalse(lambda x: x == "time_control", map(lambda x: x[3], dados)))
#     Classes = list(itertools.filterfalse(lambda x : x == 'time_class', map(lambda x: x[6], dados)))

#     daily = []

#     for e in list(zip(Classes, Time)):
#         if e[0] == 'daily':
#             daily.append(e[1])

#     dailyTime = dict.fromkeys(daily)
#     dailyDic = {}

#     dailyCount = list(map(lambda x: {x:daily.count(x)}, dailyTime))
#     for _ in dailyCount:
#         dailyDic.update(_)

#     return dailyDic

# def bulletDados():
#     dados = ler_csv("xadrez.csv")
#     Time = list(itertools.filterfalse(lambda x: x == "time_control", map(lambda x: x[3], dados)))
#     Classes = list(itertools.filterfalse(lambda x : x == 'time_class', map(lambda x: x[6], dados)))

#     bullet = []

#     for e in list(zip(Classes, Time)):
#         if e[0] == 'bullet':
#             bullet.append(e[1])

#     bulletTime = dict.fromkeys(bullet)
#     bulletDic = {}

#     bulletCount = list(map(lambda x: {x:bullet.count(x)}, bulletTime))
#     for _ in bulletCount:
#         bulletDic.update(_)

#     return bulletDic

# def blitzDados():
#     dados = ler_csv("xadrez.csv")

#     Time = list(itertools.filterfalse(lambda x: x == "time_control", map(lambda x: x[3], dados)))
#     Classes = list(itertools.filterfalse(lambda x : x == 'time_class', map(lambda x: x[6], dados)))
#     blitz = []
#     for e in list(zip(Classes, Time)):
        
#         if e[0] == 'blitz':
#             blitz.append(e[1])
    
#     blitzTime = dict.fromkeys(blitz)
#     blitzDic = {}
    
#     blitzCount = list(map(lambda x: {x:blitz.count(x)}, blitzTime))
#     for _ in blitzCount:
#         blitzDic.update(_)
    
#     return blitzDic


def classes(ficheiro, numero):
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
    
    



def filtrarDados5(ficheiro):
    dados = ler_csv(ficheiro)

    Users = dict.fromkeys(list(dict.fromkeys(list(itertools.filterfalse(lambda x: x == "white_username", map(lambda x: x[9], dados)))+list(itertools.filterfalse(lambda x: x == "black_username", map(lambda x: x[12], dados))))))
    WUsersResult = list(zip(list(itertools.filterfalse(lambda x: x == "white_username", map(lambda x: x[9], dados))), list(itertools.filterfalse(lambda x: x == "white_result", map(lambda x: x[11], dados)))))
    BUsersResult = list(zip(list(itertools.filterfalse(lambda x: x == "black_username", map(lambda x: x[12], dados))), list(itertools.filterfalse(lambda x: x == "black_result", map(lambda x: x[14], dados)))))

    UserGames = sorted(list(zip(WUsersResult, BUsersResult)))
    Wins = sorted(list(itertools.filterfalse(lambda x: x[1] != "win" , WUsersResult)) + list(itertools.filterfalse(lambda x: x[1] != "win" , BUsersResult)))
    
    UserGamesWinCKM = list(itertools.filterfalse(lambda x: x[0][1] == "timeout" or x[0][1] == "resigned" or x[0][1] == "abandoned" or x[0][1] == "repetition" or x[0][1] == "insufficient" or x[0][1] == "agreed" or x[0][1] == "timevsinsufficient" or x[0][1] == "bughousepartnerlose" or x[0][1] == "stalemate" or x[0][1] == "50move" or x[1][1] == "timeout" or x[1][1] == "resigned" or x[1][1] == "abandoned" or x[1][1] == "repetition" or x[1][1] == "insufficient" or x[1][1] == "agreed" or x[1][1] == "timevsinsufficient" or x[1][1] == "bughousepartnerlose" or x[1][1] == "stalemate" or x[1][1] == "50move",  UserGames))

    WinCnt =  Counter(U[0] for U in Wins)
    CheckMCnt =  Counter(U[0][0] for U in UserGamesWinCKM if U[1][1] == "checkmated") + Counter(U[1][0] for U in UserGamesWinCKM if U[0][1] == "checkmated")
    
    return WinCnt, CheckMCnt
    
def mate(ficheiro, numero):

    dados = filtrarDados5(ficheiro)
    Wins = sorted(dados[0].items(), key=lambda x: x[1], reverse=True)
    CheckM = sorted(dados[1].items(), key=lambda x: x[1], reverse=True)

    abss = list(map(lambda x: x[0], Wins))
    ordeWins = list(map(lambda x: x[1], Wins))
    ordeCheck = list(map(lambda x: x[1], CheckM))
    ratio = list(map(lambda x,y:x/y, ordeCheck, ordeWins))


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



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('ficheiro', help='Nome do ficheiro')
    parser.add_argument("funcao", help="Nome da função a utilizar", choices=["classes", "mate"])
    parser.add_argument('-c', type=int, default=5)
    
    args = parser.parse_args()
    
    if args.funcao == "classes":
        classes(args.ficheiro, numero=args.c)
    elif args.funcao == "mate":
        mate(args.ficheiro, numero=args.c)

       