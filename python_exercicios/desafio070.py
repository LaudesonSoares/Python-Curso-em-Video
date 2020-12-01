#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

total = m1000 = menor = cont = 0
prodmenor = ''
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco >= 1000:
        m1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        prodmenor = nome
#    else:
#        if preco < menor:
#            menor = preco
#            prodmenor = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        print('{:-^40}'.format('FIM DO PROGRAMA'))
        break
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {m1000} produtos custando mais de R$ 1.000,00.')
print(f'O produto mais barato foi {prodmenor} que custa R$ {menor}.')
