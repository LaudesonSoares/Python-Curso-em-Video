#Escreva um programa que leia um número N inteiro qualquer e
#mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} → {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2         #O t1 assume o lugar do t2
    t2 = t3         #O t2 assume o lugar do t3
    cont += 1
print(' → FIM')

#Lógica do programa
# O t1 deve assumir o lugar do t2 e o t2 assumir o lugar do t3 para que o loop acrescente a soma do valor anterior da sequência
'''0 - 1 - 1 - 2 - 3 - 5 - 8 - 13
t1  t2  t3
0 - 1 - 1 - 2 - 3 - 5 - 8 - 13
    t1  t2  t3
0 - 1 - 1 - 2 - 3 - 5 - 8 - 13
        t1  t2  t3
0 - 1 - 1 - 2 - 3 - 5 - 8 - 13
            t1  t2  t3
0 - 1 - 1 - 2 - 3 - 5 - 8 - 13
                t1  t2  t3
0 - 1 - 1 - 2 - 3 - 5 - 8 - 13
                    t1  t2  t3'''