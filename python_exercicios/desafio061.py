#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('Gerador de PA')
print('-='*10)
t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
pa = t + r
c = 1
while c <= 10:
    c += 1
    print(pa, end=' ')
    pa += r
print('Fim')

