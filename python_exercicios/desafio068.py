#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

print('-=-'*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-'*10)

from random import randint
c = 0
while True:
    ec = randint(0, 10)
    n = int(input('Diga um valor: '))
    e = ' '
    while e not in 'PI':
        e = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    if (n+ec) % 2 == 0:
        r = 'P'
    else:
        r = 'I'
    if r == e == 'P':
        c += 1
        print('-'*30)
        print(f'O computador escolheu {ec} e você escolheu {n}. Total {ec + n}, deu PAR!')
        print('-'*30)
        print('''VOCÊ GANHOU!
    Vamos jogar novamente...''')
        print('-=-'*10)
    elif r == e == 'I':
        c += 1
        print('-'*30)
        print(f'O computador escolheu {ec} e você escolheu {n}. Total {ec + n}, deu ÍMPAR!')
        print('-'*30)
        print('''VOCÊ GANHOU!
    Vamos jogar novamente...''')
        print('-=-'*10)
    else:
        break
if r == 'P':
    print('-'*30)
    print(f'O computador escolheu {ec} e você escolheu {n}. Total {ec + n}, deu PAR.')
    print('-'*30)
    print('VOCÊ PERDEU!')
    print('-=-'*10)
    print(f'GAME OVER! Você venceu {c} vezes.')
else:
    print('-'*30)
    print(f'O computador escolheu {ec} e você escolheu {n}. Total {ec + n}, deu ÍMPAR.')
    print('-'*30)
    print('VOCÊ PERDEU!')
    print('-=-'*10)
    print(f'GAME OVER! Você venceu {c} vezes.')
