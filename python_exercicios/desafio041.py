# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date

anonasc = int(input('Informe o ano de nascimento do atleta: '))
anoatual = date.today().year
idade = anoatual-anonasc

if idade <= 9:
    print('A idade do atleta é {} anos e sua categoria é a MIRIM.'.format(idade))
elif idade <= 14:
    print('A idade do atleta é {} anos e sua categoria é INFANTIL.'.format(idade))
elif idade <= 19:
    print('A idade do atleta é {} anos e sua categoria é JÚNIOR.'.format(idade))
elif idade <= 25:
    print('A idade do atleta é {} anos e sua categoria é SÊNIOR.'.format(idade))
else:
    print('A idade do atleta é {} anos e sua categoria é MASTER.'.format(idade))
