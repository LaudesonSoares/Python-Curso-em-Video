# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Informe o valor de seu salário: '))
if sal<=1250:
    print('Você terá um reajuste de 15% e seu novo salário será de R$ {:.2f}'.format(sal*1.15))
else:
    print('Você terá um reajuste de 10% e seu novo salário será de R$ {:.2f}'.format(sal*1.1))
