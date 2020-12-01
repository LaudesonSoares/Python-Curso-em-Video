# Dicionários
#
# Dicionários são estruturas de variáveis compostas onde múltiplas informações são guardadas em grupo na memória,
# semelhantes as tuplas e listas, mas é possível ter índices literais.
# Dicionários possuem as seguintes características
#
# São definidas por {} ou dict()
# São mutáveis

dados = dict()
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])
print(dados['idade'])

#Adicionando elementos ao dicionário
dados['sexo'] = 'M'

#Removendo elementos
del dados['idade']

#As chaves de abertura e fechamento podem ser lançadas em linhas diferentes para o dicionário
filme = {'título':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
         }

#Itens, Chaves e Valores
print(filme.values()) #São os valores do dicionário: 'Star Wars', '1977', 'George Lucas'
print(filme.keys()) #São as chaves do dicionário: 'título', 'ano', 'diretor'
print(filme.items()) #São todos os itens do dicionário: Valores e Chaves

# Laços com Dicionários
for k,v in filme.items():
    print(f'O {k} é {v}')
    #O título é Star Wars
    #O ano é 1977
    #O diretor é George Lucas

#Listas com Dicionários
# É possível incluir dicionários dentro das listas
locadora = [{'título':'Star Wars','ano':'1977', 'autor':'George Lucas'},{'título':'Avengers','ano':'2012', 'autor':'Joss Whedon'}
            {'título':'Matrix','ano':'1999', 'autor':'Wachowski'}]
print(locadora[0]['ano']) #1977
print(locadora[2]['título']) #Matrix

#Prática
#Exemplo 1
pessoas = {'nome':'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
----------------------------------------------------------------------------------------------
pessoas = {'nome':'Gustavo', 'sexo': 'M', 'idade': 22}
del pessoas['sexo'] #Deleta item do dicionário
pessoas['nome'] = 'Leandro' #Alterando valores no dicionário
pessoas['peso'] = 98.5 #Adicionando elementos no dicionário
for k, v in pessoas.items(): #O laço com items funciona como o enumerate nas tuplas e listas
    print(f'{k}={v}')

-----------------------------------------------------------------------------------------
brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

#Laços com dicionário e lista

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #A estrutura copy() deve ser utilizada para gerar cópia do dicionário ao invés do [:] em tuplas ou listas
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
    for v in e.values():
        print(v, end=' ')
    print()

# Ordenando Dicionários

from random import randint
from time import sleep
from operator import itemgetter #método para rankear o dicionário
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1,6)}
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # Ordena o dicionário através da chave '1' (valor do dado) em ordem reversa do maior para menor
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)