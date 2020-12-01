# Crie um programa que faça o computador jogar Jokenpô com você.

print('-=-'*20)
print('{:=^60}'.format(' JO KEN PÔ '))
print('-=-'*20)

from random import choice
from time import sleep
j1 = str(input('Escolha entre Pedra, Papel ou Tesoura: ')).title()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ !!')

maq = ['Pedra','Papel','Tesoura']
result = choice(maq)

if j1 == 'Pedra' and result == 'Papel':
    print('A máquina escolheu {}! Você PERDEU!!'.format(result))
elif j1 =='Pedra' and result == 'Tesoura':
    print('A máquina escolheu {}. VOCÊ GANHOU!'.format(result))
elif j1 == 'Papel' and result == 'Pedra':
    print('A máquina escolheu {}. VOCÊ GANHOU!'.format(result))
elif j1 == 'Papel' and result == 'Tesoura':
    print('A máquina escolheu {}. VOCÊ PERDEU!'.format(result))
elif j1 == 'Tesoura' and result == 'Papel':
    print('A máquina escolheu {}. VOCÊ GANHOU!'.format(result))
elif j1 == 'Tesoura' and result == 'Pedra':
    print('A máquina escolheu {}. VOCÊ PERDEU!'.format(result))
else:
    print('A máquina também escolheu {}. EMPATE!!'.format(result))
