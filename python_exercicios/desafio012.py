# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco=float(input('Qual preço do produto? '))
desconto=preco*0.95

print('O preço com desconto de 5% é R$ {:.2f}'.format(desconto))
