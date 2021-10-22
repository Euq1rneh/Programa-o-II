def copia(ficheiroOrig, string):
    with open(ficheiroOrig, 'r') as de, open(string, 'w')as para:
        conteudo = de.read()
        para.write(conteudo)


def lista_floats(lista):
    nova=[]
    for elemento in lista:
        nova.append(float(elemento))
    return nova

def media(lista):
    soma = sum(lista)
    div = len(lista)
    med=soma/div
    return med

def imprimeMedias(ficheiro):
    val=[]
    medias=[]
    with open(ficheiro, 'r')as file:
        linhas = file.read().splitlines()
        for _ in linhas:
           numlist = _.split()
           val.append(numlist)
        for _ in range(len(val)):
            for x in range(len(val[_])):
                val[_][x]=float(val[_][x])
        for _ in val:
            medias.append(media(_))
        for elem in medias:
            print(elem)

    



