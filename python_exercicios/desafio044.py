# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

print('-=-'*20)
print('{:=^60}'.format(' SX CONSULTORIA FINANCEIRA '))
print('-=-'*20)

preco = float(input('Informe o preço da compra: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] - Pagamento à vista dinheiro/cheque
[ 2 ] - à vista cartão
[ 3 ] - em até 2x no cartão
[ 4 ] - 3x ou mais no cartão''')
tipo = int(input('Qual a forma de pagamento? '))
parcela = int(input('Quantas parcelas? '))

if tipo == 1:
    print('Sua compra terá 10% de desconto é seu valor será R$ {:.2f}.'.format(preco*0.90))
elif tipo == 2:
    print('Sua compra terá 5% de desconto e seu valor será R$ {:.2f}.'.format(preco*0.95))
elif tipo == 3 and parcela <=2:
    print('Sua compra será parcelada em {}x de R$ {:.2f} SEM JUROS. O valor total será R$ {}.'.format(parcela, preco/parcela, preco))
elif tipo == 4 and parcela >=3:
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS. O valor total será R$ {}'.format(parcela, (preco*1.2)/parcela, preco*1.2))
else:
    print('A forma de pagamento e parcelas estão divergentes. Favor, verificar!')