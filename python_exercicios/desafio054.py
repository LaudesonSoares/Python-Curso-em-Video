# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

anoatual = date.today().year
totmaior = 0
totmenor = 0

for anonasc in range(1, 8):
    anonasc = int(input('Em que ano a {}º pessoa nasceu? '.format(anonasc)))
    mi = anoatual - anonasc
    if mi >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Temos {} pessoas que são MAIORES e {} pessoas NÃO atingiram a MAIORIDADE!'.format(totmaior, totmenor))
