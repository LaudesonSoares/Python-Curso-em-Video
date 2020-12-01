# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

print('-=-'*20)
print('Informe o comprimento de três retas para formar um triângulo.')
print('-=-'*20)

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1+r2==r3:
    print('Essas retas NÃO podem formar um triângulo!')
elif r1 == r2 == r3:
    print('Essas retas formam um triângulo EQUILÁTERO!')
elif r1==r2 or r2==r3 or r3==r1:
    print('Essas retas formam um triângulo ISÓSCELES!')
else:
    print('Essas retas formam um triângulo ESCALENO!')