# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
#
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep
def contador (início, fim, passo):
    if passo == 0:
        passo = 1
    print('-='*20)
    print(f'Contagem de {início+1} até {fim} de {passo} em {passo}')
    for c in range(início, fim, passo):
        print(c+1, end=' ')
        sleep(0.5)
    print('FIM!')


contador(0, 10, 1)
contador(9, 0, -2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i-1, f, p)
