# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario=float(input('Qual é o salário do funcionário? '))
promocao=salario*1.15

print('O salário após a promoção com aumento de 15% será de R$ {:.2f}'.format(promocao))