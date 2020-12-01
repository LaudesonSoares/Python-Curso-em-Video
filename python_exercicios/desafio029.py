#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

veloc = float(input('Qual a velocidade atual de um carro? '))
multa = ((veloc-80)*7)
print('Tenha um bom dia. Dirija com segurança.')
if veloc > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80 km/h.\nVocê deve pagar uma multa de R$ {:.2f}. '.format(multa))
    print('Tenha um bom dia. Dirija com segurança.')

