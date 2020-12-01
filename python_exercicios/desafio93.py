# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

scout = {}
scout['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {scout["nome"]} jogou? '))
gols = list()
for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
scout['gols'] = gols
scout['total'] = sum(gols)
print('-='*30)
print(scout)
print('-='*30)
for k, v in scout.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {scout["nome"]} jogou {partidas} partidas.')
for i in range(0, partidas):
    print(f'    => Na partida {i+1}, fez {gols[i]} gols.')
print(f'Foi um total de {scout["total"]} gols.')
