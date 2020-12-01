# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('Digite três números e vou te dizer qual é o maior e qual é o menor.')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

# Verificando quem é menor
if n1<n2 and n1<n3:
    print('O menor número é {}'.format(n1))
if n2<n1 and n2<n3:
    print('O menor número é {}'.format(n2))
if n3<n1 and n3<n2:
    print('O menor número é {}'.format(n3))
#Verificando quem é maior
if n1>n2 and n1>n3:
    print('O maior número é {}'.format(n1))
if n2>n1 and n2>n3:
    print('O maior número é {}'.format(n2))
if n3>n1 and n3>n2:
    print('O maior número é {}'.format(n3))

#Maneira mais enxuta de executar o programa
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))
