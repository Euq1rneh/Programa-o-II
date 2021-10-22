__author__='Henrique Marques, 57153'

def busca_lista_dupla(lista, x):
    """Verifica se um valor inteiro se encontra numa lista de listas ordenada

    Pre:
        As listas estão ordenadas;
        Nenhuma das sublistas está vazia;
        O conteúdo das listas são valores inteiros;

    Args:
        lista (list): lista de listas que contêm os valores inteiros
        x (int): número inteiro que será utlizado na procura

    Returns:
        [bool]: devolve True se o elemento x se encontrar na lista, caso
                contrário devolve False
    """
    return x in [num for listalista in lista for num in listalista]
    
     