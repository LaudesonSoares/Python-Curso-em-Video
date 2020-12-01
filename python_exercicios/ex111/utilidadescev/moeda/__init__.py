def aumentar(preço=0, taxa=0, formato=False):
    '''
    :param preço: Preço digitado pelo usuário.
    :param taxa: Taxa aplicada para aumentar o preço do usuário.
    :param formato: Formatação em R$ se True e sem Formatação se False
    :return: Resultado do preço com a taxa aplicada.
    '''
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',') #Função replace é utilizada para substituir valores

def resumo(preço=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30)) #Função center é utilizada para centralizar uma string ou número
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}') #\t é utilizado para tabulação dos valores
    print(f'Dobro do preço: \t{dobro(preço,True)}')
    print(f'Metade do preço: \t{metade(preço,True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}') #Quando necessário, utilizar \t mais de uma vez para tabulação
    print('-'*30)
