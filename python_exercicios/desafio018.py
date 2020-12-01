# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ang=float(input('Digite o ângulo desejado: '))
seno=math.sin(math.radians(ang))
cos=math.cos(math.radians(ang))
tang=math.tan(math.radians(ang))

print(f'O seno é {seno:.2f}\nO cosseno é {cos:.2f} \nA tangente é {tang:.2f}')
