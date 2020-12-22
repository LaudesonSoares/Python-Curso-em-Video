# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
#
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas(*n, sit=False):
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
    if not sit:
        return {'Total': total, 'maior': maior, 'menor': menor, 'média': média}
    if média < 5:
        situação = 'RUIM'
    situação = 'BOA' if 5 < média < 7 else 'ÓTIMO'
    return {
        'Total': total,
        'maior': maior,
        'menor': menor,
        'média': média,
        'situação': situação,
    }


#Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)

#Resposta Guanabara --------------------------------------------------------------------------
def notas(*n, sit=False):
    r = {
        'total': len(n),
        'maior': max(n),
        'menor': min(n),
        'média': sum(n) / len(n),
    }

    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        r['situação'] = 'RAZOÁVEL' if r['média'] >= 5 else 'RUIM'
    return r

#Programa Principal
resp = notas(1, 8, 5.5, 2.5, 8.5, sit=True)
print(resp)
