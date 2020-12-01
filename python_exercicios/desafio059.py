#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
op = 0

while op != 5:
    op = int(input('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Que operação deseja executar? '''))
    print('-==' * 15)
    if op == 1:
        print(' O resultado da soma {} + {} é {}.'.format(n1, n2, n1 + n2))
        print('-==' * 15)
    elif op == 2:
        print('O resultado da multiplicação {} x {} é {}.'.format(n1, n2, n1*n2))
        print('-==' * 15)
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}.'.format(n1, n2, maior))
    elif op == 4:
        print('Digite novos valores.')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
        print('-==' * 15)
from time import sleep
sleep(1)
print('Execução finalizada!')
