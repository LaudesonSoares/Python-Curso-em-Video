#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep
num = random.randint(0,5) #Faz o computador "PENSAR'
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
numusu = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
print('Em pensei em {}!'.format(num))
if num==numusu:
    print('PARABÉNS! Você venceu!!')
else:
    print('GANHEI! Você perdeu...Tente novamente!')

