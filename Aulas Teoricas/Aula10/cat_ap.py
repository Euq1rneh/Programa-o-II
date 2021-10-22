#!/usr/bin/env python
"""
Universidade de Lisboa
Faculdade de Ciências
Departamento de Informática
Licenciatura em Tecnologias da Informação
2020/2021

Programação II

Ferramentas de sistema

Impressão de um ficheiro com número de linha, marca de fim de linha,
começando numa dada linha e juntando várias linhas brancas numa
só. Tudo controlado por parâmetros opcionais.
Utiliza o módulo argparse para analisar a linha de comandos.

Exemplifica a utilização do módulo argparse.

Exemplo de utilização:
$ python cat_ap.py -n -p41 -s cat_ap.py 
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

def cat (nome_ficheiro, numeros = False, dolar = False, primeira = 1, juntar = False):
    """Imprimir o conteúdo de um ficheiro com:
    - números de linha à esquerda (opcional),
    - o símbolo dolar à direita (opcional),
    - começando numa dada linha (primeira linha por omissão) e
    - juntando várias linhas em branco seguidas numa só (opcional)

    Args:
        nome_ficheiro (str): O nome do ficheiro
        numeros (bool, optional): Queremos imprimir números de linha?. Defaults to False.
        dolar (bool, optional): Queremos $ à direita?. Defaults to False.
        primeira (int, optional): A primeira linha a afixar. Defaults to 1.
        juntar (bool, optional): Juntar várias linhas em branco seguidas
        numa só. Defaults to False.
    """
    with open(nome_ficheiro) as leitor:
        linhas = leitor.read().splitlines()
        linhas = linhas[primeira:]
        carateres = len(str(len(linhas))) # n de carateres do n de linhas
        numero_linha = primeira
        vazia = False
        for linha in linhas:
            numero_linha += 1
            if juntar and linha == '':
                if vazia: # anterior é vazia?
                    continue
                vazia = True
            else:
                vazia = False
            inicio = para_str(numero_linha, carateres) if numeros else ''
            fim = '$' if dolar else ''
            print(inicio + ' ' + linha + fim)

if __name__ == '__main__':
    import argparse
    # 1. iniciar o analisador sintatico
    parser = argparse.ArgumentParser()
    # 2. juntar argumentos
    parser.add_argument('nome_ficheiro',
                        help = 'O nome do ficheiro a imprimir')
    parser.add_argument('-n',
                        action = 'store_true',
                        help = 'Imprimir o número de linha')
    parser.add_argument('-e',
                        action = 'store_true',
                        help = 'Imprimir um $ no fim da linha')
    parser.add_argument('-p',
                        nargs = '?', type = int, default = 1,
                        help = 'Começar numa dada linha')
    parser.add_argument('-s',
                        action = 'store_true',
                        help = 'Juntar múltiplas linhas em branco adjacentes')
    # 3. analisar linha comandos
    arguments = parser.parse_args()
    # 4. usar os argumentos da linha de comandos
    cat(arguments.nome_ficheiro,
        numeros = arguments.n,
        dolar = arguments.e,
        primeira = arguments.p,
        juntar = arguments.s)