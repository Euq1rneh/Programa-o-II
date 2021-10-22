#!/usr/bin/env python
"""
Universidade de Lisboa
Faculdade de Ciências
Departamento de Informática
Licenciatura em Tecnologias da Informação
2020/2021

Programação II

Ferramentas de sistema

Impressão de um ficheiro com número de linha e marca de fim de linha,
ambos opcionais.

Exemplifica a utilização da linha de comandos.

Exemplo de utilização:
$ python cat.py -n -e cat.py 
"""

__author__ = "Vasco T. Vasconcelos"
__copyright__ = "Programação II, LTI, DI/FC/UL, 2021"
__email__ = "docentes-prog2-lti@listas.di.ciencias.ulisboa.pt"

def para_str(numero, carateres):
    """Um número em formato string, precedido de espaços, de modo a que
    o comprimento total da string tenha um dado número de carateres

    Args:
        numero (int): O número a converter em string
        carateres (int): O número de carateres total

    Returns:
        str: A string com a representação textual do número
    """
    numero = str(numero)
    espacos = carateres - len(numero)
    return ' ' * espacos + numero

def cat (nome_ficheiro, numeros = False, dolar = False):
    """Imprimir o conteúdo de um ficheiro com números de linha à
    esquerda (opcional) e o símbolo dolar à direita (opcional)

    Args:
        nome_ficheiro (str): O nome do ficheiro
        numeros (bool, optional): Queremos imprimir números de linha?. Defaults to False.
        dolar (bool, optional): Queremos $ à direita?. Defaults to False.
    """
    with open(nome_ficheiro) as leitor:
        linhas = leitor.read().splitlines()
        carateres = len(str(len(linhas))) # n de carateres do n de linhas
        numero_linha = 1
        for linha in linhas:
            inicio = para_str(numero_linha, carateres) if numeros else ''
            fim = '$' if dolar else ''
            print(inicio + ' ' + linha + fim)
            numero_linha += 1

if __name__ == '__main__':
    import sys
    utilizacao = 'Utilização: cat [-e,-n] ficheiro'
    if len(sys.argv) < 2:
        print(utilizacao)
    else:
        dolar, numeros = False, False
        i = 1
        while i < len(sys.argv) - 1:
            if sys.argv[i] == '-n':
                numeros = True
            elif sys.argv[i] == '-e':
                dolar = True
            else:
                print(utilizacao)
                sys.exit('Opção inválida')
            i += 1
        nome_ficheiro = sys.argv[i]
        cat(nome_ficheiro, numeros = numeros, dolar = dolar)