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


def classes(ficheiro, numero = 5):
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
    
def mate(ficheiro, numero = 5):

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
    return ordeWins

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

def vitorias(ficheiro, numero): 
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


def extrair(ficheiro, regExp, coluna, novoFicheiro):
    """Função que estrai o conteúdo de determinada coluna de um ficheiro csv para outro ficheiro csv novo

    Args:
        ficheiro (file): ficheiro a csv a ler
        regExp (str): expressão regular responsável por filtrar os resultados desejados
        coluna (str): nome da coluna pela qual se devem extrair os resultados
        novoFicheiro (file): nome do novo ficheiro
    """
    with open(ficheiro, 'r') as csvfile:
        dadosE = []
        leitor = csv.DictReader(csvfile)
        for dic in leitor:
            for key in dic:
                if key == coluna:
                    if re.search(regExp, dic[key]):
                        dadosE.append(dic)
    with open(novoFicheiro, 'w', newline="") as newcsvfile:
        headers = list(dict.fromkeys(dic))
        escritor = csv.DictWriter(newcsvfile, headers)

        escritor.writeheader()
        for x in dadosE: 
            escritor.writerow(x)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('ficheiro', help='Nome do ficheiro')
    parser.add_argument("funcao", help="Nome da função a utilizar", choices=["classes", "mate"])
    parser.add_argument('-c', type=int, help="Número de resultados a mostrar", default=5)
    parser.add_argument("-r", help="Expressão regular para filtrar o ficheiro", type=str, default=".*")
    parser.add_argument("-d", help="Coluna do ficheiro", default="wgm_username", type=str)
    parser.add_argument("-o", help="nome do novo ficheiro", default="out.csv")
    
    args = parser.parse_args()
    
    if args.funcao == "classes":
        classes(args.ficheiro, numero=args.c)
    elif args.funcao == "mate":
        mate(args.ficheiro, numero=args.c)
    elif args.funcao == "extrair":
        extrair(args.ficheiro, regExp =args.r, coluna = args.d, novoFicheiro = args.o)
    
