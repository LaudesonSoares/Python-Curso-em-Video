#Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = c = s = maior = menor =  0
q = ''
while q != 'N':
    n = int(input('Digite um número: '))
    q = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    c += 1
    s += n
    if n > maior:
        maior = n
    else:
        menor = n
print('Você digitou {} números e a média foi {:.2f}'.format(c, s/c))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
