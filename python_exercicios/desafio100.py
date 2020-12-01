# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a
# segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 100)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.5)
    print('PRONTO!')


def somaPar(lista):
    s = 0
    for v in lista:
        if v % 2 == 0:
            s += v
    print(f'A soma dos pares de {lista} é {s}.')

números = []
sorteia(números)
somaPar(números)
