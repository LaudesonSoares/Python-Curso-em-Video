# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg:.1f}x{comp:.1f} é de {a:.1f} m²')


print('Cotrole de Terrenos')
print('-'*20)
l = float(input('LARGURA (M): '))
c = float(input('COMPRIMENTO (M): '))
área(l, c)
