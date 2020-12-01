# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Flamengo.

tab = ('Atlético Mineiro', 'Internacional', 'Palmeiras', 'São Paulo', 'Vasco da Gama', 'Fluminense', 'Flamengo', 'Sport', 'Santos', 'Fortaleza', 'Athletico-PR', 'Ceará', 'Corintians', 'Atlético Goianiense', 'Grêmio', 'Bahia', 'Bragantino', 'Botafogo', 'Coritiba', 'Goiás')
pos = 'Flamengo'
print(f'Tabela Brasileirão 2020: {tab}')
print('=-='*20)
print(f'Os cinco primeiros colocados são: {tab[0:5]}')
print('=-='*20)
print(f'Os quatro últimos colocados são: {tab[-4:]}')
print('=-='*20)
print(f'Times em ordem alfabética: {sorted(tab)}')
print('=-='*20)
print('O Flamengo está na {}ª posição.'.format(tab.index('Flamengo')+1))
