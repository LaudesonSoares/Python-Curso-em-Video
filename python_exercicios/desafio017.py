# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

import math
cttop=float(input('Digite o comprimento do cateto oposto: '))
cttad=float(input('Digite o comprimento do cateto adjacente: '))
print('O cateto oposto é {}, o cateto adjacente é {} e a hipotenusa é {:.1f}'.format(cttop,cttad,math.hypot(cttop,cttad)))
