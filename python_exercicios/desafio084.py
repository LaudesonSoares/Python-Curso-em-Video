# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

galera = list()
dado = list()
mai = men = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    if len(galera) == 0:
        mai = men = dado[1] #Item na posição 1 da lista dado
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    galera.append(dado[:])
    dado.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-='*30)
print(f'Ao todo você cadastrou {len(galera)} pessoas.') #Cada lista dentro da lista galera é contado como um item
print(f'O maior peso foi de {mai} KG. Peso de ', end='')
for p in galera:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men} KG. Peso de ', end='')
for p in galera:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
