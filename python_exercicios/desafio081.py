# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if r in 'SN' and r == 'N':
        break
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Os valores digitados foram {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
