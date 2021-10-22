import csv
import re

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
            for key in dic:             # lê os dados do ficheiro para uma lista
                if key == coluna:
                    if re.search(regExp, dic[key]):
                        dadosE.append(dic)

    with open(novoFicheiro, 'w', newline="") as newcsvfile:
        headers = list(dict.fromkeys(dic))
        escritor = csv.DictWriter(newcsvfile, headers)      # escreve os dados para um novo ficheiro de acordo com os respetivos cabeçalhos

        escritor.writeheader()
        for x in dadosE: 
            escritor.writerow(x)
            

        
        