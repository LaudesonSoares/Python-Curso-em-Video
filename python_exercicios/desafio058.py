#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
from time import sleep

num = random.randint(0, 10)
numtent = 1

print('-=-'*20)
print('Vou pensar em um número entre 0 e 10. Tente advinhar...')
print('-=-'*20)

numusu = int(input('Em que número eu pensei? '))

while num != numusu:
    numtent += 1
    if numusu < num:
        print('PROCESSANDO...')
        sleep(1)
        print('Você ERROU! Chute Maior...')
        numusu = int(input('Em que número eu pensei? '))
    if numusu > num:
        print('PROCESSANDO...')
        sleep(1)
        print('Você ERROU! Chute Menor...')
        numusu = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
print('ACERTOU! Foram necessários {} palpites para vencer.'.format(numtent))
