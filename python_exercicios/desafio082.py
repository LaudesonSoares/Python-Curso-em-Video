# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if r in 'SN':
        if r == 'N':
            break
    if r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).upper().strip()
print(f'Os valores gerados foram {valores}.')
par = []
for v in valores:
    if v % 2 == 0:
        par.append(v)
print(f'Os valores pares são {par}.')
impar = []
for v in valores:
    if v % 2 != 0:
        impar.append(v)
print(f'Os valores ímpares são {impar}.')
