# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

print('-=-'*20)
print('IMC - ÍNDICE DE MASSA CORPORAL')
print('-=-'*20)

peso = float(input('Informe seu peso: (KG) '))
altura = float(input('Informe sua altura: (M) '))
IMC = peso/(altura ** 2)

if IMC < 18.5:
    print('Seu IMC é {:.2f}: Abaixo do Peso.'.format(IMC))
elif IMC < 25:
    print('Seu IMC é {:.2f}: Peso Ideal'.format(IMC))
elif IMC < 30:
    print('Seu IMC é {:.2f}: Sobrepeso'.format(IMC))
elif IMC < 40:
    print('Seu IMC é {:.2f}: Obesidade'.format(IMC))
else:
    print('Seu IMC é {:.2f}: Obesidade Mórbida'.format(IMC))
