#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupnum = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
usunum = int(input('Digite um número entre 0 e 20: '))
while usunum not in range(0, 20):
    usunum = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    if usunum >= 0 and usunum <= 20:
        break
print(f'Você digitou o número {tupnum[usunum]}.')

#Ideal 80 caracteres por comando para o código ficar mais conciso