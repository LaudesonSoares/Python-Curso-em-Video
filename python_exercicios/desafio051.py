# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
décimo = t + (10 - 1) * r #Fórmula para encontrar o enésimo termo da PA
for c in range(t,décimo + r, r):
    print(c, end=' ')
