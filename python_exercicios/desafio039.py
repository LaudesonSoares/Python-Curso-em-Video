# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anonasc = int(input('Qual seu ano de nascimento? '))
anoatual = date.today().year
idade = anoatual - anonasc

if idade < 18:
    print('Você tem {} anos e ainda faltam {} para se alistar.'.format(idade,18-idade))
elif idade == 18:
    print('Você tem {} anos e deve se alistar esse ano.'.format(idade))
else:
    print('Você tem {} anos e já ULTRAPASSOU em {} anos a idade de alistamento.'.format(idade,idade-18))