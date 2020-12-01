# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

cont = 0
c = 0
for s in range(1,7):
    s = int(input('Digite o {}º número: '.format(s)))
    if s % 2 == 0:
        c += s
        cont += 1
print('Você informou {} números PARES e a soma é {}.'.format(cont, c))
