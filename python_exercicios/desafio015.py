#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km=float(input('Qual a quantidade de Km percorridos? '))
d=int(input('Qual a quantidade de dias utilizados? '))
precokm=0.15
precodia=60
valoraluguel=km*precokm+d*precodia

print('O preço a pagar pelo aluguel do carro é de R${:.2f} '.format(valoraluguel))
