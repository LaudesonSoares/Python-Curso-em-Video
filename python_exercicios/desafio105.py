# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
#
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas (*n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''

    total = maior = menor = média = situação = cont = 0
    total = len(n)
    for valor in n:
        if cont == 0:
            maior = menor = valor
        elif valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
        cont +=1
    média = sum(n)/len(n)
    if sit:
        if média < 5:
            situação = 'RUIM'
        if 5 < média < 7:
            situação = 'BOA'
        else:
            situação = 'ÓTIMO'
        dados = {'Total': total, 'maior': maior, 'menor': menor, 'média': média, 'situação': situação}
    else:
        dados = {'Total': total, 'maior': maior, 'menor': menor, 'média': média}
    return dados


#Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)

#Resposta Guanabara --------------------------------------------------------------------------
def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        if r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

#Programa Principal
resp = notas(1, 8, 5.5, 2.5, 8.5, sit=True)
print(resp)
