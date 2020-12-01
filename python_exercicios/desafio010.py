#Crie um programa que leia quanto dinheiro um pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere US$1,00 = R$3,27

d10=float(input('Quanto você tem na carteira? '))
dollar=3.27
m=d10/dollar

print('Com esse dinheiro você pode comprar US$ {:.2f} dollares'.format(m))