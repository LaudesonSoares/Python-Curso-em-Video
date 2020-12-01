# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))

#if n % 1 == 0 and n % n == 0 and n % 2 == 0 or n % 3 ==0:
#    print('O número {} é NÃO PRIMO.'.format(n))
#else:
#    print('O número {} é PRIMO.'.format(n))

tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\33[33m', end='')
        tot += 1
    else:
        print('\33[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
