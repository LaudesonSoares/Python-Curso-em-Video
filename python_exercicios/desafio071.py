#Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
# programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*30)
print('{:^30}'.format('BANCO SX'))
print('='*30)

# Minha solução com IF

saque = int(input('Que valor você quer sacar: R$ '))
c50 = saque // 50
if c50 > 0:
    print(f'Total de {c50} cédulas de R$ 50.')
c20 = (saque - (50*c50)) // 20
if c20 > 0:
    print(f'Total de {c20} cédulas de R$ 20.')
c10 = (saque - (50*c50) - (20*c20)) // 10
if c10 > 0:
    print(f'Total de {c10} cédulas de R$ 10.')
c1 = (saque - (50*c50) - (20*c20) - (10*c10)) // 1
if c1 > 0:
    print(f'Total de {c1} cédulas de R$ 1.')
print('='*30)
print('Volte sempre ao BANCO SX! Tenha um bom dia!')

# Solução Guanabara com While

print('='*30)
print('{:^30}'.format('BANCO SX'))
print('='*30)

valor = int(input('Que valor você quer sacar: R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R$ {céd}.')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO SX! Tenha um bom dia!')