# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

c = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    print('-'*30)
    if n < 0:
        break
    while c < 10:
        c += 1
        print(f'{n}x{c}={n*c}')
    print('-'*30)
    d = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    c = 0
    while d not in 'SN':
        d = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if d == 'S':
        while c > 10:
            print(f'{n}x{c}={n * c}')
            c += 1
        print('-'*30)
    if d == 'N':
        break
print('PROGRAMA DE TABUADA ENCERRADO!')
