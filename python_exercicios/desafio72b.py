#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
#Incluir se o usuário deseja seguir

tupnum = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    usunum = int(input('Digite um número entre 0 e 20: '))
    if 0 <= usunum <= 20:
        print(f'Você digitou o número {tupnum[usunum]}.')
        seguir = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if seguir in 'SN':
            if seguir == 'N':
                break
    else:
        usunum = int(input('Tente novamente. Digite um número entre 0 e 20: '))
        seguir = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if seguir in 'SN':
            if seguir == 'N':
                break