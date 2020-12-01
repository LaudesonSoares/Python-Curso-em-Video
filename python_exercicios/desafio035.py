# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# Se a soma entre os dois lados é igual ao terceiro, esse triângulonão pode existir.
print('-=-'*20)
print('Informe o comprimento de três retas para formar um triângulo.')
print('-=-'*20)
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1+r2==r3:
    print('Essas retas NÃO PODEM formar um triângulo.')
else:
    print('Essas retas PODEM formar um triângulo.')