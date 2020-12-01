# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

vlrcasa = float(input('Qual valor da casa a ser financiada? '))
salario = float(input('Qual seu salário? '))
anos = int(input('O financiamento será de quantos anos? '))
prestação = vlrcasa/(anos*12)

if prestação > salario*0.30:
    print('No prazo de {} anos serão {} parcelas de R$ {}. Esse valor supera 30% do seu salário e não será possível conceder o financiamento.'.format
          (anos, anos*12, prestação))
else:
    print('Seu financiamento foi APROVADO! Sua prestação será de R$ {:.2f} em {} parcelas.'.format(prestação,anos*12))
